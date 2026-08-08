class AutoPromotionEngine:

    def __init__(self):
        self.promoted = None


    def promote(self, ranked_strategies):

        if not ranked_strategies:
            return None


        best = ranked_strategies[0]


        if best.get("rank") == 1:

            self.promoted = best

            return best


        return None


    def get_promoted(self):

        return self.promoted