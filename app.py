import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SABA AUDIO EMPIRE | AURA V3.0",
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

audio_masterpiece_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA AUDIO EMPIRE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=Tajawal:wght@400;700;900&display=swap');
        :root { --gold: #f59e0b; --bg-dark: #050811; --accent-glow: rgba(245, 158, 11, 0.25); }
        body { font-family: 'Tajawal', sans-serif; background-color: var(--bg-dark); color: #f3f4f6; overflow-x: hidden; user-select: none; }
        .eng-font { font-family: 'Plus Jakarta Sans', sans-serif; }
        
        .glass-shell {
            background: linear-gradient(135deg, rgba(13, 20, 35, 0.96) 0%, rgba(4, 7, 14, 0.99) 100%);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(245, 158, 11, 0.25);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.95);
        }
        
        .sound-wave {
            display: flex;
            align-items: center;
            gap: 3px;
            height: 24px;
        }
        .sound-wave span {
            width: 3px;
            background: #f59e0b;
            border-radius: 99px;
            animation: pulseWave 1.2s infinite ease-in-out;
        }
        .sound-wave span:nth-child(2) { animation-delay: 0.2s; }
        .sound-wave span:nth-child(3) { animation-delay: 0.4s; }
        .sound-wave span:nth-child(4) { animation-delay: 0.6s; }

        @keyframes pulseWave {
            0%, 100% { height: 6px; opacity: 0.3; }
            50% { height: 22px; opacity: 1; }
        }

        .listening-glow {
            box-shadow: 0 0 35px rgba(239, 68, 68, 0.5);
            border-color: rgba(239, 68, 68, 0.8) !important;
        }

        .course-card {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.07);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .course-card:hover {
            border-color: var(--gold);
            transform: translateY(-2px);
        }
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
                    <h1 class="text-[11px] font-black tracking-wider text-amber-400 uppercase eng-font">SABA AUDIO EMPIRE</h1>
                    <div class="flex items-center gap-1.5 mt-0.5">
                        <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                        <span class="text-[10px] text-gray-400 font-medium">مختبر النطق العصبي (AURA)</span>
                    </div>
                </div>
            </div>
            <div class="bg-amber-500/10 border border-amber-500/20 px-3 py-1 rounded-full flex items-center gap-1.5">
                <i data-lucide="award" class="w-3.5 h-3.5 text-amber-400"></i>
                <span id="totalXp" class="eng-font text-xs font-bold text-amber-300">3,120 XP</span>
            </div>
        </header>

        <!-- Main Body -->
        <div class="flex-1 overflow-y-auto no-scrollbar p-4 space-y-4">
            
            <!-- SECTION 1: AUDIO COURSES LIST -->
            <div>
                <div class="flex items-center justify-between mb-2.5">
                    <h2 class="text-xs font-black text-amber-400 flex items-center gap-1.5">
                        <i data-lucide="headphones" class="w-4 h-4 text-amber-400"></i> الكورسات الصوتية النشطة
                    </h2>
                    <span class="text-[10px] text-gray-400">اختر مساقاً للاستماع</span>
                </div>
                
                <div class="space-y-2.5">
                    <!-- Course Item 1 -->
                    <div onclick="selectCourse('مفاوضات وول ستريت التنفيذية', '“Price optimization is critical for quarterly growth.”')" class="course-card p-3 rounded-2xl cursor-pointer flex items-center justify-between group">
                        <div class="flex items-center gap-3">
                            <div class="w-11 h-11 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400 group-hover:bg-amber-500 group-hover:text-black transition">
                                <i data-lucide="briefcase" class="w-5 h-5"></i>
                            </div>
                            <div>
                                <h3 class="text-xs font-bold text-white group-hover:text-amber-300 transition">Wall Street Executive English</h3>
                                <p class="text-[10px] text-gray-400 mt-0.5">مفاوضات الأعمال وإدارة الصفقات الكبرى</p>
                            </div>
                        </div>
                        <div class="sound-wave">
                            <span></span><span></span><span></span><span></span>
                        </div>
                    </div>

                    <!-- Course Item 2 -->
                    <div onclick="selectCourse('دبلوم القيادة الدبلوماسية', '“Effective diplomacy requires absolute clarity and confidence.”')" class="course-card p-3 rounded-2xl cursor-pointer flex items-center justify-between group">
                        <div class="flex items-center gap-3">
                            <div class="w-11 h-11 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400 group-hover:bg-cyan-500 group-hover:text-black transition">
                                <i data-lucide="globe" class="w-5 h-5"></i>
                            </div>
                            <div>
                                <h3 class="text-xs font-bold text-white group-hover:text-cyan-300 transition">Diplomatic Leadership</h3>
                                <p class="text-[10px] text-gray-400 mt-0.5">الخطابة الرسمية وتجاوز لهجات النطق</p>
                            </div>
                        </div>
                        <div class="sound-wave">
                            <span></span><span></span><span></span><span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SECTION 2: THE AURA SPEECH RECOGNITION & CORRECTION LAB -->
            <div class="glass-shell p-4 rounded-3xl border border-amber-500/30 relative overflow-hidden space-y-3">
                <div class="absolute -right-12 -top-12 w-32 h-32 bg-amber-500/10 rounded-full blur-2xl"></div>
                
                <div class="flex items-center justify-between">
                    <span class="text-[11px] font-black text-amber-400 uppercase eng-font flex items-center gap-1.5">
                        <i data-lucide="mic-2" class="w-4 h-4 text-amber-400 animate-pulse"></i> محاكي النطق والتصحيح (AURA)
                    </span>
                    <span id="micStatusText" class="text-[10px] bg-blue-500/10 text-blue-400 px-2 py-0.5 rounded-full border border-blue-500/20 font-bold">جاهز للاستماع</span>
                </div>

                <!-- Active Sentence Display -->
                <div class="bg-black/60 p-3.5 rounded-2xl border border-white/5 space-y-1">
                    <span class="text-[9px] text-gray-500 font-bold uppercase">الجملة المطلوبة للنطق:</span>
                    <p id="targetSentence" class="eng-font text-xs font-semibold text-white tracking-wide">
                        “Price optimization is critical for quarterly growth.”
                    </p>
                </div>

                <!-- Interactive Record & Correction Box -->
                <div id="correctionBox" class="hidden bg-slate-900/90 border border-amber-500/30 p-3.5 rounded-2xl space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="text-[10px] font-bold text-amber-300">تقرير الذكاء الاصطناعي لتحليل الصوت:</span>
                        <span id="scoreBadge" class="eng-font text-[10px] bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded font-bold">96% توافق</span>
                    </div>
                    <div class="space-y-1 text-[11px]">
                        <p class="text-gray-300">🗣️ <b class="text-white">نطقك:</b> <span id="userSpeechText" class="eng-font text-amber-200">“Price optmization is critical...”</span></p>
                        <p class="text-gray-300">🛠️ <b class="text-amber-400">التصحيح الموصى به:</b> نطق كلمة <code class="bg-black/50 px-1 py-0.5 rounded text-amber-300 eng-font">Optimization</code> يجب أن يكون بضغط خفيف على حرف الـ z.</p>
                    </div>
                </div>

                <!-- Control Button -->
                <button id="micBtn" onclick="toggleListening()" class="w-full py-3 bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-black font-black text-xs rounded-2xl shadow-lg transition flex items-center justify-center gap-2 eng-font">
                    <i data-lucide="mic" class="w-4 h-4"></i> اضغط لتفعيل الميكروفون وتصحيح النطق فوراً
                </button>
            </div>

            <!-- SECTION 3: INNOVATIVE AUDIO IDEAS -->
            <div class="bg-gradient-to-br from-slate-900/90 to-black p-4 rounded-3xl border border-white/10 space-y-2.5">
                <div class="flex items-center gap-2">
                    <div class="w-7 h-7 rounded-lg bg-amber-500/20 flex items-center justify-center text-amber-400">
                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                    </div>
                    <h3 class="text-xs font-black text-white">الأفكار الصوتية المبتكرة في المنصة</h3>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10px]">
                    <div class="bg-black/40 p-2.5 rounded-xl border border-white/5">
                        <span class="text-amber-400 font-bold block mb-0.5">🎙️ مرآة النبرة (Tone Mirror)</span>
                        <p class="text-gray-400 leading-tight">تقارن نبرة صوتك بنبرة المتحدث الأصلي (رسمي vs ودي).</p>
                    </div>
                    <div class="bg-black/40 p-2.5 rounded-xl border border-white/5">
                        <span class="text-cyan-400 font-bold block mb-0.5">⚡ المحاكاة العكسية (Reverse AI)</span>
                        <p class="text-gray-400 leading-tight">يجبرك الذكاء الاصطناعي على تصحيح خطأك فوراً قبل الانتقال.</p>
                    </div>
                </div>
            </div>

        </div>

        <!-- Bottom Navigation -->
        <nav class="grid grid-cols-4 bg-black/90 border-t border-white/5 p-2 text-[10px] font-bold text-center text-amber-400 z-30">
            <button class="flex flex-col items-center gap-1 text-amber-400">
                <i data-lucide="headphones" class="w-4 h-4"></i> الصوتيات
            </button>
            <button onclick="alert('جاري الانتقال إلى مكتبة النصوص...')" class="flex flex-col items-center gap-1 text-gray-400 hover:text-white transition">
                <i data-lucide="book-open" class="w-4 h-4"></i> المكتبة
            </button>
            <button onclick="alert('جاري فتح حلبة التحدي الصوتي...')" class="flex flex-col items-center gap-1 text-gray-400 hover:text-white transition">
                <i data-lucide="trophy" class="w-4 h-4"></i> التحديات
            </button>
            <button onclick="alert('لوحة قيادة الإمبراطور الصوتي...')" class="flex flex-col items-center gap-1 text-gray-400 hover:text-white transition">
                <i data-lucide="user" class="w-4 h-4"></i> الإمبراطور
            </button>
        </nav>
    </main>

    <script>
        lucide.createIcons();

        function selectCourse(title, sentence) {
            document.getElementById('targetSentence').innerText = sentence;
            alert("🎧 تم تحميل المساق الصوتي بنجاح:\n" + title + "\n\nاستمع للعبارة ثم انقر على زر الميكروفون لتحليل نطقك.");
        }

        let isListening = false;
        function toggleListening() {
            const btn = document.getElementById('micBtn');
            const status = document.getElementById('micStatusText');
            const box = document.getElementById('correctionBox');
            
            if (!isListening) {
                isListening = true;
                btn.classList.add('listening-glow', 'from-red-600', 'to-rose-600');
                btn.innerHTML = '<i data-lucide="radio" class="w-4 h-4 animate-spin"></i> جاري الاستماع وتحليل النبرة الصوتية...';
                status.innerText = "جاري التقاط الصوت...";
                status.className = "text-[10px] bg-red-500/10 text-red-400 px-2 py-0.5 rounded-full border border-red-500/20 font-bold animate-pulse";
                box.classList.add('hidden');
                lucide.createIcons();

                setTimeout(() => {
                    isListening = false;
                    btn.classList.remove('listening-glow', 'from-red-600', 'to-rose-600');
                    btn.innerHTML = '<i data-lucide="mic" class="w-4 h-4"></i> اضغط لتفعيل الميكروفون وتصحيح النطق فوراً';
                    status.innerText = "تم التحليل بنجاح";
                    status.className = "text-[10px] bg-emerald-500/10 text-emerald-400 px-2 py-0.5 rounded-full border border-emerald-500/20 font-bold";
                    
                    box.classList.remove('hidden');
                    let xp = document.getElementById('totalXp');
                    let current = parseInt(xp.innerText.replace(',', ''));
                    xp.innerText = (current + 50) + " XP";
                    lucide.createIcons();
                }, 3000);
            }
        }
    </script>
</body>
</html>
"""

components.html(audio_masterpiece_app, height=880, scrolling=False)
