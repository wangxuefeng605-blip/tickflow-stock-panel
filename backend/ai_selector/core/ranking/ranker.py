from .types import RankingResult
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


            explanation = item.get(
                "explanation",
                {}
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


                    signals=item.get(
                        "signals",
                        []
                    ),


                    confidence=item.get(
                        "confidence",
                        explanation.get(
                            "confidence",
                            0
                        )
                    ),


                    market_state=item.get(
                        "market_state",
                        "UNKNOWN"
                    ),


                    explanation=explanation

                )
            )


        return ranked