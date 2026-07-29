from core.orchestrator.pipeline import AIOrchestrator
from core.orchestrator.dependencies import OrchestratorDependencies



class MockRanking:

    def run(self, market):

        return "ranking"



class MockDecision:

    def run(self, ranking):

        return "decision"



class MockStrategy:

    def select(self, market):

        return "momentum"



class MockExecution:

    def execute(self, strategy):

        return [
            "ORDER"
        ]



def test_full_flow():


    deps = OrchestratorDependencies(

        ranking=MockRanking(),

        decision=MockDecision(),

        strategy=MockStrategy(),

        execution=MockExecution()
    )


    engine = AIOrchestrator(
        deps
    )


    result = engine.run(
        "BULL"
    )


    assert result.ranking=="ranking"

    assert result.decision=="decision"

    assert result.strategy=="momentum"

    assert result.orders==["ORDER"]