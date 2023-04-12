import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    response = requests.get(url)
    html_content = response.content
    return html_content


def get_style_data(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    style_name = soup.find("h1", class_="entry-title")
    style_description = soup.find(
        "div", class_="entry-content"
    )

    commercial_examples = soup.find("div", class_="commercial-examples")
    style_attributes = soup.find("div", class_="style-attributes")

    vital_statistics_table = soup.find("div", class_="vital-statistics")
    if not all([style_name, style_description, commercial_examples, style_attributes, vital_statistics_table]):
        return None
    
    commercial_examples = commercial_examples.text.strip()
    style_attributes = [
        tag.text for tag in style_attributes.find_all("a")
    ]

    rows = vital_statistics_table.find_all("div", class_="row")
    vital_statistics = {
        row.find("h3").text.strip().lower(): row.find("p").text.strip() for row in rows
    }

    return {
        "name": style_name.text.strip(),
        "description": style_description.text.strip(),
        "commercial_examples": commercial_examples,
        "style_attributes": style_attributes,
        "vital_statistics": vital_statistics,
    }




def extract_vital_stats(stats_dict):
    extracted_stats = {}

    for key, value in stats_dict.items():
        stat_range = value.split(" - ")
        extracted_stats[f"{key}_min"] = float(stat_range[0].rstrip('%'))
        extracted_stats[f"{key}_max"] = float(stat_range[1].rstrip('%'))

    return extracted_stats



def extract_style_data(url):
    data = get_style_data(url)

    name_text = data["name"].text.strip()
    designation, name = name_text.split(". ")

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
        div = data["description"].find("div", class_=characteristic)
        para = div.find("p")
        style[characteristic] = para.text.strip()

    vital_stats = extract_vital_stats(data["vital_statistics"])
    
    return {
        "style_designation": designation,
        "style_name": name,
        **style,
        **vital_stats,
        "commercial_examples": data["commercial_examples"],
        "style_attributes": data["style_attributes"],
    }
