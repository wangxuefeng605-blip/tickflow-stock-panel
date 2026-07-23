from core.stock_pool import get_stock_pool
from core.ranking import rank_stocks, print_top10
from core.scanner.engine import ScannerEngine
from core.report_writer import write_report



def run_fast_scan():

    stocks = get_stock_pool()

    print(
        f"Stock Pool Size: {len(stocks)}"
    )


    engine = ScannerEngine(
        stocks
    )


    results = engine.run()


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



if __name__=="__main__":

    run_fast_scan()


def run_fast_scan():
    stocks = get_stock_pool()

    print(f"Stock Pool Size: {len(stocks)}")

    engine = ScannerEngine(stocks)

    results = engine.run()

    top10 = rank_stocks(results, top_n=10)

    print_top10(top10)


if __name__ == "__main__":
    run_fast_scan()