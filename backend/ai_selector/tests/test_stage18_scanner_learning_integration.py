from core.learning.scanner_learning_integration import ScannerLearningIntegration

def test_scanner_learning_integration():

    integration = ScannerLearningIntegration()

    result = integration.apply(
        {
            "momentum":0.8
        },
        {
            "weights":{
                "momentum":1.2
            }
        }
    )

    assert result["momentum"] > 0.8