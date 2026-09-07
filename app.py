import streamlit as st
import google.generativeai as genai
import random

# 1. Platform Core & Theme Setup
st.set_page_config(page_title="Al-Saeeda AI Academy", page_icon="🇾🇪", layout="wide")

# 2. Secure AI Configuration
if "GENAI_KEY" in st.secrets:
    API_KEY = st.secrets["GENAI_KEY"]
else:
    API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if API_KEY and API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=API_KEY)

# 🎨 Netflix X Duolingo Premium Dark-Mode UI Configuration
# هذا الكود معزول تماماً ومحمي ضد الترجمة لمنع تعطل التطبيق
app_css = """
<style>
    @import url('https://googleapis.com');
    
    /* Global Base styling */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0b0f12 !important;
        color: #e2e8f0 !important;
        font-family: 'Cairo', sans-serif !important;
    }
    
    /* Premium Netflix-style Top Banner */
    .netflix-banner {
        background: linear-gradient(135deg, #e50914 0%, #1a0204 60%, #0b0f12 100%);
        padding: 40px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(229,9,20,0.15);
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.05);
    }
    
    /* Duolingo-style Interactive Dashboard Cards */
    .duo-card {
        background-color: #13191c;
        border: 2px solid #232d32;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 0 #232d32;
    }
    .duo-card:hover {
        transform: translateY(-4px);
        border-color: #58cc02;
        box-shadow: 0 8px 0 #46a302;
    }
    
    /* Text Adjustments */
    .main-title { font-size: 2.8rem; font-weight: 700; color: #ffffff; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
    .sub-title { font-size: 1.2rem; color: #a0aec0; margin-top: 8px; }
    .card-title { color: #ffffff; font-size: 1.4rem; font-weight: 700; margin-bottom: 10px; display: flex; align-items: center; gap: 10px; }
    .card-text { color: #cbd5e0; font-size: 1rem; line-height: 1.6; }
</style>
"""
st.markdown(app_css, unsafe_allowed_html=True)

# Render Netflix Header
st.markdown("""
<div class="netflix-banner">
    <h1 class="main-title">🇾🇪 ACADEMY X</h1>
    <div class="sub-title">أول منصة سينمائية وتفاعلية مدعومة بالذكاء الاصطناعي لتعلم الإنجليزية في الشرق الأوسط</div>
</div>
""", unsafe_allowed_html=True)

# 3. Gamified Sidebar System (Duolingo Style XP)
if "xp" not in st.session_state:
    st.session_state.xp = random.randint(120, 250)

st.sidebar.markdown(f"""
<div style='background-color:#13191c; padding:20px; border-radius:16px; border:2px solid #232d32; text-align:center;'>
    <h3 style='color:white; margin:0;'>⚡ رصيد نقاطك الحالي</h3>
    <h1 style='color:#58cc02; margin:10px 0;'>🔥 {st.session_state.xp} XP</h1>
    <p style='color:#a0aec0; font-size:0.9rem; margin:0;'>استمر في التحدث مع البوت لمضاعفة النقاط!</p>
</div>
""", unsafe_allowed_html=True)

st.sidebar.markdown("---")
user_profile = st.sidebar.selectbox("🎯 اختر فئتك التعليمية:", ["🧸 قسم الأطفال والناشئين", "💼 قسم الكبار والمحترفين"])
menu_hub = st.sidebar.radio("📂 تصفح استوديو المنصة:", ["🎬 سينما التعلم وبوت النطق", "🚀 حقيبة المناهج العالمية"])

sys_instruction = "You are a master English AI professor. Explain concepts smoothly using an elite mix of simple Arabic and expert English."

# --- Engine Core Features ---

