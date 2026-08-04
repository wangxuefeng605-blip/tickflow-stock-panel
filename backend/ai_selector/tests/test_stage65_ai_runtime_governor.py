from core.ai_runtime_governor import AIRuntimeGovernor


def test_ai_runtime_governor():

    governor = AIRuntimeGovernor()


    result = governor.evaluate(
        {
            "success_rate": 0.98,
            "retry_count": 1
        }
    )


    assert result["decision"] == "AGGRESSIVE"

    assert result["workers"] == 8