from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_portfolio_risk_management_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioRiskManagementEngine
)



def test_add_position():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioRiskManagementEngine()
    )


    result = engine.add_position(
        "000001",
        0.2
    )


    assert result["weight"] == 0.2



def test_risk_calculation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioRiskManagementEngine()
    )


    engine.add_position(
        "000001",
        0.5
    )


    result = engine.calculate_risk(
        "000001",
        0.2
    )


    assert result["risk"] == 0.1



def test_exposure_control():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioRiskManagementEngine()
    )


    engine.add_position(
        "A",
        0.5
    )


    result = engine.check_exposure(
        0.3
    )


    assert result["A"] is False



def test_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioRiskManagementEngine()
    )


    engine.add_position(
        "test",
        0.1
    )


    assert len(
        engine.get_history()
    ) == 1