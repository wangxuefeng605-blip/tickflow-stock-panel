from .types import RankingResult


class Ranker:


    def rank(self, results):

        if not results:
            return []


        ordered = sorted(
            results,
            key=lambda x: x.get("score",0),
            reverse=True
        )


        ranked = []


        for idx,item in enumerate(
            ordered,
            start=1
        ):

            if "code" not in item:
                continue


            ranked.append(
                RankingResult(
                    code=item["code"],
                    score=item.get("score",0),
                    rank=idx,
                    confidence=0.0,
                    signals=item.get(
                        "signals",
                        []
                    ),
                    risks=item.get(
                        "risks",
                        []
                    )
                )
            )


        return ranked