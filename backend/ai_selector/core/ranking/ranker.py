from .types import RankingResult


class Ranker:


    def rank(self, results):

        ordered = sorted(
            results,
            key=lambda x:x["score"],
            reverse=True
        )


        output=[]


        for idx,item in enumerate(
            ordered,
            start=1
        ):

            output.append(
                RankingResult(
                    code=item["code"],
                    score=item["score"],
                    rank=idx
                )
            )


        return output