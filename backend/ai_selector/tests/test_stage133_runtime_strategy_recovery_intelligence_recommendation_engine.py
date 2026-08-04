from core.runtime_strategy_recovery_intelligence_recommendation_engine import (
    RuntimeStrategyRecoveryIntelligenceRecommendationEngine
)



def test_recommendation_generate():

    engine = (
        RuntimeStrategyRecoveryIntelligenceRecommendationEngine()
    )


    result = engine.recommend(
        {
            "policy": "restore",
            "confidence": 0.9
        }
    )


    assert result["policy"] == "restore"
    assert result["confidence"] == 0.9



def test_recommendation_empty():

    engine = (
        RuntimeStrategyRecoveryIntelligenceRecommendationEngine()
    )


    result = engine.recommend(
        {
            "policy": None
        }
    )


    assert result["reason"] == "no_prediction"



def test_recommendation_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceRecommendationEngine()
    )


    engine.recommend(
        {
            "policy": "fallback",
            "confidence": 0.7
        }
    )


    assert len(
        engine.get_history()
    ) == 1