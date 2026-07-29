class RankingAdapter:


    def __init__(
        self,
        pipeline
    ):

        self.pipeline = pipeline



    def run(
        self,
        market
    ):

        scan_results = self._prepare_scan_results(
            market
        )


        return self.pipeline.run(
            scan_results
        )



    def _prepare_scan_results(
        self,
        market
    ):

        return market