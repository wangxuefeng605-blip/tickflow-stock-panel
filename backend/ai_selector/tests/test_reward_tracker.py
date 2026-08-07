from core.meta_learning.reward_tracker import RewardTracker


def test_reward_tracker():

    tracker = RewardTracker()

    tracker.record(
        {
            "factor":"momentum",
            "return":0.12
        }
    )

    rewards = tracker.history()

    assert len(rewards) == 1

    assert rewards[0]["factor"] == "momentum"