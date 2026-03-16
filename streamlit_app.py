import streamlit as st

# Page Config
st.set_page_config(page_title="Sony+", layout="wide", initial_sidebar_state="collapsed")

# 1. Custom CSS for the "Sony" Aesthetic
st.markdown("""
    <style>
    /* Hide the 'stupid' Streamlit header and footer to make it an 'Experience' */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp {
        background: radial-gradient(circle, #001d5a 0%, #000000 100%);
    }

    /* Massive Sony+ Logo */
    .sony-logo {
        font-size: 120px !important;
        font-weight: 800;
        color: white;
        text-align: center;
        margin-top: 100px;
        letter-spacing: -5px;
        text-shadow: 0px 0px 30px rgba(0, 217, 255, 0.8);
        font-family: 'Inter', sans-serif;
    }

    /* Subtext styling */
    .experience-subtext {
        font-size: 24px;
        color: #00d9ff;
        text-align: center;
        margin-top: -30px;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: 300;
    }

    /* Gritty Login Button */
    div.stButton > button:first-child {
        background-color: transparent;
        color: white;
        border: 2px solid white;
        border-radius: 0px;
        padding: 15px 50px;
        font-size: 20px;
        display: block;
        margin: 50px auto;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: white;
        color: black;
        box-shadow: 0px 0px 20px #00d9ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. The Layout
st.markdown('<p class="sony-logo">Sony+</p>', unsafe_allow_html=True)
st.markdown('<p class="experience-subtext">An Experience Beyond the Screen</p>', unsafe_allow_html=True)

# 3. The Login Interaction
if st.button("LOGIN TO THE MULTIVERSE"):
    st.balloons() # Temporary feedback
    st.success("Accessing Sony ecosystem...")
