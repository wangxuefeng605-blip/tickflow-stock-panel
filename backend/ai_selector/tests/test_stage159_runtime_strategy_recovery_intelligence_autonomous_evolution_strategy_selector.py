from core.runtime_strategy_recovery_intelligence_autonomous_evolution_strategy_selector import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategySelector
)



def test_strategy_selection():

    selector = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategySelector()
    )


    result = selector.select(
        [
            {
                "strategy": "restore",
                "fitness": 0.8
            },
            {
                "strategy": "rollback",
                "fitness": 0.5
            }
        ]
    )


    assert result["strategy"] == "restore"
    assert result["fitness"] == 0.8
    assert result["status"] == "selected"



def test_strategy_ranking():

    selector = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategySelector()
    )


    result = selector.rank(
        [
            {
                "strategy": "a",
                "fitness": 0.3
            },
            {
                "strategy": "b",
                "fitness": 0.9
            }
        ]
    )


    assert result[0]["strategy"] == "b"



def test_strategy_empty():

    selector = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategySelector()
    )


    assert selector.select([]) is None



def test_strategy_history():

    selector = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionStrategySelector()
    )


    selector.select(
        [
            {
                "strategy": "test",
                "fitness": 1.0
            }
        ]
    )


    assert len(
        selector.get_history()
    ) == 1