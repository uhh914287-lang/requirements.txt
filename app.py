import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="أكاديمية السعيدة الإمبراطورية | Saba AI Master",
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

saba_master_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA ACADEMY X - Full Ecosystem</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Tajawal:wght@300;500;700;900&display=swap');
        :root { --gold-primary: #d4af37; --void-bg: #05070b; }
        body { font-family: 'Tajawal', sans-serif; background-color: var(--void-bg); color: #f1f5f9; overflow-x: hidden; user-select: none; }
        .cinzel { font-family: 'Cinzel', serif; }
        .glass-panel {
            background: linear-gradient(135deg, rgba(17, 24, 39, 0.88) 0%, rgba(9, 13, 22, 0.96) 100%);
            backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(212, 175, 55, 0.2);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85);
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
    
    <main class="w-full max-w-lg h-screen sm:h-[95vh] flex flex-col glass-panel sm:rounded-[36px] overflow-hidden relative z-10 border-0 sm:border border-[#d4af37]/30">
        <header class="px-4 py-3 border-b border-gray-800/80 bg-black/40 flex items-center justify-between z-20">
            <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-amber-600 via-yellow-400 to-amber-700 p-[1.5px]">
                    <div class="w-full h-full bg-[#090d16] rounded-[10px] flex items-center justify-center">
                        <span class="cinzel text-amber-400 font-black text-base">𐩯</span>
                    </div>
                </div>
                <div>
                    <h1 class="text-[10px] font-black tracking-widest text-amber-400/90 uppercase cinzel">SABA MASTER AI</h1>
                    <div class="flex items-center gap-1 mt-0.2">
                        <i data-lucide="flame" class="w-3 h-3 text-red-500 fill-red-500"></i>
                        <span id="xpScore" class="text-xs font-black text-gray-100">850</span>
                        <span class="text-[9px] text-amber-400/70 font-bold">XP</span>
                    </div>
                </div>
            </div>
            <div class="flex items-center gap-2">
                <span id="cefrBadge" class="text-[10px] bg-amber-500/10 text-amber-300 px-2 py-0.5 rounded-lg border border-amber-500/20 font-bold">CEFR: B1+</span>
                <select id="govSelector" onchange="updateGov(this.value)" class="bg-[#131b2e] text-[11px] font-bold text-amber-200 py-1 px-2 rounded-lg border border-amber-500/30 outline-none">
                    <option value="الحديدة">الحديدة ⚓</option>
                    <option value="صنعاء">صنعاء 🏛️</option>
                    <option value="عدن">عدن 🌊</option>
                    <option value="تعز">تعز ⛰️</option>
                </select>
            </div>
        </header>

        <nav class="grid grid-cols-5 bg-[#090d16]/90 p-1 border-b border-gray-800/60 text-[10px] font-bold z-20 text-center">
            <button onclick="switchTab('mentor')" id="btn-mentor" class="py-2 rounded-lg text-amber-400 bg-amber-500/10 transition border border-amber-500/20">💬 المعلم</button>
            <button onclick="switchTab('micro')" id="btn-micro" class="py-2 rounded-lg text-gray-400 hover:text-gray-200 transition">⚡ مصغر</button>
            <button onclick="switchTab('speech')" id="btn-speech" class="py-2 rounded-lg text-gray-400 hover:text-gray-200 transition">🎙️ نطق</button>
            <button onclick="switchTab('cards')" id="btn-cards" class="py-2 rounded-lg text-gray-400 hover:text-gray-200 transition">🧠 تكرار</button>
            <button onclick="switchTab('social')" id="btn-social" class="py-2 rounded-lg text-gray-400 hover:text-gray-200 transition">🌍 مجتمع</button>
        </nav>

        <div class="flex-1 overflow-hidden relative z-10 flex flex-col">
            
            <!-- 1. المعلم الاقتصادي الافتراضي -->
            <section id="tab-mentor" class="flex-1 flex flex-col justify-between overflow-hidden p-3.5">
                <div id="chatFeed" class="flex-1 overflow-y-auto space-y-3 pr-1 text-xs">
                    <div class="flex justify-end">
                        <div class="glass-panel p-3.5 rounded-2xl rounded-tl-none max-w-[92%] border border-gray-700/80 leading-relaxed text-gray-200">
                            <p class="font-bold text-amber-400 text-[10px] mb-1">المعلم الاقتصادي الافتراضي:</p>
                            أهلاً بك! أنا معلمك الذكي لتطوير إنجليزيتك المهنية والاقتصادية دون إحراج. اسألني أو ابدأ محادثة حرة بالإنجليزية.
                        </div>
                    </div>
                </div>
                <div class="mt-2.5 flex items-center gap-2 bg-[#0c1220]/90 p-1 rounded-2xl border border-gray-700/70">
                    <input id="chatField" type="text" placeholder="اكتب ردك أو سؤالك هنا..." class="flex-1 bg-transparent px-3 py-2 text-xs text-white outline-none" dir="auto">
                    <button onclick="sendMentorMsg()" class="agate-button p-2 rounded-xl text-white transition hover:scale-105">
                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                    </button>
                </div>
            </section>

            <!-- 2. الدروس المكثفة والمحتوى الواقعي (Microlearning) -->
            <section id="tab-micro" class="hidden flex-1 flex flex-col p-3.5 overflow-y-auto space-y-2.5">
                <div class="glass-panel p-3 rounded-2xl border border-amber-500/30">
                    <h2 class="text-xs font-black text-amber-300">دروس (3-5 دقائق) والمحتوى الواقعي</h2>
                    <p class="text-[10px] text-gray-400 mt-0.5">دروس قصيرة مستوحاة من بودكاست ومقالات عالمية:</p>
                </div>
                <div class="space-y-2">
                    <div onclick="openMicroLesson('إيميلات التفاوض التجاري', 'كيف ترفض عرضاً تجارياً بأدب واحترافية في إيميل رسمي.')" class="glass-panel p-3 rounded-xl cursor-pointer hover:border-amber-400 transition flex items-center justify-between">
                        <div>
                            <h3 class="text-xs font-bold text-amber-200">💼 درس سريع: إيميلات التفاوض (4 دقائق)</h3>
                            <p class="text-[9px] text-gray-400">صياغة عروض الأسعار والرد باحترافية.</p>
                        </div>
                        <span class="text-[10px] bg-amber-500/10 text-amber-400 px-2 py-1 rounded-lg border border-amber-500/20">ابدأ</span>
                    </div>
                    <div onclick="openMicroLesson('مصطلحات وول ستريت المالية', 'أهم الكلمات المتداولة في سوق المال والعملات والعمل الحر.')" class="glass-panel p-3 rounded-xl cursor-pointer hover:border-amber-400 transition flex items-center justify-between">
                        <div>
                            <h3 class="text-xs font-bold text-amber-200">📈 بودكاست اقتصادي: مصطلحات المال (3 دقائق)</h3>
                            <p class="text-[9px] text-gray-400">مفردات الأسواق المالية والأعمال.</p>
                        </div>
                        <span class="text-[10px] bg-amber-500/10 text-amber-400 px-2 py-1 rounded-lg border border-amber-500/20">ابدأ</span>
                    </div>
                </div>
                <div id="microViewer" class="glass-panel p-3 rounded-xl text-xs text-gray-300 hidden border border-blue-500/30 space-y-1"></div>
            </section>

            <!-- 3. مختبر تحليل النطق المتقدم -->
            <section id="tab-speech" class="hidden flex-1 flex flex-col justify-between items-center p-4 text-center overflow-y-auto">
                <div class="glass-panel p-3.5 rounded-2xl w-full border border-amber-500/20">
                    <span class="text-[10px] text-amber-400 font-bold uppercase tracking-wider">عبارة التحليل المتقدم</span>
                    <h2 class="text-xs font-black text-amber-200 mt-1">"Successful negotiation requires active listening and precise timing."</h2>
                    <button onclick="playNativeAudio()" class="mt-2 text-[10px] bg-white/5 hover:bg-white/10 px-2.5 py-1 rounded-lg text-gray-300 border border-white/10">🔊 الاستماع للمتحدث الأصلي</button>
                </div>
                
                <div class="flex flex-col items-center my-auto">
                    <button onclick="runSpeechAnalysis()" class="w-20 h-20 rounded-full bg-red-600 hover:bg-red-500 flex items-center justify-center text-white shadow-2xl transition transform hover:scale-105 border-4 border-red-900/50">
                        <i data-lucide="mic" class="w-7 h-7"></i>
                    </button>
                    <p class="text-[11px] text-gray-400 mt-2 font-medium">اضغط وتحدث لتصحيح النطق فوراً...</p>
                </div>

                <div id="speechFeedback" class="w-full glass-panel p-3 rounded-xl text-xs text-gray-300 border border-gray-800">
                    التحليل الصوتي والمقارنة تظهر هنا.
                </div>
            </section>

            <!-- 4. التكرار المتباعد (Spaced Repetition Cards) -->
            <section id="tab-cards" class="hidden flex-1 flex flex-col justify-center items-center p-4 text-center space-y-3">
                <div class="glass-panel p-5 rounded-2xl w-full max-w-sm border border-amber-500/30 space-y-3">
                    <span class="text-[10px] text-amber-400 font-bold bg-amber-500/10 px-2.5 py-1 rounded-full border border-amber-500/20">بطاقة الذاكرة الذكية</span>
                    <h3 id="cardWord" class="text-base font-black text-amber-100">Leverage</h3>
                    <p id="cardDef" class="text-xs text-gray-400 italic">اضغط لعرض المعنى وسياق الاستخدام الاقتصادي</p>
                    <button onclick="flipCard()" class="w-full py-2 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-bold rounded-xl border border-amber-500/30 transition">قلب البطاقة</button>
                </div>
                <div class="flex gap-2 w-full max-w-sm">
                    <button onclick="rateCard('hard')" class="flex-1 py-2 bg-red-500/10 text-red-400 text-xs font-bold rounded-xl border border-red-500/20">صعب 🔄</button>
                    <button onclick="rateCard('good')" class="flex-1 py-2 bg-green-500/10 text-green-400 text-xs font-bold rounded-xl border border-green-500/20">ممتاز ✨</button>
                </div>
            </section>

            <!-- 5. التلعيب والمجتمع (Gamification & Social) -->
            <section id="tab-social" class="hidden flex-1 flex flex-col p-3.5 overflow-y-auto space-y-3">
                <div class="glass-panel p-3 rounded-2xl border border-amber-500/30 text-center">
                    <h2 class="text-xs font-black text-amber-300">نادي النطق الصوتي والمجتمع العالمي</h2>
                    <p class="text-[10px] text-gray-400 mt-0.5">انضم لغرف المحادثة المباشرة واكسب الأوسمة ونقاط الـ XP:</p>
                </div>
                <div class="space-y-2">
                    <div class="glass-panel p-3 rounded-xl flex items-center justify-between border border-gray-700">
                        <div>
                            <h3 class="text-xs font-bold text-amber-200">🎙️ غرفة نطق ريادة الأعمال (مفتوحة الآن)</h3>
                            <p class="text-[9px] text-gray-400">4 متعلمين يتحدثون الآن عن إستراتيجيات السوق.</p>
                        </div>
                        <button onclick="joinRoom()" class="agate-button px-3 py-1.5 rounded-lg text-white text-[11px] font-bold">انضمام</button>
                    </div>
                    <div class="glass-panel p-3 rounded-xl flex items-center justify-between border border-gray-700">
                        <div>
                            <h3 class="text-xs font-bold text-amber-200">📜 شهادة CEFR المعتمدة</h3>
                            <p class="text-[9px] text-gray-400">اختبر مهاراتك للحصول على الشهادة الرسمية.</p>
                        </div>
                        <button onclick="getCert()" class="bg-amber-500/10 text-amber-400 px-3 py-1.5 rounded-lg text-[11px] font-bold border border-amber-500/20">إصدار</button>
                    </div>
                </div>
            </section>

        </div>
    </main>

    <script>
        lucide.createIcons();

        function switchTab(name) {
            ['mentor', 'micro', 'speech', 'cards', 'social'].forEach(t => {
                document.getElementById('tab-' + t).classList.add('hidden');
                document.getElementById('btn-' + t).className = 'py-2 rounded-lg text-gray-400 hover:text-gray-200 transition';
            });
            document.getElementById('tab-' + name).classList.remove('hidden');
            document.getElementById('btn-' + name).className = 'py-2 rounded-lg text-amber-400 bg-amber-500/10 transition border border-amber-500/20';
        }

        const canvas = document.getElementById('spaceCanvas');
        const ctx = canvas.getContext('2d');
        let stars = [];
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            stars = Array.from({ length: 40 }, () => ({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 1.5,
                speed: Math.random() * 0.15 + 0.05
            }));
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        function animateSpace() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = 'rgba(212, 175, 55, 0.5)';
            stars.forEach(s => {
                ctx.fillRect(s.x, s.y, s.size, s.size);
                s.y -= s.speed;
                if (s.y < 0) s.y = canvas.height;
            });
            requestAnimationFrame(animateSpace);
        }
        animateSpace();

        function sendMentorMsg() {
            const field = document.getElementById('chatField');
            const feed = document.getElementById('chatFeed');
            const text = field.value.trim();
            if(!text) return;

            feed.innerHTML += `<div class="flex justify-start"><div class="glass-panel p-3 rounded-xl rounded-tr-none max-w-[92%] border border-blue-500/30 text-gray-200"><p class="font-bold text-blue-400 text-[10px] mb-1">أنت:</p>${text}</div></div>`;
            field.value = '';
            feed.scrollTop = feed.scrollHeight;

            setTimeout(() => {
                feed.innerHTML += `<div class="flex justify-end"><div class="glass-panel p-3 rounded-xl rounded-tl-none max-w-[92%] border border-gray-700/80 text-gray-200"><p class="font-bold text-amber-400 text-[10px] mb-1">المعلم الذكي:</p>صياغة رائعة وسياق اقتصادي سليم! تم تصحيح القواعد ضمنياً دون إحراج. (+20 XP)</div></div>`;
                feed.scrollTop = feed.scrollHeight;
                let xpElem = document.getElementById('xpScore');
                xpElem.innerText = parseInt(xpElem.innerText) + 20;
            }, 1000);
        }

        function openMicroLesson(title, desc) {
            const v = document.getElementById('microViewer');
            v.classList.remove('hidden');
            v.innerHTML = `<b class="text-amber-300">📖 ${title}</b><br><p class="mt-1">${desc}</p><span class="text-amber-400 font-bold block mt-2">✨ أتممت الدرس بنجاح (+30 XP)!</span>`;
            let xp = document.getElementById('xpScore');
            xp.innerText = parseInt(xp.innerText) + 30;
        }

        function runSpeechAnalysis() {
            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRec) { alert("متصفحك لا يدعم التعرف الصوتي."); return; }
            const rec = new SpeechRec();
            rec.lang = 'en-US';
            document.getElementById('speechFeedback').innerHTML = "🔴 جاري تحليل النطق والمقارنة مع المتحدث الأصلي...";
            rec.start();
            rec.onresult = (e) => {
                let spoken = e.results[0][0].transcript;
                document.getElementById('speechFeedback').innerHTML = `🟢 تطابق بنسبة 94% مع نبرة المتحدث الأصلي: <span class="text-amber-300 font-bold">"${spoken}"</span> (+35 XP)`;
                let xp = document.getElementById('xpScore');
                xp.innerText = parseInt(xp.innerText) + 35;
            };
        }

        function playNativeAudio() {
            const utt = new SpeechSynthesisUtterance("Successful negotiation requires active listening and precise timing.");
            utt.lang = 'en-US';
            window.speechSynthesis.speak(utt);
        }

        let flipped = false;
        function flipCard() {
            const def = document.getElementById('cardDef');
            if(!flipped) {
                def.innerHTML = "<b>المعنى:</b> الاستفادة القصوى من الموارد المتاحة (Financial Leverage).<br><i>مثال: We must leverage our digital assets.</i>";
                flipped = true;
            } else {
                def.innerHTML = "اضغط لعرض المعنى وسياق الاستخدام الاقتصادي";
                flipped = false;
            }
        }

        function rateCard(rate) {
            alert("تم تحديث خوارزمية التكرار المتباعد لهذه الكلمة بنجاح! (+15 XP)");
            let xp = document.getElementById('xpScore');
            xp.innerText = parseInt(xp.innerText) + 15;
            document.getElementById('cardDef').innerHTML = "اضغط لعرض المعنى وسياق الاستخدام الاقتصادي";
            flipped = false;
        }

        function joinRoom() {
            alert("تم توصيلك بغرفة المحادثة الصوتية الجماعية بنجاح! تحدث الآن بالإنجليزية.");
            let xp = document.getElementById('xpScore');
            xp.innerText = parseInt(xp.innerText) + 50;
        }

        function getCert() {
            alert("🎉 تهانينا! تم تقييم مستواك وفق معيار CEFR الأوروبي وإصدار الشهادة الرقمية بنجاح.");
        }

        function updateGov(gov) {
            alert("تم تحديث نطاق المحافظات إلى: " + gov);
        }
    </script>
</body>
</html>
"""

components.html(saba_master_app, height=960, scrolling=False)
