import DB_Creation as crt_db
import User as user
import mysql.connector as conn
import streamlit as st
from streamlit_option_menu import option_menu as om
import Home
import Login
import Signup

st.set_page_config(
    page_title="Career Recommendation System",
    page_icon="🌟"
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def run():
    # Sidebar Navigation
    with st.sidebar:
        page = om(
            menu_title="Navigation",
            options=["Home", "Login", "Signup"],
            icons=["house-fill", "person-fill", "pencil-square"],
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#f8f9fa"},
                "icon": {"color": "black", "font-size": "25px"}, 
                "nav-link": {"color": "black", "font-size": "18px", "text-align": "left"},
                "nav-link-selected": {"background-color": "#007bff"},
            },
        )

    # Page Content
    if page == "Home":
        if st.session_state["logged_in"]:
            Home.run()
        else:
            st.warning("You haven't logged in yet. Please log in first!")
    elif page == "Login":
        Login.run()
    elif page == "Signup":
        Signup.run()

if __name__ == "__main__":
    crt_db.db_creation()
    run()