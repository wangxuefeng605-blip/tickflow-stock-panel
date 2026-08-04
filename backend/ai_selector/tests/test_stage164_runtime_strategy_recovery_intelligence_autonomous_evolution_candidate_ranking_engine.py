from core.runtime_strategy_recovery_intelligence_autonomous_evolution_candidate_ranking_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionCandidateRankingEngine
)



def test_candidate_ranking():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionCandidateRankingEngine()
    )


    result = engine.rank(
        [
            {
                "strategy": "restore",
                "fitness": 0.8,
                "confidence": 0.9,
                "risk": 0.1
            },
            {
                "strategy": "rollback",
                "fitness": 0.5,
                "confidence": 0.6,
                "risk": 0.2
            }
        ]
    )


    assert result["best"]["strategy"] == "restore"



def test_candidate_score():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionCandidateRankingEngine()
    )


    score = engine._score(
        {
            "fitness": 1.0,
            "confidence": 1.0,
            "risk": 0
        }
    )


    assert score == 0.9



def test_empty_candidates():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionCandidateRankingEngine()
    )


    result = engine.rank([])


    assert result["best"] is None



def test_ranking_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionCandidateRankingEngine()
    )


    engine.rank(
        [
            {
                "strategy": "test",
                "fitness": 1
            }
        ]
    )


    assert len(
        engine.get_history()
    ) == 1