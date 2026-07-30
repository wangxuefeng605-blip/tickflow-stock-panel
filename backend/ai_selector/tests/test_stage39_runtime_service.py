from core.scanner.runtime_service import RuntimeService


def test_runtime_service():

    service = RuntimeService()

    result = service.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_service_completed"]