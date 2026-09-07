import streamlit as st
import google.generativeai as genai
import random

# 1. إعدادات المنصة وهويتها البصرية
st.set_page_config(page_title="أكاديمية السعيدة الدولية للغات - AI", page_icon="🇾🇪", layout="wide")

# 2. إعداد مفتاح الذكاء الاصطناعي الآمن
if "GENAI_KEY" in st.secrets:
    GENAI_API_KEY = st.secrets["GENAI_KEY"]
else:
    GENAI_API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if GENAI_API_KEY and GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=GENAI_API_KEY)

# 🗺️ العنوان الرئيسي للمنصة
st.title("🇾🇪 أكاديمية السعيدة الدولية للغات")
st.caption("أول منصة يمنية وعربية مدعومة بالذكاء الاصطناعي لتعليم الإنجليزية من الصفر إلى الاحتراف")

# 3. القائمة الجانبية لتحديد فئة المتعلم
st.sidebar.markdown("### 👤 الملف الشخصي للمتعلم")
user_type = st.sidebar.radio("🎯 اختر الفئة المستهدفة:", ["🧸 قسم الأطفال والناشئين (تأسيس)", "💼 قسم الكبار والمحترفين (متقدم)"])

# توجيهات الذكاء الاصطناعي لتقديم شرح تفاعلي مزدوج (عربي + إنجليزي)
sys_instruction = (
    "You are an elite bilingual English tutor. "
    "Always explain English rules using a clear mix of Arabic and English so learners can easily understand. "
    "Check the user's grammar, provide immediate feedback, and give them a practice sentence."
)

# 4. بناء الواجهة الداخلية التفاعلية باستخدام الأقسام (Tabs)
tab1, tab2, tab3 = st.tabs(["🗣️ المساعد الافتراضي والمدرب الذكي", "📚 كورسات ومناهج المنصة", "🎙️ مختبر تصحيح النطق"])

