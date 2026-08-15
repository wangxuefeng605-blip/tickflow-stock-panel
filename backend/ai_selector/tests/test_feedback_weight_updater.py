from core.feedback.weight_updater import FeedbackWeightUpdater


def test_weight_update():

    updater = FeedbackWeightUpdater()


    weights = {
        "momentum":0.5,
        "trend":0.5
    }


    result = updater.update(
        weights,
        0.8
    )


    assert result["momentum"] > 0
    assert abs(
        sum(result.values()) - 1
    ) < 0.0001