from scrape import get_style_data
from utils import save_to_json

import string
import json

from urllib.parse import quote
from rich.progress import Progress


def scrape_bjcp_website(output_file=None):
    base_url = "https://www.bjcp.org/style/2021"
    styles_data = []

    with open(output_file, "a", encoding="utf-8") as f:
        f.write("[")
    with Progress() as progress:
        task = progress.add_task("Scraping...", total=34 * 10)
        for family_id in range(1, 35):
            family_id_encoded = quote(str(family_id))
            family_url = f"{base_url}/{family_id_encoded}"
            for letter in string.ascii_uppercase:
                letter_encoded = quote(letter)
                style_url = f"{family_url}/{family_id_encoded}{letter_encoded}"
                style_data = get_style_data(style_url)
                if style_data:
                    styles_data.append(style_data)
                    if output_file:
                        with open(output_file, "a", encoding="utf-8") as f:
                            f.write(json.dumps(style_data, ensure_ascii=False))
                            f.write(",\n")
                else:
                    break
                progress.advance(task)

    with open(output_file, "a", encoding="utf-8") as f:
        f.write("]")
    print("Done.")
    return styles_data


output_file = "data/output.json"
scrape_bjcp_website(output_file)
