from .types import RankingResult
from .scoring import build_ranking_reason

from .scoring import build_ranking_reason


class Ranker:


    def rank(self, results):

        if not results:
            return []


        ordered = sorted(
            results,
            key=lambda x: x.get(
                "score",
                0
            ),
            reverse=True
        )


        ranked = []


        for idx, item in enumerate(
            ordered,
            start=1
        ):

            if "code" not in item:
                continue


            ai = item
                
            

            print(
                "RANKER AI:",
                ai
            )

            ranked.append(
                RankingResult(

                    code=item["code"],

                    score=item.get(

                        "score",
                        0
                    ),

                    rank=idx,

                    ranking_reason=build_ranking_reason(
                        item
                    ),

                    factors=item.get(
                        "factors",
                        {}
                    ),


                    signals=ai.get(
                         0
                          "signals",
                        []
                    ),


                   confidence = item.get(
                       "confidence",
                       item.get(
                           "explanation",
                           {}
                       ).get(
                           "confidence",
                           0
                        )
                    )

                    market_state=ai.get(
                       "market_state",
                       "UNKNOWN"
                    ),

                    explanation=ai.get(
                        "explanation",
                        {}
                    )

                )
            )
        return ranked
    
    def ai_rank_score(item):

        score = item.get(
            "score",
            0
        )


        confidence = item.get(
            "confidence",
            0
        )


        signals = item.get(
            "signals",
            []
        )


        bonus = 0


        # AI 信心奖励
        bonus += confidence * 0.05


        # 信号奖励
        if signals:
            bonus += min(
                len(signals) * 0.01,
                0.05
            )


        return score + bonus