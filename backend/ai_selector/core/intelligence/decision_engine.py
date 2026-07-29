from .decision_types import AIDecision
from .decision_policy import decide_action


class AIDecisionEngine:


    def decide(
        self,
        item,
        context
    ):


        score = item.get(
            "score",
            0
        )


        confidence = item.get(
            "confidence",
            0
        )


        action = decide_action(
            score,
            confidence,
            context.market_state
        )


        return AIDecision(

            code=item["code"],

            action=action,

            confidence=confidence,

            score=score,

            reason=f"{context.market_state} market decision"
        )