from ic_analysis import rolling_ic



def get_factor_weight(history):


    ic=rolling_ic(
        history
    )


    mean_ic=ic.mean()



    weight=abs(
        mean_ic
    )


    weight=weight / weight.sum()



    return weight.to_dict()