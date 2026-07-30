from core.runtime.runtime_pipeline import RuntimePipeline


def test_runtime_pipeline():

    pipeline = RuntimePipeline()

    result = pipeline.execute(
        {
            "code":"000001",
            "momentum":0.8
        }
    )

    assert result["runtime_completed"]
    assert result["pipeline_runtime_completed"]