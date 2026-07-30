from core.runtime.contract import RuntimeRequest, RuntimeResponse


def test_runtime_contract():

    request = RuntimeRequest(
        "000001",
        {
            "momentum":0.8
        }
    )

    assert request.code=="000001"


    response = RuntimeResponse(
        "000001",
        {}
    )