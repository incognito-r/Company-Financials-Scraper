import streamlit as st
import os
from src.financial_tool import get_financials

def handle_user_inputs():
    """Handle user inputs for company name and financial parameter URLs."""
    company_name = st.text_input("Company Name:", placeholder="e.g., SBI")

    parameters = [
        'Balance Sheet', 'Profit Loss', 'Quarterly Results',
        'Half Yearly Results', 'Nine Months Results',
        'Yearly Results', 'Cash Flow', 'Ratios'
    ]

    selected_parameters = st.multiselect(
        "Select financial parameters for which you want to provide URLs:", parameters
    )

    user_links = {}
    if selected_parameters:
        st.subheader("Enter URLs:")
        for param in selected_parameters:
            placeholder = f"e.g., https://www.moneycontrol.com/financials/company/{param.lower().replace(' ', '-')}/SYMBOL#SYMBOL"
            user_links[param] = st.text_input(f"URL for {param}:", placeholder=placeholder)

    return company_name, user_links

def process_financials(company_name, user_links):
    """Process financial data based on user inputs."""
    if st.button("Submit URLs"):
        # Ensure all selected URLs are provided
        if all(user_links.get(param, '') for param in user_links):
            st.success("URLs submitted successfully!")
            st.write(f"Company Name: {company_name}")
            st.write("Here are the URLs you've provided:")
            st.json(user_links)

            try:
                # Scrape and process data
                data_path = get_financials(links=user_links, company_name=company_name)

                # Provide download button for the resulting file
                with open(data_path, "rb") as file:
                    file_bytes = file.read()

                st.download_button(
                    label="Download Excel File",
                    data=file_bytes,
                    file_name=os.path.basename(data_path),
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")

            finally:
                # Clean up temporary file
                if os.path.exists(data_path):
                    os.remove(data_path)
        else:
            st.error("Please fill in all URLs for the selected parameters before submitting.")

