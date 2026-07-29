feedback = FeedbackEngine()

result = feedback.record(
    "000001",
    0.8,
    0.1
)

assert result.success