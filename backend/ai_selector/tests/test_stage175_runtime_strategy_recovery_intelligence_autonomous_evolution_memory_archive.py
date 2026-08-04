from core.runtime_strategy_recovery_intelligence_autonomous_evolution_memory_archive import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryArchive
)



def test_archive_generation():

    archive = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryArchive()
    )


    result = archive.archive_generation(
        {
            "generation": 1,
            "fitness": 0.8
        }
    )


    assert result["generation"] == 1
    assert len(
        archive.get_generations()
    ) == 1



def test_archive_lineage():

    archive = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryArchive()
    )


    result = archive.archive_strategy_lineage(
        "restore",
        "restore_mutated"
    )


    assert result["parent"] == "restore"
    assert result["child"] == "restore_mutated"



def test_best_generation():

    archive = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryArchive()
    )


    archive.archive_generation(
        {
            "generation": 1,
            "fitness": 0.5
        }
    )


    archive.archive_generation(
        {
            "generation": 2,
            "fitness": 0.9
        }
    )


    result = archive.get_best_generation()


    assert result["generation"] == 2



def test_archive_history():

    archive = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryArchive()
    )


    archive.archive_generation(
        {
            "generation": 1
        }
    )


    assert len(
        archive.get_history()
    ) == 1