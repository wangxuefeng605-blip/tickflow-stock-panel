from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_dynamic_asset_allocation_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionDynamicAssetAllocationEngine
)



def test_set_asset():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionDynamicAssetAllocationEngine()
    )


    result = engine.set_asset(
        "stock_alpha",
        0.5
    )


    assert result["weight"] == 0.5



def test_bull_adjustment():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionDynamicAssetAllocationEngine()
    )


    engine.set_asset(
        "stock",
        0.5
    )


    result = engine.adjust_by_market(
        "BULL"
    )


    assert result["stock"] == 0.6



def test_bear_adjustment():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionDynamicAssetAllocationEngine()
    )


    engine.set_asset(
        "stock",
        0.5
    )


    result = engine.adjust_by_market(
        "BEAR"
    )


    assert result["stock"] == 0.3



def test_normalize():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionDynamicAssetAllocationEngine()
    )


    engine.set_asset(
        "A",
        30
    )


    engine.set_asset(
        "B",
        70
    )


    result = engine.normalize()


    assert result["A"] == 0.3

    assert result["B"] == 0.7