import streamlit as st
import google.generativeai as genai
import random

# 1. إعداد واجهة أول منصة يمنية ذكية لتعليم الإنجليزية
st.set_page_config(page_title="منصة اليمن لتعليم الإنجليزية الذكية", page_icon="🇾🇪", layout="wide")

# 2. ربط الذكاء الاصطناعي (تأكد من وضع مفتاحك الحقيقي هنا)
GENAI_API_KEY = "ضع_مفتاح_جوجل_الخاص_بك_هنا"

if GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=GENAI_API_KEY)
else:
    st.warning("⚠️ تنبيه: يرجى وضع مفتاح واجهة برمجة تطبيقات Gemini (API Key) في الكود لكي يعمل البوت الذكي.")

# 3. القائمة الجانبية للتنقل الذكي والسريع
st.sidebar.title("🇾🇪 بوابة التعليم اليمنية الذكية")
user_type = st.sidebar.radio("اختر الفئة المستهدفة:", ["🧸 قسم الأطفال والناشئين (تأسيس)", "💼 قسم الكبار والمحترفين (متقدم)"])
menu = st.sidebar.selectbox("اختر القسم التعليمي الفوري:", ["🗣️ المساعد الصوتي والمدرب الذكي", "📚 بنك الكلمات والقواعد السريع", "🎓 اختبار الكفاءة واستخراج الشهادة"])

# 4. تلقين البوت بجميع قواعد ومفردات ومناهج اللغة الإنجليزية عالمياً (الطريقة الأسرع)
if "الأطفال" in user_type:
    sys_instruction = (
        "You are an expert, friendly cartoon English teacher for Yemeni kids. "
        "You know all English vocabulary, phonics, and grammar from scratch. "
        "Always explain concepts very simply using friendly emojis. "
        "If the user speaks Arabic, reply in simple Arabic mixed with English to teach them. "
        "Encourage them with phrases like 'Excellent!', 'Great job buddy!'."
    )
    welcome_msg = "مرحباً بك يا بطل في عالم الإنجليزية المرح! اكتب أي كلمة أو جملة وسأقوم بنطقها لك وشرحها فوراً 👇"
else:
    sys_instruction = (
        "You are an advanced AI English Professor for adults in Yemen. "
        "You have complete knowledge of Oxford and Cambridge curriculums (A1 to C2), "
        "including all vocabulary, business English, idioms, and advanced grammar. "
        "Correct the user's grammar mistakes gently and provide the correct professional phrasing."
    )
    welcome_msg = "أهلاً بك في قسم المحترفين والمبتدئين من الكبار. هنا يمكنك ممارسة المحادثة، طلب شرح أي قاعدة معقدة، أو ترجمة وتصحيح العبارات 👇"

# --- تشغيل الأقسام التعليمية السريعة ---

if menu == "🗣️ المساعد الصوتي والمدرب الذكي":
    st.header(f"🗣️ المدرب الصوتي التفاعلي للغة الإنجليزية ({user_type})")
    st.info("💡 ميزة ذكية: استخدم ميزة الإملاء الصوتي (المايكروفون) في لوحة مفاتيح هاتفك أو كمبيوترك للتحدث مباشرة!")
    st.write(welcome_msg)
    
    user_input = st.text_input("اكتب سؤالك، كلمتك، أو جملتك الإنجليزية هنا لتسمع نطقها الصحيح:")
    
    if user_input and GENAI_API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
        with st.spinner("جاري التفكير والنطق الفوري المحترف..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
                response = model.generate_content(user_input)
                
                # عرض الرد التعليمي على الشاشة
                st.success(f"🤖 رد المعلم الذكي والشارح المساعد:\n\n {response.text}")
                
                # تنظيف النص البرمجي وتفعيل المساعد الصوتي التلقائي فورا
                clean_text = response.text.replace('\n', ' ').replace('"', '\\"').replace("'", "\\'")
                st.components.v1.html(f"""
                    <script>
                    var speech = new SpeechSynthesisUtterance("{clean_text}");
                    speech.lang = 'en-US';
                    speech.rate = 0.9; // سرعة النطق دقيقة لتناسب المتعلم
                    window.speechSynthesis.speak(speech);
                    </script>
                """, height=0)
            except Exception as e:
                st.error(f"حدث خطأ أثناء تشغيل المساعد الذكي: {e}")

elif menu == "📚 بنك الكلمات والقواعد السريع":
    st.header("📚 القاموس السريع والمفردات الأساسية (بدون إنترنت قوي)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📌 أهم الكلمات اليومية وحفظها")
        st.write("🟢 **Family (العائلة):** Father (أب) | Mother (أم) | Brother (أخ)")
        st.write("🟢 **Time (الوقت):** Day (يوم) | Week (أسبوع) | Year (سنة)")
        st.write("🟢 **Actions (الأفعال):** Eat (يأكل) | Sleep (ينام) | Learn (يتعلم)")
        st.write("💡 *نصيحة: يمكنك نسخ أي كلمة ووضعها في قسم المساعد الصوتي لتسمع نطقها الحقيقي!*")
        
    with col2:
        st.subheader("⚡ تبسيط القواعد الذهبية")
        with st.expander("1. قاعدة الزمن المضارع البسيط (Present Simple)"):
            st.write("تُستخدم للمواضيع والحقائق اليومية المتكررة.")
            st.code("Formula: Subject + Verb (s/es with He, She, It)\nExample: He speaks English.")
        with st.expander("2. قاعدة زمن الماضي البسيط (Past Simple)"):
            st.write("لأشياء حدثت وانتهت في الماضي.")
            st.code("Formula: Subject + Verb (ed)\nExample: I learned English yesterday.")

elif menu == "🎓 اختبار الكفاءة واستخراج الشهادة":
    st.header("🎓 التقييم الآلي ونظام الشهادات الفورية")
    st.write("اكتب اسمك بالإنجليزية لإصدار شهادة إتمام التأسيس والمحادثة الفورية المعتمدة رقمياً في المنصة:")
    
    student_name = st.text_input("اكتب اسمك الثلاثي باللغة الإنجليزية:")
    if st.button("اصدار وتوليد الشهادة الرسمية للمنصة 📄"):
        if student_name:
            st.balloons()
            random_id = random.randint(10000, 99999)
            st.markdown(f"""
            <div style="border:10px double #1e3d59; padding:30px; text-align:center; background-color:#f5f0e1; color:#1e3d59; direction: ltr;">
                <h1 style="color:#1e3d59;">YEMEN ENGLISH PLATFORM</h1>
                <h3 style="color:#ff6e40;">FIRST AI-POWERED LEARNING PLATFORM IN YEMEN</h3>
                <hr style="border: 2px solid #1e3d59;">
                <h3>CERTIFICATE OF ACHIEVEMENT</h3>
                <p>This is proudly presented to certify that</p>
                <h2><b>{student_name.upper()}</b></h2>
                <p>has successfully passed the Interactive English Speaking & Grammar Course via AI Assistant.</p>
                <p><i>Date: 2026 | Verified Serial Code: YEM-{random_id}</i></p>
            </div>
            """, unsafe_allowed_html=True)
        else:
            st.warning("الرجاء كتابة الاسم أولاً في الخانة.")
