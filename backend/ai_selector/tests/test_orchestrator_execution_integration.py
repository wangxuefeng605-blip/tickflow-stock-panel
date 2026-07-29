from core.orchestrator.pipeline import AIOrchestrator


def test_execution():

    engine = AIOrchestrator(
        dependencies={}
    )


    result = engine.run(
        market="BULL"
    )


    assert result.orders["status"]=="CREATED"