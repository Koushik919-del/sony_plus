import streamlit as st

# 1. Page Configuration (The "Experience" Meta-Data)
st.set_page_config(
    page_title="Sony+", 
    page_icon="🎮", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. The "Gritty" Sony Styling (CSS)
st.markdown("""
    <style>
    /* Main Background - PlayStation Deep Blue Radial Gradient */
    .stApp {
        background: radial-gradient(circle, #003087 0%, #000000 100%);
        color: white;
    }
    
    /* Custom Font Styling */
    h1 {
        font-family: 'Inter', sans-serif;
        letter-spacing: -2px;
        text-shadow: 0px 0px 20px rgba(0, 217, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Startup Logo
st.title("Sony+")
st.subheader("An Experience Beyond the Screen")

# 4. Placeholder for your Portal Loading Minigame
st.info("Preparing the Multiverse... (Your Dr. Strange Portal will load here)")
