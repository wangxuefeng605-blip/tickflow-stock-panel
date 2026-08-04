from core.runtime.runtime_api import RuntimeAPI


def test_runtime_api():

    api = RuntimeAPI()

    result = api.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["api_completed"]