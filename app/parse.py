from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com/"


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]

def get_all_quotes():
    text = requests.get(BASE_URL).content
    soup = BeautifulSoup(text, "html.parser")
    print(soup.prettify())

def main(output_csv_path: str) -> None:
    get_all_quotes()


if __name__ == "__main__":
    main("quotes.csv")
