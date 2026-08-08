"""
Mutation Engine

Generate mutated strategy candidates.
"""


class MutationEngine:


    def mutate(
        self,
        strategy
    ):

        mutated = strategy.copy()


        changes = {}


        for key, value in strategy.items():

            if isinstance(value, (int, float)):

                new_value = round(
                    value * 1.1,
                    4
                )

                mutated[key] = new_value

                changes[key] = {
                    "from": value,
                    "to": new_value
                }


        return {

            "strategy":
                mutated,

            "mutation":
            {
                "type":
                    "parameter",

                "changes":
                    changes
            }
        }