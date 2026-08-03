class OutcomeTracker:


    def __init__(self):

        self.records=[]


    def record(
        self,
        trade,
        result
    ):

        item={

            "trade":trade,

            "result":result

        }

        self.records.append(item)

        return item