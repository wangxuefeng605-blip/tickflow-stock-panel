from core.learning.learning_state import LearningState
from core.learning.experience_collector import ExperienceCollector
from core.learning.learning_evaluator import LearningEvaluator
from core.learning.learning_controller import LearningController



def test_learning_controller():


    state = LearningState()


    controller = LearningController(
        ExperienceCollector(state),
        LearningEvaluator(),
        state
    )


    result = controller.learn(
        {
            "decision":{
                "action":"BUY"
            },
            "reward":30
        }
    )


    assert result["status"] == "LEARNED"

    assert result["evaluation"]["level"] == "POSITIVE"

    assert result["state"]["reward"] == 30