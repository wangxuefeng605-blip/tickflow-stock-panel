from core.runtime.ai_selector_runtime import AISelectorRuntime


def test_ai_selector_runtime_entry():

    runtime = AISelectorRuntime()

    result = runtime.run(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_completed"]