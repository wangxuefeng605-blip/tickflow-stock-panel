from core.runtime_strategy_recovery_intelligence_autonomous_evolution_experience_retriever import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceRetriever
)



def test_experience_best_retrieve():

    retriever = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceRetriever()
    )


    retriever.add_experience(
        {
            "version": 1,
            "fitness": 0.6
        }
    )


    retriever.add_experience(
        {
            "version": 2,
            "fitness": 0.9
        }
    )


    result = retriever.retrieve_best()


    assert result["version"] == 2
    assert result["fitness"] == 0.9



def test_experience_success():

    retriever = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceRetriever()
    )


    retriever.add_experience(
        {
            "fitness": 0.8
        }
    )


    assert len(
        retriever.retrieve_success()
    ) == 1



def test_experience_failure():

    retriever = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceRetriever()
    )


    retriever.add_experience(
        {
            "fitness": 0.2
        }
    )


    assert len(
        retriever.retrieve_failure()
    ) == 1



def test_experience_history():

    retriever = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceRetriever()
    )


    retriever.add_experience(
        {
            "fitness": 0.7
        }
    )


    assert len(
        retriever.get_history()
    ) == 1