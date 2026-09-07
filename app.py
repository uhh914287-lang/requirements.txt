import streamlit as st
import streamlit.components.v1 as components
import os

# إعداد الصفحة لتظهر بحجم الهاتف بالكامل
st.set_page_config(
    page_title="أكاديمية السعيدة للإنجليزية الذكية",
    page_icon="🇾🇪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# إخفاء قوائم Streamlit الافتراضية لمنح المستخدم تجربة تطبيق هاتف كامل
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 480px !important; margin: auto;}
    </style>
""", unsafe_allowed_html=True)

# قراءة واجهة الهاتف الذكي بأمان من ملف خارجي لمنع أخطاء علامات الاقتباس والأقواس
html_path = "index.html"
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=920, scrolling=False)
else:
    st.error("جاري تحميل واجهة التطبيق الذكي... يرجى التأكد من إضافة ملف index.html في حسابك.")
