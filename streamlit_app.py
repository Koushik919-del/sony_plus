import streamlit as st

# Page Config
st.set_page_config(page_title="Sony+", layout="wide", initial_sidebar_state="collapsed")

# 1. Custom CSS: Fonts & Centering
st.markdown("""
    <style>
    /* Import Google Fonts: Clarendon-style (Slab Serif) and Roboto */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Arvo:wght@700&display=swap'); /* Good Clarendon alternative */

    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp {
        background: radial-gradient(circle, #001d5a 0%, #000000 100%);
    }

    /* Massive Sony+ Logo (Arvo is a slab-serif that mimics Clarendon) */
    .sony-logo {
        font-size: 160px !important; /* Made even bigger */
        font-weight: 700;
        color: white;
        text-align: center;
        margin-top: 80px;
        letter-spacing: -2px;
        text-shadow: 0px 0px 40px rgba(0, 217, 255, 0.6);
        font-family: 'Arvo', serif;
    }

    /* Subtext styling (Roboto Light) */
    .experience-subtext {
        font-size: 26px;
        color: #00d9ff;
        text-align: center;
        margin-top: -40px;
        letter-spacing: 5px;
        text-transform: uppercase;
        font-family: 'Roboto', sans-serif;
        font-weight: 300;
        opacity: 0.9;
    }

    /* THE CENTERING FIX: Using a Flexbox container for the button */
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 60px;
    }

    div.stButton > button:first-child {
        background-color: transparent;
        color: white;
        border: 2px solid white;
        border-radius: 0px;
        padding: 18px 60px;
        font-size: 22px;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        letter-spacing: 2px;
        transition: 0.4s ease-in-out;
    }

    div.stButton > button:first-child:hover {
        background-color: white;
        color: black;
        box-shadow: 0px 0px 30px #00d9ff;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Render the Logo and Subtext
st.markdown('<p class="sony-logo">Sony+</p>', unsafe_allow_html=True)
st.markdown('<p class="experience-subtext">An Experience Beyond the Screen</p>', unsafe_allow_html=True)

# 3. Render the Centered Button
# We use st.columns to help with positioning in Streamlit's grid
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    if st.button("LOGIN TO THE MULTIVERSE"):
        st.toast("Authenticating DualSense...", icon="🎮")
