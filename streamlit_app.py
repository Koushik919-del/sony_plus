import streamlit as st
from streamlit_google_auth import Authenticate

st.write(st.experimental_get_query_params())
st.write(dict(st.context.headers))

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

    .sony-logo-container {
        position: relative;
        height: 220px;
        width: 100%;
        margin-top: 80px;
        text-align: center;
    }

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

# Define the HTML for the logo so it can be reused in the logic below
logo_html = f"""
<div class="sony-logo-container">
    <div class="glitch-layer sony-logo-cyan">Sony+</div>
    <div class="glitch-layer sony-logo-red">Sony+</div>
    <div class="glitch-layer sony-logo-main">Sony+</div>
</div>
"""

import json

# Build and write client_secrets.json
client_secrets_dict = {
    "web": {
        "client_id": st.secrets["GOOGLE_CLIENT_ID"],
        "client_secret": st.secrets["GOOGLE_CLIENT_SECRET"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "redirect_uris": ["https://sony-plus.streamlit.app/_stcore/host-config"]
    }
}

with open("client_secrets.json", "w") as f:
    json.dump(client_secrets_dict, f)

# --- SINGLE authenticator instance ---
try:
    authenticator = Authenticate(
        secret_credentials_path="client_secrets.json",
        cookie_name="sony_plus_auth",
        cookie_key=st.secrets["GOOGLE_AUTH_SECRET"],
        redirect_uri="https://sony-plus.streamlit.app/_stcore/host-config",
    )
except Exception as e:
    st.error(f"Handshake failed: {e}")
    st.stop()

# --- THE GATEKEEPER LOGIC ---
is_logged_in = authenticator.check_authentification()

if not is_logged_in:
    # Render the Stacked Logo
    st.markdown(logo_html, unsafe_allow_html=True)

    # Render the Subtext
    st.markdown('<p class="experience-subtext">An Experience Beyond the Screen</p>', unsafe_allow_html=True)
    
    # Center and Render Login Button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        authenticator.login()

else:
    # --- INTERNAL DASHBOARD ---
    st.markdown(logo_html, unsafe_allow_html=True)
    st.markdown(f"### Welcome to the Multiverse, {st.session_state.get('name', 'User')}")
    st.write("Fetching your Sony Pictures library...")
    
    if st.button("Log Out"):
        authenticator.logout()
