from .models import BacktestResult


class BacktestEngine:


    def run(
        self,
        request
    ):


        if isinstance(request, list):

            trades = len(request)

            total_return = sum(
                item.get(
                    "return",
                    0
                )
                for item in request
            )

        else:

            trades = 0

            total_return = 0



        return BacktestResult(

            trades=trades,

            total_return=total_return,

            max_drawdown=0,

            equity_curve=[],

            return_rate=total_return

        )