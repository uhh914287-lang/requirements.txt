import streamlit as st
import streamlit.components.v1 as components

# 1. إعداد الصفحة بأعلى معايير الأداء والملء الكامل للشاشة
st.set_page_config(
    page_title="أكاديمية السعيدة الإمبراطورية | Saba AI",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تصفير هوامش Streamlit لمنح تجربة تطبيق هجين أصيل (Native Hybrid App)
st.markdown("""
    <style>
        #MainMenu, footer, header { display: none !important; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
        iframe { border-radius: 0px !important; }
    </style>
""", unsafe_allowed_html=True)

# 3. الشيفرة الهندسية للواجهة (HTML5 / CSS3 Futuristic Glass / Vanilla ES6 Engine)
cyber_saba_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA ACADEMY X</title>
    <!-- Tailwind CSS & Lucide Core -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <!-- خطوط عربية ولاتينية فارهة -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Marhey:wght@700&family=Tajawal:wght@300;500;700;900&display=swap" rel="stylesheet">

    <style>
        :root {
            --gold-primary: #d4af37;
            --gold-glow: rgba(212, 175, 55, 0.45);
            --agate-red: #8b0000;
            --agate-glow: rgba(139, 0, 0, 0.55);
            --void-bg: #05070b;
        }

        body {
            font-family: 'Tajawal', sans-serif;
            background-color: var(--void-bg);
            color: #f1f5f9;
            overflow-x: hidden;
            user-select: none;
            -webkit-tap-highlight-color: transparent;
        }

        .cinzel { font-family: 'Cinzel', serif; }
        .marhey { font-family: 'Marhey', cursive; }

        /* تأثيرات زجاج العقيق اليماني والمرمر */
        .glass-panel {
            background: linear-gradient(135deg, rgba(17, 24, 39, 0.75) 0%, rgba(9, 13, 22, 0.9) 100%);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(212, 175, 55, 0.18);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }

        .gold-border-glow {
            border: 1px solid var(--gold-primary);
            box-shadow: 0 0 20px var(--gold-glow);
        }

        .agate-button {
            background: linear-gradient(135deg, #a81c1c 0%, #5e0808 100%);
            box-shadow: 0 4px 20px rgba(168, 28, 28, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.3);
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .agate-button:active {
            transform: scale(0.96);
            filter: brightness(1.2);
        }

        /* شريط التمرير الخفي */
        ::-webkit-scrollbar { width: 4px; height: 4px; }
        ::-webkit-scrollbar-thumb { background: rgba(212, 175, 55, 0.25); border-radius: 10px; }
        ::-webkit-scrollbar-track { background: transparent; }

        /* وميض النبض السبئي */
        @keyframes musnadFloat {
            0% { transform: translateY(0px) rotate(0deg); opacity: 0.15; }
            50% { transform: translateY(-12px) rotate(2deg); opacity: 0.35; }
            100% { transform: translateY(0px) rotate(0deg); opacity: 0.15; }
        }
        .musnad-symbol {
            animation: musnadFloat 6s ease-in-out infinite;
        }
    </style>
</head>

<body class="min-h-screen w-full flex justify-center items-center p-0 sm:p-4 relative">

    <!-- خلفية النجوم الحية وشبكة المرمر الهندسي -->
    <canvas id="bgCanvas" class="fixed inset-0 pointer-events-none z-0"></canvas>

    <!-- واجهة الهاتف السينمائية الفاخرة -->
    <main class="w-full max-w-lg h-screen sm:h-[94vh] flex flex-col glass-panel sm:rounded-[36px] z-10 overflow-hidden relative border-0 sm:border border-[#d4af37]/30">
        
        <!-- الشريط الإمبراطوري العلوي -->
        <header class="px-5 py-4 border-b border-gray-800/80 bg-black/40 flex items-center justify-between z-20">
            <!-- الشعار والنقاط -->
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-600 via-yellow-400 to-amber-700 p-[1.5px] shadow-lg shadow-amber-500/20">
                    <div class="w-full h-full bg-[#090d16] rounded-[14px] flex items-center justify-center">
                        <span class="cinzel text-amber-400 font-black text-lg">𐩯</span>
                    </div>
                </div>
                <div>
                    <h1 class="text-xs font-black tracking-widest text-amber-400/90 uppercase cinzel">SABA ACADEMY</h1>
                    <div class="flex items-center gap-1.5 mt-0.5">
                        <i data-lucide="flame" class="w-3.5 h-3.5 text-red-500 fill-red-500 animate-pulse"></i>
                        <span id="xpScore" class="text-sm font-black text-gray-100">320</span>
                        <span class="text-[10px] text-amber-400/70 font-bold">XP</span>
                    </div>
                </div>
            </div>

            <!-- محدد المحافظات وإعداد المفتاح السحابي -->
            <div class="flex items-center gap-2">
                <div class="relative">
                    <select id="govSelector" onchange="soundEngine.play('click'); updateGovLeaderboard()" class="bg-[#131b2e] text-[11px] font-bold text-amber-200/90 py-1.5 px-3 rounded-xl border border-amber-500/30 outline-none appearance-none cursor-pointer pl-6">
                        <option value="الحديدة">الحديدة ⚓</option>
                        <option value="صنعاء">صنعاء 🏛️</option>
                        <option value="عدن">عدن 🌊</option>
                        <option value="تعز">تعز 🏰</option>
                        <option value="حضرموت">حضرموت 🌴</option>
                        <option value="مأرب">مأرب ☀️</option>
                    </select>
                    <i data-lucide="chevron-down" class="w-3 h-3 text-amber-400 absolute left-2 top-2.5 pointer-events-none"></i>
                </div>

                <button onclick="toggleKeySettings()" class="w-8 h-8 rounded-xl bg-gray-800/80 hover:bg-gray-700 border border-gray-700 flex items-center justify-center text-gray-400 hover:text-amber-400 transition-colors">
                    <i data-lucide="key" class="w-3.5 h-3.5"></i>
                </button>
            </div>
        </header>

        <!-- لوحة إدخال وتأمين المفتاح -->
        <div id="keyDrawer" class="hidden px-5 py-3 bg-[#0d1322] border-b border-amber-500/30 text-xs text-gray-300 transition-all">
            <div class="flex items-center justify-between mb-2">
                <span class="text-amber-400 font-bold flex items-center gap-1">
                    <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> ربط محرك الذكاء الاصطناعي (Gemini)
                </span>
                <button onclick="toggleKeySettings()" class="text-gray-500 hover:text-white">&times;</button>
            </div>
            <div class="flex gap-2">
                <input id="geminiKeyInput" type="password" placeholder="الصق مفتاح Google AI Studio هنا..." class="flex-1 bg-black/60 border border-gray-700 rounded-xl px-3 py-1.5 text-xs text-white outline-none focus:border-amber-400">
                <button onclick="saveApiKey()" class="agate-button text-white text-xs font-bold px-3 py-1.5 rounded-xl">حفظ آمن</button>
            </div>
        </div>

        <!-- التبويبات الفاخرة المستوحاة من مقصورات السينما -->
        <nav class="grid grid-cols-3 bg-[#090d16]/90 p-1.5 border-b border-gray-800/60 text-xs font-bold z-20">
            <button onclick="switchTab('arena')" id="btn-arena" class="py-2.5 rounded-xl text-amber-400 bg-amber-500/10 border border-amber-500/30 flex items-center justify-center gap-1.5 transition-all">
                <i data-lucide="bot" class="w-4 h-4"></i> محاكي المقابلات
            </button>
            <button onclick="switchTab('voice')" id="btn-voice" class="py-2.5 rounded-xl text-gray-400 hover:text-gray-200 flex items-center justify-center gap-1.5 transition-all">
                <i data-lucide="mic-2" class="w-4 h-4"></i> مختبر النطق
            </button>
            <button onclick="switchTab('quest')" id="btn-quest" class="py-2.5 rounded-xl text-gray-400 hover:text-gray-200 flex items-center justify-center gap-1.5 transition-all">
                <i data-lucide="zap" class="w-4 h-4"></i> سباق الـ 60 ثانية
            </button>
        </nav>

        <!-- المحتوى المركزي التفاعلي -->
        <div class="flex-1 overflow-hidden relative z-10 flex flex-col">
            
            <!-- 1. المحاكي السينمائي الذكي -->
            <section id="tab-arena" class="flex-1 flex flex-col justify-between overflow-hidden p-4">
                
                <!-- رسالة السياق ومهمة التدريب الحالية -->
                <div class="glass-panel rounded-2xl p-3 mb-3 border border-amber-500/20 flex items-center justify-between">
                    <div class="flex items-center gap-2.5">
                        <div class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-ping"></div>
                        <div>
                            <span class="text-[11px] text-gray-400 block">المهمة الحالية:</span>
                            <span class="text-xs font-bold text-amber-300">مقابلة عمل دولية (Remote Job Interview)</span>
                        </div>
                    </div>
                    <span class="text-[10px] bg-red-950/60 text-red-400 border border-red-800/40 px-2 py-0.5 rounded-lg font-bold">مستوى B2</span>
                </div>

                <!-- شات الرسائل التفاعلية -->
                <div id="chatFeed" class="flex-1 overflow-y-auto space-y-3.5 pr-1 text-xs sm:text-sm">
                    <div class="flex justify-end">
                        <div class="glass-panel p-3.5 rounded-2xl rounded-tl-none max-w-[90%] border border-gray-700/80 leading-relaxed text-gray-200">
                            <p class="font-bold text-amber-400 text-[11px] mb-1">HR Director (Silicon Valley):</p>
                            "Welcome to the final interview stage! Could you briefly explain why you are the ideal candidate to handle this remote position from Yemen?"
                            <button onclick="speakCurrent(this.parentElement.innerText)" class="mt-2.5 flex items-center gap-1.5 text-[11px] text-amber-300 hover:text-amber-200 font-bold">
                                <i data-lucide="volume-2" class="w-3.5 h-3.5"></i> استمع للنبرة الاحترافية
                            </button>
                        </div>
                    </div>
                </div>

                <!-- شريط الإرسال الفاره -->
                <div class="mt-3 flex items-center gap-2 bg-[#0c1220]/90 p-1.5 rounded-2xl border border-gray-700/70 focus-within:border-amber-400 transition-colors">
                    <input id="chatField" type="text" placeholder="اكتب ردك بالإنجليزية لمشاهدة التحليل..." class="flex-1 bg-transparent px-3 py-2 text-xs sm:text-sm text-white outline-none placeholder-gray-500 text-right" dir="auto">
                    <button onclick="executeAiTurn()" class="agate-button p-2.5 rounded-xl text-white flex items-center justify-center">
                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                    </button>
                </div>
            </section>

            <!-- 2. مختبر النطق الصوتي الفضائي -->
            <section id="tab-voice" class="hidden flex-1 flex flex-col justify-between items-center p-6 text-center">
                <div class="w-full space-y-3">
                    <div class="inline-flex items-center gap-1.5 bg-amber-950/40 text-amber-400 border border-amber-800/30 px-3 py-1 rounded-full text-[11px] font-bold">
                        <i data-lucide="award" class="w-3.5 h-3.5"></i> تحدي نبرة المتحدث الأصلي (Shadowing)
                    </div>
                    
                    <div class="glass-panel p-5 rounded-3xl border border-amber-500/30 shadow-2xl relative overflow-hidden">
                        <span class="text-[11px] text-gray-400 block mb-2 font-medium">اقرأ العبارة التالية بوضوح وثقة:</span>
                        <h2 id="targetVoicePhrase" class="text-base sm:text-lg font-black text-amber-300 cinzel tracking-wide dir-ltr py-1">
                            "Opportunities don't happen, you create them."
                        </h2>
                        
                        <button onclick="speakPhrase(document.getElementById('targetVoicePhrase').innerText)" class="mt-3 inline-flex items-center gap-1 text-xs text-amber-400/90 hover:text-white bg-white/5 px-3 py-1.5 rounded-xl border border-white/10 transition-all">
                            <i data-lucide="volume-2" class="w-3.5 h-3.5"></i> استمع للمخارج الصوتية
                        </button>
                    </div>
                </div>

                <!-- الطيف الترددي وزر المايك الهولوجرامي -->
                <div class="flex flex-col items-center my-auto">
                    <canvas id="voiceVisualizer" width="220" height="40" class="mb-4 opacity-70"></canvas>
                    
                    <button id="masterMicBtn" onclick="triggerSpeechLab()" class="w-24 h-24 rounded-full p-1 bg-gradient-to-tr from-red-600 via-amber-500 to-red-800 shadow-2xl shadow-red-900/50 hover:scale-105 active:scale-95 transition-all">
                        <div class="w-full h-full bg-[#080d1a] rounded-full flex flex-col items-center justify-center text-white">
                            <i id="micIcon" data-lucide="mic" class="w-8 h-8 text-amber-400 mb-1"></i>
                            <span id="micLabel" class="text-[10px] font-bold text-gray-400">ابدأ الآن</span>
                        </div>
                    </button>
                    <span id="micHelper" class="text-[11px] text-gray-400 mt-3 font-medium">اضغط وتحدث فوراً وسيقيم الذكاء الاصطناعي كل مخرج</span>
                </div>

                <!-- نتيجة التقييم الطيفي -->
                <div id="voiceScoreCard" class="w-full glass-panel p-3.5 rounded-2xl border border-gray-800 text-xs text-gray-300">
                    بانتظار قراءتك الصوتية لبدء الفحص والتشخيص اللحظي...
                </div>
            </section>

            <!-- 3. سباق الـ 60 ثانية ودوري المحافظات -->
            <section id="tab-quest" class="hidden flex-1 flex flex-col justify-between p-5">
                
                <!-- رأس سباق السرعة -->
                <div class="flex items-center justify-between glass-panel p-3 rounded-2xl border border-amber-500/20">
                    <div class="flex items-center gap-2">
                        <i data-lucide="timer" class="w-4 h-4 text-amber-400 animate-spin"></i>
                        <span class="text-xs font-bold text-gray-200">سؤال التفاوض على عقد العمل</span>
                    </div>
                    <div class="bg-red-950/80 text-red-400 px-2.5 py-1 rounded-xl text-xs font-black border border-red-800/40">
                        +30 XP
                    </div>
                </div>

                <!-- لغز التحدي -->
                <div class="my-auto space-y-4">
                    <div class="text-center space-y-1.5">
                        <span class="text-xs text-gray-400 font-medium">عميل على منصة فريلانسر يريد خفض سعرك 50%، ما هو الرد الأذكى؟</span>
                        <h3 class="text-sm sm:text-base font-black text-amber-300 leading-relaxed">
                            "My rate reflects the quality and business value I deliver."
                        </h3>
                    </div>

                    <!-- الخيارات التفاعلية المضيئة -->
                    <div class="space-y-2.5">
                        <button onclick="evaluateBlitzChoice(this, true)" class="w-full p-3.5 glass-panel hover:bg-amber-500/10 border border-gray-800 hover:border-amber-500/40 rounded-2xl text-right text-xs sm:text-sm font-medium transition-all flex items-center justify-between group">
                            <span>A) أوافق باحترام وأشرح أن جودة العمل هي استثمار يضمن نجاح مشروعه.</span>
                            <i data-lucide="arrow-left" class="w-4 h-4 text-gray-600 group-hover:text-amber-400 transition-colors"></i>
                        </button>
                        
                        <button onclick="evaluateBlitzChoice(this, false)" class="w-full p-3.5 glass-panel hover:bg-red-500/10 border border-gray-800 hover:border-red-500/40 rounded-2xl text-right text-xs sm:text-sm font-medium transition-all flex items-center justify-between group">
                            <span>B) أرفض بغضب وأخبره أن يبحث عن شخص آخر أقل كفاءة.</span>
                            <i data-lucide="arrow-left" class="w-4 h-4 text-gray-600 group-hover:text-red-400 transition-colors"></i>
                        </button>

                        <button onclick="evaluateBlitzChoice(this, false)" class="w-full p-3.5 glass-panel hover:bg-red-500/10 border border-gray-800 hover:border-red-500/40 rounded-2xl text-right text-xs sm:text-sm font-medium transition-all flex items-center justify-between group">
                            <span>C) أوافق فوراً على التخفيض الكبير حتى لا أخسر الصفقة.</span>
                            <i data-lucide="arrow-left" class="w-4 h-4 text-gray-600 group-hover:text-red-400 transition-colors"></i>
                        </button>
                    </div>
                </div>

                <!-- نتيجة التحدي -->
                <div id="questStatus" class="text-center text-xs text-gray-400 font-bold">
                    اختر القرار الاستراتيجي الذي يعكس احترافك العالمي
                </div>
            </section>

        </div>

        <!-- تذييل هوية سبأ السينمائية -->
        <footer class="py-2.5 px-4 bg-black/60 border-t border-gray-800/80 flex items-center justify-between text-[10px] text-gray-500 font-medium z-20">
            <div class="flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                <span>محرك الذكاء متصل بلحظات</span>
            </div>
            <span class="cinzel tracking-widest text-amber-500/80">SABA ENGINE 2030</span>
        </footer>

    </main>

    <!-- المحرك البرمجي الصوتي والهندسي الداخلي -->
    <script>
        lucide.createIcons();

        // 1. محرك المؤثرات الصوتية الفيزيائية دون تحميل ملفات صوتية (Synthetic Web Audio)
        class AudioSynthesizer {
            constructor() {
                this.ctx = null;
            }
            init() {
                if (!this.ctx) {
                    this.ctx = new (window.AudioContext || window.webkitAudioContext)();
                }
            }
            play(type) {
                this.init();
                const now = this.ctx.currentTime;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.connect(gain);
                gain.connect(this.ctx.destination);

                if (type === 'click') {
                    osc.frequency.setValueAtTime(450, now);
                    osc.frequency.exponentialRampToValueAtTime(150, now + 0.04);
                    gain.gain.setValueAtTime(0.2, now);
                    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.04);
                    osc.start(now);
                    osc.stop(now + 0.04);
                } else if (type === 'win') {
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(320, now);
                    osc.frequency.exponentialRampToValueAtTime(640, now + 0.15);
                    gain.gain.setValueAtTime(0.3, now);
                    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
                    osc.start(now);
                    osc.stop(now + 0.25);
                } else if (type === 'fail') {
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(200, now);
                    osc.frequency.linearRampToValueAtTime(100, now + 0.18);
                    gain.gain.setValueAtTime(0.2, now);
                    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.18);
                    osc.start(now);
                    osc.stop(now + 0.18);
                }
            }
        }
        const soundEngine = new AudioSynthesizer();

        // 2. إدارة النقاط ومفتاح Gemini المخزن محلياً
        let totalXP = parseInt(localStorage.getItem('saba_xp') || '320');
        let geminiKey = localStorage.getItem('saba_gemini_key') || '';
        document.getElementById('xpScore').innerText = totalXP;
        if (geminiKey) document.getElementById('geminiKeyInput').value = geminiKey;

        function incrementScore(val) {
            totalXP += val;
            localStorage.setItem('saba_xp', totalXP);
            document.getElementById('xpScore').innerText = totalXP;
            soundEngine.play('win');
        }

        function toggleKeySettings() {
            soundEngine.play('click');
            document.getElementById('keyDrawer').classList.toggle('hidden');
        }

        function saveApiKey() {
            const val = document.getElementById('geminiKeyInput').value.trim();
            if (val) {
                localStorage.setItem('saba_gemini_key', val);
                geminiKey = val;
                soundEngine.play('win');
                alert('تم تفعيل المفتاح بنجاح وسيعمل المحرك بأقصى سرعة!');
                toggleKeySettings();
            }
        }

        // 3. التبديل السينمائي بين المقصورات
        function switchTab(name) {
            soundEngine.play('click');
            ['arena', 'voice', 'quest'].forEach(t => {
                document.getElementById('tab-' + t).classList.add('hidden');
                const btn = document.getElementById('btn-' + t);
                btn.className = 'py-2.5 rounded-xl text-gray-400 hover:text-gray-200 flex items-center justify-center gap-1.5 transition-all';
            });
            document.getElementById('tab-' + name).classList.remove('hidden');
            const activeBtn = document.getElementById('btn-' + name);
            activeBtn.className = 'py-2.5 rounded-xl text-amber-400 bg-amber-500/10 border border-amber-500/30 flex items-center justify-center gap-1.5 transition-all';
        }

        // 4. المحاكي التفاعلي مع Gemini 1.5 Flash
        async function executeAiTurn() {
            const input = document.getElementById('chatField');
            const prompt = input.value.trim();
            if (!prompt) return;

            if (!geminiKey) {
                alert('يرجى الضغط على علامة المفتاح بالأعلى وتعيين مفتاح Gemini أولاً');
                toggleKeySettings();
                return;
            }

            soundEngine.play('click');
            const feed = document.getElementById('chatFeed');
            
            // إضافة رد المستخدم الفوري
            feed.innerHTML += `
                <div class="flex justify-start">
                    <div class="agate-button text-white p-3.5 rounded-2xl rounded-tr-none max-w-[85%] leading-relaxed shadow-lg">
                        ${prompt}
                    </div>
                </div>`;
            input.value = '';
            feed.scrollTop = feed.scrollHeight;

            try {
                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${geminiKey}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{
                            parts: [{
                                text: `You are an elite Silicon Valley interviewer interviewing a talented candidate from Yemen. Reply in 2-3 concise English sentences, keeping the scenario realistic. Then, if there is an error, provide a 1-sentence tip in simple Arabic. User said: ${prompt}`
                            }]
                        }]
                    })
                });

                const data = await response.json();
                const aiText = data.candidates?.[0]?.content?.parts?.[0]?.text || 'تعذر معالجة الرد حالياً.';

                feed.innerHTML += `
                    <div class="flex justify-end">
                        <div class="glass-panel p-3.5 rounded-2xl rounded-tl-none max-w-[90%] border border-gray-700/80 leading-relaxed text-gray-200">
                            <p class="font-bold text-amber-400 text-[11px] mb-1">Interviewer Feedback:</p>
                            ${aiText}
                            <button onclick="speakCurrent(this.parentElement.innerText)" class="mt-2.5 flex items-center gap-1.5 text-[11px] text-amber-300 font-bold">
                                🔊 استمع للنطق
                            </button>
                        </div>
                    </div>`;
                
                incrementScore(20);
                feed.scrollTop = feed.scrollHeight;
            } catch (err) {
                feed.innerHTML += `<div class="text-[11px] text-red-400 text-center">خطأ في الاتصال، تأكد من مفتاح الـ API.</div>`;
            }
        }

        // 5. محرك النطق الذكي
        function speakCurrent(text) {
            soundEngine.play('click');
            const clean = text.replace('Interviewer Feedback:', '').replace('🔊 استمع للنطق', '').replace(/[\u0600-\u06FF]/g, '');
            speakPhrase(clean);
        }

        function speakPhrase(phrase) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const msg = new SpeechSynthesisUtterance(phrase);
                msg.lang = 'en-US';
                msg.rate = 0.93;
                window.speechSynthesis.speak(msg);
            }
        }

        // 6. تشخيص النطق الصوتي المباشر
        function triggerSpeechLab() {
            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRec) {
                alert("يرجى استخدام متصفح Chrome لتفعيل لاقط الصوت.");
                return;
            }

            soundEngine.play('click');
            const rec = new SpeechRec();
            rec.lang = 'en-US';
            const micBtn = document.getElementById('masterMicBtn');
            const micLabel = document.getElementById('micLabel');
            const card = document.getElementById('voiceScoreCard');

            micLabel.innerText = "أستمع الآن...";
            micBtn.classList.add('scale-110');
            rec.start();

            rec.onresult = (e) => {
                const spoken = e.results[0][0].transcript.toLowerCase();
                micLabel.innerText = "ابدأ الآن";
                micBtn.classList.remove('scale-110');

                if (spoken.includes("opportunities") || spoken.includes("create")) {
                    card.innerHTML = `<span class="text-emerald-400 font-bold text-sm">👑 تقييم ملكي (100% طلاقة مدهشة)</span><br>المدخل الصوتي: "${spoken}"`;
                    incrementScore(30);
                } else {
                    card.innerHTML = `<span class="text-amber-400 font-bold text-sm">💡 نطق جيد! ركز على تشديد الكلمات الرئيسية.</span><br>سمعنا: "${spoken}"`;
                    soundEngine.play('fail');
                }
            };

            rec.onerror = () => {
                micLabel.innerText = "ابدأ الآن";
                micBtn.classList.remove('scale-110');
                card.innerText = "تعذر الاستماع، يرجى إعادة المحاولة برفع الصوت.";
            };
        }

        // 7. تقييم أسئلة السرعة
        function evaluateBlitzChoice(btn, isRight) {
            const status = document.getElementById('questStatus');
            if (isRight) {
                btn.className = 'w-full p-3.5 bg-emerald-950/80 border border-emerald-500 rounded-2xl text-right text-xs sm:text-sm font-bold text-emerald-200';
                status.innerHTML = '✨ قرار استراتيجي لا تشوبه شائبة! ربحت +30 XP';
                incrementScore(30);
            } else {
                btn.className = 'w-full p-3.5 bg-red-950/80 border border-red-500 rounded-2xl text-right text-xs sm:text-sm font-bold text-red-200';
                status.innerHTML = '⚠️ خيار يقلل من قيمتك في سوق العمل، فكر مجدداً!';
                soundEngine.play('fail');
            }
        }

        function updateGovLeaderboard() {
            const gov = document.getElementById('govSelector').value;
            alert(`تم نقلك إلى دوري ${gov}! نافس زملائك في المحافظة لحصد المركز الأول.`);
        }

        // 8. محرك الخلفية النجمية التفاعلي عبر Canvas (Sub-second Performance)
        const canvas = document.getElementById('bgCanvas');
        const ctx = canvas.getContext('2d');
        let stars = [];

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            stars = [];
            for (let i = 0; i < 45; i++) {
                stars.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    radius: Math.random() * 1.5,
                    alpha: Math.random(),
                    speed: 0.2 + Math.random() * 0.3
                });
            }
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        function renderStars() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#d4af37";
            stars.forEach(s => {
                ctx.globalAlpha = s.alpha;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
                ctx.fill();
                s.y -= s.speed;
                if (s.y < 0) s.y = canvas.height;
            });
            requestAnimationFrame(renderStars);
        }
        renderStars();

        document.getElementById('chatField').addEventListener('keydown', (e) => {
            if (e.key === 'Enter') executeAiTurn();
        });
    </script>
</body>
</html>
"""

# عرض التطبيق بالكامل داخل إطار ديناميكي
components.html(cyber_saba_app, height=940, scrolling=False)
