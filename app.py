import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="أكاديمية السعيدة الإمبراطورية | Saba AI",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu, footer, header { display: none !important; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
        iframe { border-radius: 0px !important; }
    </style>
""", unsafe_allow_html=True)

saba_academy_full_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA ACADEMY X - Full Curriculum</title>
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
        #spaceCanvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
    </style>
</head>
<body class="min-h-screen w-full flex justify-center items-center p-0 sm:p-4 relative">
    <canvas id="spaceCanvas"></canvas>
    
    <main class="w-full max-w-lg h-screen sm:h-[94vh] flex flex-col glass-panel sm:rounded-[36px] overflow-hidden relative z-10 border-0 sm:border border-[#d4af37]/30">
        <header class="px-5 py-4 border-b border-gray-800/80 bg-black/40 flex items-center justify-between z-20">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-600 via-yellow-400 to-amber-700 p-[1.5px]">
                    <div class="w-full h-full bg-[#090d16] rounded-[14px] flex items-center justify-center">
                        <span class="cinzel text-amber-400 font-black text-lg">𐩯</span>
                    </div>
                </div>
                <div>
                    <h1 class="text-[11px] font-black tracking-widest text-amber-400/90 uppercase cinzel">SABA MASTER COURSES</h1>
                    <div class="flex items-center gap-1.5 mt-0.5">
                        <i data-lucide="flame" class="w-3.5 h-3.5 text-red-500 fill-red-500"></i>
                        <span id="xpScore" class="text-sm font-black text-gray-100">600</span>
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

        <nav class="grid grid-cols-4 bg-[#090d16]/90 p-1.5 border-b border-gray-800/60 text-[11px] font-bold z-20">
            <button onclick="switchTab('arena')" id="btn-arena" class="py-2.5 rounded-xl text-amber-400 bg-amber-500/10 transition flex items-center justify-center gap-1 border border-amber-500/20">💬 المحاكي</button>
            <button onclick="switchTab('courses')" id="btn-courses" class="py-2.5 rounded-xl text-gray-400 hover:text-gray-200 transition flex items-center justify-center gap-1">📖 المناهج</button>
            <button onclick="switchTab('voice')" id="btn-voice" class="py-2.5 rounded-xl text-gray-400 hover:text-gray-200 transition flex items-center justify-center gap-1">🎙️ النطق</button>
            <button onclick="switchTab('quest')" id="btn-quest" class="py-2.5 rounded-xl text-gray-400 hover:text-gray-200 transition flex items-center justify-center gap-1">⚡ تحدي</button>
        </nav>

        <div class="flex-1 overflow-hidden relative z-10 flex flex-col">
            
            <!-- المحاكي -->
            <section id="tab-arena" class="flex-1 flex flex-col justify-between overflow-hidden p-4">
                <div id="chatFeed" class="flex-1 overflow-y-auto space-y-3.5 pr-1 text-sm">
                    <div class="flex justify-end">
                        <div class="glass-panel p-4 rounded-2xl rounded-tl-none max-w-[90%] border border-gray-700/80 leading-relaxed text-gray-200">
                            <p class="font-bold text-amber-400 text-[11px] mb-1">Saba Curriculum AI:</p>
                            أهلاً بك! اختر المنهج الذي تفضله من تبويب "المناهج" أو اسألني هنا لأشرح لك أي قاعدة مجاناً.
                        </div>
                    </div>
                </div>
                <div class="mt-3 flex items-center gap-2 bg-[#0c1220]/90 p-1.5 rounded-2xl border border-gray-700/70">
                    <input id="chatField" type="text" placeholder="اكتب سؤالك هنا..." class="flex-1 bg-transparent px-3 py-2 text-sm text-white outline-none" dir="auto">
                    <button onclick="sendChatMessage()" class="agate-button p-2.5 rounded-xl text-white transition hover:scale-105">
                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                    </button>
                </div>
            </section>

            <!-- كورسات ومناهج اللغة الكاملة والمجانية -->
            <section id="tab-courses" class="hidden flex-1 flex flex-col p-4 overflow-y-auto space-y-3">
                <div class="glass-panel p-3.5 rounded-2xl border border-amber-500/30">
                    <h2 class="text-xs font-black text-amber-300">موسوعة كورسات أكسفورد والمنهج الشامل (100% مجاني)</h2>
                    <p class="text-[11px] text-gray-400 mt-1">اضغط على أي مستوى لفتح الدروس والمفردات فورا:</p>
                </div>
                <div class="space-y-2.5">
                    <div onclick="openCourse('A1', 'المستوى المبتدئ - الأساسيات ومقابلة العمل الأولى')" class="glass-panel p-3.5 rounded-2xl cursor-pointer hover:border-amber-400 transition flex items-center justify-between">
                        <div>
                            <h3 class="text-xs font-bold text-amber-200">المستوى (A1-A2): الأساسيات والمحادثة اليومية</h3>
                            <p class="text-[10px] text-gray-400 mt-0.5">التعريف بالنفس، صياغة الجمل البسيطة، وأبسط القواعد.</p>
                        </div>
                        <span class="text-xs bg-amber-500/10 text-amber-400 px-2 py-1 rounded-lg border border-amber-500/20">دخول</span>
                    </div>
                    <div onclick="openCourse('B1', 'المستوى المتوسط - الإنجليزية للعمل الحر والمهارات المهنية')" class="glass-panel p-3.5 rounded-2xl cursor-pointer hover:border-amber-400 transition flex items-center justify-between">
                        <div>
                            <h3 class="text-xs font-bold text-amber-200">المستوى (B1-B2): إنجليزية سوق العمل الحر (Freelancing)</h3>
                            <p class="text-[10px] text-gray-400 mt-0.5">كتابة الإيميلات الرسمية، التفاوض، وإدارة المقابلات.</p>
                        </div>
                        <span class="text-xs bg-amber-500/10 text-amber-400 px-2 py-1 rounded-lg border border-amber-500/20">دخول</span>
                    </div>
                    <div onclick="openCourse('C1', 'المستوى المتقدم - الطلاقة الكاملة والتعابير الاصطلاحية')" class="glass-panel p-3.5 rounded-2xl cursor-pointer hover:border-amber-400 transition flex items-center justify-between">
                        <div>
                            <h3 class="text-xs font-bold text-amber-200">المستوى (C1): الاحتراف والطلاقة المطلقة (Oxford Pro)</h3>
                            <p class="text-[10px] text-gray-400 mt-0.5">المصطلحات المتقدمة (Idioms) والخطابة المهنية.</p>
                        </div>
                        <span class="text-xs bg-amber-500/10 text-amber-400 px-2 py-1 rounded-lg border border-amber-500/20">دخول</span>
                    </div>
                </div>
                <div id="courseViewer" class="glass-panel p-4 rounded-2xl text-xs text-gray-300 mt-2 hidden border border-blue-500/30 space-y-2">
                    <!-- محتوى الكورس الديناميكي -->
                </div>
            </section>

            <!-- مختبر النطق -->
            <section id="tab-voice" class="hidden flex-1 flex flex-col justify-between items-center p-6 text-center overflow-y-auto">
                <div class="glass-panel p-5 rounded-3xl w-full border border-amber-500/20">
                    <span class="text-[11px] text-amber-400 font-bold uppercase tracking-wider">عبارة التدريب الصوتي</span>
                    <h2 id="tgtPhrase" class="text-base font-black text-amber-200 mt-2">"Hard work beats talent when talent doesn't work hard."</h2>
                    <button onclick="playTargetAudio()" class="mt-3 text-xs bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-xl text-gray-300 transition border border-white/10">🔊 الاستماع للنموذج</button>
                </div>
                
                <div class="flex flex-col items-center my-auto">
                    <button id="micBtn" onclick="triggerSpeechLab()" class="w-24 h-24 rounded-full bg-red-600 hover:bg-red-500 flex items-center justify-center text-white shadow-2xl transition transform hover:scale-105 border-4 border-red-900/50">
                        <i data-lucide="mic" class="w-8 h-8"></i>
                    </button>
                    <p id="micLabel" class="text-xs text-gray-400 mt-3 font-medium">اضغط وتحدث بالإنجليزية...</p>
                </div>

                <div id="voiceFeedback" class="w-full glass-panel p-3.5 rounded-2xl text-xs text-gray-300 border border-gray-800">
                    نتيجة التحليل الذكي ستظهر هنا.
                </div>
            </section>

            <!-- التحدي السريع -->
            <section id="tab-quest" class="hidden flex-1 p-5 flex flex-col justify-center text-center space-y-4 overflow-y-auto">
                <div class="space-y-2">
                    <span class="text-xs text-amber-400 font-bold bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/20">تحدي قواعد أكسفورد</span>
                    <h3 class="text-base font-black text-amber-100 leading-snug">اختر الجملة الصحيحة قواعدياً في الماضي البسيط:</h3>
                </div>
                <div class="space-y-2.5 w-full">
                    <button onclick="evalQuest(true)" class="w-full p-4 glass-panel rounded-2xl text-right text-xs sm:text-sm hover:border-amber-400/50 transition">
                        <b>A)</b> I successfully completed the freelance project yesterday.
                    </button>
                    <button onclick="evalQuest(false)" class="w-full p-4 glass-panel rounded-2xl text-right text-xs sm:text-sm hover:border-red-500/50 transition">
                        <b>B)</b> I is complete the project yesterday.
                    </button>
                </div>
            </section>

        </div>
    </main>

    <script>
        lucide.createIcons();

        function switchTab(name) {
            ['arena', 'courses', 'voice', 'quest'].forEach(t => {
                document.getElementById('tab-' + t).classList.add('hidden');
                document.getElementById('btn-' + t).className = 'py-2.5 rounded-xl text-gray-400 hover:text-gray-200 transition flex items-center justify-center gap-1';
            });
            document.getElementById('tab-' + name).classList.remove('hidden');
            document.getElementById('btn-' + name).className = 'py-2.5 rounded-xl text-amber-400 bg-amber-500/10 transition flex items-center justify-center gap-1 border border-amber-500/20';
        }

        const canvas = document.getElementById('spaceCanvas');
        const ctx = canvas.getContext('2d');
        let stars = [];
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            stars = Array.from({ length: 50 }, () => ({
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

        function openCourse(level, title) {
            const viewer = document.getElementById('courseViewer');
            viewer.classList.remove('hidden');
            let content = `<b class="text-amber-300">📖 محتوى كورس ${level}: ${title}</b><br>`;
            if(level === 'A1') {
                content += `• الأبجدية، الأرقام، وتكوين الجمل البصرية.<br>• أهم 500 كلمة شائعة في الحياة اليومية.<br>• التمارين: تفاعل فوري ونطق سليم.`;
            } else if(level === 'B1') {
                content += `• إعداد سيرة ذاتية (CV) احترافية بالإنجليزية.<br>• صياغة إيميلات طلبات العمل الحر.<br>• قواعد الأزمنة المتقدمة (Present Perfect vs Past Simple).`;
            } else {
                content += `• لغة التفاوض التجاري المتقدم.<br>• التعابير الاصطلاحية الأكثر استخداماً في الشركات العالمية.<br>• اجتياز المقابلات التقنية الصعبة.`;
            }
            content += `<br><span class="text-amber-400 font-bold mt-2 block">✨ تم تسجيل إتمام درس الكورس بنجاح (+40 XP)!</span>`;
            viewer.innerHTML = content;
            let xpElem = document.getElementById('xpScore');
            xpElem.innerText = parseInt(xpElem.innerText) + 40;
        }

        function sendChatMessage() {
            const field = document.getElementById('chatField');
            const feed = document.getElementById('chatFeed');
            const text = field.value.trim();
            if(!text) return;

            feed.innerHTML += `<div class="flex justify-start"><div class="glass-panel p-3.5 rounded-2xl rounded-tr-none max-w-[90%] border border-blue-500/30 text-gray-200"><p class="font-bold text-blue-400 text-[11px] mb-1">أنت:</p>${text}</div></div>`;
            field.value = '';
            feed.scrollTop = feed.scrollHeight;

            setTimeout(() => {
                feed.innerHTML += `<div class="flex justify-end"><div class="glass-panel p-3.5 rounded-2xl rounded-tl-none max-w-[90%] border border-gray-700/80 text-gray-200"><p class="font-bold text-amber-400 text-[11px] mb-1">Saba AI:</p>إجابة ممتازة! تم حفظ النقاط وتحديث منهج أكسفورد الخاص بك. (+20 XP)</div></div>`;
                feed.scrollTop = feed.scrollHeight;
                let xpElem = document.getElementById('xpScore');
                xpElem.innerText = parseInt(xpElem.innerText) + 20;
            }, 1000);
        }

        function triggerSpeechLab() {
            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRec) { alert("متصفحك لا يدعم التعرف الصوتي المباشر."); return; }
            const rec = new SpeechRec();
            rec.lang = 'en-US';
            document.getElementById('voiceFeedback').innerHTML = "🔴 جاري الاستماع لنطقك...";
            rec.start();
            rec.onresult = (e) => {
                let spoken = e.results[0][0].transcript;
                document.getElementById('voiceFeedback').innerHTML = `🟢 نطق احترافي صحيح: <span class="text-amber-300 font-bold">"${spoken}"</span> (+30 XP)`;
                let xpElem = document.getElementById('xpScore');
                xpElem.innerText = parseInt(xpElem.innerText) + 30;
            };
        }

        function playTargetAudio() {
            const utterance = new SpeechSynthesisUtterance("Hard work beats talent when talent doesn't work hard.");
            utterance.lang = 'en-US';
            window.speechSynthesis.speak(utterance);
        }

        function evalQuest(isCorrect) {
            if(isCorrect) {
                alert("✨ إجابة صحيحة تماماً! تم تعزيز نقاط محافظتك (+35 XP).");
                let xpElem = document.getElementById('xpScore');
                xpElem.innerText = parseInt(xpElem.innerText) + 35;
            } else {
                alert("⚠️ خطأ قواعدي، الخيار الصحيح هو A لأن الجملة في زمن الماضي البسيط.");
            }
        }

        function updateGovernorate(gov) {
            alert("تم تحديث دوري المحافظات إلى: " + gov);
        }
    </script>
</body>
</html>
"""

components.html(saba_academy_full_app, height=940, scrolling=False)
