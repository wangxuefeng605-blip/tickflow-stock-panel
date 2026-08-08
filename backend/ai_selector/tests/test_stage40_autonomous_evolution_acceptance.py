runtime = AutonomyRuntime()

result = runtime.run()

assert result["status"]=="SUCCESS"
assert result["cycle"]==1
assert "strategy" in result
assert "generation" in result