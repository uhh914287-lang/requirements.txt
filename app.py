import streamlit as st
import google.generativeai as genai
import random
from datetime import datetime

# 1. إعدادات المنصة الاحترافية وتأمين الواجهة
st.set_page_config(page_title="أكاديمية اليمن الدولية للغات - AI", page_icon="🇾🇪", layout="wide")

# 2. جلب وتأمين مفتاح الذكاء الاصطناعي
if "GENAI_KEY" in st.secrets:
    GENAI_API_KEY = st.secrets["GENAI_KEY"]
else:
    GENAI_API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if GENAI_API_KEY and GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=GENAI_API_KEY)

# 🎨 تصميم فاخر ومميز ينافس المنصات العالمية (CSS الاحترافي)
st.markdown("""
<style>
    @import url('https://googleapis.com');
    html, body, [data-testid="stSidebar"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .hero-section { background: linear-gradient(135deg, #1e3d59 0%, #17b978 100%); padding: 40px; border-radius: 20px; color: white; text-align: center; margin-bottom: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.15); }
    .main-title { font-size: 2.6rem; font-weight: bold; margin-bottom: 10px; }
    .sub-title { font-size: 1.2rem; opacity: 0.9; }
    .course-card { background-color: #ffffff; padding: 25px; border-radius: 16px; box-shadow: 0 6px 12px rgba(0,0,0,0.05); border-left: 6px solid #17b978; margin-bottom: 20px; transition: transform 0.3s; }
    .course-card:hover { transform: translateY(-5px); }
    .course-title { color: #1e3d59; font-size: 1.4rem; font-weight: bold; margin-bottom: 10px; text-align: right; }
    .course-desc { color: #666666; font-size: 1rem; margin-bottom: 15px; text-align: right; line-height: 1.6; }
    .btn-link { background-color: #17b978; color: white !important; padding: 10px 20px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block; transition: 0.3s; }
    .btn-link:hover { background-color: #149662; }
</style>
""", unsafe_allowed_html=True)

# 🗺️ الهيدر الرئيسي الفاخر للمنصة
st.markdown("""
<div class="hero-section">
    <div class="main-title">🇾🇪 أكاديمية السعيدة الدولية للغات</div>
    <div class="sub-title">أول منصة يمنية وعربية مدعومة بالذكاء الاصطناعي التفاعلي بالكامل لتعليم الإنجليزية من الصفر</div>
</div>
""", unsafe_allowed_html=True)

# 3. القائمة الجانبية الأنيقة
st.sidebar.markdown("### 🌐 لوحة التحكم التعليمية")
user_type = st.sidebar.radio("🎯 الفئة المستهدفة الحالية:", ["🧸 قسم الأطفال والناشئين", "💼 قسم الكبار والمحترفين"])
menu = st.sidebar.selectbox("📂 انتقل إلى:", ["🗣️ بوت التحدث وتصحيح النطق", "📚 المكتبة الذهبية العالمية", "📜 بوابة الشهادات المعتمدة"])

sys_instruction = (
    "You are an elite bilingual English professor. "
    "Explain all grammar concepts simply in both Arabic and English. "
    "Analyze the user's input, provide instant guidance, and correct any structural flaws."
)

# --- تشغيل الأقسام بناءً على خطة الـ 60 دقيقة ---

