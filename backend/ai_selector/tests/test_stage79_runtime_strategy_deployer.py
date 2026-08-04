from core.runtime_strategy_deployer import RuntimeStrategyDeployer


def test_runtime_strategy_deployer():

    deployer = RuntimeStrategyDeployer()


    result = deployer.deploy(
        {
            "version":2,
            "score":0.9
        }
    )


    assert result["deployed"] is True

    assert deployer.current()["version"] == 2