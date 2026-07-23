import numpy as np


def alpha_score(factor, weights):


    score = 0


    for key,value in weights.items():


        score += (
            factor.get(key,0)
            *
            value
        )


    return round(
        score,
        4
    )