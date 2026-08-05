from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_market_regime_intelligence_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionMarketRegimeIntelligenceEngine
)



def test_bull_detection():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionMarketRegimeIntelligenceEngine()
    )


    result = engine.analyze(
        0.8,
        0.2,
        0.9
    )


    assert result["regime"] == "BULL"



def test_bear_detection():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionMarketRegimeIntelligenceEngine()
    )


    result = engine.analyze(
        0.2,
        0.8,
        0.1
    )


    assert result["regime"] == "BEAR"



def test_sideways_detection():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionMarketRegimeIntelligenceEngine()
    )


    result = engine.analyze(
        0.5,
        0.5,
        0.5
    )


    assert result["regime"] == "SIDEWAYS"



def test_current_regime():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionMarketRegimeIntelligenceEngine()
    )


    engine.analyze(
        0.8,
        0.2,
        0.9
    )


    assert engine.current_regime() == "BULL"