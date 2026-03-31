# app.py

import streamlit as st
from prompts import (
    generate_code,
    explain_code,
    explain_code_simple,
    debug_code,
    explain_concept
)
from llm import ask_llm


# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="AI Coding Assistant",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Advanced Modern UI Styling
# --------------------------------------------------
st.markdown("""
<style>

/* Global Background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(10px);
}

/* Main container spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Title */
h1 {
    font-size: 2.5rem;
    font-weight: 800;
    color: #ffffff;
}

/* Card effect */
.custom-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 25px;
    border-radius: 16px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Labels */
label {
    color: #f1f5f9 !important;
    font-weight: 600 !important;
}

/* Inputs */
textarea, input, select {
    background-color: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
}

/* Neon Buttons */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6em 1.4em;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,114,255,0.4);
}

div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(0,114,255,0.7);
}

/* Response Box */
.response-box {
    background: rgba(0,0,0,0.6);
    padding: 20px;
    border-radius: 15px;
    color: #f8fafc;
    margin-top: 15px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.4);
}

/* Code block */
pre {
    background-color: rgba(0,0,0,0.75) !important;
    border-radius: 12px !important;
    padding: 15px !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

.stApp {
    background-image: 
        linear-gradient(rgba(15,23,42,0.8), rgba(15,23,42,0.8)),
        url("https://media.istockphoto.com/id/1488335095/vector/3d-vector-robot-chatbot-ai-in-science-and-business-technology-and-engineering-concept.jpg?s=612x612&w=0&k=20&c=MSxiR6V1gROmrUBe1GpylDXs0D5CHT-mn0Up8D50mr8=");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 AI Coding Assistant")


# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("⚡ Features")

option = st.sidebar.radio(
    "Choose a tool:",
    [
        "Generate Code",
        "Explain Code",
        "Explain Simply",
        "Debug Code",
        "Explain Concept"
    ]
)

if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = None

if "last_reply" not in st.session_state:
    st.session_state.last_reply = None

prompt = None


# --------------------------------------------------
# Feature Sections
# --------------------------------------------------

if option == "Generate Code":
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        language = st.selectbox(
            "Programming Language",
            ["Python", "Java", "C", "C++", "JavaScript"]
        )

    with col2:
        level = st.selectbox(
            "Difficulty Level",
            ["Beginner", "Intermediate", "Advanced"]
        )

    problem = st.text_area("Enter the problem statement")

    st.markdown('</div>', unsafe_allow_html=True)

    if problem:
        prompt = generate_code(language, problem, level)


elif option == "Explain Code":
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    code = st.text_area("Paste your code here")
    st.markdown('</div>', unsafe_allow_html=True)

    if code:
        prompt = explain_code(code)


elif option == "Explain Simply":
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    code = st.text_area("Paste your code here")
    st.markdown('</div>', unsafe_allow_html=True)

    if code:
        prompt = explain_code_simple(code)


elif option == "Debug Code":
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    code = st.text_area("Paste the code")
    error = st.text_area("Paste the error message")
    st.markdown('</div>', unsafe_allow_html=True)

    if code and error:
        prompt = debug_code(code, error)


elif option == "Explain Concept":
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    concept = st.text_area("Enter the concept")
    st.markdown('</div>', unsafe_allow_html=True)

    if concept:
        prompt = explain_concept(concept)


# --------------------------------------------------
# Action Buttons
# --------------------------------------------------
col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("🚀 Ask AI"):
        if prompt:
            st.session_state.last_prompt = prompt
            st.session_state.last_reply = ask_llm(prompt)
        else:
            st.warning("Please provide input.")

with col2:
    if st.button("🔄 Regenerate"):
        if st.session_state.last_prompt:
            st.session_state.last_reply = ask_llm(
                st.session_state.last_prompt
            )

with col3:
    if st.button("🗑 Clear"):
        st.session_state.last_prompt = None
        st.session_state.last_reply = None
        st.rerun()


# --------------------------------------------------
# Output Section
# --------------------------------------------------
if st.session_state.last_reply:
    st.markdown("## 🤖 AI Response")

    if option == "Generate Code":
        st.code(st.session_state.last_reply)
    else:
        st.markdown(
            f'<div class="response-box">{st.session_state.last_reply}</div>',
            unsafe_allow_html=True
        )