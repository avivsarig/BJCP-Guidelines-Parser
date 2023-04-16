# 🍺 BJCP Guidelines Parser 🍺

A simple Python script to scrape and parse the [Beer Judge Certification Program (BJCP)](https://www.bjcp.org/style/2021/) style guideline.

## Features

- 🌐 Scrapes beer style data from the BJCP website
- 🧹 Cleans and organizes data into a structured format
- 💾 Saves output to a JSON file for easy access
- ⏳ Resumes scraping from the last saved point if interrupted
- 📊 Displays progress with a CLI progress bar

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/yourusername/BJCP-Guidelines-Parser.git
    ```

2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```
    python src/main.py
    ```

2. The script will begin scraping the BJCP style guidelines and display progress in the terminal.

3. Upon completion, the parsed data will be saved to `data/output.json`.


## Style Description Format

For more information on the format of a style description, please refer to the [BJCP 2021 Style Guidelines Introduction](https://www.bjcp.org/beer-styles/introduction-to-the-2021-guidelines/).

## Example from the final JSON
```json
{
    "style_designation": "1A",
    "style_name": "American Light Lager",
    "overall-impression": "A highly carbonated, very light-bodied, nearly flavorless lager designed to be consumed very cold. Very refreshing and thirst-quenching.",
    "appearance": "Very pale straw to pale yellow color. White, frothy head seldom persists. Very clear.",
    "aroma": "Low malt aroma optional, but may be perceived as grainy, sweet, or corn-like, if present. Light spicy, floral, or herbal hop aroma optional. While a clean fermentation profile is desirable, a light amount of yeast character is not a fault.",
    "flavor": "Relatively neutral palate with a crisp, dry finish and a low to very low grainy or corn-like flavor that might be perceived as sweetness due to the low bitterness. Low floral, spicy, or herbal hop flavor optional, but is rarely strong enough to detect. Low to very low bitterness. Balance may vary from slightly malty to slightly bitter, but is usually close to even. High carbonation may accentuate the crispness of the dry finish. Clean fermentation profile.",
    "mouthfeel": "Very light, sometimes watery, body. Very highly carbonated with slight carbonic bite on the tongue.",
    "comments": "Designed to appeal to as broad a range of the general public as possible. Strong flavors are a fault. With little malt or hop flavor, the yeast character often is what most differentiates brands.",
    "history": "Coors briefly made a light lager in the early 1940s. Modern versions were first produced by Rheingold in 1967 to appeal to diet-conscious drinkers, but only became popular starting in 1973 after Miller Brewing acquired the recipe and marketed the beer heavily to sports fans with the “tastes great, less filling” campaign. Beers of this genre became the largest sellers in the United States in the 1990s.",
    "ingredients": "Two- or six-row barley with up to 40% rice or corn as adjuncts. Additional enzymes can further lighten the body and lower carbohydrates. Lager yeast. Negligible hops.",
    "style-comparison": "A lighter-bodied, lower-alcohol, lower calorie version of an American Lager. Less hop character and bitterness than a German Leichtbier.",
    "ibu_min": 8.0,
    "ibu_max": 12.0,
    "srm_min": 2.0,
    "srm_max": 3.0,
    "og_min": 1.028,
    "og_max": 1.04,
    "fg_min": 0.998,
    "fg_max": 1.008,
    "abv_min": 2.8,
    "abv_max": 4.2,
    "commercial_examples": "Bud Light, Coors Light, Grain Belt Premium Light American Lager, Michelob Light, Miller Lite, Old Milwaukee Light.",
    "style_attributes": [
        "balanced",
        "bottom-fermented",
        "lagered",
        "north-america",
        "pale-color",
        "pale-lager-family",
        "session-strength",
        "traditional-style"
    ]
}
