from core.runtime_strategy_recovery_intelligence_autonomous_evolution_knowledge_graph_builder import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeGraphBuilder
)



def test_add_strategy():

    builder = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeGraphBuilder()
    )


    result = builder.add_strategy(
        "restore"
    )


    assert result["name"] == "restore"



def test_add_relation():

    builder = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeGraphBuilder()
    )


    builder.add_strategy(
        "restore"
    )

    builder.add_strategy(
        "adaptive_restore"
    )


    result = builder.add_relation(
        "restore",
        "adaptive_restore",
        "evolved_from"
    )


    assert result["relation"] == "evolved_from"



def test_find_strategy():

    builder = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeGraphBuilder()
    )


    builder.add_strategy(
        "rollback"
    )


    result = builder.find_strategy(
        "rollback"
    )


    assert result["name"] == "rollback"



def test_graph():

    builder = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeGraphBuilder()
    )


    builder.add_strategy(
        "test"
    )


    graph = builder.get_graph()


    assert len(graph["nodes"]) == 1



def test_history():

    builder = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeGraphBuilder()
    )


    builder.add_strategy(
        "test"
    )


    assert len(
        builder.get_history()
    ) == 1