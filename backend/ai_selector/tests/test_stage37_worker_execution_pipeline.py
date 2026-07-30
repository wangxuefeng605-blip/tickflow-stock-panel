from core.scanner.worker_execution_pipeline import WorkerExecutionPipeline


def test_worker_execution_pipeline():

    pipeline = WorkerExecutionPipeline()

    result = pipeline.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["worker_pipeline_completed"]