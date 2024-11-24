# Company Financials Scraper

A Python tool to scrape financial data from URLs and save it in an Excel file within the `output` folder.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/incognito-r/Company-Financials-Scraper.git
    cd Company-Financials
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Edit the `main.py` file:
    - Set the company name.
    - Update the `links` dictionary with URLs for scraping.

2. Run `main.py`:

    ```bash
    python main.py
    ```

3. The financial data will be saved in the `output` folder as an Excel file.

## Dependencies

- `pandas`
- `requests`
- `beautifulsoup4`
- `lxml`
- `openpyxl`

