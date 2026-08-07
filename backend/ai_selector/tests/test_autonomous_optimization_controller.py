from core.optimization.autonomous_optimization_controller import (
    AutonomousOptimizationController
)



class MockLoop:


    def process(
        self,
        metrics,
        feedback
    ):

        return {
            "optimized": True
        }



class MockHealer:


    def execute(self):

        return "healed"



def test_autonomous_controller():


    controller = AutonomousOptimizationController(
        MockLoop(),
        MockHealer()
    )


    result = controller.run(
        {
            "latency": 1
        },
        {
            "ranking": 1
        }
    )


    assert (
        result["optimized"]
        is True
    )


    assert (
        result["healing"]
        ==
        "healed"
    )