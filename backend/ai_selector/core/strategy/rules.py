def momentum_entry(factors):

    if factors.get(
        "momentum",
        0
    ) > 0.05:

        return True

    return False



def trend_exit(factors):

    if factors.get(
        "trend",
        0
    ) < 0:

        return True

    return False