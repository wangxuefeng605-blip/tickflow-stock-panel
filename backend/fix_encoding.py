from pathlib import Path

root = Path("ai_selector")

for p in root.rglob("*.py"):
    try:
        data = p.read_bytes()

        # 删除 BOM
        data = data.replace(b"\xef\xbb\xbf", b"")

        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            text = data.decode("gb18030")

        p.write_text(
            text,
            encoding="utf-8",
            newline=""
        )

        print("fixed:", p)

    except Exception as e:
        print("ERROR:", p, e)