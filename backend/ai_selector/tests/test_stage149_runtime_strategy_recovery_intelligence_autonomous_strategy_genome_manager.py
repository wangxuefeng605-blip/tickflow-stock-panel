from core.runtime_strategy_recovery_intelligence_autonomous_strategy_genome_manager import (
    RuntimeStrategyRecoveryIntelligenceAutonomousStrategyGenomeManager
)



def test_genome_register():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyGenomeManager()
    )


    result = manager.register(
        {
            "version": 2,
            "parent": 1,
            "fitness": 0.88
        }
    )


    assert result["version"] == 2
    assert result["parent"] == 1
    assert result["fitness"] == 0.88



def test_best_genome():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyGenomeManager()
    )


    manager.register(
        {
            "version": 1,
            "fitness": 0.5
        }
    )


    manager.register(
        {
            "version": 2,
            "fitness": 0.9
        }
    )


    result = manager.get_best_genome()


    assert result["version"] == 2
    assert result["fitness"] == 0.9



def test_genome_history():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyGenomeManager()
    )


    manager.register(
        {
            "version": 1,
            "fitness": 0.7
        }
    )


    assert len(
        manager.get_history()
    ) == 1