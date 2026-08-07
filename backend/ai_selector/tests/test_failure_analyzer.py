from core.healing.failure_analyzer import (
    FailureAnalyzer
)



def test_failure_analyze():

    analyzer = FailureAnalyzer()


    result = analyzer.analyze(
        [
            {
                "component":"scanner",
                "error":
                    "connection timeout"
            }
        ]
    )


    assert result[0]["type"] == (
        "TIMEOUT"
    )

    assert result[0]["action"] == (
        "RETRY"
    )