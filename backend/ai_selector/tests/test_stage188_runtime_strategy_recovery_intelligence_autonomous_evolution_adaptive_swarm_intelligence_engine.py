from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_swarm_intelligence_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveSwarmIntelligenceEngine
)



def test_add_agent():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveSwarmIntelligenceEngine()
    )


    result = engine.add_agent(
        "agent_a",
        {
            "fitness": 0.7
        }
    )


    assert result["fitness"] == 0.7



def test_global_best():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveSwarmIntelligenceEngine()
    )


    engine.add_agent(
        "agent_a",
        {
            "fitness": 0.5
        }
    )


    engine.add_agent(
        "agent_b",
        {
            "fitness": 0.9
        }
    )


    result = engine.update_global_best()


    assert result["agent"] == "agent_b"



def test_empty_swarm():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveSwarmIntelligenceEngine()
    )


    assert engine.update_global_best() is None



def test_swarm_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveSwarmIntelligenceEngine()
    )


    engine.add_agent(
        "test",
        {}
    )


    assert len(
        engine.get_history()
    ) == 1