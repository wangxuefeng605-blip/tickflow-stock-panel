from core.learning import LearningPipeline



def test_learning_pipeline():

    pipeline = LearningPipeline()


    result = [
        {
            "code":"000001",
            "score":0.8
        }
    ]


    output = pipeline.run(
        result
    )


    assert output == result