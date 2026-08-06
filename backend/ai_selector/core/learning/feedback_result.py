class FeedbackResult(dict):


    def __init__(
        self,
        feedback,
        weights,
        performance,
        learning
    ):

        super().__init__()

        self["feedback"] = feedback
        self["weights"] = weights
        self["performance"] = performance
        self["learning"] = learning


    def __getitem__(self, key):

        if isinstance(key,int):

            return self["feedback"][key]

        return super().__getitem__(key)