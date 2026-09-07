import streamlit as st
import google.generativeai as genai
import random

# إعداد المنصة بالهوية البصرية الحديثة المواكبة للجيل الحالي
st.set_page_config(page_title="أكاديمية السعيدة الدولية للغات الذكية", page_icon="🇾🇪", layout="wide")

# جلب وتأمين مفتاح الذكاء الاصطناعي
if "GENAI_KEY" in st.secrets:
    GENAI_API_KEY = st.secrets["GENAI_KEY"]
else:
    GENAI_API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if GENAI_API_KEY and GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=GENAI_API_KEY)

# تصميم واجهة مستخدم مخصصة وجذابة جداً عبر CSS
st.markdown("""
<style>
    @import url('https://googleapis.com');
    html, body, [data-testid="stSidebar"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .premium-hero { background: linear-gradient(135deg, #111e25 0%, #1e3d59 100%); padding: 35px; border-radius: 15px; color: white; text-align: center; margin-bottom: 20px; border-bottom: 5px solid #17b978; }
    .feature-box { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-right: 4px solid #17b978; margin-bottom: 10px; text-align: right; }
</style>
""", unsafe_allowed_html=True)

# الهيدر الفاخر المحدث للمنصة
st.markdown("""
<div class="premium-hero">
    <h1 style="margin:0; font-size: 2.5rem;">🇾🇪 أكاديمية السعيدة الذكية للغات</h1>
    <p style="margin:5px 0; opacity: 0.8; font-size: 1.1rem;">بيئة تعليمية من الجيل القادم مدعومة بالذكاء الاصطناعي التفاعلي التام</p>
</div>
""", unsafe_allowed_html=True)

# لوحة التحكم الجانبية الذكية
st.sidebar.markdown("### 👤 إعدادات رائد الأعمال التعليمي")
user_profile = st.sidebar.radio("🎯 الفئة المستهدفة الحالية للمتعلم:", ["🧸 قسم الأطفال والناشئين (تأسيس)", "💼 قسم الكبار والمحترفين (متقدم)"])
main_hub = st.sidebar.selectbox("📂 انتقل إلى أدوات الجيل القادم الـ 20:", ["🗣️ غرف المحادثة ومعالجة النطق بـ AI", "⚡ مركز الأدوات اللغوية السريعة للمحترفين", "📚 المناهج وحقائب السفر الذكية"])

# نظام تتبع النقاط التشجيعي (العقيق اليمني الرقمي)
if "points" not in st.session_state:
    st.session_state.points = random.randint(50, 120)

st.sidebar.metric(label="💎 رصيد الطالب من العقيق اليمني الرقمي:", value=f"{st.session_state.points} نقطة")

# توجيهات البوت للشرح المزدوج والمكثف
sys_instruction = (
    "You are a master bilingual English AI professor. "
    "Explain all concepts using a smooth blend of simple Arabic and expert English. "
    "Always provide a corrective breakdown of mistakes and encourage the student with emojis."
)

# --- تشغيل المحاور التفاعلية الكبرى ---

