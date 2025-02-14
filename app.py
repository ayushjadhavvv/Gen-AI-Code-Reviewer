import streamlit as st
import google.generativeai as genai
import os
import json
import time
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Streamlit UI Configuration
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

# Custom CSS for Center Alignment & Styling
st.markdown(
    """
    <style>
    /* Center-align everything */
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    
    h1, h2, h3, h4, h5, h6 {
        text-align: center !important;
    }

    /* Reduce height and center align the text area */
    .stTextArea textarea {
        text-align: center;
        font-size: 14px;
        font-family: 'Source Code Pro', monospace;
        height: 100px !important;  /* Adjusted Height */
        width: 80% !important;  /* Makes it narrower */
        margin: auto;
        display: block;
    }

    .stButton > button {
        display: block;
        margin: auto;
        background-color: #FF4B4B;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #FF3333;
    }

    .report-text {
        background-color: #1e1e1e;
        color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-size: 16px;
    }

    .stDownloadButton {
        display: flex;
        justify-content: center;
    }

    .st-expander {
        text-align: center;
    }

    .stCheckbox {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom Header
st.markdown("<h1>🤖 Aapka AI Code Reviewer Dost</h1>", unsafe_allow_html=True)
st.write("<h3>💡 Paste your Python code below and get AI-powered feedback on Bugs, Optimizations, and Best Practices.</h3>", unsafe_allow_html=True)

# Center-align Content
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Smaller Code Input Box (Centered)
user_code = st.text_area("📝 Enter Your Python Code Here:", height=100, key="code_input")  # Reduced height

# History of previous submissions
if "history" not in st.session_state:
    st.session_state.history = []

# Dark Mode Toggle
dark_mode = st.checkbox("🌙 Dark Mode", value=False)

# Process Code Review
if st.button("🔎 Review Code"):
    if user_code.strip():
        with st.spinner("🔄 Analyzing your code with AI..."):
            try:
                model = genai.GenerativeModel("gemini-pro")  # Free-tier model
                response = model.generate_content(f"Review this Python code and identify issues:\n{user_code}")

                # Store history
                st.session_state.history.append({"code": user_code, "review": response.text})

                # Display AI response in collapsible sections
                st.subheader("📌 AI Code Review Summary")
                st.markdown(f"<div class='report-text'>{response.text}</div>", unsafe_allow_html=True)

                # Add option to download report
                report_filename = "AI_Code_Review.txt"
                with open(report_filename, "w") as f:
                    f.write(response.text)
                st.download_button("📥 Download Report", report_filename, file_name="AI_Code_Review.txt")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter some Python code before submitting.")

# Show History
st.subheader("📜 Review History")
if st.session_state.history:
    for idx, entry in enumerate(reversed(st.session_state.history)):
        with st.expander(f"📌 Review {idx+1}"):
            st.code(entry["code"], language="python")
            st.text_area("💡 AI Review:", entry["review"], height=150)

# Live AI Analysis (Real-time Feedback)
if user_code.strip():
    with st.spinner("⚡ Live AI Analysis in progress..."):
        time.sleep(1)
        model = genai.GenerativeModel("gemini-pro")
        live_response = model.generate_content(f"Give a brief analysis of the following Python code:\n{user_code[:200]}")
        st.markdown(f"<h3>🚀 Live Analysis: {live_response.text}</h3>", unsafe_allow_html=True)

# Close the centered div
st.markdown("</div>", unsafe_allow_html=True)