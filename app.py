import streamlit as st

st.set_page_config(
    page_title="أكاديمية السعيدة الإمبراطورية | Saba Cinema X",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إخفاء عناصر ستريملايت الافتراضية للحصول على تجربة سينمائية نقية
st.markdown("""
    <style>
        #MainMenu, footer, header { display: none !important; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; background-color: #020408; }
    </style>
""", unsafe_allow_html=True)

# واجهة التطبيق السينمائية الفائقة
st.markdown("""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA IMPERIAL EMPIRE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Tajawal:wght@300;500;700;900&display=swap');
        :root { --gold: #d4af37; --void: #020408; }
        body { font-family: 'Tajawal', sans-serif; background-color: var(--void); color: #f1f5f9; overflow-x: hidden; user-select: none; }
        .cinzel { font-family: 'Cinzel', serif; }
        .neo-glass {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(5, 7, 12, 0.99) 100%);
            backdrop-filter: blur(30px);
            border: 1px solid rgba(212, 175, 55, 0.3);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
        }
        .imperial-gold-text {
            background: linear-gradient(135deg, #fff 0%, #d4af37 50%, #aa771c 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .net-card {
            transition: all 0.3s ease;
            background: rgba(13, 18, 30, 0.9);
            border: 1px solid rgba(255,255,255,0.08);
        }
        .net-card:hover {
            transform: scale(1.03);
            border-color: var(--gold);
        }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body class="min-h-screen w-full flex justify-center items-center p-0 sm:p-4">
    
    <main class="w-full max-w-md h-screen sm:h-[95vh] flex flex-col neo-glass sm:rounded-[36px] overflow-hidden relative border border-amber-500/30">
        
        <!-- Header -->
        <header class="px-4 py-3 bg-black/80 border-b border-gray-800 flex items-center justify-between z-30">
            <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-amber-600 via-yellow-400 to-amber-700 p-[1.5px]">
                    <div class="w-full h-full bg-[#05070b] rounded-[10px] flex items-center justify-center">
                        <span class="cinzel text-amber-400 font-black text-base">𐩯</span>
                    </div>
                </div>
                <div>
                    <h1 class="text-[10px] font-black tracking-widest imperial-gold-text uppercase cinzel">SABA CINEMA X</h1>
                    <div class="flex items-center gap-1 mt-0.5">
                        <span id="xpScore" class="text-xs font-black text-white">1,420</span>
                        <span class="text-[9px] text-amber-400/80 font-bold">XP</span>
                    </div>
                </div>
            </div>
            <span class="text-[10px] bg-red-600/20 text-red-400 px-2.5 py-0.5 rounded-full border border-red-500/30 font-extrabold">ULTRA 4K</span>
        </header>

        <!-- Content -->
        <div class="flex-1 overflow-y-auto no-scrollbar p-4 space-y-4">
            
            <!-- Hero Banner -->
            <div class="relative w-full h-44 rounded-2xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-end bg-gradient-to-t from-black via-black/50 to-transparent">
                <span class="text-[9px] bg-amber-500 text-black font-black px-2 py-0.5 rounded w-max mb-1 uppercase cinzel">عرض حصري</span>
                <h2 class="text-sm font-black text-white cinzel">Wall Street & Tech Negotiation</h2>
                <p class="text-[10px] text-gray-300 mt-0.5">تعلم لغة كبرى الشركات العالمية بطريقة سينمائية فائقة السرعة.</p>
                <button onclick="alert('جاري تشغيل الدرس السينمائي...')" class="mt-2.5 py-1.5 bg-white text-black font-black text-xs rounded-xl hover:bg-amber-400 transition">
                    تشغيل فوري 🎬
                </button>
            </div>

            <!-- Horizontal Scroll (Netflix style) -->
            <div>
                <h3 class="text-xs font-black text-amber-300 mb-2 cinzel">🎥 مسلسلات وأفلام لغوية</h3>
                <div class="flex gap-3 overflow-x-auto no-scrollbar pb-1">
                    <div class="min-w-[120px] h-32 rounded-xl net-card p-2.5 flex flex-col justify-between cursor-pointer">
                        <span class="text-[9px] bg-blue-600 text-white px-1.5 py-0.5 rounded w-max">تقني</span>
                        <h4 class="text-xs font-bold text-white">Silicon Valley</h4>
                    </div>
                    <div class="min-w-[120px] h-32 rounded-xl net-card p-2.5 flex flex-col justify-between cursor-pointer">
                        <span class="text-[9px] bg-amber-600 text-white px-1.5 py-0.5 rounded w-max">ريادة</span>
                        <h4 class="text-xs font-bold text-white">TED Business</h4>
                    </div>
                    <div class="min-w-[120px] h-32 rounded-xl net-card p-2.5 flex flex-col justify-between cursor-pointer">
                        <span class="text-[9px] bg-red-600 text-white px-1.5 py-0.5 rounded w-max">سفر</span>
                        <h4 class="text-xs font-bold text-white">Airport Survival</h4>
                    </div>
                </div>
            </div>

            <!-- Voice Lab -->
            <div class="neo-glass p-3.5 rounded-2xl border border-amber-500/20 space-y-2 text-center">
                <span class="text-[10px] text-amber-400 font-bold">مختبر النطق والذكاء الاصطناعي الفائق</span>
                <p class="text-[11px] text-gray-300">"Artificial Intelligence empowers global communication."</p>
                <button onclick="alert('تم تحليل النطق بنجاح! (+30 XP)')" class="w-full py-2 bg-red-700 hover:bg-red-600 text-white font-bold text-xs rounded-xl transition">
                    🎙️ اضغط لاختبار نطقك فوراً
                </button>
            </div>

        </div>

        <!-- Footer Nav -->
        <nav class="grid grid-cols-4 bg-black/90 border-t border-gray-800 p-2 text-[10px] font-bold text-center text-amber-400">
            <div>🏠 الرئيسية</div>
            <div class="text-gray-400">📚 المكتبة</div>
            <div class="text-gray-400">🎮 الألعاب</div>
            <div class="text-gray-400">👑 الإمبراطور</div>
        </nav>
    </main>

    <script>
        lucide.createIcons();
    </script>
</body>
</html>
""", height=850, scrolling=False)
