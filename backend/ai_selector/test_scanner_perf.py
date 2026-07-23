from core.stock_pool import get_stock_pool
from core.scanner.engine import ScannerEngine


stocks=get_stock_pool()[:100]


engine=ScannerEngine(
    stocks,
    workers=8
)


engine.run()