import streamlit as st

# Page Config
st.set_page_config(page_title="Sony+", layout="wide", initial_sidebar_state="collapsed")

# 1. Custom CSS: Fonts & Positioning
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&family=Roboto:wght@900&display=swap');

    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp {
        background: radial-gradient(circle, #001d5a 0%, #000000 100%);
    }

    /* THE FIX: Container must have a height to hold absolute elements */
    .sony-logo-container {
        position: relative;
        height: 220px;
        width: 100%;
        margin-top: 80px;
        text-align: center;
    }

    /* Base style for all layers */
    .glitch-layer {
        position: absolute;
        width: 100%;
        left: 50%;
        transform: translateX(-50%);
        font-size: 160px !important;
        font-weight: 900;
        letter-spacing: -5px;
        font-family: 'Roboto', sans-serif;
        text-transform: uppercase;
    }

    .sony-logo-cyan {
        color: #00fbff;
        top: 4px;
        left: calc(50% + 4px);
        opacity: 0.6;
        z-index: 1;
    }

    .sony-logo-red {
        color: #ff0055;
        top: -4px;
        left: calc(50% - 4px);
        opacity: 0.6;
        z-index: 1;
    }

    .sony-logo-main {
        color: white;
        z-index: 2;
        text-shadow: 0px 0px 40px rgba(255, 255, 255, 0.4);
    }

    .experience-subtext {
        font-size: 24px;
        color: rgba(0, 217, 255, 0.8);
        text-align: center;
        margin-top: 20px;
        letter-spacing: 6px;
        text-transform: uppercase;
        font-family: 'Roboto Mono', monospace;
    }

    /* BUTTON FIX: Standard Streamlit buttons are hard to center without this specific wrapper */
    .center-btn {
        display: flex;
        justify-content: center;
        padding-top: 50px;
    }

    div.stButton > button:first-child {
        background-color: transparent;
        color: white;
        border: 2px solid white;
        border-radius: 0px;
        padding: 15px 50px;
        font-size: 18px;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        letter-spacing: 2px;
        transition: 0.3s;
    }

    div.stButton > button:first-child:hover {
        background-color: white;
        color: black;
        box-shadow: 0px 0px 30px #00fbff;
        transform: translateY(-3px);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Render the Stacked Logo
st.markdown(f"""
<div class="sony-logo-container">
    <div class="glitch-layer sony-logo-cyan">Sony+</div>
    <div class="glitch-layer sony-logo-red">Sony+</div>
    <div class="glitch-layer sony-logo-main">Sony+</div>
</div>
""", unsafe_allow_html=True)

# 3. Render the Subtext
st.markdown('<p class="experience-subtext">An Experience Beyond the Screen</p>', unsafe_allow_html=True)

# 4. Render the Centered Button
_, col2, _ = st.columns([1, 1, 1])
with col2:
    if st.button("LOGIN TO THE MULTIVERSE"):
        st.toast("Syncing DualSense Controller...", icon="🎮")
