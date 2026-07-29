from core.stock_pool import get_stock_pool

from core.ranking import rank_stocks, print_top10

from core.scanner.engine import ScannerEngine

from core.report_writer import write_report

from core.intelligence.context_builder import ContextBuilder
from core.intelligence.market_provider import MarketDataProvider



def run_fast_scan():

    stocks = get_stock_pool()


    print(
        f"Stock Pool Size: {len(stocks)}"
    )


    # ==========================
    # AI Intelligence Layer
    # ==========================

    market_data = (
        MarketDataProvider()
        .get_market_data()
    )


    ai_context = (
        ContextBuilder()
        .build(
            market_data
        )
    )


    print(
        "AI Context:",
        ai_context.market_state
    )


    print(
        "AI Weights:",
        ai_context.weights
    )


    # ==========================
    # Scanner Engine
    # ==========================

    engine = ScannerEngine(
        stocks,
        workers=8,
        context=ai_context
    )


    results = engine.run()



    # ==========================
    # Ranking
    # ==========================

    top10 = rank_stocks(
        results,
        top_n=10
    )


    print_top10(
        top10
    )


    write_report(
        top10
    )



if __name__ == "__main__":

    run_fast_scan()