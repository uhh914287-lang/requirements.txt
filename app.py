import streamlit as st
import google.generativeai as genai
import random

# 1. إعدادات المنصة الأساسية
st.set_page_config(page_title="Al-Saeeda AI Academy", page_icon="🇾🇪", layout="wide")

# 2. إعداد مفتاح الذكاء الاصطناعي
if "GENAI_KEY" in st.secrets:
    API_KEY = st.secrets["GENAI_KEY"]
else:
    API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if API_KEY and API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=API_KEY)

# 🗺️ العناوين الرئيسية للمنصة (بدون أكواد CSS معقدة لضمان التشغيل)
st.title("🇾🇪 أكاديمية السعيدة الدولية للغات")
st.subheader("أول منصة سينمائية وتفاعلية مدعومة بالذكاء الاصطناعي لتعلم الإنجليزية في الشرق الأوسط")
st.markdown("---")

# 3. نظام تتبع النقاط التفاعلي (Duolingo Style XP)
if "xp" not in st.session_state:
    st.session_state.xp = random.randint(120, 250)

st.sidebar.metric(label="⚡ رصيد نقاطك الحالي (XP):", value=f"{st.session_state.xp} 🔥")
st.sidebar.markdown("---")

user_profile = st.sidebar.selectbox("🎯 اختر فئتك التعليمية:", ["🧸 قسم الأطفال والناشئين", "💼 قسم الكبار والمحترفين"])
menu_hub = st.sidebar.radio("📂 تصفح استوديو المنصة:", ["🎬 سينما التعلم وبوت النطق", "🚀 حقيبة المناهج العالمية"])

sys_instruction = "You are a master English AI professor. Explain concepts smoothly using an elite mix of simple Arabic and expert English."

# --- تشغيل وظائف المنصة ---

if menu_hub == "🎬 سينما التعلم وبوت النطق":
    tab_chat, tab_mic = st.tabs(["💬 شات المعيل الذكي", "🎙️ مختبر تصحيح النطق بالمايك"])
    
    with tab_chat:
        st.write("🤖 **السينما الافتراضية والشارح الذكي:** اكتب أي قاعدة لغوية؛ سيشرحها البوت باللغتين وينطقها أوتوماتيكياً!")
        user_input = st.text_input("اسأل المحاور الافتراضي هنا:")
        
        if user_input and API_KEY:
            with st.spinner("جاري صياغة الرد التعليمي..."):
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
        st.write("🎙️ **تحدي النطق الصوتي الفوري:** اضغط على زر المايك بالأسفل واقرأ هذه الجملة بدقة وبصوتك:")
        st.warning(f"الجملة المطلوبة: {test_phrase}")
        
        mic_js_code = f"""
        <div style="text-align: center; margin-top: 10px;">
            <button id="mButton" style="background-color: #58cc02; color: white; border: none; padding: 16px 36px; font-size: 16px; border-radius: 12px; cursor: pointer; font-weight: bold;">
                🎤 اضغط الآن وتحدث بالجملة بوضوح
            </button>
            <p id="status" style="color: #666; margin-top: 12px;">انطق الجملة ليقوم الذكاء الاصطناعي برصد مخارج الحروف الفورية...</p>
            <div id="resultBox" style="margin-top: 15px; padding: 15px; border-radius: 12px; display: none; background-color: #f8f9fa; direction: ltr; text-align: left; color: black;">
                <p><b>Your Input:</b> <span id="userText" style="color: #58cc02; font-weight:bold;"></span></p>
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
            }});
            r.addEventListener('result', (e) => {{
                const res = e.results.transcript;
                uText.innerText = res;
                if (res.toLowerCase().trim() === target) {{
                    score.innerText = "🟢 Perfect Pronunciation (100%)! Excellent.";
                }} else {{
                    score.innerText = "🟡 Good Attempt! Try again focusing on clarity.";
                }}
                box.style.display = "block"; status.innerText = "تم التحليل بنجاح!";
            }});
        }}
        </script>
        """
        st.components.v1.html(mic_js_code, height=230)

elif menu_hub == "🚀 حقيبة المناهج العالمية":
    st.markdown("### 🚀 حقائب كورسات البث والتعلم المباشر")
    st.info("🇺🇸 **مسار إنجليزية الأعمال والتوظيف - جامعة بنسلفانيا**")
    st.markdown("[🔗 اضغط هنا لبدء التدريب فورا عبر Coursera](https://coursera.org)")
    st.markdown("---")
    st.info("🇬🇧 **أكاديمية المجلس الثقافي البريطاني الشاملة - British Council**")
    st.markdown("[🔗 اضغط هنا لإجراء اختبار المستوى والتعلم](https://britishcouncil.org)")