if menu_hub == "🎬 سينما التعلم وبوت النطق":
    tab_chat, tab_mic = st.tabs(["💬 شات المعلم الذكي الفاخر", "🎙️ مختبر معالجة وتصحيح النطق"])
    
    with tab_chat:
        st.markdown("""
        <div class="duo-card">
            <div class="card-title">🤖 السينما الافتراضية والشارح الذكي</div>
            <div class="card-text">اكتب أي قاعدة أو موضوع لغوي؛ سيقوم البوت بصياغة شرح سينمائي ممتع باللغتين ونطق ردوده أوتوماتيكياً بصوت نقي.</div>
        </div>
        """, unsafe_allowed_html=True)
        
        user_input = st.text_input("اسأل المحاور الافتراضي هنا:")
        if user_input and API_KEY:
            with st.spinner("جاري التوليد البصري واللغوي..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
                    response = model.generate_content(user_input)
                    st.info(response.text)
                    st.session_state.xp += 15
                    
                    clean_text = response.text.replace('\n', ' ').replace('"', '\\"').replace("'", "\\'")
                    st.components.v1.html(f"""
                        <script>
                        var speech = new SpeechSynthesisUtterance("{clean_text}");
                        speech.lang = 'en-US';
                        speech.rate = 0.92;
                        window.speechSynthesis.speak(speech);
                        </script>
                    """, height=0)
                except Exception as e:
                    st.error(f"Error: {e}")

    with tab_mic:
        test_phrase = "Learning English with games is very fun" if "الأطفال" in user_profile else "Global communication shapes the future of technology"
        st.markdown(f"""
        <div class="duo-card" style="border-color: #ff6e40; box-shadow: 0 4px 0 #ff6e40;">
            <div class="card-title" style="color: #ff6e40;">🎙️ تحدي النطق الصوتي الفوري</div>
            <div class="card-text">اضغط على زر المايك بالأسفل واقرأ هذه الجملة بدقة وبصوتك:</div>
            <h3 style="color: #ffffff; text-align: center; margin: 15px 0; font-family: monospace;">"{test_phrase}"</h3>
        </div>
        """, unsafe_allowed_html=True)
        
        mic_js_code = f"""
        <div style="text-align: center; margin-top: 10px;">
            <button id="mButton" style="background-color: #58cc02; color: white; border: none; padding: 16px 36px; font-size: 16px; border-radius: 12px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 0 #46a302; transition: 0.1s;">
                🎤 اضغط الآن وتحدث بالجملة بوضوح
            </button>
            <p id="status" style="color: #a0aec0; margin-top: 12px;">انطق الجملة ليقوم الذكاء الاصطناعي برصد مخارج الحروف الفورية...</p>
            <div id="resultBox" style="margin-top: 15px; padding: 15px; border-radius: 12px; display: none; background-color: #13191c; border: 2px solid #232d32; direction: ltr; text-align: left; color: white;">
                <p><b>Your Input:</b> <span id="userText" style="color: #58cc02;"></span></p>
                <p><b>AI Feedback:</b> <span id="score" style="font-weight: bold;"></span></p>
            </div>
        </div>
        <script>
        const btn = document.getElementById('mButton');
        const status = document.getElementById('status');
        const box = document.getElementById('resultBox');
        const uText = document.getElementById('userText');
        const score = document.getElementById('score');
        const target = "{test_phrase}".toLowerCase().trim();

        const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!Recognition) {{
            status.innerText = "المتصفح لا يدعم المايك، يرجى الفتح عبر Google Chrome.";
            btn.disabled = true;
        }} else {{
            const r = new Recognition(); r.lang = 'en-US';
            btn.addEventListener('click', () => {{ 
                r.start(); 
                status.innerText = "🎙️ جاري الاستماع لنطقك... تحدث الآن..."; 
                btn.style.transform = "translateY(4px)";
                btn.style.boxShadow = "none";
            }});
            r.addEventListener('result', (e) => {{
                const res = e.results.transcript;
                uText.innerText = res;
                if (res.toLowerCase().trim() === target) {{
                    score.innerText = "🟢 Perfect Pronunciation (100%)! Excellent.";
                }} else {{
                    score.innerText = "領 Good Attempt! Try again focusing on letter clarity.";
                }}
                box.style.display = "block"; status.innerText = "تم التحليل بنجاح!";
                btn.style.transform = "none";
                btn.style.boxShadow = "0 4px 0 #46a302";
            }});
        }}
        </script>
        """
        st.components.v1.html(mic_js_code, height=230)

elif menu_hub == "🚀 حقيبة المناهج العالمية":
    st.markdown("### 🚀 حقائب كورسات البث والتعلم المباشر")
    
    st.markdown("""
    <div class="duo-card">
        <div class="card-title">🇺🇸 مسار إنجليزية الأعمال والتوظيف - جامعة بنسلفانيا</div>
        <div class="card-text">منهج فاخر وتفاعلي بالكامل يعلم مهارات الإدارة والتواصل المباشر مع الشركات العالمية، متاح للدراسة الحرة مجاناً.</div>
        <p style="margin-top:12px;"><a href="https://coursera.org" target="_blank" style="color:#58cc02; font-weight:bold; text-decoration:none;">🔗 اضغط هنا لبدء التدريب فورا ←</a></p>
    </div>
    
    <div class="duo-card">
        <div class="duo-card-title" style="color:white; font-size:1.4rem; font-weight:bold; margin-bottom:10px;">🇬🇧 أكاديمية المجلس الثقافي البريطاني الشاملة - British Council</div>
        <div class="card-text">يحتوي على مسارات متدرجة من مستويات المبتدئين حتى الطلاقة الكاملة، مدعوماً ببنك أنشطة وقواعد يعمل بأقل استهلاك للإنترنت.</div>
        <p style="margin-top:12px;"><a href="https://britishcouncil.org" target="_blank" style="color:#58cc02; font-weight:bold; text-decoration:none;">🔗 اضغط هنا لإجراء اختبار المستوى والتعلم ←</a></p>
    </div>
    """, unsafe_allowed_html=True)
