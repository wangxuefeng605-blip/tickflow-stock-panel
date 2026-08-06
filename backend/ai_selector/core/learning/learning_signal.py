"""
Learning Signal Generator

Convert portfolio performance
into ranking adjustment signals.
"""


class LearningSignalGenerator:


    def generate(self, performance):

        if not performance:
            return {
                "signals": {},
                "confidence": 0
            }


        success_rate = performance.get(
            "success_rate",
            0
        )

        avg_return = performance.get(
            "avg_return",
            0
        )


        signals = {}


        # overall performance

        if success_rate >= 0.6:
            signals["momentum"] = 0.03
            signals["trend"] = 0.02

        else:
            signals["risk"] = 0.03


        # return feedback

        if avg_return > 0.05:
            signals["quality"] = 0.02

        elif avg_return < 0:
            signals["risk"] = (
                signals.get("risk", 0)
                + 0.02
            )


        return {
            "signals": signals,
            "confidence": success_rate
        }