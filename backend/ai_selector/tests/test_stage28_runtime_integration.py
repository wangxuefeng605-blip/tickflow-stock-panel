from core.runtime.runtime_api import RuntimeAPI


def test_runtime_integration():

    api = RuntimeAPI()

    result = api.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_completed"]
    assert result["pipeline_runtime_completed"]
    assert result["executor_completed"]
    assert result["service_completed"]
    assert result["api_completed"]