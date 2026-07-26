from .ranker import Ranker
from .explain import explain


class RankingPipeline:


    def run(self, scan_results):

        ranked = Ranker().rank(
            scan_results
        )


        output = []


        for item in ranked:

            item.explanation = explain(item)

            output.append(item)


        return output