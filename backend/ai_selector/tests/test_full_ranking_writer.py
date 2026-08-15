from pathlib import Path

from core.full_ranking_writer import save_full_ranking
from core.ranking import rank_stocks


def test_ranking_writer_serializable(tmp_path, monkeypatch):

    data = [
        {
            "code": "000001",
            "score": 0.95,
            "factors": {},
        },
        {
            "code": "600000",
            "score": 0.85,
            "factors": {},
        },
    ]

    results = rank_stocks(data)

    monkeypatch.setattr(
        "core.full_ranking_writer.REPORT_DIR",
        tmp_path,
    )

    output = save_full_ranking(results)

    assert output["json"].exists()
    assert output["csv"].exists()

    assert output["json"].stat().st_size > 0
    assert output["csv"].stat().st_size > 0
