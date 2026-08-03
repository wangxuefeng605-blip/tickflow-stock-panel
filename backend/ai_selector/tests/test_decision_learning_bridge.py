from core.learning.weight_provider import LearningWeightProvider
from core.decision.decision_learning_bridge import DecisionLearningBridge



def test_decision_learning_bridge():


    provider = LearningWeightProvider(
        {
            "momentum":1,
            "trend":1
        }
    )


    bridge = DecisionLearningBridge(
        provider
    )


    feedback = {
        "success":True
    }


    bridge.apply(
        feedback
    )


    assert (
        provider.get_weight(
            "momentum"
        )
        >
        1
    )