from core.runtime.realtime_pipeline import (
    RealtimePipeline
)


def test_realtime_pipeline():

    pipeline = RealtimePipeline()


    result = pipeline.run()


    assert "ranking" in result
    assert "decisions" in result