import collections
import datetime as dt
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_age_since(establish_year):
    establish_date = dt.date(establish_year, 1, 1)
    time_passed = dt.date.today() - establish_date
    years = int(time_passed.days / 365.25)

    if years % 100 != 11 and years % 10 == 1:
        years_name = "год"
    elif years % 100 not in [12, 13, 14] and years % 10 in [2, 3, 4]:
        years_name = "года"
    else:
        years_name = "лет"

    return f"{years} {years_name}"


def main():
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
    )

    template = env.get_template("template.html")

    wines = pandas.read_excel(
        "wine.xlsx", na_values=" ", keep_default_na=False
    ).to_dict(orient="records")

    wines_categorised = collections.defaultdict(list)

    for wine in wines:
        wines_categorised[wine["Категория"]].append(wine)

    rendered_page = template.render(
        age=get_age_since(1920),
        wines_categorised=wines_categorised,
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
