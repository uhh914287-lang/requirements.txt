import streamlit as st
import streamlit.components.v1 as components
import os

# 1. App Main Configuration
st.set_page_config(
    page_title="أكاديمية السعيدة الإمبراطورية | Saba AI",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Streamlit Main UI elements
st.markdown("""
    <style>
        #MainMenu, footer, header { display: none !important; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
        iframe { border-radius: 0px !important; }
    </style>
""", unsafe_allowed_html=True)

# 3. Read and render the interface from external HTML file safely
html_file_path = "index.html"
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        cyber_saba_app_code = f.read()
    components.html(cyber_saba_app_code, height=940, scrolling=False)
else:
    st.error("جاري تحميل واجهة التطبيق الذكي... يرجى التأكد من إضافة ملف index.html في حسابك.")