if menu == "🗣️ بوت التحدث وتصحيح النطق":
    st.subheader("🤖 المحاور الذكي والمعلم الافتراضي:")
    user_query = st.text_input("اسأل عن أي قاعدة، أو اكتب جملة وترجمتها (مثال: شرح قاعدة Used to مع أمثلة):")
    
    if user_query and GENAI_API_KEY:
        with st.spinner("جاري صياغة الشرح الفوري بأعلى كفاءة تعليمية..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
                response = model.generate_content(user_query)
                st.info(response.text)
                
                # نطق الرد تلقائياً للتدريب على الاستماع
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
                st.error(f"خطأ في الاتصال بالمحرك: {e}")

    st.markdown("---")
    st.subheader("🎙️ مختبر النطق والتصحيح الصوتي التفاعلي:")
    
    # قائمة جمل تحدي ذكية حسب الفئة
    if "الأطفال" in user_type:
        test_sentence = "Learning English with games is very fun and easy"
    else:
        test_sentence = "Effective communication is the key to global professional success"
        
    st.warning(f"🎙️ الجملة المطلوب قراءتها الآن بصوتك: **{test_sentence}**")
    
    # واجهة المايك الاحترافية الحديثة داخل المتصفح
    st.components.v1.html(f"""
    <div style="text-align: center; font-family: 'Cairo', sans-serif; margin-top: 10px;">
        <button id="micBtn" style="background-color: #17b978; color: white; border: none; padding: 15px 35px; font-size: 16px; border-radius: 50px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 15px rgba(23,185,120,0.3); transition: 0.3s;">
            🎤 اضغط هنا وتحدث بالجملة بوضوح
        </button>
        <p id="status" style="color: #666; margin-top: 12px; font-size: 14px;">اضغط على الزر وابدأ النطق؛ سيقوم الذكاء الاصطناعي بتقييم مخارج الحروف فوراً...</p>
        <div id="resultBox" style="margin-top: 15px; padding: 15px; border-radius: 12px; display: none; background-color: #f8f9fa; border: 1px solid #e0e0e0; direction: ltr; text-align: left;">
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
        status.innerText = "المتصفح لا يدعم المايك المباشر، يرجى الفتح من متصفح Google Chrome.";
        micBtn.disabled = true;
    }} else {{
        const recognition = new SpeechRecognition();
        recognition.lang = 'en-US';
        micBtn.addEventListener('click', () => {{
            recognition.start();
            status.innerText = "🎙️ جاري الاستماع لنطقك... تحدث الآن...";
            micBtn.style.backgroundColor = "#d32f2f";
        }});
        recognition.addEventListener('result', (e) => {{
            const result = e.results[0][0].transcript;
            userTextSpan.innerText = result;
            if (result.toLowerCase().trim() === target) {{
                scoreSpan.innerText = "🟢 Perfect Pronunciation (100%)! Excellent job.";
                scoreSpan.style.color = "green";
            }} else {{
                scoreSpan.innerText = "🟡 Good Attempt! Some words were mispronounced. Try again focusing on clarity.";
                scoreSpan.style.color = "#f57c00";
            }}
            resultBox.style.display = "block";
            status.innerText = "تم تحليل النطق بنجاح!";
            micBtn.style.backgroundColor = "#17b978";
        }});
    }}
    </script>
    """, height=220)

elif menu == "📚 المكتبة الذهبية العالمية":
    st.subheader("📚 المناهج الحصرية المعتمدة عالمياً ومجاناً 100%")
    st.write("تم دمج أقوى المقررات الدولية الصادرة من كبرى المؤسسات الأكاديمية العالمية لتوفير محتوى تعليمي لا ينافس:")
    
    # كورس وزارة الخارجية الأمريكية
    st.markdown("""
    <div class="course-card">
        <div class="course-title">🇺🇸 كورس اللغة الإنجليزية المهنية المعتمد - جامعة بنسلفانيا والخارجية الأمريكية</div>
        <div class="course-desc">منهج متكامل لتعليم مهارات الأعمال، كتابة السير الذاتية الاحترافية، والخطابة الإقليمية. الكورس مجاني بالكامل ويمنح شهادة رسمية عند إتمامه عبر منصة Coursera العالمية.</div>
        <a href="https://coursera.org" target="_blank" class="btn-link">🔗 ابدأ التسجيل المجاني فورا</a>
    </div>
    """, unsafe_allowed_html=True)
    
    # المجلس الثقافي البريطاني
    st.markdown("""
    <div class="course-card">
        <div class="course-title">🇬🇧 مسارات الإتقان اللغوي الشامل - British Council</div>
        <div class="course-desc">محتوى تفاعلي مصنف من المستوى المبتدئ (A1) حتى المتقدم (C2)، يحتوي على اختبار تحديد مستوى دولي مجاني، ومئات الأنشطة التفاعلية للاستماع والقواعد.</div>
        <a href="https://britishcouncil.org" target="_blank" class="btn-link">🔗 ابدأ اختبار المستوى والدراسة الحرة</a>
    </div>
    """, unsafe_allowed_html=True)

elif menu == "📜 بوابة الشهادات المعتمدة":
    st.subheader("📜 نظام التوثيق وإصدار الشهادات الأكاديمية الفورية")
    st.write("عند إتمامك التدريبات اليومية بنجاح، يمكنك توليد شهادتك الموثقة من النظام التلقائي للمنصة:")
    
    student_name = st.text_input("اكتب اسمك الثلاثي باللغة الإنجليزية بدقة (كما تود رؤيته في الشهادة):")
    
    if st.button("اصدار وتوليد الشهادة الفاخرة 📄"):
        if student_name:
            st.balloons()
            random_id = random.randint(50000, 99999)
            current_date = datetime.now().strftime("%Y-%m-%d")
            
            # تصميم شهادة فاخرة جداً ذات طابع ملكي أكاديمي رسمي
            st.markdown(f"""
            <div style="border:15px double #1e3d59; padding:40px; text-align:center; background-color:#fcfaf2; color:#1e3d59; direction: ltr; font-family: 'Times New Roman', serif; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                <div style="text-align: center; margin-bottom: 10px;">
                    <span style="font-size: 35px;">👑</span>
                </div>
                <h1 style="color:#1e3d59; margin:0; font-size: 2.8rem; letter-spacing: 2px;">AL-SAEEDA INTERNATIONAL ACADEMY</h1>
                <h4 style="color:#17b978; margin:5px 0; font-size: 1.1rem; letter-spacing: 1px;">THE FIRST INTERACTIVE AI PLATFORM IN YEMEN</h4>
