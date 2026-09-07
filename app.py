import streamlit as st
import google.generativeai as genai
import random

# 1. Page Configuration (Netflix Dark Mode Baseline)
st.set_page_config(page_title="أكاديمية السعيدة الذكية للغات", page_icon="🇾🇪", layout="wide")

# 2. AI Key Configuration
if "GENAI_KEY" in st.secrets:
    API_KEY = st.secrets["GENAI_KEY"]
else:
    API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if API_KEY and API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=API_KEY)

# 🎨 Native Luxury Styling (حماية كاملة ضد الترجمة)
st.markdown("<h1 style='text-align:center; color:#ff0914; font-size:3rem; margin-bottom:0;'>🇾🇪 ACADEMY X</h1>", unsafe_allowed_html=True)
st.markdown("<p style='text-align:center; color:#a0aec0; font-size:1.2rem;'>أول منصة سينمائية تفاعلية بذكاء اصطناعي فوري في الشرق الأوسط</p>", unsafe_allowed_html=True)
st.markdown("---")

# 3. Duolingo Gamification Engine (نظام النقاط والمتصدرين)
if "xp" not in st.session_state:
    st.session_state.xp = random.randint(150, 300)

# القائمة الجانبية الفاخرة
st.sidebar.markdown(f"## ⚡ مستوى الطالب الحركي\n# 🔥 {st.session_state.xp} XP")
st.sidebar.markdown("🏆 **قائمة المتصدرين في اليمن لهذا الأسبوع:**\n1. أحمد م. (صنعاء) - 950 XP\n2. سارة ع. (عدن) - 880 XP\n3. **أنت حالياً** - {st.session_state.xp} XP")
st.sidebar.markdown("---")

user_profile = st.sidebar.selectbox("🎯 الفئة العمرية المستهدفة:", ["🧸 قسم الأطفال والناشئين", "💼 قسم الكبار والمحترفين"])
menu_hub = st.sidebar.radio("📂 استوديو الأدوات اللغوية الـ 5 المبتكرة:", [
    "🎬 شات المعلم السينمائي (مزدوج)", 
    "🎙️ مختبر تصحيح النطق بالمايك", 
    "⚡ مصحح القواعد الفوري وإعادة الصياغة",
    "💼 محاكي مقابلات العمل وإيميلات البزنس",
    "🚀 المناهج العالمية المعتمدة مجاناً"
])

sys_instruction = "You are an elite bilingual English professor. Explain concepts smoothly using an elite mix of simple Arabic and expert English."

# --- تشغيل الأدوات الـ 5 الكبرى باحترافية ---

if menu_hub == "🎬 شات المعلم السينمائي (مزدوج)":
    st.markdown("### 🤖 السينما الافتراضية والشارح الذكي")
    st.caption("اكتب أي قاعدة أو كلمة؛ سيقوم البوت بصياغة شرح سينمائي مبسط باللغتين ونطق ردوده أوتوماتيكياً!")
    
    user_input = st.text_input("اسأل المحاور الافتراضي هنا:")
    if user_input and API_KEY:
        with st.spinner("جاري التوليد اللغوي والصوتي..."):
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

