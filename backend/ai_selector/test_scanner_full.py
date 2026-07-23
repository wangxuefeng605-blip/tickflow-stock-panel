from core.stock_pool import get_stock_pool
from core.scanner.engine import ScannerEngine

stocks = get_stock_pool()

print(f"Stock count: {len(stocks)}")

engine = ScannerEngine(
    stocks=stocks,
    workers=8,
)

results = engine.run()

print()
print(f"Success: {len(results)}")