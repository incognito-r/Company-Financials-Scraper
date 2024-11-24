import pandas as pd
import requests
from io import StringIO
from bs4 import BeautifulSoup

def get_financials(links, company):
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
    output_file = f'Output/{company}_Financials.xlsx'
    # Track if any sheet is written
    sheet_written = False
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
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
                df.drop(columns=6, inplace=True)  # Drop column 6
                df.columns = df.iloc[0]  # Set the first row as column headers
                df = df[2:]  # Drop the first two rows
                df = df.set_index(df.columns[0])  # Set the first column as index
                df = df.dropna(how='all')  # Drop rows with all NaN values
                df.reset_index(inplace=True)  # Reset index
                df = df.T  # Transpose the DataFrame
                df.columns = df.iloc[0]  # Set the first row as column headers
                df = df[1:]  # Drop the header row
                df.index.name = 'Date'  # Name the index as 'Date'
                df.columns.name = None  # Remove column group name

                # Write DataFrame to Excel
                df.to_excel(writer, sheet_name=key)
                sheet_written = True  # Mark that at least one sheet is written

            except Exception as e:
                print(f"Error processing {key}: {e}\n")
                continue

    if not sheet_written:
        raise ValueError("No valid data to write to Excel. Ensure the links contain valid tables.")

    print(f"Financial data successfully saved to {output_file}")
    return output_file
