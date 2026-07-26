import streamlit as st
from translator import translate

# Set up page configurations
st.set_page_config(
    page_title="NMT English to French Translator",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for a professional and premium feel
st.markdown("""
<style>
    /* Styling the main container */
    .reportview-container {
        background: #f5f7f8;
    }
    
    /* Title and Subtitle styling */
    .main-title {
        color: #1E3A8A;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #4B5563;
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Custom Translate Button */
    div.stButton > button:first-child {
        background-color: #2563EB;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.6rem 2.5rem;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
        transition: all 0.2s ease-in-out;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #1D4ED8;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3);
        transform: translateY(-1px);
    }
    
    /* Result Box styling */
    .result-box {
        background-color: #FFFFFF;
        border-left: 5px solid #10B981;
        padding: 1.5rem;
        border-radius: 4px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        margin-top: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar contents
st.sidebar.markdown("# 🌐 Neural Machine Translation")
st.sidebar.markdown(
    """
    This application utilizes a pre-trained **MarianMT** model to translate English text into French.
    
    ### Model Details
    - **Name:** `Helsinki-NLP/opus-mt-en-fr`
    - **Framework:** PyTorch & Transformers
    - **Language Pair:** English (en) ➡️ French (fr)
    
    ---
    ### How it works
    1. Enter your text in the English field.
    2. Click **Translate**.
    3. The model processes the tokens and outputs the French translation.
    """
)
st.sidebar.caption("Built with Streamlit and Hugging Face Transformers.")

# Main app structure
st.markdown('<h1 class="main-title">English to French Translator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">State-of-the-art Neural Machine Translation powered by MarianMT</p>', unsafe_allow_html=True)

# User input text area
english_text = st.text_area(
    "English Source Text:",
    placeholder="Enter the English text you would like to translate here...",
    height=200
)

# Translation trigger and logic
if st.button("Translate to French"):
    if not english_text.strip():
        st.warning("Please enter some English text to translate.")
    else:
        try:
            # Loading spinner
            with st.spinner("Translating... Please wait while the model processes your text."):
                french_translation = translate(english_text)
            
            # Display results
            st.subheader("French Translation:")
            st.markdown(
                f'<div class="result-box"><p style="font-size:1.15rem; color:#1F2937;">{french_translation}</p></div>',
                unsafe_allow_html=True
            )
            st.balloons()
            
        except Exception as e:
            st.error("An error occurred during translation.")
            st.exception(e)
