import streamlit as st
from app.styling import set_page_config, display_header, display_footer
from app.functions import handle_user_inputs, process_financials

# Set up the page styling and configuration
set_page_config()

# Display app header
display_header()

# Collect and handle user inputs
company_name, user_links = handle_user_inputs()

# Process user inputs and provide a download option
if company_name and user_links:
    process_financials(company_name, user_links)

# Display footer
display_footer()