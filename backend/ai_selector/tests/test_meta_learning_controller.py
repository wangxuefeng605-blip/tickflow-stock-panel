from core.meta_learning.meta_learning_controller import (
    MetaLearningController
)


def test_meta_learning_controller():

    controller = MetaLearningController()


    result = controller.learn(
        {
            "factor":"momentum",
            "reward":1
        },
        {
            "momentum":0.3
        }
    )


    assert result["momentum"] > 0.3