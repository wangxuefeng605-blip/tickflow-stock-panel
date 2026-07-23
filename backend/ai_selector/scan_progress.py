import json
import os


FILE="scan_progress.json"



def load_progress():

    if not os.path.exists(FILE):

        return {
            "finished":[],
            "failed":[]
        }


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)





def save_progress(data):


    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )





def mark_finished(code):


    data=load_progress()


    if code not in data["finished"]:

        data["finished"].append(code)


    save_progress(data)





def mark_failed(code):


    data=load_progress()


    if code not in data["failed"]:

        data["failed"].append(code)


    save_progress(data)