def alpha_score(
    factor,
    weights
):


    score=0


    for k,w in weights.items():


        if k in factor:


            score += (
                factor[k]
                *
                w
            )


    return round(
        score*100,
       2
    )