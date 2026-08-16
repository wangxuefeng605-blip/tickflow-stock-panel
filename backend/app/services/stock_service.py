from app.market_data.eastmoney import get_stock_spot


def get_all_stocks():

    df = get_stock_spot()

    records = df.to_dict(
        orient="records"
    )

    return records
