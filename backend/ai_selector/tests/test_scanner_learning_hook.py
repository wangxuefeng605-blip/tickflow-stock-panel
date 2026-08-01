from core.learning import ScannerLearningHook

def test_scanner_learning_hook():

    hook = ScannerLearningHook()

    result = [
        {
            "code": "000001",
            "score": 0.8
        }
    ]

    output = hook.after_scan(result)

    assert output == result