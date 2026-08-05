"""
AI TOP10 Report Generator

Generate:
- JSON
- CSV
- Markdown
- HTML

"""

import json
import csv
from pathlib import Path
from datetime import datetime



REPORT_DIR = Path(
    "data/reports"
)


def load_top10(path=None):

    if path is None:

        path = REPORT_DIR / "top10.json"


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)


    # v17.4 scanner format
    #
    # {
    #    "data":[
    #        {
    #          "code":"000533"
    #        }
    #    ]
    # }


    if isinstance(data, dict):


        if "data" in data:

            return data["data"]



        if "top10" in data:

            return data["top10"]



        if "results" in data:

            return data["results"]



    if isinstance(data, list):

        return data



    return []



def generate_json(
    data
):

    output = REPORT_DIR / "AI_Top10_latest.json"


    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


    return output



def generate_csv(
    data
):

    output = REPORT_DIR / "AI_Top10_latest.csv"


    rows = []


    for item in data:


        if not isinstance(item, dict):

            continue


    rows.append(
        {
            "rank":
                item.get("rank"),

            "code":
                item.get("code"),

            "score":
                item.get("score"),

            "alpha_score":
                item.get("alpha_score"),

            "confidence":
                item.get("confidence"),

            "market_state":
                item.get("market_state"),

            "signals":
                ",".join(
                    item.get("signals", [])
                ),

            "momentum":
                item.get(
                    "factors",
                    {}
                ).get(
                    "momentum"
                ),

            "trend":
                item.get(
                   "factors",
                    {}
                ).get(
                    "trend"
                ),

            "volume_factor":
                item.get(
                    "factors",
                    {}
                ).get(
                    "volume_factor"
                ),

            "volatility":
                item.get(
                    "factors",
                    {}
                ).get(
                    "volatility"
                ),

             "quality":
                item.get(
                    "factors",
                    {}
                ).get(
                    "quality"
                ), 

            "growth":
                item.get(
                    "factors",
                    {}
                ).get(
                    "growth"
                ),

            "reason":
                item.get("reason")
                or
                item.get(
                    "explanation",
                    {}
                ).get(
                    "reason"
                )
        }
    )

    with open(
        output,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:


        writer = csv.DictWriter(
            f,
            fieldnames=rows[0].keys()
        )


        writer.writeheader()

        writer.writerows(
            rows
        )


    return output



def generate_markdown(
    data
):

    output = REPORT_DIR / "AI_Top10_latest.md"


    lines = []


    lines.append(
        "# AI Selector TOP10 Report\n"
    )


    lines.append(
        f"Date: {datetime.now()}\n"
    )


    for i,item in enumerate(data,1):


        if not isinstance(item,dict):

            continue

        lines.append(
            f"""
## {i}. {item.get('code')}

Score:
{item.get('score')}

Confidence:
{item.get('confidence')}

Market:
{item.get('market')}

Reason:
{item.get('reason','')}

"""
        )


    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(lines)
        )


    return output



def generate_html(
    data
):

    output = REPORT_DIR / "AI_Top10_latest.html"


    html = """

<html>

<head>
<title>AI Selector TOP10</title>
</head>

<body>

<h1>AI Selector TOP10 Report</h1>

<table border="1">

<tr>
<th>Code</th>
<th>Score</th>
<th>Confidence</th>
</tr>

"""


    for item in data:


        if not isinstance(item,dict):

            continue

         
        html += f"""
<tr>

<td>{item.get('code')}</td>

<td>{item.get('score')}</td>

<td>{item.get('confidence')}</td>

</tr>

"""


    html += """

</table>

</body>

</html>

"""


    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)


    return output



def generate_report():

    data = load_top10()


    return {

        "json":
            generate_json(data),

        "csv":
            generate_csv(data),

        "markdown":
            generate_markdown(data),

        "html":
            generate_html(data)

    }