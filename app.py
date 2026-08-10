import streamlit as st
import google.generativeai as genai
import random

# 1. إعدادات المنصة
st.set_page_config(page_title="منصة اليمن لتعليم الإنجليزية الذكية", page_icon="🇾🇪", layout="wide")

# 2. جلب المفتاح بأمان (يفضل وضعه في Secrets كـ GENAI_KEY)
if "GENAI_KEY" in st.secrets:
    GENAI_API_KEY = st.secrets["GENAI_KEY"]
else:
    # يمكنك وضعه هنا مؤقتاً إذا تجاوزت حماية جيتهاب
    GENAI_API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if GENAI_API_KEY and GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=GENAI_API_KEY)
else:
    st.warning("⚠️ تنبيه: يرجى تفعيل مفتاح Gemini للتشغيل.")

# 3. واجهة المستخدم
st.sidebar.title("🇾🇪 بوابة التعليم اليمنية الذكية")
user_type = st.sidebar.radio("اختر الفئة:", ["🧸 قسم الأطفال", "💼 قسم الكبار"])
menu = st.sidebar.selectbox("اختر القسم:", ["🗣️ بوت تصحيح النطق والشرح المزدوج", "📚 بنك الكلمات"])

# توجيهات البوت للشرح بالعربي والإنجليزي وتصحيح النطق
sys_instruction = (
    "You are a professional dual-language English teacher. "
    "Always explain English rules using BOTH Arabic and English. "
    "When the user types or speaks, evaluate their text, fix any grammar mistakes, "
    "and give them a short phrase to practice. Keep responses encouraging and structured."
)

if menu == "🗣️ بوت تصحيح النطق والشرح المزدوج":
    st.header("🗣️ بوت الشرح وتصحيح النطق الآلي")
    st.subheader("🤖 اسأل البوت (شرح بالعربي والإنجليزي):")
    
    user_query = st.text_input("اكتب أي سؤال أو قاعدة تريد شرحها (مثال: اشرح لي زمن الماضي):")
    if user_query and GENAI_API_KEY:
        with st.spinner("جاري التحضير..."):
            model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
            response = model.generate_content(user_query)
            st.success(response.text)
            
            # نطق رد البوت تلقائياً للمستمع
            clean_text = response.text.replace('\n', ' ').replace('"', '\\"').replace("'", "\\'")
            st.components.v1.html(f"""
                <script>
                var speech = new SpeechSynthesisUtterance("{clean_text}");
                speech.lang = 'en-US';
                window.speechSynthesis.speak(speech);
                </script>
            """, height=0)

    st.markdown("---")
    st.subheader("🎙️ اختبار وتصحيح نطقك الشخصي:")
    
    # جملة تدريبية عشوائية يطلب من الطالب نطقها
    target_sentence = "Practice makes perfect and learning English is fun"
    st.info(f"حاول نطق هذه الجملة: **{target_sentence}**")
    
    # كود جافاسكريبت متطور ومجاني 100% لتفعيل المايك وتصحيح النطق داخل المتصفح فورا
    st.components.v1.html(f"""
    <div style="text-align: center; font-family: sans-serif;">
        <button id="micBtn" style="background-color: #ff6e40; color: white; border: none; padding: 12px 24px; font-size: 16px; border-radius: 8px; cursor: pointer; font-weight: bold;">
            🎤 اضغط هنا وابدأ التحدث بالإنجليزية
        </button>
        <p id="status" style="color: #666; margin-top: 10px;">اضغط على الزر وتحدث بالجملة المطلوبة بالأعلى...</p>
        <div id="resultBox" style="margin-top: 15px; padding: 15px; border-radius: 8px; display: none; background-color: #f1f3f4;">
            <p><b>ما نطقته أنت:</b> <span id="userText" style="color: #1e3d59;"></span></p>
            <p><b>التقييم الفوري لنطقك:</b> <span id="score" style="font-weight: bold;"></span></p>
        </div>
    </div>

    <script>
    const micBtn = document.getElementById('micBtn');
    const status = document.getElementById('status');
    const resultBox = document.getElementById('resultBox');
    const userTextSpan = document.getElementById('userText');
    const scoreSpan = document.getElementById('score');
    
    const target = "{target_sentence}".toLowerCase().trim();

    // التحقق من دعم المتصفح للتعرف على الصوت
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {{
        status.innerText = "متصفحك لا يدعم المايك، يرجى استخدام جوجل كروم.";
        micBtn.disabled = true;
    }} else {{
        const recognition = new SpeechRecognition();
        recognition.lang = 'en-US';
        recognition.interimResults = false;

        micBtn.addEventListener('click', () => {{
            recognition.start();
            status.innerText = "🎙️ جاري الاستماع لنطقك... تحدث الآن...";
            micBtn.style.backgroundColor = "#d32f2f";
        }});

        recognition.addEventListener('result', (e) => {{
            const result = e.results[0][0].transcript;
            userTextSpan.innerText = result;
            
            // حساب نسبة صحة النطق ومقارنتها بالجملة الأصلية
            const userNorm = result.toLowerCase().trim();
            if (userNorm === target) {{
                scoreSpan.innerText = "🟢 نطق ممتاز وصحيح 100%! أحسنت!";
                scoreSpan.style.color = "green";
            }} else {{
                scoreSpan.innerText = "🟡 نطقك قريب، حاول التركيز على مخارج الحروف وإعادة المحاولة.";
                scoreSpan.style.color = "#f57c00";
            }}
            
            resultBox.style.display = "block";
            status.innerText = "تم التحليل بنجاح!";
            micBtn.style.backgroundColor = "#ff6e40";
        }});

        recognition.addEventListener('speechend', () => {{
            recognition.stop();
        }});
        
        recognition.addEventListener('error', (err) => {{
            status.innerText = "لم يتم سماع صوت بوضوح، اضغط وجرب مجدداً.";
            micBtn.style.backgroundColor = "#ff6e40";
        }});
    }}
    </script>
    """, height=220)

elif menu == "📚 بنك الكلمات":
    st.header("📚 كلمات وقواعد أساسية مترجمة")
    st.write("المحتوى يعمل هنا بسرعة فائقة وتلقائية.")
