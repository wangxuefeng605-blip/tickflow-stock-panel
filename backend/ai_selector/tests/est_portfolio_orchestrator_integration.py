orchestrator = PortfolioOrchestrator()

result = orchestrator.run(
    market="BULL",
    signals={
        "reward":0.8,
        "risk":0.1
    }
)

assert result["decision"]["action"] == "BUY"