bridge = PortfolioRuntimeBridge()

result = bridge.process(
    {
        "reward":1,
        "performance":{
            "return":0.2
        }
    }
)

assert result["adjustment"]=="increase"