# --- القسم الأول: بوت التحدث التفاعلي ---
with tab1:
    st.subheader("🤖 اسأل المعلم الافتراضي (شرح فوري باللغتين العربية والإنجليزية):")
    user_query = st.text_input("اكتب أي قاعدة أو سؤال تريد شرحه (مثال: متى نستخدم Present Continuous؟):")
    
    if user_query and GENAI_API_KEY:
        with st.spinner("جاري إعداد الشرح المبسط..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
                response = model.generate_content(user_query)
                st.info(response.text)
                
                # كود النطق الصوتي التلقائي لرد البوت
                clean_text = response.text.replace('\n', ' ').replace('"', '\\"').replace("'", "\\'")
                st.components.v1.html(f"""
                    <script>
                    var speech = new SpeechSynthesisUtterance("{clean_text}");
                    speech.lang = 'en-US';
                    speech.rate = 0.95;
                    window.speechSynthesis.speak(speech);
                    </script>
                """, height=0)
            except Exception as e:
                st.error(f"خطأ في الاتصال بالذكاء الاصطناعي: {e}")

# --- القسم الثاني: الكورسات والمناهج المجدولة خطوة بخطوة ---
with tab2:
    st.subheader("📚 المناهج الدراسية المرتبة (من الصفر)")
    
    if "الأطفال" in user_type:
        st.markdown("### 🧸 كورس التأسيس الشامل للأطفال والناشئين")
        
        c1, c2 = st.columns(2)
        with c1:
            st.success("🟢 الدرس الأول: الحروف والأصوات (Phonics)")
            st.write("• **A** is for **Apple** (تفاحة) | نطق الحرف: /æ/")
            st.write("• **B** is for **Boy** (ولد) | نطق الحرف: /b/")
            st.write("• **C** is for **Cat** (قطة) | نطق الحرف: /k/")
        with c2:
            st.success("🔵 الدرس الثاني: الأرقام والألوان الأساسية")
            st.write("• **One (1)** - **Red** (أحمر)")
            st.write("• **Two (2)** - **Blue** (أزرق)")
            st.write("• **Three (3)** - **Green** (أخضر)")
            
        st.markdown("---")
        st.info("🔗 **مصادر عالمية إضافية للأطفال:** [افتح مكتبة القصص والألعاب التفاعلية من American English](https://state.gov)")
        
    else:
        st.markdown("### 💼 كورس المحادثة والقواعد المتقدمة للكبار")
        
        exp1 = st.expander("📌 الدرس الأول: التحيات والتعارف المهني (Greetings)")
        with exp1:
            st.write("• **Formal (رسمي):** Hello, how do you do? (تُستخدم عند لقاء شخص لأول مرة)")
            st.write("• **Informal (غير رسمي):** Hey, what's up? (بين الأصدقاء والزملاء المقربين)")
            st.code("Practice context: Introduce your name and job to the AI bot in the first tab.")
            
        exp2 = st.expander("📌 الدرس الثاني: تركيب الجملة الإنجليزية الأساسية (Sentence Structure)")
        with exp2:
            st.write("تتكون الجملة الأساسية دائماً من: **فاعل (Subject) + فعل (Verb) + مفعول به (Object)**")
            st.code("Formula: Subject + Verb + Object\nExample: I (Subject) learn (Verb) English (Object).")

        st.markdown("---")
        st.info("🔗 **مصادر عالمية معتمدة للكبار:** [افتح منهاج المحادثة الحرة واختبار تحديد المستوى من British Council](https://britishcouncil.org)")

# --- القسم الثالث: مختبر تصحيح النطق بالمايك ---
with tab3:
    st.subheader("🎙️ اختبار وتصحيح النطق الشخصي الفوري:")
    
    if "الأطفال" in user_type:
        test_sentence = "Learning English with games is very fun and easy"
    else:
        test_sentence = "Effective communication is the key to global professional success"
        
    st.warning(f"🎙️ اقرأ هذه الجملة بصوتك: **{test_sentence}**")
    
    # برمجة أداة التعرف على الصوت المقاومة للأخطاء
    mic_js = f"""
    <div style="text-align: center; margin-top: 15px;">
        <button id="micBtn" style="background-color: #17b978; color: white; border: none; padding: 14px 30px; font-size: 16px; border-radius: 8px; cursor: pointer; font-weight: bold;">
            🎤 اضغط هنا وابدأ التحدث بالإنجليزية
        </button>
        <p id="status" style="color: #666; margin-top: 10px;">اضغط على الزر واقرأ الجملة بوضوح لنصحح نطقك...</p>
        <div id="resultBox" style="margin-top: 15px; padding: 15px; border-radius: 8px; display: none; background-color: #f8f9fa; direction: ltr; text-align: left;">
            <p><b>Your Spoken Text:</b> <span id="userText" style="color: #1e3d59; font-weight: bold;"></span></p>
            <p><b>Evaluation:</b> <span id="score" style="font-weight: bold;"></span></p>
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
        status.innerText = "متصفحك لا يدعم المايك، يرجى فتح الموقع باستخدام Google Chrome.";
        micBtn.disabled = true;
    }} else {{
        const recognition = new SpeechRecognition();
        recognition.lang = 'en-US';
        
        micBtn.addEventListener('click', () => {{
            recognition.start();
            status.innerText = "🎙️ جاري الاستماع... تحدث الآن...";
        }});
        
        recognition.addEventListener('result', (e) => {{
            const result = e.results.transcript;
            userTextSpan.innerText = result;
            if (result.toLowerCase().trim() === target) {{
                scoreSpan.innerText = "🟢 Perfect Pronunciation (100%)! Excellent.";
                scoreSpan.style.color = "green";
            }} else {{
                scoreSpan.innerText = "🟡 Good Attempt! Try again for better clarity.";
                scoreSpan.style.color = "orange";
            }}
            resultBox.style.display = "block";
            status.innerText = "تم التحليل بنجاح!";
        }});
    }}
    </script>
    """
    st.components.v1.html(mic_js, height=220)
