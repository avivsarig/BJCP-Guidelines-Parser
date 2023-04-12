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
    python main.py
    ```

2. The script will begin scraping the BJCP style guidelines and display progress in the terminal.

3. Upon completion, the parsed data will be saved to `data/output.json`.
