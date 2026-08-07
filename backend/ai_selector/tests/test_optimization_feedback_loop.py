from core.optimization.optimization_feedback_loop import (
    OptimizationFeedbackLoop
)


class MockOptimizer:


    def analyze(self, metrics):

        return {
            "latency": metrics["latency"]
        }



class MockTuner:


    def update(self, metric, value):

        return {
            "metric": metric,
            "value": value
        }



class MockEvolution:


    def evaluate(self, feedback):

        return feedback



def test_feedback_loop():


    loop = OptimizationFeedbackLoop(
        MockOptimizer(),
        MockTuner(),
        MockEvolution()
    )


    result = loop.process(
        {
            "latency": 2
        },
        {
            "ranking": 1
        }
    )


    assert (
        result["performance"]["latency"]
        ==
        2
    )


    assert (
        result["strategies"]["ranking"]
        ==
        1
    )