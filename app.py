import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="AI Academy", page_icon="🇾🇪", layout="wide")

# 2. AI Model setup
if "GENAI_KEY" in st.secrets:
    API_KEY = st.secrets["GENAI_KEY"]
else:
    API_KEY = "AQ.Ab8RN6ITkIbjgXlrf_18zQIJEeDNBtE9M53aNTiDba2MtqbsLg"

if API_KEY and API_KEY != "ضع_مفتاح_جوجل_الخاص_بك_هنا":
    genai.configure(api_key=API_KEY)

# Native App Headers
st.title("أكاديمية السعيدة الدولية للغات")
st.caption("أول منصة يمنية وعربية مدعومة بالذكاء الاصطناعي لتعليم الإنجليزية من الصفر")

# Sidebar
st.sidebar.markdown("### لوحة التحكم")
user_profile = st.sidebar.radio("اختر الفئة:", ["الأطفال والناشئين", "الكبار والمحترفين"])
hub = st.sidebar.selectbox("أدوات الجيل القادم:", ["غرف المحادثة ومعالجة النطق", "المكتبة الذهبية العالمية"])

sys_instruction = "You are a master bilingual English AI professor. Explain everything using a smooth blend of simple Arabic and expert English."

if hub == "غرف المحادثة ومعالجة النطق":
    tab_chat, tab_voice = st.tabs(["شات المعلم الذكي", "مختبر تصحيح النطق"])
    
    with tab_chat:
        st.write("اكتب أي كلمة أو قاعدة صعبة وسيشرحها البوت بالعربي والإنجليزي مع نطقها بالصوت!")
        user_msg = st.text_input("اسأل المعلم الذكي:")
        if user_msg and API_KEY:
            with st.spinner("جاري التحضير..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_instruction)
                    response = model.generate_content(user_msg)
                    st.info(response.text)
                    
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
                    st.error(f"Error: {e}")

    with tab_voice:
        test_phrase = "Learning English is very fun and easy" if "الأطفال" in user_profile else "Artificial intelligence is shifting global education"
        st.warning(f"اقرأ هذه الجملة بصوتك: {test_phrase}")
        
        mic_html = f"""
        <div style="text-align: center; margin-top: 10px;">
            <button id="mBtn" style="background-color: #17b978; color: white; border: none; padding: 14px 28px; font-size: 16px; border-radius: 8px; cursor: pointer; font-weight: bold;">
                🎤 اضغط هنا وتحدث بالإنجليزية
            </button>
            <p id="st" style="color: #666; margin-top: 10px;">تحدث الآن ليتم تقييم نطقك...</p>
            <div id="bx" style="margin-top: 12px; padding: 12px; border-radius: 8px; display: none; background-color: #f8f9fa; direction: ltr; text-align: left;">
                <p><b>Your Speech:</b> <span id="uTxt"></span></p>
                <p><b>AI Result:</b> <span id="sc" style="font-weight: bold;"></span></p>
            </div>
        </div>
        <script>
        const btn = document.getElementById('mBtn');
        const st = document.getElementById('st');
        const bx = document.getElementById('bx');
        const uTxt = document.getElementById('uTxt');
        const sc = document.getElementById('sc');
        const tgt = "{test_phrase}".toLowerCase().trim();

        const Rec = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!Rec) {{
            st.innerText = "المتصفح لا يدعم المايك، افتح من جوجل كروم.";
            btn.disabled = true;
        }} else {{
            const r = new Rec(); r.lang = 'en-US';
            btn.addEventListener('click', () => {{ r.start(); st.innerText = "🎙️ جاري الاستماع... تحدث الآن..."; }});
            r.addEventListener('result', (e) => {{
                const res = e.results[0][0].transcript;
                uTxt.innerText = res;
                if (res.toLowerCase().trim() === tgt) {{
                    sc.innerText = "🟢 Perfect Pronunciation (100%)!";
                }} else {{
                    sc.innerText = "自由 Good Attempt! Try again.";
                }}
                bx.style.display = "block"; st.innerText = "تم التحليل!";
            }});
        }}
        </script>
        """
        st.components.v1.html(mic_html, height=220)

elif hub == "المكتبة الذهبية العالمية":
    st.subheader("المناهج المعتمدة عالمياً")
    st.markdown("[🇺🇸 كورس الخارجية الأمريكية وجامعة بنسلفانيا مجاناً](https://coursera.org)")
    st.markdown("[🇬🇧 منصة اختبار المستوى والدراسة الحرة من British Council مجاناً](https://britishcouncil.org)")
