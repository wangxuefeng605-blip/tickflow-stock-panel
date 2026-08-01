from core.scanner.engine import ScannerEngine
from core.scanner import worker


def test_worker_exception_isolation(monkeypatch):


    def fake_scan(self):

        if self.code == "000002":

            raise RuntimeError(
                "mock worker failure"
            )


        return {
            "code": self.code,
            "score": 1
        }


    monkeypatch.setattr(
        worker.ScanWorker,
        "scan",
        fake_scan
    )


    scanner = ScannerEngine(
        [
            "000001",
            "000002",
            "000003",
        ],
        workers=3
    )


    results = scanner.run()


    codes = [
        item["code"]
        for item in results
    ]


    assert "000001" in codes
    assert "000003" in codes
    assert "000002" not in codes