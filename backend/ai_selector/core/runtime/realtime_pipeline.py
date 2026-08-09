from core.runtime.intraday_scanner import IntradayScanner
from core.ranking.realtime_ranking import RealtimeRanking
from core.decision.realtime_decision import RealtimeDecisionEngine


class RealtimePipeline:


    def __init__(self):

        self.scanner = IntradayScanner()

        self.ranker = RealtimeRanking()

        self.decision = RealtimeDecisionEngine()



    def run(self):

        stocks = self.scanner.scan()


        ranked = self.ranker.rank(
            stocks
        )


        decisions = []

        for item in ranked:

            decisions.append(
                self.decision.decide(item)
            )


        return {
            "stocks": len(stocks),
            "ranking": ranked,
            "decisions": decisions
        }