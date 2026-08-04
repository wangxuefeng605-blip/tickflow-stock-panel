from core.runtime_strategy_auto_response_engine import (
    RuntimeStrategyAutoResponseEngine
)



def test_runtime_strategy_warning_response():

    engine = RuntimeStrategyAutoResponseEngine()


    response = engine.handle(
        {
            "level": "warning",
            "type": "reward_drift"
        }
    )


    assert (
        response["action"]
        ==
        "adjust_parameters"
    )



def test_runtime_strategy_critical_response():

    engine = RuntimeStrategyAutoResponseEngine()


    response = engine.handle(
        {
            "level": "critical",
            "type": "execution_failure_spike"
        }
    )


    assert (
        response["action"]
        ==
        "fallback_strategy"
    )



def test_runtime_strategy_response_history():

    engine = RuntimeStrategyAutoResponseEngine()


    engine.handle(
        {
            "level": "warning",
            "type": "behavior_deviation"
        }
    )


    assert len(
        engine.history()
    ) == 1