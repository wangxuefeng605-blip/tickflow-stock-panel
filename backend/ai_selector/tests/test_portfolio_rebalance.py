from core.portfolio.rebalance import RebalanceEngine



def test_rebalance():


    engine = RebalanceEngine()


    current = {

        "000001":100

    }


    target = {

        "000002":200

    }


    orders = engine.rebalance(

        current,

        target

    )


    assert len(orders)==2


    assert orders[0]["action"]=="BUY"

    assert orders[1]["action"]=="SELL"