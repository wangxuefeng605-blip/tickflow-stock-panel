from core.runtime.runtime_state import RuntimeState



def test_runtime_state():


    runtime = RuntimeState()


    runtime.update(
        "decision",
        {
            "action":"BUY"
        }
    )


    result = runtime.get(
        "decision"
    )


    assert result["action"] == "BUY"


    snapshot = runtime.snapshot()


    assert "portfolio" in snapshot