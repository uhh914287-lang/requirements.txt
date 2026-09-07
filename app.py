import streamlit as st
import streamlit.components.v1 as components

# 1. إعداد الصفحة بأعلى معايير الأداء والملء الكامل للشاشة
st.set_page_config(
    page_title="أكاديمية السعيدة الإمبراطورية | Saba AI",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تصفير هوامش Streamlit لمنح تجربة تطبيق هجين أصيل
st.markdown("""
    <style>
        #MainMenu, footer, header { display: none !important; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
        iframe { border-radius: 0px !important; }
    </style>
""", unsafe_allowed_html=True)

# 3. الشيفرة الهندسية الموحدة للواجهة (HTML5 / CSS3 / JavaScript Engine)
cyber_saba_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA ACADEMY X</title>
    <script src="https://tailwindcss.com"></script>
    <script src="https://unpkg.com"></script>
    <style>
        @import url('https://googleapis.com');
        body { font-family: 'Tajawal', sans-serif; background-color: #05070b; color: #f1f5f9; }
        .glass-panel { background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(9, 13, 22, 0.95) 100%); border: 1px solid rgba(212, 175, 55, 0.18); }
        .agate-button { background: linear-gradient(135deg, #a81c1c 0%, #5e0808 100%); }
    </style>
</head>
<body class="min-h-screen w-full flex justify-center items-center p-0 sm:p-4">
    <main class="w-full max-w-lg h-screen sm:h-[94vh] flex flex-col glass-panel sm:rounded-[36px] overflow-hidden relative">
        <header class="px-5 py-4 border-b border-gray-800 bg-black/40 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <span class="text-amber-400 font-black text-lg">𐩯</span>
                <div>
                    <h1 class="text-xs font-black text-amber-400">SABA ACADEMY</h1>
                    <span id="xpScore" class="text-sm font-black text-gray-100">320 XP</span>
                </div>
            </div>
            <select id="govSelector" onchange="alert('تم نقلك لدوري المحافظات!')" class="bg-[#131b2e] text-[11px] font-bold text-amber-200 py-1.5 px-3 rounded-xl border border-amber-500/30">
                <option value="الحديدة">الحديدة ⚓</option>
                <option value="صنعاء">صنعاء 🏛️</option>
                <option value="عدن">عدن 🌊</option>
            </select>
        </header>
        <nav class="grid grid-cols-3 bg-[#090d16] p-1.5 border-b border-gray-800 text-xs font-bold text-center">
            <button onclick="switchTab('arena')" id="btn-arena" class="py-2.5 rounded-xl text-amber-400 bg-amber-500/10">💬 المحاكي</button>
            <button onclick="switchTab('voice')" id="btn-voice" class="py-2.5 rounded-xl text-gray-400">🎙️ مختبر النطق</button>
            <button onclick="switchTab('quest')" id="btn-quest" class="py-2.5 rounded-xl text-gray-400">⚡ التحدي</button>
        </nav>
        <div class="flex-1 flex flex-col overflow-hidden">
            <section id="tab-arena" class="flex-1 flex flex-col justify-between p-4">
                <div id="chatFeed" class="flex-1 overflow-y-auto space-y-3 text-sm">
                    <div class="flex justify-end">
                        <div class="glass-panel p-3.5 rounded-2xl text-gray-200">
                            <b>HR Director:</b> Welcome! Why are you the ideal candidate for this remote position from Yemen?
                        </div>
                    </div>
                </div>
                <div class="mt-3 flex items-center gap-2 bg-[#0c1220] p-1.5 rounded-2xl border border-gray-700">
                    <input id="chatField" type="text" placeholder="اكتب ردك بالإنجليزية هنا..." class="flex-1 bg-transparent px-3 py-2 text-sm text-white outline-none text-right">
                    <button onclick="executeAiTurn()" class="agate-button p-2.5 rounded-xl text-white">🚀</button>
                </div>
            </section>
            <section id="tab-voice" class="hidden flex-1 flex flex-col justify-between items-center p-6 text-center">
                <h2 class="text-amber-300 font-bold">"Opportunities don't happen, you create them."</h2>
                <button id="masterMicBtn" onclick="triggerSpeechLab()" class="w-24 h-24 rounded-full bg-red-600 text-white font-bold">🎤 ابدأ الآن</button>
                <div id="voiceScoreCard" class="text-xs text-gray-400">اضغط وتحدث ليتم تقييم نطقك تلقائياً...</div>
            </section>
            <section id="tab-quest" class="hidden flex-1 p-5 flex flex-col justify-center text-center space-y-4">
                <h3 class="text-amber-300 font-bold">ما هو الرد الأذكى إذا طلب العميل خفض سعرك 50%؟</h3>
                <button onclick="alert('✨ إجابة احترافية ممتازة!')" class="w-full p-3.5 glass-panel rounded-2xl text-right text-sm">A) My rate reflects the quality and value I deliver.</button>
                <button onclick="alert('⚠️ خيار يقلل من قيمتك في سوق العمل!')" class="w-full p-3.5 glass-panel rounded-2xl text-right text-sm">B) I accept the discount immediately.</button>
            </section>
        </div>
    </main>
    <script>
        lucide.createIcons();
        function switchTab(name) {
            ['arena', 'voice', 'quest'].forEach(t => { document.getElementById('tab-' + t).classList.add('hidden'); document.getElementById('btn-' + t).className = 'py-2.5 rounded-xl text-gray-400'; });
            document.getElementById('tab-' + name).classList.remove('hidden'); document.getElementById('btn-' + name).className = 'py-2.5 rounded-xl text-amber-400 bg-amber-500/10';
        }
        function triggerSpeechLab() {
            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRec) { alert("يرجى استخدام متصفح Chrome لتفعيل لاقط الصوت."); return; }
            const rec = new SpeechRec(); rec.lang = 'en-US';
            document.getElementById('voiceScoreCard').innerText = "جاري الاستماع..."; rec.start();
            rec.onresult = (e) => { document.getElementById('voiceScoreCard').innerHTML = "🟢 نطق ممتاز ومفهوم! سمعنا: " + e.results[0][0].transcript; };
        }
    </script>
</body>
</html>
"""

components.html(cyber_saba_app, height=940, scrolling=False)
