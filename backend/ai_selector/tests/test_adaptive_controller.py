from core.adaptive.adaptive_state import AdaptiveState
from core.adaptive.adaptive_evaluator import AdaptiveEvaluator
from core.adaptive.adaptive_controller import AdaptiveController



def test_adaptive_controller():


    state = AdaptiveState()


    controller = AdaptiveController(
        state,
        AdaptiveEvaluator()
    )


    result = controller.adapt(
        0.3
    )


    assert result["status"] == "ADAPTED"

    assert result["evaluation"]["level"] == "WEAK"

    assert result["state"]["strategy_version"] == 2