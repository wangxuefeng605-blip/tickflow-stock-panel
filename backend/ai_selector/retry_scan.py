from scan_progress import load_progress
from stock_factor import get_stock_factor
from score import calculate_score

import time



def retry_failed():


    data=load_progress()


    failed=data["failed"]


    print(
        "失败数量:",
        len(failed)
    )


    success=[]


    for code in failed:


        for i in range(3):


            try:

                print(
                    code,
                    "重试",
                    i+1
                )


                factors=get_stock_factor(code)


                score=calculate_score(
                    factors
                )


                factors["score"]=score


                success.append(
                    factors
                )


                break


            except Exception as e:


                print(
                    "失败",
                    e
                )


                time.sleep(2)


    return success





if __name__=="__main__":

    retry_failed()