from .types import RankingResult


class Ranker:


    def rank(self, results):

        if not results:
            return []


        ordered = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )


        ranked = []


        for idx,item in enumerate(
            ordered,
            start=1
        ):

            ranked.append(
                RankingResult(
                    code=item["code"],
                    score=item["score"],
                    rank=idx
                )
            )


        return ranked