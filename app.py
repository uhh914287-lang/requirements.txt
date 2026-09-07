import streamlit as st
import streamlit.components.v1 as components
import os

# 1. إعداد الصفحة بأعلى معايير الأداء والملء الكامل للشاشة
st.set_page_config(
    page_title="أكاديمية السعيدة الإمبراطورية | Saba AI",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تصفير هوامش Streamlit لمنح تجربة تطبيق هجين أصيل
st.markdown("""
    <style>
        #MainMenu, footer, header { display: none !important; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
        iframe { border-radius: 0px !important; }
    </style>
""", unsafe_allowed_html=True)

# 3. قراءة الواجهة بأمان من ملف خارجي لمنع أخطاء الترجمة وعلامات الاقتباس
html_path = "index.html"
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        cyber_saba_app = f.read()
    components.html(cyber_saba_app, height=940, scrolling=False)
else:
    st.error("جاري تحميل واجهة التطبيق الذكي... يرجى التأكد من إضافة ملف index.html في حسابك.")
