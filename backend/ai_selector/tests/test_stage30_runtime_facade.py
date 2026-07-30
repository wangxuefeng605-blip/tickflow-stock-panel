from core.runtime.runtime_facade import RuntimeFacade


def test_runtime_facade():

    facade = RuntimeFacade()

    result = facade.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_completed"]
    assert result["service_completed"]
    assert result["executor_completed"]
    assert result["facade_completed"]