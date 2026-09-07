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

# 3. الشيفرة الهندسية الكاملة للواجهة (HTML5 / CSS3 Futuristic Glass / Vanilla ES6 Engine)
cyber_saba_app = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA ACADEMY X</title>
    <!-- Tailwind CSS & Lucide Core -->
    <script src="https://tailwindcss.com"></script>
    <script src="https://unpkg.com"></script>
    
    <!-- خطوط عربية ولاتينية فارهة -->
    <link rel="preconnect" href="https://googleapis.com">
    <link rel="preconnect" href="https://gstatic.com" crossorigin>
    <link href="https://googleapis.com/css2?family=Cinzel:wght=700;900&family=Marhey:wght=700&family=Tajawal:wght=300;500;700;900&display=swap" rel="stylesheet">

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
            0 { transform: translateY(0px) rotate(0deg); opacity: 0.15; }
            50 { transform: translateY(-12px) rotate(2deg); opacity: 0.35; }
            100 { transform: translateY(0px) rotate(0deg); opacity: 0.15; }
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