if main_hub == "🗣️ غرف المحادثة ومعالجة النطق بـ AI":
    
    # واجهة الأقسام التفاعلية للدردشة والمحاكاة ونطق الكلمات
    chat_tab, interview_tab, voice_tab = st.tabs(["💬 شات المعلم الذكي (مزدوج)", "💼 محاكي مقابلات العمل والمسارات", "🎙️ مختبر تصحيح النطق بالمايك"])
    
    with chat_tab:
        st.markdown("<div class='feature-box'>💡 <b>ميزة الشرح المزدوج:</b> اكتب أي كلمة أو قاعدة صعبة، وسيقوم البوت بشرحها بالعربي والإنجليزي مع نطقها تلقائياً بالصوت الفصيح!</div>", unsafe_allowed_html=True)
        user_msg = st.text_input("اسأل المعلم الذكي عن أي شيء هنا (مثال: اشرح لي الفرق بين Do و Does):")
        
        if user_msg and GENAI_API_KEY:
            with st.spinner("جاري التفكير والصياغة التعليمية..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
                    response = model.generate_content(user_msg)
                    st.info(response.text)
                    st.session_state.points += 5
                    
                    # نطق الرد الصوتي للمتعلم تلقائياً بسرعة متزنة (0.9x) تناسب المبتدئين والأطفال
                    clean_text = response.text.replace('\n', ' ').replace('"', '\\"').replace("'", "\\'")
                    st.components.v1.html(f"""
                        <script>
                        var speech = new SpeechSynthesisUtterance("{clean_text}");
                        speech.lang = 'en-US';
                        speech.rate = 0.9;
                        window.speechSynthesis.speak(speech);
                        </script>
                    """, height=0)
                except Exception as e:
                    st.error(f"خطأ في محرك الذكاء الاصطناعي: {e}")

    with interview_tab:
        st.markdown("<div class='feature-box'>💼 <b>محاكي مقابلات العمل والسفر:</b> البوت سيطرح عليك سؤالاً بالإنجليزية كأنك في مقابلة عمل أو مطار، اكتب ردك ليرى مدى جهوزيتك اللغوية!</div>", unsafe_allowed_html=True)
        st.info("🤖 سؤال المحاكاة الحالي: 'Tell me about yourself and why do you want to learn English?'")
        interview_reply = st.text_input("اكتب إجابتك هنا بالإنجليزية ليقوم البوت بتقييمها وصياغتها باحترافية:")
        if interview_reply and GENAI_API_KEY:
            with st.spinner("جاري تحليل صياغتك المهنية..."):
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction="You are a professional HR manager. Grade the user's response to the interview question, fix errors, and write an elite corporate version of their answer.")
                res = model.generate_content(interview_reply)
                st.success(res.text)

    with voice_tab:
        st.subheader("🎙️ مختبر النطق البصري ومعالجة مخارج الحروف:")
        if "الأطفال" in user_profile:
            test_phrase = "The quick brown fox jumps over the lazy dog"
        else:
            test_phrase = "Artificial intelligence is shifting the global education paradigm"
            
        st.warning(f"الجملة المطلوب قراءتها بصوتك الآن: **{test_phrase}**")
        
        # أداة معالجة النطق والمايك المباشر المعزولة برمجياً لعدم كسر بايثون
        mic_code = f"""
        <div style="text-align: center; margin-top: 10px;">
            <button id="micButton" style="background-color: #17b978; color: white; border: none; padding: 14px 28px; font-size: 16px; border-radius: 8px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 10px rgba(23,185,120,0.2);">
                🎤 اضغط هنا وتحدث بالجملة بوضوح
            </button>
            <p id="st" style="color: #666; margin-top: 10px;">تحدث؛ وسيقوم النظام بمقارنة الكلمات وإعطائك نسبة دقة نطقك الفورية...</p>
            <div id="box" style="margin-top: 12px; padding: 12px; border-radius: 8px; display: none; background-color: #f8f9fa; direction: ltr; text-align: left;">
                <p><b>What you said:</b> <span id="uText" style="color: #1e3d59; font-weight: bold;"></span></p>
                <p><b>AI Result:</b> <span id="sc" style="font-weight: bold;"></span></p>
            </div>
        </div>
        <script>
        const btn = document.getElementById('micButton');
        const st = document.getElementById('st');
        const box = document.getElementById('box');
        const uText = document.getElementById('uText');
        const sc = document.getElementById('sc');
        const tgt = "{test_phrase}".toLowerCase().trim();

        const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!Recognition) {{
            st.innerText = "المتصفح لا يدعم المايك، يرجى الفتح من متصفح Google Chrome.";
            btn.disabled = true;
        }} else {{
            const rec = new Recognition();
            rec.lang = 'en-US';
            btn.addEventListener('click', () => {{ rec.start(); st.innerText = "🎙️ جاري الاستماع الحقيقي... تحدث الآن..."; }});
            rec.addEventListener('result', (e) => {{
                const res = e.results[0][0].transcript;
                uText.innerText = res;
                if (res.toLowerCase().trim() === tgt) {{
                    sc.innerText = "🟢 Perfect Pronunciation (100%)! Brilliant.";
                }} else {{
                    sc.innerText = "🟡 Good Attempt! Practice again for clearer letter outputs.";
                }}
                box.style.display = "block"; st.innerText = "تم التحليل الفوري!";
            }});
        }}
        </script>
        """
        st.components.v1.html(mic_code, height=220)

elif main_hub == "⚡ center الأدوات اللغوية السريعة للمحترفين":
    st.subheader("⚡ مسرعات وأدوات الذكاء الاصطناعي الفورية (جيل الـ Gen-Z)")
    
    tool_select = st.selectbox("اختر الأداة الذكية الفورية الحالية:", ["📝 مصحح القواعد وإعادة الصياغة الذكية", "💼 مطور إيميلات العمل والسير الذاتية", "📖 مبسط ومختصر القصص الإنجليزية للطلاب"])
    
    user_text = st.text_area("أدخل النص أو الجملة هنا لتطبيق الأداة الذكية عليها فوراً:")
    
    if user_text and GENAI_API_KEY:
        with st.spinner("جاري معالجة وتطوير النص اللغوي..."):
            if "مصحح القواعد" in tool_select:
                prompt = f"Fix all grammar mistakes in this text, highlight the corrections clearly, and provide 3 everyday slang expressions related to it: {user_text}"
            elif "مطور إيميلات" in tool_select:
                prompt = f"Transform this broken English into an elite corporate business email or resume summary: {user_text}"
            else:
                prompt = f"Simplify this complex English story or text into easy vocabulary suitable for beginners, and provide a 3-sentence summary: {user_text}"
                
            model = genai.GenerativeModel('gemini-1.5-flash')
            res = model.generate_content(prompt)
            st.success(res.text)
            st.session_state.points += 10

elif main_hub == "📚 المناهج وحقائب السفر الذكية":
    st.subheader("📚 المناهج المجدولة والحقائب التعليمية المعتمدة عالمياً")
    
    if "الأطفال" in user_profile:
        st.markdown("""
        <div class="feature-box">
            <h4>🧸 حقيبة التأسيس والمرح للأطفال والناشئين</h4>
            <p>• <b>قاموس أكسفورد البصري المصور:</b> لتعلم الكلمات عبر الربط الصوري الذكي.</p>
            <p>• <b>أصوات الحروف المركبة الصعبة:</b> تدريبات تفاعلية على مخارج نطق (Sh, Ch, Th, Ph).</p>
