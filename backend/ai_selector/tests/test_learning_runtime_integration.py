from core.learning.runtime import LearningRuntime


def test_learning_runtime_process():

    runtime = LearningRuntime()


    result = runtime.process(
        feedback={
            "source": "ranking",
            "signal":{
                "momentum":0.05
            }
        },
        weights={
            "momentum":0.3
        }
    )


    assert result["updated"] is True
    assert "weights" in result