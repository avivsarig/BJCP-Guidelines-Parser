import requests
import re
from bs4 import BeautifulSoup


def get_html_content(url):
    response = requests.get(url)
    html_content = response.content
    return html_content


def get_style_data(url):
    html_content = get_html_content(url)
    soup = BeautifulSoup(html_content, "html.parser")

    style_name = soup.find("h1", class_="entry-title")
    if not style_name:
        return None

    return extract_style_data(soup)


def extract_vital_stats(stats_dict):
    extracted_stats = {}

    for key, value in stats_dict.items():
        stat_range = value.split(" - ")
        min_value = "0"
        max_value = "0"

        if len(stat_range) >= 2:
            min_values = re.findall(r"[\d.]+", stat_range[0])
            max_values = re.findall(r"[\d.]+", stat_range[1])
            min_value = min_values[0] if min_values else "0"
            max_value = max_values[0] if max_values else "0"

        extracted_stats[f"{key}_min"] = float(min_value.rstrip("%"))
        extracted_stats[f"{key}_max"] = float(max_value.rstrip("%"))

    return extracted_stats


def extract_style_data(soup):
    name_text = soup.find("h1", class_="entry-title").text.strip()
    designation, name = name_text.split(". ")

    style_description = soup.find("div", class_="entry-content")
    commercial_examples = soup.find("div", class_="commercial-examples")
    style_attributes = soup.find("div", class_="style-attributes")
    vital_statistics_table = soup.find("div", class_="vital-statistics")

    commercial_examples = commercial_examples.text.strip()
    style_attributes = [tag.text for tag in style_attributes.find_all("a")]

    rows = vital_statistics_table.find_all("div", class_="row")
    vital_statistics = {
        row.find("h3").text.strip().lower(): row.find("p").text.strip() for row in rows
    }

    style = {}
    for characteristic in [
        "overall-impression",
        "appearance",
        "aroma",
        "flavor",
        "mouthfeel",
        "comments",
        "history",
        "ingredients",
        "style-comparison",
    ]:
        div = style_description.find("div", class_=characteristic)
        if div:
            para = div.find("p")
            style[characteristic] = para.text.strip()
        else:
            style[characteristic] = "N/A"

    vital_stats = extract_vital_stats(vital_statistics)

    return {
        "style_designation": designation,
        "style_name": name,
        **style,
        **vital_stats,
        "commercial_examples": commercial_examples,
        "style_attributes": style_attributes,
    }
