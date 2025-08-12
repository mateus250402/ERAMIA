import streamlit as st

def set_config(title: str):
    st.set_page_config(
        page_title=title,
        page_icon="🏥",
        layout="wide"
    )

def inject_css():
    st.markdown("""
    <style>
        .stButton > button {
            background: linear-gradient(90deg, #2E86AB, #5DADE2);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: bold;
        }
        .custom-title {
            background: linear-gradient(90deg, #2E86AB 0%, #5DADE2 100%);
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .custom-title h1 {
            color: white;
            text-align: center;
            margin: 0;
        }
        .section-title {
            text-align: center;
            margin-top: 0.5rem;
            margin-bottom: 1.2rem;
            color: #2E86AB;
            font-weight: 600;
        }
        .result-indicator {
            text-align: center;
            margin-bottom: 1.5rem;
        }
        .result-indicator .icon-success {
            font-size: 2rem;
            color: #27ae60;
        }
        .result-indicator .icon-fail {
            font-size: 2rem;
            color: #c0392b;
        }
        .result-indicator .text-success {
            color: #27ae60;
            font-weight: bold;
            font-size: 1.3rem;
        }
        .result-indicator .text-fail {
            color: #c0392b;
            font-weight: bold;
            font-size: 1.3rem;
        }
        .filters-ul {
            padding-left: 20px;
        }
        .filters-li {
            margin-left: 20px;
        }
        .footer {
            text-align: center;
            color: #1B4F72;
            padding: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

def show_title(title: str):
    st.markdown(f"""<div class="custom-title"> <h1>🏥 {title}</h1></div> """, unsafe_allow_html=True)

def section_title(title: str, emoji: str = ""):
    st.markdown(
        f'<h3 class="section-title">{emoji} {title}</h3>',
        unsafe_allow_html=True
    )

def show_footer():
    st.markdown("""
    <div class="footer">
        <small>🏥 Sistema desenvolvido para auxílio ao diagnóstico médico • Versão 1.0</small>
    </div>
    """, unsafe_allow_html=True)
