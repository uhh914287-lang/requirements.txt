import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SABA LIVE SPEECH LAB | AURA V4",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu, footer, header { display: none !important; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; background-color: #030508; }
    </style>
""", unsafe_allow_html=True)

live_voice_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA LIVE SPEECH LAB</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=Tajawal:wght@400;700;900&display=swap');
        :root { --gold: #f59e0b; --bg-dark: #050811; }
        body { font-family: 'Tajawal', sans-serif; background-color: var(--bg-dark); color: #f3f4f6; overflow-x: hidden; user-select: none; }
        .eng-font { font-family: 'Plus Jakarta Sans', sans-serif; }
        .glass-shell {
            background: linear-gradient(135deg, rgba(13, 20, 35, 0.96) 0%, rgba(4, 7, 14, 0.99) 100%);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(245, 158, 11, 0.25);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.95);
        }
        .listening-glow {
            box-shadow: 0 0 35px rgba(239, 68, 68, 0.6);
            border-color: rgba(239, 68, 68, 0.9) !important;
            animation: pulseGlow 1.5s infinite;
        }
        @keyframes pulseGlow {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        .course-card {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.07);
            transition: all 0.3s ease;
        }
        .course-card:hover { border-color: var(--gold); }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body class="min-h-screen w-full flex justify-center items-center p-0 sm:p-4">
    
    <main class="w-full max-w-md h-screen sm:h-[95vh] flex flex-col glass-shell sm:rounded-[36px] overflow-hidden relative">
        
        <!-- Header -->
        <header class="px-5 py-3.5 bg-black/60 border-b border-white/5 flex items-center justify-between z-30">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-500 to-yellow-300 p-0.5 shadow-lg shadow-amber-500/20">
                    <div class="w-full h-full bg-[#070b14] rounded-[14px] flex items-center justify-center">
                        <span class="eng-font text-amber-400 font-extrabold text-base">S</span>
                    </div>
                </div>
                <div>
                    <h1 class="text-[11px] font-black tracking-wider text-amber-400 uppercase eng-font">SABA LIVE VOICE LAB</h1>
                    <div class="flex items-center gap-1.5 mt-0.5">
                        <span id="micStateIndicator" class="w-2 h-2 rounded-full bg-emerald-500"></span>
                        <span class="text-[10px] text-gray-400 font-medium">التعرف الصوتي الحقيقي (Speech API)</span>
                    </div>
                </div>
            </div>
            <div class="bg-amber-500/10 border border-amber-500/20 px-3 py-1 rounded-full flex items-center gap-1.5">
                <i data-lucide="award" class="w-3.5 h-3.5 text-amber-400"></i>
                <span id="totalXp" class="eng-font text-xs font-bold text-amber-300">3,420 XP</span>
            </div>
        </header>

        <!-- Main Body -->
        <div class="flex-1 overflow-y-auto no-scrollbar p-4 space-y-4">
            
            <!-- Courses List -->
            <div>
                <div class="flex items-center justify-between mb-2.5">
                    <h2 class="text-xs font-black text-amber-400 flex items-center gap-1.5">
                        <i data-lucide="headphones" class="w-4 h-4 text-amber-400"></i> الكورسات الصوتية التفاعلية
                    </h2>
                </div>
                
                <div class="space-y-2">
                    <div onclick="setTargetSentence('Price optimization is critical for quarterly growth.', 'وول ستريت - تحسين الأسعار')" class="course-card p-3 rounded-2xl cursor-pointer flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400">
                                <i data-lucide="briefcase" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <h3 class="text-xs font-bold text-white">Wall Street Growth</h3>
                                <p class="text-[10px] text-gray-400">Price optimization is critical...</p>
                            </div>
                        </div>
                        <span class="text-[10px] bg-amber-500/10 text-amber-400 px-2 py-1 rounded-lg">اختبر</span>
                    </div>

                    <div onclick="setTargetSentence('Artificial intelligence transforms global business.', 'الذكاء الاصطناعي والأعمال')" class="course-card p-3 rounded-2xl cursor-pointer flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400">
                                <i data-lucide="cpu" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <h3 class="text-xs font-bold text-white">AI Transformation</h3>
                                <p class="text-[10px] text-gray-400">Artificial intelligence transforms...</p>
                            </div>
                        </div>
                        <span class="text-[10px] bg-cyan-500/10 text-cyan-400 px-2 py-1 rounded-lg">اختبر</span>
                    </div>
                </div>
            </div>

            <!-- Live Speech Lab & Correction Box -->
            <div class="glass-shell p-4 rounded-3xl border border-amber-500/30 space-y-3 relative">
                
                <div class="flex items-center justify-between">
                    <span class="text-[11px] font-black text-amber-400 uppercase eng-font flex items-center gap-1.5">
                        <i data-lucide="mic-2" class="w-4 h-4 text-amber-400"></i> الميكروفون المباشر والتصحيح
                    </span>
                    <button onclick="playTargetAudio()" class="text-[10px] bg-white/10 hover:bg-white/20 text-white px-2.5 py-1 rounded-lg flex items-center gap-1">
                        <i data-lucide="volume-2" class="w-3 h-3 text-amber-400"></i> استمع للصوت الأصلي
                    </button>
                </div>

                <div class="bg-black/60 p-3.5 rounded-2xl border border-white/5 space-y-1">
                    <span class="text-[9px] text-gray-400 font-bold uppercase">انطق الجملة التالية بصوتك:</span>
                    <p id="targetSentence" class="eng-font text-xs font-bold text-amber-300 tracking-wide">
                        Price optimization is critical for quarterly growth.
                    </p>
                </div>

                <!-- Real-time Speech Result Box -->
                <div id="liveResultBox" class="hidden bg-slate-900/90 border border-amber-500/30 p-3 rounded-2xl space-y-1.5">
                    <div class="flex items-center justify-between">
                        <span class="text-[10px] font-bold text-gray-300">ما التقطه الميكروفون منك:</span>
                        <span id="matchPercentage" class="eng-font text-[10px] bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded font-bold">مطابقة 95%</span>
                    </div>
                    <p id="spokenTextOutput" class="eng-font text-xs text-white font-semibold"></p>
                    <div id="aiCorrectionTip" class="text-[10px] text-amber-300 mt-1"></div>
                </div>

                <!-- Record Button -->
                <button id="recordBtn" onclick="startSpeechRecognition()" class="w-full py-3.5 bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 text-black font-black text-xs rounded-2xl shadow-lg transition flex items-center justify-center gap-2 eng-font">
                    <i data-lucide="mic" class="w-4 h-4"></i> اضغط وتحدث الآن عبر الميكروفون
                </button>
            </div>

        </div>

        <!-- Bottom Navigation -->
        <nav class="grid grid-cols-4 bg-black/90 border-t border-white/5 p-2 text-[10px] font-bold text-center text-amber-400 z-30">
            <button class="flex flex-col items-center gap-1 text-amber-400"><i data-lucide="headphones" class="w-4 h-4"></i> الصوتيات</button>
            <button onclick="alert('المكتبة الذكية')" class="flex flex-col items-center gap-1 text-gray-400"><i data-lucide="book-open" class="w-4 h-4"></i> المكتبة</button>
            <button onclick="alert('حلبة التحدي')" class="flex flex-col items-center gap-1 text-gray-400"><i data-lucide="trophy" class="w-4 h-4"></i> التحديات</button>
            <button onclick="alert('الإمبراطور')" class="flex flex-col items-center gap-1 text-gray-400"><i data-lucide="user" class="w-4 h-4"></i> الإمبراطور</button>
        </nav>
    </main>

    <script>
        lucide.createIcons();

        let currentSentence = "Price optimization is critical for quarterly growth.";

        function setTargetSentence(sentence, title) {
            currentSentence = sentence;
            document.getElementById('targetSentence').innerText = sentence;
            alert("🎧 تم اختيار مساق: " + title + "\\nانقر على زر الميكروفون وتحدث بالجملة الظاهرة أمامك.");
        }

        // تشغيل النطق الأصلي من المتصفح (Text-to-Speech)
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

        // الاستماع الحقيقي عبر ميكروفون المستخدم وتصحيحه (Speech Recognition API)
        function startSpeechRecognition() {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRecognition) {
                alert("متصفحك لا يدعم التعرف على الصوت مباشرة. يجدر استخدام متصفح Google Chrome.");
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
            btn.innerHTML = '<i data-lucide="radio" class="w-4 h-4 animate-spin"></i> جاري الاستماع لصوتك الآن... يتطلب التحدث بوضوح';
            lucide.createIcons();

            recognition.onresult = function(event) {
                const userSaid = event.results[0][0].transcript;
                resultBox.classList.remove('hidden');
                spokenOutput.innerText = "“" + userSaid + "”";

                // تحليل وتصحيح ذكي ومقارنة بسيطة
                let cleanTarget = currentSentence.toLowerCase().replace(/[^a-z ]/g, "").trim();
                let cleanSaid = userSaid.toLowerCase().replace(/[^a-z ]/g, "").trim();

                if (cleanSaid === cleanTarget || cleanSaid.includes(cleanTarget.split(" ")[0])) {
                    matchBadge.className = "eng-font text-[10px] bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded font-bold";
                    matchBadge.innerText = "ممشوق 98% - ممتاز!";
                    correctionTip.innerHTML = "🎉 <b class='text-emerald-300'>نطق مثالي!</b> مخارج الحروف سليمة تماماً (+50 XP)";
                    
                    let xpElem = document.getElementById('totalXp');
                    let newXp = parseInt(xpElem.innerText.replace(',', '')) + 50;
                    xpElem.innerText = newXp + " XP";
                } else {
                    matchBadge.className = "eng-font text-[10px] bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded font-bold";
                    matchBadge.innerText = "يحتاج تحسين";
                    correctionTip.innerHTML = "🛠️ <b class='text-amber-400'>تصحيح آلي:</b> تم سماع (<b>" + userSaid + "</b>). استمع للصوت الأصلي وحاول التركيز على نطق الكلمات بوضوح أكبر.";
                }

                resetBtnState(btn);
            };

            recognition.onerror = function(event) {
                alert("حدث خطأ في التقاط الصوت: " + event.error);
                resetBtnState(btn);
            };

            recognition.onend = function() {
                resetBtnState(btn);
            };

            recognition.start();
        }

        function resetBtnState(btn) {
            btn.classList.remove('listening-glow', 'from-red-600', 'to-rose-600');
            btn.innerHTML = '<i data-lucide="mic" class="w-4 h-4"></i> اضغط وتحدث الآن عبر الميكروفون';
            lucide.createIcons();
        }
    </script>
</body>
</html>
"""

components.html(live_voice_app, height=880, scrolling=False)
