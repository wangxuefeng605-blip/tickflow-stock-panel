from core.runtime_strategy_recovery_intelligence_pattern_recognition_engine import (
    RuntimeStrategyRecoveryIntelligencePatternRecognitionEngine
)



def test_pattern_observe():

    engine = (
        RuntimeStrategyRecoveryIntelligencePatternRecognitionEngine()
    )


    result = engine.observe(
        {
            "policy": "restore",
            "success": True
        }
    )


    assert result["observed"] is True



def test_pattern_analysis():

    engine = (
        RuntimeStrategyRecoveryIntelligencePatternRecognitionEngine()
    )


    engine.observe(
        {
            "policy": "restore",
            "success": True
        }
    )

    engine.observe(
        {
            "policy": "restore",
            "success": False
        }
    )


    result = engine.analyze()


    assert result["restore"]["count"] == 2
    assert result["restore"]["success_rate"] == 0.5



def test_pattern_history():

    engine = (
        RuntimeStrategyRecoveryIntelligencePatternRecognitionEngine()
    )


    engine.observe(
        {
            "policy": "fallback"
        }
    )


    assert len(
        engine.get_history()
    ) == 1