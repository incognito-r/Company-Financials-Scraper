import streamlit as st

def set_page_config():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Financials Scraper",
        layout="centered",  # centered, wide
        initial_sidebar_state="expanded", # collapsed, expanded
        page_icon="🦋",  # Adding a relevant emoji as the page icon
    )

def display_header():
    """Display the header of the web app."""
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #0073e6; font-family: 'Arial', sans-serif;">Financials Scraper</h1>
            <p style="color: #555; font-size: 1.2rem; font-family: 'Arial', sans-serif;">Enter the URLs for the financial parameters you want to scrape.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_footer():
    """Display a footer with developer credits."""
    st.markdown(
        """
        <div style="text-align: center; color: #aaa; font-size: 0.8rem;">
            <p>Developed by [Incognito-R] | © 2024</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_sidebar():
    """Display the sidebar with user-friendly sections."""
    # st.sidebar.title("Navigation")
    # st.sidebar.markdown("### Financial Parameters")
    # st.sidebar.markdown("Use this sidebar to quickly navigate the app and input required URLs.")
    # st.sidebar.info("Select the parameters for which you want to scrape data.")

