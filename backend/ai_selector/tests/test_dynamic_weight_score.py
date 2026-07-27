from core.score import alpha_score



def test_dynamic_weight_changes_score():


    factors = {

        "momentum":1.0,

        "quality":0.2

    }


    bull_weights = {

        "momentum":0.8,

        "quality":0.2

    }


    bear_weights = {

        "momentum":0.2,

        "quality":0.8

    }



    bull_score = alpha_score(
        factors,
        bull_weights
    )


    bear_score = alpha_score(
        factors,
        bear_weights
    )



    assert bull_score > bear_score