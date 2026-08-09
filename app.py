import streamlit as st
import google.generativeai as genai
import random

st.set_page_config(page_title="منصة اليمن لتعليم الإنجليزية", page_icon="🇾🇪", layout="wide")

# ضع مفتاحك الحقيقي هنا بين القوسين
GENAI_API_KEY = "ضع_مفتاح_جوجل_الخاص_بك_هنا"

if GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=GENAI_API_KEY)
else:
    st.warning("⚠️ يرجى وضع مفتاح واجهة برمجة تطبيقات Gemini (API Key) في الكود.")

st.sidebar.title("🇾🇪 بوابة التعليم اليمنية")
user_type = st.sidebar.radio("اختر الفئة المستهدفة:", ["🧸 قسم الأطفال والناشئين", "💼 قسم الكبار والمحترفين"])
menu = st.sidebar.selectbox("اختر خطتك الليلة:", ["📚 المنهج والكتب الرقمية", "🗣️ التدريب مع البوت الصوتي", "🎓 استخراج الشهادة الفورية"])

if user_type == "🧸 قسم الأطفال والناشئين":
    sys_instruction = "You are a friendly cartoon English teacher for kids. Speak very simply, use words like 'Great job!', and correct them gently."
    welcome_msg = "مرحباً بك يا بطل في عالم الإنجليزية المرح! اكتب جملتك وسأقوم بنطقها لك وتصحيحها 👇"
else:
    sys_instruction = "You are an expert academic English professor for adults. Focus on professional communication, business grammar, and academic phrasing."
    welcome_msg = "أهلاً بك في قسم المحترفين. يمكنك بدء محادثة متقدمة لممارسة اللغة وتصحيح نطقك 👇"

if menu == "📚 المنهج والكتب الرقمية":
    st.header(f"📚 المنهج المفتوح - {user_type}")
    if user_type == "🧸 قسم الأطفال والناشئين":
        st.subheader("المستوى التأسيسي (الألوان، الحروف، الأرقام)")
        st.markdown("[📖 اضغط هنا لتحميل كتاب الأطفال التأسيسي مجاناً من American English](https://state.gov)")
    else:
        st.subheader("مستوى المحادثة اليومية والمهنية (A1 - B2)")
        st.markdown("[📖 اضغط هنا لتحميل منهاج المحادثة المعتمد من British Council](https://britishcouncil.org)")

elif menu == "🗣️ التدريب مع البوت الصوتي":
    st.header(f"🗣️ المساعد الصوتي الذكي ({user_type})")
    st.write(welcome_msg)
    user_input = st.text_input("اكتب جملتك بالإنجليزية هنا:")
    
    if user_input and GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
        with st.spinner("جاري التحليل والنطق..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
                response = model.generate_content(user_input)
                st.success(f"🤖 رد المعلم الذكي:\n\n {response.text}")
                clean_text = response.text.replace('\n', ' ').replace('"', '\\"').replace("'", "\\'")
                st.components.v1.html(f"""
                    <script>
                    var speech = new SpeechSynthesisUtterance("{clean_text}");
                    speech.lang = 'en-US';
                    window.speechSynthesis.speak(speech);
                    </script>
                """, height=0)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

elif menu == "🎓 استخراج الشهادة الفورية":
    st.header("🎓 نظام الشهادات الآلي")
    student_name = st.text_input("اكتب اسمك الثلاثي باللغة الإنجليزية:")
    if st.button("اصدار وتوليد الشهادة 📄"):
        if student_name:
            st.balloons()
            random_id = random.randint(1000, 9999)
            st.markdown(f"""
            <div style="border:10px double #1e3d59; padding:30px; text-align:center; background-color:#f5f0e1; color:#1e3d59; direction: ltr;">
                <h1>YEMEN ENGLISH PLATFORM</h1>
                <h3>CERTIFICATE OF ACHIEVEMENT</h3>
                <p>This is to certify that</p>
                <h2><b>{student_name.upper()}</b></h2>
                <p>has successfully completed the Interactive English Speaking Course via AI.</p>
                <p><i>Serial Code: YEM-{random_id}</i></p>
            </div>
            """, unsafe_allowed_html=True)
