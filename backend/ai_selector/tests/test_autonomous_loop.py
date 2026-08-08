from core.autonomous.autonomous_loop import (
    AutonomousLoop
)


def test_autonomous_loop():

    loop = AutonomousLoop()


    result = loop.run(
        {
            "strategy": "trend",
            "score": 0.91
        }
    )


    assert result["status"] == "improved"

    assert result["strategy"] is not None