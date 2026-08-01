from core.learning.learning_runtime_orchestrator import (
    LearningRuntimeOrchestrator
)


def test_learning_runtime_orchestrator():

    runtime = LearningRuntimeOrchestrator()


    scan=[
        {
            "code":"000001",
            "score":0.8
        }
    ]


    result = runtime.after_scan(
        scan
    )


    assert result == scan