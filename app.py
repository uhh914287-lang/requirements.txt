import streamlit as st
import google.generativeai as genai
import random
from datetime import datetime

# 1. Platform Settings
st.set_page_config(page_title="أكاديمية اليمن الدولية للغات - AI", page_icon="🇾🇪", layout="wide")

# 2. API Key Configuration
if "GENAI_KEY" in st.secrets:
    GENAI_API_KEY = st.secrets["GENAI_KEY"]
else:
    GENAI_API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if GENAI_API_KEY and GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=GENAI_API_KEY)

# Modern Custom UI via text markdown
st.markdown("<h1 style='text-align:center; color:#1e3d59;'>🇾🇪 أكاديمية السعيدة الدولية للغات</h1>", unsafe_allowed_html=True)
st.markdown("<p style='text-align:center; color:#555;'>أول منصة يمنية وعربية مدعومة بالذكاء الاصطناعي لتعليم الإنجليزية من الصفر</p>", unsafe_allowed_html=True)

# Sidebar Menu
st.sidebar.markdown("### 🌐 لوحة التحكم التعليمية")
user_type = st.sidebar.radio("🎯 الفئة المستهدفة الحالية:", ["🧸 قسم الأطفال والناشئين", "💼 قسم الكبار والمحترفين"])
menu = st.sidebar.selectbox("📂 انتقل إلى:", ["🗣️ بوت التحدث وتصحيح النطق", "📚 المكتبة الذهبية العالمية", "📜 بوابة الشهادات المعتمدة"])

sys_instruction = (
    "You are an elite bilingual English professor. "
    "Explain all grammar concepts simply in both Arabic and English. "
    "Analyze the user's input, provide instant guidance, and correct any structural flaws."
)

# --- Features ---
if menu == "🗣️ بوت التحدث وتصحيح النطق":
    st.subheader("🤖 المحاور الذكي والمعلم الافتراضي:")
    user_query = st.text_input("اسأل عن أي قاعدة، أو اكتب جملة وترجمتها (مثال: شرح قاعدة Used to مع أمثلة):")
    
    if user_query and GENAI_API_KEY:
        with st.spinner("جاري صياغة الشرح الفوري بأعلى كفاءة تعليمية..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
                response = model.generate_content(user_query)
                st.info(response.text)
                
                clean_text = response.text.replace('\n', ' ').replace('\n', ' ').replace('"', '\\"').replace("'", "\\'")
                st.components.v1.html(f"""
                    <script>
                    var speech = new SpeechSynthesisUtterance("{clean_text}");
                    speech.lang = 'en-US';
                    speech.rate = 0.95;
                    window.speechSynthesis.speak(speech);
                    </script>
                """, height=0)
            except Exception as e:
                st.error(f"خطأ في الاتصال بالمحرك: {e}")

    st.markdown("---")
    st.subheader("🎙️ مختبر النطق والتصحيح الصوتي التفاعلي:")
    
    if "الأطفال" in user_type:
        test_sentence = "Learning English with games is very fun and easy"
    else:
        test_sentence = "Effective communication is the key to global professional success"
        
    st.warning(f"🎙️ الجملة المطلوب قراءتها الآن بصوتك: **{test_sentence}**")
    
    mic_js = f"""
    <div style="text-align: center; margin-top: 10px;">
        <button id="micBtn" style="background-color: #17b978; color: white; border: none; padding: 15px 35px; font-size: 16px; border-radius: 50px; cursor: pointer; font-weight: bold;">
            🎤 اضغط هنا وتحدث بالجملة بوضوح
        </button>
        <p id="status" style="color: #666; margin-top: 12px;">اضغط على الزر وابدأ النطق الفوري...</p>
        <div id="resultBox" style="margin-top: 15px; padding: 15px; border-radius: 12px; display: none; background-color: #f8f9fa; direction: ltr; text-align: left;">
            <p><b>Your Spoken Text:</b> <span id="userText" style="color: #1e3d59; font-weight: bold;"></span></p>
            <p><b>AI Evaluation:</b> <span id="score" style="font-weight: bold;"></span></p>
        </div>
    </div>
    <script>
    const micBtn = document.getElementById('micBtn');
    const status = document.getElementById('status');
    const resultBox = document.getElementById('resultBox');
    const userTextSpan = document.getElementById('userText');
    const scoreSpan = document.getElementById('score');
    const target = "{test_sentence}".toLowerCase().trim();

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {{
        status.innerText = "المتصفح لا يدعم المايك، يرجى الفتح من متصفح Google Chrome.";
        micBtn.disabled = true;
    }} else {{
        const recognition = new SpeechRecognition();
        recognition.lang = 'en-US';
        micBtn.addEventListener('click', () => {{
            recognition.start();
            status.innerText = "🎙️ جاري الاستماع لنطقك... تحدث الآن...";
        }});
        recognition.addEventListener('result', (e) => {{
            const result = e.results.transcript;
            userTextSpan.innerText = result;
            if (result.toLowerCase().trim() === target) {{
                scoreSpan.innerText = "🟢 Perfect Pronunciation (100%)!";
            }} else {{
                scoreSpan.innerText = "🟡 Good Attempt! Try again focusing on clarity.";
            }}
            resultBox.style.display = "block";
            status.innerText = "تم تحليل النطق!";
        }});
    }}
    </script>
    """
    st.components.v1.html(mic_js, height=220)

elif menu == "📚 المكتبة الذهبية العالمية":
    st.subheader("📚 المناهج الحصرية المعتمدة عالمياً ومجاناً 100%")
    st.info("💡 تم ربط المنصة مباشرة بأقوى المسارات العالمية المفتوحة للدراسة الحرة واستخراج الشهادات الدولية:")
    st.markdown("[🇺🇸 اضغط هنا للتسجيل الفوري في كورس الخارجية الأمريكية وجامعة بنسلفانيا مجاناً](https://coursera.org)")
    st.markdown("[🇬🇧 اضغط هنا لفتح منصة اختبار المستوى والدراسة التفاعلية من British Council مجاناً](https://britishcouncil.org)")

elif menu == "📜 بوابة الشهادات المعتمدة":
    st.subheader("📜 نظام التوثيق وإصدار الشهادات الأكاديمية الفورية")
    student_name = st.text_input("اكتب اسمك الثلاثي باللغة الإنجليزية بدقة:")
    
    if st.button("اصدار وتوليد الشهادة الفاخرة 📄"):
        if student_name:
            st.balloons()
            random_id = random.randint(50000, 99999)
            current_date = datetime.now().strftime("%Y-%m-%d")
            
            # عرض الشهادة الاحترافي الجديد والآمن تماماً من أخطاء الترجمة وعلامات الاقتباس
            st.success("🎉 تم توليد واعتماد شهادتك الأكاديمية بنجاح:")
            st.code(f"==================================================\n"
                    f"          AL-SAEEDA INTERNATIONAL ACADEMY         \n"
                    f"    FIRST INTERACTIVE AI PLATFORM IN YEMEN       \n"
                    f"==================================================\n\n"
                    f"CERTIFICATE OF ACHIEVEMENT\n\n"
                    f"This credential is proudly conferred upon:\n"
                    f"👉 {student_name.upper()} 👈\n\n"
                    f"For successfully completing the Advanced Interactive\n"
                    f"English Course and Speech Pronunciation Evaluation via AI.\n\n"
                    f"--------------------------------------------------\n"
                    f"Date of Issue: {current_date} | ID: YEM-AI-{random_id}\n"
                    f"==================================================")
        else:
            st.warning("يرجى كتابة الاسم باللغة الإنجليزية أولاً.")
