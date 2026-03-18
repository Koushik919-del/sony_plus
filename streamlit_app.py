import streamlit as st

# Page Config
st.set_page_config(page_title="Sony+", layout="wide", initial_sidebar_state="collapsed")

# 1. Custom CSS: Fonts & Positioning
st.markdown("""
    <style>
    /* Import Google Fonts for the Subtext (Hacker/Monospace) and Body */
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&family=Roboto:wght@700&display=swap');

    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp {
        background: radial-gradient(circle, #001d5a 0%, #000000 100%);
    }

    /* THE FONT FIX: Creating a "Glitch" Text Layering Effect */
    /* This imitates the multi-colored, off-center text of Sony Pictures Animation */
    .sony-logo-container {
        position: relative;
        font-size: 160px !important; 
        font-weight: 800;
        text-align: center;
        margin-top: 80px;
        letter-spacing: -5px;
        font-family: 'Avenir Next', 'Arial Black', sans-serif; /* Thick, bold base */
    }

    /* Layer 1: The Cyan Shadow */
    .sony-logo-cyan {
        color: cyan;
        position: absolute;
        top: 2px;
        left: 2px;
        opacity: 0.7;
        z-index: 1;
        text-shadow: 0px 0px 20px cyan;
    }

    /* Layer 2: The Red Shadow */
    .sony-logo-red {
        color: #ff0055;
        position: absolute;
        top: -2px;
        left: -2px;
        opacity: 0.7;
        z-index: 1;
        text-shadow: 0px 0px 20px #ff0055;
    }

    /* Layer 3: The Main White Text */
    .sony-logo-main {
        color: white;
        position: relative;
        z-index: 2;
        text-shadow: 0px 0px 30px rgba(255, 255, 255, 0.8);
    }

    /* Subtext styling (Roboto Mono) */
    .experience-subtext {
        font-size: 26px;
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        margin-top: -30px;
        letter-spacing: 4px;
        text-transform: uppercase;
        font-family: 'Roboto Mono', monospace;
        font-weight: 300;
    }

    /* THE BUTTON FIX: Precise Widescreen Centering */
    .center-button-wrapper {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-top: 60px;
    }

    div.stButton > button:first-child {
        background-color: transparent;
        color: white;
        border: 2px solid white;
        border-radius: 0px;
        padding: 20px 70px;
        font-size: 20px;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: 0.3s cubic-bezier(0.19, 1, 0.22, 1); /* Snappy animation */
        position: relative;
        overflow: hidden;
    }

    div.stButton > button:first-child:hover {
        background-color: white;
        color: black;
        box-shadow: 0px 0px 40px #00d9ff;
        transform: scale(1.05); /* Scales up slightly */
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Render the Logo with Glitch Layering
# The text is rendered three times to create the layered effect
glitch_text = f"""
<div class="sony-logo-container">
    <span class="sony-logo-cyan">Sony+</span>
    <span class="sony-logo-red">Sony+</span>
    <span class="sony-logo-main">Sony+</span>
</div>
"""
st.markdown(glitch_text, unsafe_allow_html=True)

# 3. Render the Subtext
st.markdown('<p class="experience-subtext">An Experience Beyond the Screen</p>', unsafe_allow_html=True)

# 4. Render the Centered Button
# Wrapping the button in a div allows precise Flexbox centering
st.markdown('<div class="center-button-wrapper">', unsafe_allow_html=True)
if st.button("LOGIN TO THE MULTIVERSE"):
    st.toast("Authenticating DualSense...", icon="🎮")
    # Trigger the 'Transition' effect here
st.markdown('</div>', unsafe_allow_html=True)
