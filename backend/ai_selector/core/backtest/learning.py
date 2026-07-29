from dataclasses import dataclass


@dataclass
class LearningSignal:

    strategy: str

    return_rate: float

    max_drawdown: float

    win_rate: float

    score: float



class BacktestLearningEngine:


    def analyze(self, result):

        return LearningSignal(

            strategy=result.strategy,

            return_rate=result.total_return,

            max_drawdown=result.max_drawdown,

            win_rate=self._win_rate(result),

            score=self._score(result)

        )


    def _win_rate(self, result):

        if not result.trades:
            return 0

        wins = [
            t for t in result.trades
            if getattr(t, "return_rate",0)>0
        ]

        return len(wins)/len(result.trades)



    def _score(self,result):

        return (
            result.total_return
            -
            result.max_drawdown
        )