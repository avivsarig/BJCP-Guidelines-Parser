from scrape import get_style_data, extract_style_data
from utils import pretty_print
import string

def scrape_bjcp_website():
    base_url = "https://www.bjcp.org/style/2021"
    styles_data = []

    for family_id in range(1, 35):
        family_url = f"{base_url}/{family_id}"
        for letter in string.ascii_uppercase:
            style_url = f"{family_url}/{family_id}{letter}"
            print(f"Scraping {style_url}...")
            style_data = get_style_data(style_url)
            if style_data:
                pretty_print(style_data)
                styles_data.append(style_data)
            else: break

    return styles_data



pretty_print(scrape_bjcp_website())