elif menu_hub == "🎙️ مختبر تصحيح النطق بالمايك":
    test_phrase = "Learning English with games is very fun" if "الأطفال" in user_profile else "Global communication shapes the future of technology"
    st.markdown("### 🎙️ تحدي النطق الصوتي الفوري (مواكبة للجيل الحالي)")
    st.write("اضغط على زر المايك بالأسفل واقرأ هذه الجملة بدقة وبصوتك لتقييم مخارج حروفك:")
    st.error(f"الجملة المطلوبة: {test_phrase}")
    
    mic_js_code = f"""
    <div style="text-align: center; margin-top: 15px;">
        <button id="mButton" style="background-color: #58cc02; color: white; border: none; padding: 16px 36px; font-size: 16px; border-radius: 12px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 0 #46a302;">
            🎤 اضغط الآن وتحدث بالجملة بوضوح
        </button>
        <div id="resultBox" style="margin-top: 15px; padding: 15px; border-radius: 12px; display: none; background-color: #f8f9fa; direction: ltr; text-align: left; color: black;">
            <p><b>Your Input:</b> <span id="userText" style="color: #58cc02; font-weight:bold;"></span></p>
            <p><b>AI Feedback:</b> <span id="score" style="font-weight: bold;"></span></p>
        </div>
    </div>
    <script>
    const btn = document.getElementById('mButton');
    const box = document.getElementById('resultBox');
    const uText = document.getElementById('userText');
    const score = document.getElementById('score');
    const target = "{test_phrase}".toLowerCase().trim();

    const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!Recognition) {{
        alert("المتصفح لا يدعم المايك، يرجى الفتح عبر Google Chrome.");
    }} else {{
        const r = new Recognition(); r.lang = 'en-US';
        btn.addEventListener('click', () => {{ r.start(); btn.innerText = "🎙️ جاري الاستماع الحقيقي..."; }});
        r.addEventListener('result', (e) => {{
            const res = e.results.transcript;
            uText.innerText = res;
            if (res.toLowerCase().trim() === target) {{
                score.innerText = "🟢 Perfect Pronunciation (100%)! Excellent.";
            }} else {{
                score.innerText = "🟡 Good Attempt! Try again focusing on clarity.";
            }}
            box.style.display = "block"; btn.innerText = "🎤 اضغط هنا وتحدث مجدداً";
        }});
    }}
    </script>
    """
    st.components.v1.html(mic_js_code, height=230)

elif menu_hub == "⚡ مصحح القواعد الفوري وإعادة الصياغة":
    st.markdown("### 📝 مصحح القواعد وإعادة الصياغة الذكية لجيل الـ Gen-Z")
    st.caption("ضع أي نص إنجليزي ركيك أو به أخطاء، وسيقوم البوت بإعادة كتابته بشكل احترافي مع تلوين وتوضيح الأخطاء الإملائية والنعوت.")
    
    text_to_fix = st.text_area("أدخل النص هنا:")
    if text_to_fix and API_KEY:
        with st.spinner("جاري الهندسة اللغوية الفورية..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            res = model.generate_content(f"Fix all grammar and spelling errors in this text, format it beautifully, and explain why the change happened in simple Arabic: {text_to_fix}")
            st.success(res.text)
            st.session_state.xp += 10

elif menu_hub == "💼 محاكي مقابلات العمل وإيميلات البزنس":
    st.markdown("### 💼 المطور الاحترافي والتوظيف الرقمي")
    st.caption("أداة مخصصة لخريجي الجامعات والشباب اليمني لكتابة إيميلات رسمية للشركات الدولية، أو محاكاة مقابلة عمل حقيقية.")
    
    biz_mode = st.selectbox("اختر نمط الأداة:", ["💼 محاكي مقابلة العمل الشخصية عبر AI", "✉️ منشئ ومطور إيميلات البزنس الفاخرة"])
    
    user_biz_input = st.text_area("اكتب مسودتك أو إجابتك هنا:")
    if user_biz_input and API_KEY:
        with st.spinner("جاري صياغة النص بطابع مؤسسي فاخر..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            if "مقابلة" in biz_mode:
                prompt = f"Act as an HR Manager. Evaluate this candidate response, give constructive feedback, and rewrite it in an elite professional way: {user_biz_input}"
            else:
                prompt = f"Convert this text into a high-end corporate business email or an outstanding LinkedIn resume bio: {user_biz_input}"
            res = model.generate_content(prompt)
            st.success(res.text)
            st.session_state.xp += 10

elif menu_hub == "🚀 المناهج العالمية المعتمدة مجاناً":
    st.markdown("### 🚀 المكتبة الذهبية للحقائب المعتمدة عالمياً")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🇺🇸 **مسار إنجليزية الأعمال والتوظيف - جامعة بنسلفانيا**")
        st.write("منهج تفاعلي متكامل يعلم مهارات الإدارة والخطابة، متاح للدراسة والاستفادة مجاناً.")
        st.markdown("[🔗 ابدأ التسجيل المجاني فورا عبر Coursera](https://coursera.org)")
    with col2:
        st.info("🇬🇧 **أكاديمية المجلس الثقافي البريطاني - British Council**")
        st.write("مناهج تبدأ من الصفر (A1) وتتدرج للطلاقة الكاملة، مدعوماً ببنك أنشطة يعمل بأقل استهلاك للإنترنت.")
        st.markdown("[🔗 اضغط هنا لإجراء اختبار المستوى والتعلم](https://britishcouncil.org)")
