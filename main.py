import collections
import datetime as dt
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

import configargparse
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_age_since(establish_year):
    years = dt.date.today().year - establish_year

    if years % 100 != 11 and years % 10 == 1:
        years_name = "год"
    elif years % 100 not in [12, 13, 14] and years % 10 in [2, 3, 4]:
        years_name = "года"
    else:
        years_name = "лет"

    return f"{years} {years_name}"


def main():
    argparser = configargparse.ArgParser()
    argparser.add(
        "-p",
        "--path",
        help="Full path to file with wines",
        env_var="PATH_TO_WINES",
        default="wine.xlsx",
    )

    parsed_args = argparser.parse_args()
    path_to_wines = Path(parsed_args.path)
    if not path_to_wines.exists():
        sys.exit("Не указан файл с винами")

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
    )

    template = env.get_template("template.html")

    wines = pandas.read_excel(
        path_to_wines, na_values=" ", keep_default_na=False
    ).to_dict(orient="records")

    wines_categorised = collections.defaultdict(list)

    for wine in wines:
        wines_categorised[wine["Категория"]].append(wine)

    establish_year = 1920
    rendered_page = template.render(
        age=get_age_since(establish_year),
        wines_categorised=wines_categorised,
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
