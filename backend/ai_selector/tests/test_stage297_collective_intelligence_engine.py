from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_autonomous_collective_intelligence_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousCollectiveIntelligenceEngine
)



def test_register_agent():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousCollectiveIntelligenceEngine()
    )


    result = engine.register_agent(
        "scanner_ai"
    )


    assert result["registered"] is True



def test_share():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousCollectiveIntelligenceEngine()
    )


    engine.register_agent(
        "factor_ai"
    )


    result = engine.share_knowledge(
        "factor_ai",
        {
            "key":"momentum",
            "value":"strong"
        }
    )


    assert result["shared"]["key"] == "momentum"



def test_collaboration():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionAutonomousCollectiveIntelligenceEngine()
    )


    result = engine.collaborate(
        [
            "scanner",
            "ranking"
        ],
        "find_best_strategy"
    )


    assert result["goal"] == "find_best_strategy"