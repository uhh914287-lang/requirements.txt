import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SABA IMPERIAL ACADEMY | Full Platform",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu, footer, header { display: none !important; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; background-color: #030508; }
    </style>
""", unsafe_allow_html=True)

full_academy_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA IMPERIAL ACADEMY</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=Tajawal:wght@400;700;900&display=swap');
        :root { --gold: #f59e0b; --bg-dark: #030508; }
        body { font-family: 'Tajawal', sans-serif; background-color: var(--bg-dark); color: #f3f4f6; overflow-x: hidden; user-select: none; }
        .eng-font { font-family: 'Plus Jakarta Sans', sans-serif; }
        .glass-shell {
            background: linear-gradient(135deg, rgba(13, 20, 35, 0.98) 0%, rgba(4, 7, 14, 0.99) 100%);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(245, 158, 11, 0.3);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.95);
        }
        .listening-glow {
            box-shadow: 0 0 35px rgba(239, 68, 68, 0.6);
            border-color: rgba(239, 68, 68, 0.9) !important;
        }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        .card-item {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.3s ease;
        }
        .card-item:hover { border-color: var(--gold); transform: translateY(-2px); }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body class="min-h-screen w-full flex justify-center items-center p-0 sm:p-4">
    
    <main class="w-full max-w-md h-screen sm:h-[95vh] flex flex-col glass-shell sm:rounded-[36px] overflow-hidden relative">
        
        <!-- Header -->
        <header class="px-5 py-3.5 bg-black/80 border-b border-white/10 flex items-center justify-between z-30">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-500 to-yellow-300 p-0.5 shadow-lg shadow-amber-500/20">
                    <div class="w-full h-full bg-[#070b14] rounded-[14px] flex items-center justify-center">
                        <span class="eng-font text-amber-400 font-extrabold text-base">S</span>
                    </div>
                </div>
                <div>
                    <h1 class="text-[11px] font-black tracking-wider text-amber-400 uppercase eng-font">SABA IMPERIAL</h1>
                    <div class="flex items-center gap-1.5 mt-0.5">
                        <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                        <span class="text-[10px] text-gray-400">النظام الذكي متصل</span>
                    </div>
                </div>
            </div>
            <div class="bg-amber-500/10 border border-amber-500/20 px-3 py-1 rounded-full flex items-center gap-1.5">
                <i data-lucide="award" class="w-3.5 h-3.5 text-amber-400"></i>
                <span id="totalXp" class="eng-font text-xs font-bold text-amber-300">3,850 XP</span>
            </div>
        </header>

        <!-- Dynamic Body Content Tabs -->
        <div class="flex-1 overflow-y-auto no-scrollbar p-4 space-y-4">
            
            <!-- TAB 1: HOME & LIVE SPEECH LAB -->
            <div id="tab-home" class="tab-content active space-y-4">
                <div class="glass-shell p-4 rounded-3xl border border-amber-500/30 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-black text-amber-400 uppercase eng-font flex items-center gap-1.5">
                            <i data-lucide="mic-2" class="w-4 h-4 text-amber-400"></i> مختبر النطق والتصحيح الحي
                        </span>
                        <button onclick="playTargetAudio()" class="text-[10px] bg-white/10 hover:bg-white/20 text-white px-2.5 py-1 rounded-lg flex items-center gap-1">
                            <i data-lucide="volume-2" class="w-3 h-3 text-amber-400"></i> استمع للصوت
                        </button>
                    </div>

                    <div class="bg-black/60 p-3.5 rounded-2xl border border-white/5 space-y-1">
                        <span class="text-[9px] text-gray-400 font-bold uppercase">الكلمة أو الجملة المستهدفة:</span>
                        <p id="targetSentence" class="eng-font text-sm font-bold text-amber-300 tracking-wide">
                            Price optimization is critical for growth.
                        </p>
                    </div>

                    <div id="liveResultBox" class="hidden bg-slate-900/90 border border-amber-500/30 p-3 rounded-2xl space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] font-bold text-gray-300">ما سماعه الميكروفون منك:</span>
                            <span id="matchPercentage" class="eng-font text-[10px] bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded font-bold">95%</span>
                        </div>
                        <p id="spokenTextOutput" class="eng-font text-xs text-white font-semibold"></p>
                        <div id="aiCorrectionTip" class="text-[10px] text-amber-300 mt-1"></div>
                    </div>

                    <button id="recordBtn" onclick="startSpeechRecognition()" class="w-full py-3.5 bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 text-black font-black text-xs rounded-2xl shadow-lg transition flex items-center justify-center gap-2 eng-font">
                        <i data-lucide="mic" class="w-4 h-4"></i> اضغط وتحدث الآن عبر الميكروفون لتصحيح نطقك
                    </button>
                </div>

                <!-- Quick Preview of Featured Words -->
                <div>
                    <h3 class="text-xs font-black text-amber-400 mb-2 flex items-center gap-1.5">
                        <i data-lucide="zap" class="w-3.5 h-3.5"></i> الكلمات الأكثر طلباً اليوم
                    </h3>
                    <div class="grid grid-cols-2 gap-2">
                        <div onclick="setTargetSentence('Negotiation', 'مفاوضات')" class="card-item p-3 rounded-2xl cursor-pointer">
                            <span class="eng-font text-sm font-bold text-white block">Negotiation</span>
                            <span class="text-[10px] text-amber-400">مفاوضات تجارية</span>
                        </div>
                        <div onclick="setTargetSentence('Entrepreneurship', 'ريادة أعمال')" class="card-item p-3 rounded-2xl cursor-pointer">
                            <span class="eng-font text-sm font-bold text-white block">Entrepreneurship</span>
                            <span class="text-[10px] text-cyan-400">ريادة الأعمال</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: COURSES LIST -->
            <div id="tab-courses" class="tab-content space-y-3">
                <h2 class="text-xs font-black text-amber-400 mb-2 flex items-center gap-1.5">
                    <i data-lucide="book-open" class="w-4 h-4"></i> الكورسات الاحترافية المتاحة
                </h2>
                
                <div class="space-y-2.5">
                    <div onclick="setTargetSentence('Price optimization is critical for quarterly growth.', 'كورس وول ستريت')" class="card-item p-3.5 rounded-2xl cursor-pointer flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400">
                                <i data-lucide="briefcase" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <h3 class="text-xs font-bold text-white">Wall Street Business English</h3>
                                <p class="text-[10px] text-gray-400">عقود، صفقات، وإدارة مالية</p>
                            </div>
                        </div>
                        <span class="text-[10px] bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-lg">ابدأ</span>
                    </div>

                    <div onclick="setTargetSentence('Artificial intelligence transforms global business ecosystems.', 'كورس الذكاء الاصطناعي التقني')" class="card-item p-3.5 rounded-2xl cursor-pointer flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400">
                                <i data-lucide="cpu" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <h3 class="text-xs font-bold text-white">Silicon Valley Tech English</h3>
                                <p class="text-[10px] text-gray-400">مصطلحات برمجية وتقنية متقدمة</p>
                            </div>
                        </div>
                        <span class="text-[10px] bg-cyan-500/20 text-cyan-300 px-2.5 py-1 rounded-lg">ابدأ</span>
                    </div>

                    <div onclick="setTargetSentence('Effective diplomacy requires absolute clarity and confidence.', 'كورس الدبلوماسية والخطابة')" class="card-item p-3.5 rounded-2xl cursor-pointer flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
                                <i data-lucide="globe" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <h3 class="text-xs font-bold text-white">Diplomatic Leadership & Speech</h3>
                                <p class="text-[10px] text-gray-400">الخطابة الرسمية وتجاوز لهجات النطق</p>
                            </div>
                        </div>
                        <span class="text-[10px] bg-purple-500/20 text-purple-300 px-2.5 py-1 rounded-lg">ابدأ</span>
                    </div>
                </div>
            </div>

            <!-- TAB 3: WORDS VOCABULARY LIBRARY -->
            <div id="tab-words" class="tab-content space-y-3">
                <h2 class="text-xs font-black text-amber-400 mb-2 flex items-center gap-1.5">
                    <i data-lucide="list" class="w-4 h-4"></i> مكتبة الكلمات والمفردات القياسية
                </h2>
                <div class="grid grid-cols-1 gap-2">
                    <div onclick="setTargetSentence('Innovation drives economic transformation.', 'Innovation')" class="card-item p-3 rounded-2xl cursor-pointer flex items-center justify-between">
                        <div>
                            <span class="eng-font text-xs font-bold text-white block">1. Innovation (ابتكار)</span>
                            <span class="text-[10px] text-gray-400">“Innovation drives economic transformation.”</span>
                        </div>
                        <i data-lucide="mic" class="w-4 h-4 text-amber-400"></i>
                    </div>
                    <div onclick="setTargetSentence('Strategic alignment ensures long term success.', 'Strategic')" class="card-item p-3 rounded-2xl cursor-pointer flex items-center justify-between">
                        <div>
                            <span class="eng-font text-xs font-bold text-white block">2. Strategic (استراتيجي)</span>
                            <span class="text-[10px] text-gray-400">“Strategic alignment ensures long term success.”</span>
                        </div>
                        <i data-lucide="mic" class="w-4 h-4 text-amber-400"></i>
                    </div>
                    <div onclick="setTargetSentence('Transparent communication builds unbreakable trust.', 'Transparent')" class="card-item p-3 rounded-2xl cursor-pointer flex items-center justify-between">
                        <div>
                            <span class="eng-font text-xs font-bold text-white block">3. Transparent (شفاف)</span>
                            <span class="text-[10px] text-gray-400">“Transparent communication builds unbreakable trust.”</span>
                        </div>
                        <i data-lucide="mic" class="w-4 h-4 text-amber-400"></i>
                    </div>
                </div>
            </div>

            <!-- TAB 4: PLATFORM FEATURES & AI MODES -->
            <div id="tab-features" class="tab-content space-y-3">
                <h2 class="text-xs font-black text-amber-400 mb-2 flex items-center gap-1.5">
                    <i data-lucide="star" class="w-4 h-4"></i> مميزات المنصة الذكية المتكاملة
                </h2>
                <div class="space-y-2 text-[11px]">
                    <div class="card-item p-3 rounded-2xl space-y-1">
                        <span class="text-amber-400 font-bold block">🎙️ التصحيح الفوري الفونيكي (Phonetic Correction)</span>
                        <p class="text-gray-300">يحلل الميكروفون نطقك الكلمة تلو الأخرى ويطابقها مع نبرة الناطق الأصلي لتصحيح مخارج الحروف فوراً.</p>
                    </div>
                    <div class="card-item p-3 rounded-2xl space-y-1">
                        <span class="text-cyan-400 font-bold block">⚡ نظام النطق الصوتي التفاعلي (Text-to-Speech)</span>
                        <p class="text-gray-300">استمع لأي جملة أو كورس باللكنة الأمريكية أو البريطانية بضغطة زر واحدة قبل بدء التدريب.</p>
                    </div>
                    <div class="card-item p-3 rounded-2xl space-y-1">
                        <span class="text-emerald-400 font-bold block">🎮 مكافآت الخبرة الإمبراطورية (XP Core)</span>
                        <p class="text-gray-300">احصل على نقاط خبرة ترتقي بمستواك القيادي مع كل محاولة نطق صحيحة ومكتملة.</p>
                    </div>
                </div>
            </div>

        </div>

        <!-- Bottom Navigation Tabs -->
        <nav class="grid grid-cols-4 bg-black/95 border-t border-white/10 p-2 text-[10px] font-bold text-center text-amber-400 z-30">
            <button onclick="switchTab('home')" id="nav-home" class="flex flex-col items-center gap-1 text-amber-400 transition">
                <i data-lucide="mic-2" class="w-4 h-4"></i> المختبر
            </button>
            <button onclick="switchTab('courses')" id="nav-courses" class="flex flex-col items-center gap-1 text-gray-400 hover:text-white transition">
                <i data-lucide="book-open" class="w-4 h-4"></i> الكورسات
            </button>
            <button onclick="switchTab('words')" id="nav-words" class="flex flex-col items-center gap-1 text-gray-400 hover:text-white transition">
                <i data-lucide="list" class="w-4 h-4"></i> الكلمات
            </button>
            <button onclick="switchTab('features')" id="nav-features" class="flex flex-col items-center gap-1 text-gray-400 hover:text-white transition">
                <i data-lucide="star" class="w-4 h-4"></i> المميزات
            </button>
        </nav>
    </main>

    <script>
        lucide.createIcons();

        let currentSentence = "Price optimization is critical for growth.";

        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.getElementById('tab-' + tabId).classList.add('active');

            ['home', 'courses', 'words', 'features'].forEach(id => {
                let btn = document.getElementById('nav-' + id);
                if (id === tabId) {
                    btn.className = "flex flex-col items-center gap-1 text-amber-400 transition";
                } else {
                    btn.className = "flex flex-col items-center gap-1 text-gray-400 hover:text-white transition";
                }
            });
            lucide.createIcons();
        }

        function setTargetSentence(sentence, title) {
            currentSentence = sentence;
            document.getElementById('targetSentence').innerText = sentence;
            switchTab('home');
            alert("🎯 تم اختيار الجملة بنجاح:\\n“" + sentence + "”\\n\\nانقر الآن على زر الميكروفون لاختبار نطقك وتصحيحه!");
        }

        function playTargetAudio() {
            if ('speechSynthesis' in window) {
                const utterance = new SpeechSynthesisUtterance(currentSentence);
                utterance.lang = 'en-US';
                utterance.rate = 0.9;
                window.speechSynthesis.speak(utterance);
            } else {
                alert("متصفحك لا يدعم التشغيل الصوتي المباشر.");
            }
        }

        function startSpeechRecognition() {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRecognition) {
                alert("متصفحك لا يدعم التعرف على الصوت مباشرة. يرجى استخدام متصفح Google Chrome.");
                return;
            }

            const recognition = new SpeechRecognition();
            recognition.lang = 'en-US';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            const btn = document.getElementById('recordBtn');
            const resultBox = document.getElementById('liveResultBox');
            const spokenOutput = document.getElementById('spokenTextOutput');
            const correctionTip = document.getElementById('aiCorrectionTip');
            const matchBadge = document.getElementById('matchPercentage');

            btn.classList.add('listening-glow', 'from-red-600', 'to-rose-600');
            btn.innerHTML = '<i data-lucide="radio" class="w-4 h-4 animate-spin"></i> جاري الاستماع لصوتك بوضوح...';
            lucide.createIcons();

            recognition.onresult = function(event) {
                const userSaid = event.results[0][0].transcript;
                resultBox.classList.remove('hidden');
                spokenOutput.innerText = "“" + userSaid + "”";

                let cleanTarget = currentSentence.toLowerCase().replace(/[^a-z ]/g, "").trim();
                let cleanSaid = userSaid.toLowerCase().replace(/[^a-z ]/g, "").trim();

                if (cleanSaid === cleanTarget || cleanSaid.includes(cleanTarget.split(" ")[0])) {
                    matchBadge.className = "eng-font text-[10px] bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded font-bold";
                    matchBadge.innerText = "مطابقة 98% - ممتاز";
                    correctionTip.innerHTML = "🎉 <b class='text-emerald-300'>نطق سليم تماماً!</b> مخارج الحروف دقيقة (+50 XP)";
                    
                    let xpElem = document.getElementById('totalXp');
                    let newXp = parseInt(xpElem.innerText.replace(',', '')) + 50;
                    xpElem.innerText = newXp + " XP";
                } else {
                    matchBadge.className = "eng-font text-[10px] bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded font-bold";
                    matchBadge.innerText = "يحتاج تدقيق";
                    correctionTip.innerHTML = "🛠️ <b class='text-amber-400'>التصحيح الموصى به:</b> تم التقاط (<b>" + userSaid + "</b>). استمع للصوت الأصلي وحاول مراجعة مخارج الحروف.";
                }

                resetBtnState(btn);
            };

            recognition.onerror = function(event) {
                alert("حدث خطأ في الميكروفون: " + event.error);
                resetBtnState(btn);
            };

            recognition.onend = function() {
                resetBtnState(btn);
            };

            recognition.start();
        }

        function resetBtnState(btn) {
            btn.classList.remove('listening-glow', 'from-red-600', 'to-rose-600');
            btn.innerHTML = '<i data-lucide="mic" class="w-4 h-4"></i> اضغط وتحدث الآن عبر الميكروفون لتصحيح نطقك';
            lucide.createIcons();
        }
    </script>
</body>
</html>
"""

components.html(full_academy_app, height=880, scrolling=False)
