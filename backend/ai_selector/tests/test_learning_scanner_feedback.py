from core.learning.weight_provider import WeightProvider
from core.orchestrator.adapters.learning_scanner_adapter import LearningScannerAdapter



def test_scanner_uses_learning_weight():

    provider = WeightProvider(
        {
            "momentum":0.8
        }
    )


    adapter = LearningScannerAdapter(
        provider
    )


    weight = adapter.get_factor_weight(
        "momentum"
    )


    assert weight == 0.8