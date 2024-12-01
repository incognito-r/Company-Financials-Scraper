# Company Financials Scraper

**Link to the App**: [Company Financials Scraper](https://company-financials-scrap.streamlit.app)

## About the Project

The **Company Financials Scraper** is a powerful web tool designed to scrape comprehensive financial data from the [Moneycontrol website](https://www.moneycontrol.com/). It simplifies the process of obtaining financial information for a company and allows users to download it as an Excel file for further analysis. 

### Features

- **Scrape Financial Data**: Extract detailed financial information for a selected company, including:
  - Balance Sheet
  - Profit and Loss Statement
  - Quarterly Results
  - Half-Yearly Results
  - Nine Months Results
  - Yearly Results
  - Cash Flow Statement
  - Financial Ratios
- **Excel Download**: Easily download the scraped data in a structured Excel file format.

## How to Use

1. Visit the [web app](https://company-financials-scrap.streamlit.app).
2. Enter the name or URL of the company whose financial data you want to scrape.
3. Select the financial report type (e.g., Balance Sheet, Profit & Loss, etc.).
4. Click on the "Download" button to export the data as an Excel file.


## Installation (for Local Setup)

If you'd like to run the scraper locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/incognito-r/Company-Financials-Scraper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd company-financials-scraper
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run main.py
   ```

## Contribute or Improve

If you'd like to contribute to this project or suggest improvements for the web app, feel free to get in touch! You can contact me at:

**Email**: [Contact Me](mailto:itsnovember10@gmail.com)  
**GitHub Issues**: [Open an issue on this repository](https://github.com/incognito-r/Company-Financials-Scraper/issues)


## Technology Stack

- **Frontend**: Streamlit - A Python-based framework for building interactive web apps.
- **Backend**: Web scraping scripts in Python using libraries like `requests`, `BeautifulSoup`, or others as needed.
- **Output Format**: Financial data is formatted and saved as an Excel file.