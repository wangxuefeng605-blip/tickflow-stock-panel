class RealtimeRanking:


    def rank(self, items):

        ordered = sorted(
            items,
            key=lambda x:x["score"],
            reverse=True
        )


        result=[]

        for i,item in enumerate(ordered,1):

            result.append(
                {
                    **item,
                    "rank":i
                }
            )

        return result