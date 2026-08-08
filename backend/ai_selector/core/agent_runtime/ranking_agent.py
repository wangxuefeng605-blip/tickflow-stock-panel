class RankingAgent:

    def run(self, context):

        candidates = context.get(
            "candidates",
            []
        )

        if not candidates:
            return {
                "agent": "ranking",
                "leader": None
            }

        leader = max(
            candidates,
            key=lambda x: x.get(
                "score",
                0
            )
        )

        return {
            "agent": "ranking",
            "leader": leader
        }