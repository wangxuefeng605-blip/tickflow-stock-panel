from core.feedback.weight_manager import WeightManager

def test_weight_manager():

    manager = WeightManager()

    manager.save({
        "momentum":1.2
    })

    result = manager.current()

    assert result["momentum"] == 1.2