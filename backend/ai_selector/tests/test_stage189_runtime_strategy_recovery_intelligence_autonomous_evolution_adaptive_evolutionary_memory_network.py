from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_memory_network import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryMemoryNetwork
)



def test_add_strategy():

    network = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryMemoryNetwork()
    )


    result = network.add_strategy(
        "strategy_a",
        {
            "fitness": 0.8
        }
    )


    assert result["fitness"] == 0.8



def test_connect_strategy():

    network = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryMemoryNetwork()
    )


    result = network.connect_strategy(
        "parent",
        "child"
    )


    assert result["parent"] == "parent"

    assert result["child"] == "child"



def test_get_strategy():

    network = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryMemoryNetwork()
    )


    network.add_strategy(
        "best",
        {
            "fitness": 1
        }
    )


    result = network.get_strategy(
        "best"
    )


    assert result["fitness"] == 1



def test_memory_history():

    network = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryMemoryNetwork()
    )


    network.add_strategy(
        "test",
        {}
    )


    assert len(
        network.get_history()
    ) == 1