from core.learning.feedback import LearningFeedback
from core.learning.feedback_aggregator import LearningFeedbackAggregator



def test_collect_feedback():


    agg = LearningFeedbackAggregator()


    feedback = LearningFeedback(

        source="ranking",

        signal={

            "ranking":{

                "momentum":0.05

            }

        }

    )


    agg.collect(feedback)


    assert len(
        agg.feedbacks
    ) == 1



def test_aggregate_feedback():


    agg = LearningFeedbackAggregator()


    agg.collect(

        LearningFeedback(

            source="ranking",

            signal={

                "ranking":{

                    "momentum":0.05

                }

            }

        )

    )


    result = agg.aggregate()


    assert result[
        "ranking_adjustment"
    ][
        "momentum"
    ] == 0.05