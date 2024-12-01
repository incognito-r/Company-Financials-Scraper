import pandas as pd
import requests
from io import StringIO
from bs4 import BeautifulSoup

def get_financials(company_name, links):
    """
    Fetch financial data from multiple URLs, process the tables,
    and save them into an Excel file.

    Parameters:
    - links (dict): A dictionary where keys are sheet names and values are URLs.
    - company (str): The company name to use in the Excel file name.

    Returns:
    - str: Path to the saved Excel file.
    """
    # Create the output Excel file name
    file_path = f'output/{company_name}_Financials.xlsx'
    # Track if any sheet is written
    sheet_written = False
    
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for key, url in links.items():
            print(f"Processing {key}...\n")

            try:
                # Get HTML data
                response = requests.get(url)
                html_data = response.content

                # Parse the HTML
                soup = BeautifulSoup(html_data, 'html.parser')

                # Get table
                table = StringIO(str(soup.find_all('table', class_='mctable1')))

                # Convert to DataFrame
                df = pd.read_html(table)[0]  # Using pandas to read the HTML table
                df.drop(df.columns[-1], axis=1, inplace=True)  # Drop the last column
                df.columns = df.iloc[0]  # Set the first row as column headers
                df = df[1:]  # Drop the first row (header row)
                
                # Enable silent downcasting
                pd.set_option('future.no_silent_downcasting', True)

                mask = df.iloc[:, 1:].isnull().all(axis=1)
                df['Category'] = df.iloc[:, 0].where(mask)
                df['Category'] = df['Category'].ffill()  # Forward fill categories
                df = df[~mask]

                df.set_index(['Category', df.iloc[:, 0]], inplace=True)
                df = df.iloc[:, 1:]

                # Write DataFrame to Excel
                df.to_excel(writer, sheet_name=key, index=True)
                sheet_written = True  # Mark that at least one sheet is written

            except Exception as e:
                print(f"Error processing {key}: {e}\n")
                continue

    if not sheet_written:
        raise ValueError("No valid data to write to Excel. Ensure the links contain valid tables.")

    print(f"Financial data successfully saved to {file_path}")

    return file_path
