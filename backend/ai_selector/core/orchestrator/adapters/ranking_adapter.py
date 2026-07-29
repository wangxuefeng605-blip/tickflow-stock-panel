class RankingAdapter:


    def __init__(self, pipeline):
        self.pipeline=pipeline


    def run(
        self,
        market
    ):

        scan_results=[
            {
                "code":"000001",
                "score":0.9
            }
        ]

        return self.pipeline.run(
            scan_results
        )