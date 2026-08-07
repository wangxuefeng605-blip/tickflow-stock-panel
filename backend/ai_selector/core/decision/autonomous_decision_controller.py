"""
Autonomous Decision Controller

Stage30 Autonomous Decision Intelligence
"""

from .decision_context import DecisionContext
from .decision_rule_engine import DecisionRuleEngine
from .decision_score_engine import DecisionScoreEngine



class AutonomousDecisionController:


    def __init__(self):

        self.rule_engine = DecisionRuleEngine()

        self.score_engine = DecisionScoreEngine()



    def decide(
        self,
        data
    ):

        context = DecisionContext(
            data
        )


        rule = self.rule_engine.evaluate(
            context
        )


        score = self.score_engine.score(
            data
        )


        return {
            "action": rule["action"],
            "score": score["score"],
            "level": score["level"]
        }