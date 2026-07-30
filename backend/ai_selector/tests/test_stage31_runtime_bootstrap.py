from core.runtime.runtime_bootstrap import create_runtime


def test_runtime_bootstrap():

    runtime = create_runtime()

    result = runtime.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )

    assert result["runtime_completed"]
    assert result["facade_completed"]