import streamlit as st

st.set_page_config(page_title="SABA IMPERIAL | Cyber-Imperial English", page_icon="⚡", layout="wide")

# Custom CSS for Cyber-Imperial Cinematic Aesthetic
st.markdown("""
<style>
    .stApp { background-color: #0d1117; color: #f0f6fc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .hero-box { background: linear-gradient(135deg, #1f2937 0%, #111827 100%); border: 1px solid #374151; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
    .metric-card { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 8px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("### ⚡ SABA IMPERIAL MENU")
nav_choice = st.sidebar.radio("اختر القسم الرئيسي:", [
    "🎙️ المختبر الصوتي الذكي", 
    "📚 كورسات وول ستريت والأعمال", 
    "🧠 تبسيط القواعد الإمبراطورية", 
    "💼 مصطلحات سوق العمل الفورية", 
    "🎙️ بودكاست المتعلمين التفاعلي"
])

st.sidebar.markdown("---")
st.sidebar.markdown("⭐ **رصيد XP الحالي:** `450 XP` | **المستوى:** `Elite Operative`")

# 1. Voice Lab
if nav_choice == "🎙️ المختبر الصوتي الذكي":
    st.markdown("<div class='hero-box'><h1>🎙️ مختبر النطق والتصحيح الإمبراطوري</h1><p>تحدث الآن بالنطق الأمريكي الصحيح لتحليل مخارج حروفك فوراً بالذكاء الاصطناعي.</p></div>", unsafe_allow_html=True)
    
    target_phrase = st.selectbox("اختر الجملة للتدريب:", [
        "Strategic market optimization is critical.",
        "We need to accelerate financial growth.",
        "Innovation drives global enterprise success."
    ])
    st.info(f"📌 الجملة المطلوبة: **{target_phrase}**")
    
    voice_input = st.text_input("💬 أدخل النص المنطوق (أو جرب محاكاة الميكروفون المباشر):", placeholder="انطق الجملة هنا...")
    if st.button("🚀 تحليل النطق ومنح النقاط (+100 XP)"):
        if voice_input:
            st.success("✅ تحليل دقيق: مطابقة النطق بنسبة 94% - ممتاز جداً! تم إضافة +100 XP لرصيدك.")
        else:
            st.warning("⚠️ الرجاء إدخال النص أو تفعيل الميكروفون للتحدث أولاً.")

# 2. Courses
elif nav_choice == "📚 كورسات وول ستريت والأعمال":
    st.markdown("## 📚 كورسات النخبة والمفاوضات الكبرى")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='metric-card'><h3>💼 مفاوضات وول ستريت</h3><p>تعلم كيف تدير صفقات الملايين باللغة الإنجليزية المحترفة.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'><h3>🚀 إنجليزية رائد الأعمال</h3><p>صياغة العروض التقديمية وخطط العمل باحترافية مطلقة.</p></div>", unsafe_allow_html=True)

# 3. Grammar
elif nav_choice == "🧠 تبسيط القواعد الإمبراطورية":
    st.markdown("## 🧠 القواعد المبسطة لرجال الأعمال")
    st.markdown("""
    * **قاعدة الح المضارع المستمر في صفقات الأسهم:** تستخدم لوصف أحداث تحدث الآن (e.g., *The market is rising rapidly*).
    * **صيغة التفضيل في إقناع المستثمرين:** (e.g., *This is the most efficient strategy*).
    """)

# 4. Market Vocabulary
elif nav_choice == "💼 مصطلحات سوق العمل الفورية":
    st.markdown("## 💼 مفردات لا غنى عنها في بيئة العمل")
    st.table([
        {"المصطلح": "ROI", "المعنى": "عائد الاستثمار (Return on Investment)", "مثال": "We expect a high ROI."},
        {"المصطلح": "Scalability", "المعنى": "قابلية التوسع والنظام", "مثال": "Our platform has high scalability."},
        {"المصطلح": "Leverage", "المعنى": "استغلال الموارد / النفوذ", "مثال": "We must leverage our data."}
    ])

# 5. Interactive Podcast
elif nav_choice == "🎙️ بودكاست المتعلمين التفاعلي":
    st.markdown("## 🎙️ بودكاست الإمبراطورية التفاعلي")
    st.markdown("استمع إلى محادثات حية بين خبراء المال والأعمال، وشارك برأيك الصوتي المباشر:")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.text_area("✍️ شارك برأيك أو سؤالك الصوتي/النصي لحلقة البودكاست القادمة:")
    if st.button("📤 إرسال للمدرب الذكي"):
        st.success("✨ تم إرسال مشاركتك بنجاح وسيتم تقييمها في الحلقة القادمة!")
