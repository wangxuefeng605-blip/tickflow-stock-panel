from core.runtime_adaptive_governor import RuntimeAdaptiveGovernor


def test_runtime_adaptive_governor():

    governor = RuntimeAdaptiveGovernor()


    result = governor.decide()


    assert "runtime_mode" in result

    assert "workers" in result