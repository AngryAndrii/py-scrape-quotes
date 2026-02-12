from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup, Tag

BASE_URL = "https://quotes.toscrape.com/"


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]

def parse_single_block(block: Tag) -> Quote:
    return Quote(
        text=block.select_one(".text").text,
        author=block.select_one(".author").text,
        tags=[tag.text for tag in block.select(".tag")]
    )

def get_all_quotes() -> list[Quote]:
    text = requests.get(BASE_URL).content
    soup = BeautifulSoup(text, "html.parser")
    blocks = soup.select(".quote")
    return [parse_single_block(block) for block in blocks]




def main(output_csv_path: str) -> None:
    get_all_quotes()


if __name__ == "__main__":
    main("quotes.csv")
