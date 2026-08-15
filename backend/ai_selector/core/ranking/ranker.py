from .types import RankingResult
from .scoring import build_ranking_reason


class Ranker:

    def rank(
        self,
        results
    ):

        if not results:
            return []

        valid_results = [
            item
            for item in results
            if isinstance(item, dict)
            and "code" in item
        ]

        ordered = sorted(
            valid_results,
            key=lambda x: x.get(
                "score",
                0
            ),
            reverse=True
        )

        ranked = []

        for rank, item in enumerate(
            ordered,
            start=1
        ):

            print(
                "RANKER AI:",
                item
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

                    final_score=item.get(
                        "final_score",
                        item.get(
                            "score",
                            0
                        )
                    ),

                    rank=rank,

                    alpha_score=item.get(
                        "alpha_score",
                        explanation.get(
                            "score",
                            0
                        )
                    ),

                    ranking_reason=build_ranking_reason(
                        item
                    ),

                    factors=item.get(
                        "factors",
                        {}
                    ),

                    weights=item.get(
                        "weights",
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

                    explanation=explanation,

                    reason=item.get(
                        "reason",
                        ""
                    )
                )
            )

        return ranked