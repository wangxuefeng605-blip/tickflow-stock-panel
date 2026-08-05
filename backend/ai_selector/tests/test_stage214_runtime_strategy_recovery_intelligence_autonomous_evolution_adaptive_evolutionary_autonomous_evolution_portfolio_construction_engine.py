from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_portfolio_construction_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioConstructionEngine
)



def test_add_strategy():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioConstructionEngine()
    )


    result = engine.add_strategy(
        "alpha_strategy",
        80
    )


    assert result["name"] == "alpha_strategy"



def test_weight_allocation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioConstructionEngine()
    )


    engine.add_strategy(
        "A",
        60
    )


    engine.add_strategy(
        "B",
        40
    )


    result = engine.allocate_weights()


    assert result[0]["weight"] == 0.6

    assert result[1]["weight"] == 0.4



def test_build_portfolio():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioConstructionEngine()
    )


    engine.add_strategy(
        "TOP10",
        100
    )


    result = engine.build_portfolio()


    assert result["status"] == "constructed"



def test_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioConstructionEngine()
    )


    engine.add_strategy(
        "test",
        1
    )


    assert len(
        engine.get_history()
    ) == 1