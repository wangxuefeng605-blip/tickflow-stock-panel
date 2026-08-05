from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_transfer_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionTransferEngine
)



def test_register():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionTransferEngine()
    )


    result = engine.register_strategy(
        "source"
    )


    assert result["registered"] is True



def test_add_gene():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionTransferEngine()
    )


    engine.register_strategy(
        "source"
    )


    result = engine.add_gene(
        "source",
        {
            "factor":"momentum"
        }
    )


    assert result["stored"] is True



def test_gene_transfer():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionTransferEngine()
    )


    engine.register_strategy(
        "A"
    )


    engine.register_strategy(
        "B"
    )


    engine.add_gene(
        "A",
        {
            "trend":1
        }
    )


    result = engine.transfer_gene(
        "A",
        "B"
    )


    assert result["count"] == 1



def test_knowledge_transfer():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionTransferEngine()
    )


    engine.register_strategy(
        "old"
    )


    engine.register_strategy(
        "new"
    )


    result = engine.transfer_knowledge(
        "old",
        "new",
        "bull_market_pattern"
    )


    assert result["knowledge"] == "bull_market_pattern"