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
""", unsafe_allow_html=True)

# 3. الواجهة الإمبراطورية الكاملة (تصميم Neo-Sabaean Glassmorphism مع تفاعلات كاملة)
saba_academy_full_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA ACADEMY X</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Tajawal:wght@300;500;700;900&display=swap');
        :root { --gold-primary: #d4af37; --void-bg: #05070b; }
        body { font-family: 'Tajawal', sans-serif; background-color: var(--void-bg); color: #f1f5f9; overflow-x: hidden; user-select: none; }
        .cinzel { font-family: 'Cinzel', serif; }
        .glass-panel {
            background: linear-gradient(135deg, rgba(17, 24, 39, 0.85) 0%, rgba(9, 13, 22, 0.95) 100%);
            backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(212, 175, 55, 0.18);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
        }
        .agate-button {
            background: linear-gradient(135deg, #a81c1c 0%, #5e0808 100%);
            box-shadow: 0 4px 20px rgba(168, 28, 28, 0.4);
        }
        /* تصميم خلفية النجوم المتحركة Canvas */
        #spaceCanvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
    </style>
</head>
<body class="min-h-screen w-full flex justify-center items-center p-0 sm:p-4 relative">
    <canvas id="spaceCanvas"></canvas>
    
    <main class="w-full max-w-lg h-screen sm:h-[94vh] flex flex-col glass-panel sm:rounded-[36px] overflow-hidden relative z-10 border-0 sm:border border-[#d4af37]/30">
        <!-- الهيدر الملكي -->
        <header class="px-5 py-4 border-b border-gray-800/80 bg-black/40 flex items-center justify-between z-20">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-600 via-yellow-400 to-amber-700 p-[1.5px]">
                    <div class="w-full h-full bg-[#090d16] rounded-[14px] flex items-center justify-center">
                        <span class="cinzel text-amber-400 font-black text-lg">𐩯</span>
                    </div>
                </div>
                <div>
                    <h1 class="text-[11px] font-black tracking-widest text-amber-400/90 uppercase cinzel">SABA ACADEMY</h1>
                    <div class="flex items-center gap-1.5 mt-0.5">
                        <i data-lucide="flame" class="w-3.5 h-3.5 text-red-500 fill-red-500"></i>
                        <span id="xpScore" class="text-sm font-black text-gray-100">320</span>
                        <span class="text-[10px] text-amber-400/70 font-bold">XP</span>
                    </div>
                </div>
            </div>
            <select id="govSelector" onchange="updateGovernorate(this.value)" class="bg-[#131b2e] text-xs font-bold text-amber-200 py-1.5 px-3 rounded-xl border border-amber-500/30 outline-none">
                <option value="الحديدة">الحديدة ⚓</option>
                <option value="صنعاء">صنعاء 🏛️</option>
                <option value="عدن">عدن 🌊</option>
                <option value="تعز">تعز ⛰️</option>
                <option value="حضرموت">حضرموت 🌴</option>
                <option value="مأرب">مأرب 🏜️</option>
            </select>
        </header>

        <!-- شريط التنقل السفلي للتبويبات -->
        <nav class="grid grid-cols-3 bg-[#090d16]/90 p-1.5 border-b border-gray-800/60 text-xs font-bold z-20">
            <button onclick="switchTab('arena')" id="btn-arena" class="py-2.5 rounded-xl text-amber-400 bg-amber-500/10 transition flex items-center justify-center gap-1.5 border border-amber-500/20">💬 المحاكي</button>
            <button onclick="switchTab('voice')" id="btn-voice" class="py-2.5 rounded-xl text-gray-400 hover:text-gray-200 transition flex items-center justify-center gap-1.5">🎙️ مختبر النطق</button>
            <button onclick="switchTab('quest')" id="btn-quest" class="py-2.5 rounded-xl text-gray-400 hover:text-gray-200 transition flex items-center justify-center gap-1.5">⚡ سباق 60ث</button>
        </nav>

        <!-- محتوى الأقسام الديناميكية -->
        <div class="flex-1 overflow-hidden relative z-10 flex flex-col">
            
            <!-- 1. قسم المحاكي الذكي للمقابلات -->
            <section id="tab-arena" class="flex-1 flex flex-col justify-between overflow-hidden p-4">
                <div id="chatFeed" class="flex-1 overflow-y-auto space-y-3.5 pr-1 text-sm">
                    <div class="flex justify-end">
                        <div class="glass-panel p-4 rounded-2xl rounded-tl-none max-w-[90%] border border-gray-700/80 leading-relaxed text-gray-200">
                            <p class="font-bold text-amber-400 text-[11px] mb-1">HR Director (Saba AI):</p>
                            Welcome to Saba Academy X! Why are you the ideal remote freelancer for this international contract?
                        </div>
                    </div>
                </div>
                <div class="mt-3 flex items-center gap-2 bg-[#0c1220]/90 p-1.5 rounded-2xl border border-gray-700/70">
                    <input id="chatField" type="text" placeholder="اكتب ردك بالإنجليزية هنا..." class="flex-1 bg-transparent px-3 py-2 text-sm text-white outline-none" dir="auto">
                    <button onclick="sendChatMessage()" class="agate-button p-2.5 rounded-xl text-white transition hover:scale-105">
                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                    </button>
                </div>
            </section>

            <!-- 2. قسم مختبر النطق الصوتي Shadowing -->
            <section id="tab-voice" class="hidden flex-1 flex flex-col justify-between items-center p-6 text-center overflow-y-auto">
                <div class="glass-panel p-5 rounded-3xl w-full border border-amber-500/20">
                    <span class="text-[11px] text-amber-400 font-bold uppercase tracking-wider">عبارة التدريب الاحترافية</span>
                    <h2 id="tgtPhrase" class="text-base font-black text-amber-200 mt-2">"Opportunities don't happen, you create them."</h2>
                    <button onclick="playTargetAudio()" class="mt-3 text-xs bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-xl text-gray-300 transition border border-white/10">🔊 الاستماع للنموذج</button>
                </div>
                
                <div class="flex flex-col items-center my-auto">
                    <button id="micBtn" onclick="triggerSpeechLab()" class="w-24 h-24 rounded-full bg-red-600 hover:bg-red-500 flex items-center justify-center text-white shadow-2xl transition transform hover:scale-105 border-4 border-red-900/50">
                        <i data-lucide="mic" class="w-8 h-8"></i>
                    </button>
                    <p id="micLabel" class="text-xs text-gray-400 mt-3 font-medium">اضغط على الميكروفون وابدأ القراءة...</p>
                </div>

                <div id="voiceFeedback" class="w-full glass-panel p-3.5 rounded-2xl text-xs text-gray-300 border border-gray-800">
                    نتيجة التحليل الذكي والتقييم ستظهر هنا فور انتهائك من التحدث.
                </div>
            </section>

            <!-- 3. قسم تحدي الـ 60 ثانية ودوري المحافظات -->
            <section id="tab-quest" class="hidden flex-1 p-5 flex flex-col justify-center text-center space-y-4 overflow-y-auto">
                <div class="space-y-2">
                    <span class="text-xs text-amber-400 font-bold bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/20">تحدي سوق العمل الحر</span>
                    <h3 class="text-base font-black text-amber-100 leading-snug">كيف ترد باحترافية على عميل يطلب تخفيض سعرك بنسبة 50%؟</h3>
                </div>
                <div class="space-y-2.5 w-full">
                    <button onclick="evalQuest(true)" class="w-full p-4 glass-panel rounded-2xl text-right text-xs sm:text-sm hover:border-amber-400/50 transition leading-relaxed">
                        <b>A)</b> My rate reflects the high quality, speed, and business value I deliver to your project.
                    </button>
                    <button onclick="evalQuest(false)" class="w-full p-4 glass-panel rounded-2xl text-right text-xs sm:text-sm hover:border-red-500/50 transition leading-relaxed">
                        <b>B)</b> Okay, I will reduce my price immediately to get the job.
                    </button>
                </div>
            </section>

        </div>
    </main>

    <script>
        lucide.createIcons();

        // نظام تبديل التبويبات بسلاسة
        function switchTab(name) {
            ['arena', 'voice', 'quest'].forEach(t => {
                document.getElementById('tab-' + t).classList.add('hidden');
                document.getElementById('btn-' + t).className = 'py-2.5 rounded-xl text-gray-400 hover:text-gray-200 transition flex items-center justify-center gap-1.5';
            });
            document.getElementById('tab-' + name).classList.remove('hidden');
            document.getElementById('btn-' + name).className = 'py-2.5 rounded-xl text-amber-400 bg-amber-500/10 transition flex items-center justify-center gap-1.5 border border-amber-500/20';
        }

        // تأثير النجوم المتحركة في الخلفية (Canvas)
        const canvas = document.getElementById('spaceCanvas');
        const ctx = canvas.getContext('2d');
        let stars = [];
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            stars = Array.from({ length: 60 }, () => ({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 1.5,
                speed: Math.random() * 0.2 + 0.05
            }));
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        function animateSpace() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = 'rgba(212, 175, 55, 0.6)';
            stars.forEach(s => {
                ctx.fillRect(s.x, s.y, s.size, s.size);
                s.y -= s.speed;
                if (s.y < 0) s.y = canvas.height;
            });
            requestAnimationFrame(animateSpace);
        }
        animateSpace();

        // محاكي المحادثة التفاعلي
        function sendChatMessage() {
            const field = document.getElementById('chatField');
            const feed = document.getElementById('chatFeed');
            const text = field.value.trim();
            if(!text) return;

            feed.innerHTML += `
                <div class="flex justify-start">
                    <div class="glass-panel p-3.5 rounded-2xl rounded-tr-none max-w-[90%] border border-blue-500/30 text-gray-200">
                        <p class="font-bold text-blue-400 text-[11px] mb-1">أنت (Freelancer):</p>
                        ${text}
                    </div>
                </div>`;
            field.value = '';
            feed.scrollTop = feed.scrollHeight;

            setTimeout(() => {
                feed.innerHTML += `
                    <div class="flex justify-end">
                        <div class="glass-panel p-3.5 rounded-2xl rounded-tl-none max-w-[90%] border border-gray-700/80 text-gray-200">
                            <p class="font-bold text-amber-400 text-[11px] mb-1">HR Director (Saba AI):</p>
                            إجابة ممتازة ومقنعة! تم إضافة +15 XP لرصيد محافظتك. واصل التقدم.
                        </div>
                    </div>`;
                feed.scrollTop = feed.scrollHeight;
                let xpElem = document.getElementById('xpScore');
                xpElem.innerText = parseInt(xpElem.innerText) + 15;
            }, 1000);
        }

        // مختبر النطق عبر Web Speech API
        function triggerSpeechLab() {
            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRec) {
                alert("عذراً، متصفحك لا يدعم التعرف على الصوت المباشر. يجدر استخدام متصفح Google Chrome.");
                return;
            }
            const rec = new SpeechRec();
            rec.lang = 'en-US';
            document.getElementById('voiceFeedback').innerHTML = "🔴 جاري الاستماع لنطقك... تحدث الآن بوضوح.";
            rec.start();

            rec.onresult = (e) => {
                let spoken = e.results[0][0].transcript;
                document.getElementById('voiceFeedback').innerHTML = `🟢 نطق رائع! تم رصد: <span class="text-amber-300 font-bold">"${spoken}"</span> (+20 XP)`;
                let xpElem = document.getElementById('xpScore');
                xpElem.innerText = parseInt(xpElem.innerText) + 20;
            };
            rec.onerror = () => {
                document.getElementById('voiceFeedback').innerHTML = "⚠️ لم يتم التقاط الصوت بوضوح، حاول مرة أخرى.";
            };
        }

        function playTargetAudio() {
            const utterance = new SpeechSynthesisUtterance("Opportunities don't happen, you create them.");
            utterance.lang = 'en-US';
            window.speechSynthesis.speak(utterance);
        }

        // تقييم التحدي
        function evalQuest(isCorrect) {
            if(isCorrect) {
                alert("✨ إجابة ذكية واحترافية للغاية! تم رفع نقاط محافظتك بنجاح (+30 XP).");
                let xpElem = document.getElementById('xpScore');
                xpElem.innerText = parseInt(xpElem.innerText) + 30;
            } else {
                alert("⚠️ تنبيه: قبول التخفيض الفوري يقلل من قيمتك المهنية في السوق الحر. حاول اختيار الإجابة A.");
            }
        }

        function updateGovernorate(gov) {
            alert("تم تغيير نطاق المنافسة إلى دوري محافظة: " + gov + "! بالتوفيق.");
        }
    </script>
</body>
</html>
"""

# عرض التطبيق بالكامل داخل Streamlit بدقة عالية
components.html(saba_app_full_code if 'saba_app_full_code' in locals() else saba_academy_full_app, height=940, scrolling=False)
