from core.adaptive.adaptive_state import AdaptiveState
from core.adaptive.adaptive_evaluator import AdaptiveEvaluator
from core.adaptive.adaptive_controller import AdaptiveController
from core.adaptive.strategy_adapter import StrategyAdapter



def test_stage36_full_adaptive_loop():


    state = AdaptiveState()


    controller = AdaptiveController(
        state,
        AdaptiveEvaluator()
    )


    result = controller.adapt(
        0.2
    )


    assert result["status"] == "ADAPTED"

    assert result["evaluation"]["should_adjust"] is True


    adapter = StrategyAdapter(
        state
    )


    strategy = adapter.apply(
        "trend_following"
    )


    assert strategy["adaptive"] is True

    assert strategy["version"] == 2