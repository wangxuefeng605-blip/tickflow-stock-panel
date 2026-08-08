from core.learning.learning_state import LearningState
from core.learning.experience_collector import ExperienceCollector



def test_experience_collector():


    state = LearningState()


    collector = ExperienceCollector(
        state
    )


    result = collector.collect_result(
        {
            "action":"BUY"
        },
        {
            "status":"SUCCESS"
        },
        15
    )


    assert result["status"] == "RECORDED"


    snapshot = state.snapshot()


    assert snapshot["experience_count"] == 1