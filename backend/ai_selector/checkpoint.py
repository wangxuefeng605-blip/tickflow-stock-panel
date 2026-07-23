import os
import json
import hashlib
from datetime import datetime

CHECKPOINT_FILE = "data/cache/checkpoint.json"
VERSION = "v17.2"

class CheckpointManager:
    def __init__(self, stock_pool):
        self.stock_pool = [str(x) for x in stock_pool]
        self.pool_hash = self._calc_pool_hash()
        self.data = {
            "version": VERSION,
            "session": datetime.now().strftime("scan_%Y%m%d_%H%M%S"),
            "pool_hash": self.pool_hash,
            "completed": [],
            "failed": [],
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def _calc_pool_hash(self):
        raw = json.dumps(sorted(self.stock_pool))
        return hashlib.md5(raw.encode("utf-8")).hexdigest()

    def load(self):
        if not os.path.exists(CHECKPOINT_FILE):
            return self.data

        try:
            with open(CHECKPOINT_FILE, "r", encoding="utf-8") as f:
                ckpt = json.load(f)

            # 版本或股票池变化，废弃旧断点
            if ckpt.get("version") != VERSION:
                return self.data

            if ckpt.get("pool_hash") != self.pool_hash:
                return self.data

            self.data = ckpt
            return self.data

        except Exception:
            return self.data

    def save(self):
        os.makedirs(os.path.dirname(CHECKPOINT_FILE), exist_ok=True)
        self.data["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def mark_completed(self, code):
        code = str(code)
        if code not in self.data["completed"]:
            self.data["completed"].append(code)

    def mark_failed(self, code):
        code = str(code)
        if code not in self.data["failed"]:
            self.data["failed"].append(code)

    def get_remaining(self):
        done = set(self.data["completed"])
        return [x for x in self.stock_pool if x not in done]

    def clear(self):
        if os.path.exists(CHECKPOINT_FILE):
            os.remove(CHECKPOINT_FILE)