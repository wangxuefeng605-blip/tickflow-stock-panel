from .types import RankingResult


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


            ai = item.get(
                "ai",
                {}
            )

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


                    factors=item.get(
                        "factors",
                        {}
                    ),


                    signals=ai.get(
                        "signals",
                        []
                    ),


                    confidence=ai.get(
                        "confidence",
                        0
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