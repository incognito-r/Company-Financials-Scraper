import streamlit as st
import os
import src


# App title and description
st.title("Financials Scraper")
st.text("Enter the URLs for the financial parameters you want to scrape:")

# Input field for company name
company_name = st.text_input("Company Name:", placeholder="e.g., SBI")

# Define the financial parameters
parameters = [
    'Balance Sheet',
    'Profit Loss',
    'Quarterly Results',
    'Half Yearly Results',
    'Nine Months Results',
    'Yearly Results',
    'Cash Flow',
    'Ratios'
]

# User selects parameters they want to input URLs for
selected_parameters = st.multiselect("Select financial parameters for which you want to provide URLs:", parameters)

# Dictionary to store user input links
user_links = {}
if selected_parameters:
    st.subheader("Enter URLs:")
    for param in selected_parameters:
        text = f"URL for {param}:"
        placeholder = f"e.g., https://www.moneycontrol.com/financials/company/{param.lower().replace(' ', '-')}/SYMBOL#SYMBOL"
        user_links[param] = st.text_input(text, placeholder=placeholder)

# Button to display entered URLs
if st.button("Submit URLs"):
    
    # Check if all selected URLs are filled
    if all(user_links.get(param, '') for param in selected_parameters):
        st.success("URLs submitted successfully!")
        st.write(f"Company Name: {company_name}")
        st.write("Here are the URLs you've provided:")
        st.json(user_links)

        # Pass the ordered links to your scraping function
        data_path = src.get_financials(links=user_links, company_name=company_name)

        # Provide a download button for the Excel file
        try:
            with open(data_path, "rb") as file:
                file_bytes = file.read()

            st.download_button(
                label="Download Excel File",
                data=file_bytes,
                file_name=data_path.split('/')[-1],  # Extract the file name
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        finally:
            # Delete the file after it is read
            if os.path.exists(data_path):
                os.remove(data_path)

    else:
        st.error("Please fill in all URLs for the selected parameters before submitting.")
