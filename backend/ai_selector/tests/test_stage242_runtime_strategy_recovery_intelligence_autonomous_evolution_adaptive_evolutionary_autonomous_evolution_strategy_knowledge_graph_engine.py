from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_knowledge_graph_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyKnowledgeGraphEngine
)



def test_add_node():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyKnowledgeGraphEngine()
    )


    result = engine.add_node(
        "momentum",
        "strategy"
    )


    assert result["created"] is True



def test_relation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyKnowledgeGraphEngine()
    )


    engine.add_node(
        "momentum",
        "strategy"
    )


    engine.add_node(
        "bull_market",
        "market"
    )


    result = engine.add_relation(
        "momentum",
        "works_in",
        "bull_market"
    )


    assert result["relation_added"] is True



def test_query():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyKnowledgeGraphEngine()
    )


    engine.add_node(
        "trend",
        "strategy"
    )


    engine.add_node(
        "strong_trend",
        "signal"
    )


    engine.add_relation(
        "trend",
        "uses",
        "strong_trend"
    )


    result = engine.query_relation(
        "trend"
    )


    assert len(result) == 1



def test_graph_size():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyKnowledgeGraphEngine()
    )


    engine.add_node(
        "A",
        "strategy"
    )


    result = engine.get_graph_size()


    assert result["nodes"] == 1