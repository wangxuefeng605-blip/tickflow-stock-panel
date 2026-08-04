from core.runtime_strategy_self_healing_engine import (
    RuntimeStrategySelfHealingEngine
)



def test_runtime_strategy_success_healing():

    engine = RuntimeStrategySelfHealingEngine()


    result = engine.heal(
        {
            "action": "fallback_strategy",
            "success": True
        }
    )


    assert result["status"] == "healed"



def test_runtime_strategy_failed_healing_rollback():

    engine = RuntimeStrategySelfHealingEngine()


    result = engine.heal(
        {
            "action": "parameter_restore",
            "success": False
        }
    )


    assert result["status"] == "rollback"



def test_runtime_strategy_healing_history():

    engine = RuntimeStrategySelfHealingEngine()


    engine.heal(
        {
            "action": "fallback_strategy"
        }
    )


    assert len(
        engine.healing_history()
    ) == 1