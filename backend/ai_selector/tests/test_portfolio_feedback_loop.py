from core.portfolio.outcome_tracker import (
    OutcomeTracker
)

from core.portfolio.portfolio_feedback import (
    PortfolioFeedback
)

from core.portfolio.learning_adapter import (
    PortfolioLearningAdapter
)


class MockLearner:


    def __init__(self):

        self.updated = False



    def update(
        self,
        feedback
    ):

        self.updated = True

        return {

            "updated":True

        }



class PortfolioFeedbackRuntime:


    def __init__(self):

        self.tracker = OutcomeTracker()

        self.feedback_engine = PortfolioFeedback()

        self.learner = MockLearner()

        self.adapter = PortfolioLearningAdapter(
            self.learner
        )


    def execute(
        self,
        decision
    ):

        return self.tracker.record(

            decision,

            {
                "profit":1
            }

        )


    def feedback(
        self,
        result
    ):

        feedback = self.feedback_engine.evaluate(
            result["result"]
        )


        self.adapter.update(
            feedback
        )


        return {

            "reward":
                feedback["reward"],

            "learning_updated":
                self.learner.updated

        }



runtime = PortfolioFeedbackRuntime()



def test_portfolio_feedback_loop():


    result = runtime.execute(

        decision={

            "action":"BUY",

            "allocation":0.5

        }

    )


    feedback = runtime.feedback(
        result
    )


    assert feedback["reward"] > 0


    assert feedback["learning_updated"] is True