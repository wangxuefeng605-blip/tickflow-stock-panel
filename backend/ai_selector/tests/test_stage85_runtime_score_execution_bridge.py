from core.runtime_score_execution_bridge import RuntimeScoreExecutionBridge


def test_runtime_score_execution_bridge():

    bridge = RuntimeScoreExecutionBridge()


    result = bridge.bind(
        {
            "momentum":0.8
        }
    )


    assert result["connected"] is True


    score = bridge.execute(100)


    assert score == 80