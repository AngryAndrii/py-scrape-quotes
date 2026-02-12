from dataclasses import dataclass

BASE_URL = "https://quotes.toscrape.com/"


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]


def main(output_csv_path: str) -> None:
    pass


if __name__ == "__main__":
    main("quotes.csv")
