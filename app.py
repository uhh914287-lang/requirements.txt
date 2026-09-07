import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة لتظهر بحجم الهاتف بالكامل
st.set_page_config(
    page_title="أكاديمية السعيدة للإنجليزية الذكية",
    page_icon="🇾🇪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# إخفاء قوائم Streamlit الافتراضية لمنح المستخدم تجربة تطبيق هاتف كامل
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 480px !important; margin: auto;}
    </style>
""", unsafe_allowed_html=True)

html_code = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أكاديمية السعيدة للإنجليزية الذكية</title>
    <!-- Tailwind CSS & Lucide Icons via CDN -->
    <script src="https://tailwindcss.com"></script>
    <script src="https://unpkg.com"></script>
    <style>
        @import url('https://googleapis.com');
        body { font-family: 'Tajawal', sans-serif; }
        .hide-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body class="bg-[#0b0f19] text-gray-100 min-h-screen flex flex-col items-center p-3 sm:p-5">

    <!-- الحاوية الرئيسية للهاتف -->
    <div class="w-full max-w-md flex flex-col h-[92vh] bg-[#111827] rounded-3xl border border-gray-800 shadow-2xl overflow-hidden">
        
        <!-- الشريط العلوي: النقاط والمحافظة -->
        <header class="bg-[#1f2937]/90 p-4 border-b border-gray-800 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <div class="flex items-center gap-1 bg-red-950/60 text-red-500 px-3 py-1 rounded-xl text-sm font-black border border-red-800/40">
                    <i data-lucide="flame" class="w-4 h-4 animate-bounce"></i>
                    <span id="xpDisplay">250 XP</span>
                </div>
                <div class="flex items-center gap-1 bg-amber-950/50 text-amber-400 px-2.5 py-1 rounded-xl text-xs font-bold border border-amber-800/30">
                    <i data-lucide="trophy" class="w-3.5 h-3.5"></i>
                    <span>دوري المحافظات</span>
                </div>
            </div>

            <div class="flex items-center gap-2">
                <select id="govSelect" class="bg-gray-900 text-xs text-gray-300 rounded-xl px-2 py-1.5 border border-gray-700 outline-none">
                    <option value="الحديدة">الحديدة ⚓</option>
                    <option value="صنعاء">صنعاء 🏛️</option>
                    <option value="عدن">عدن 🌊</option>
                    <option value="تعز">تعز 🏰</option>
                    <option value="حضرموت">حضرموت 🌴</option>
                </select>
                <button onclick="toggleKeyModal()" class="p-1.5 bg-gray-800 hover:bg-gray-700 rounded-xl text-gray-400 hover:text-white" title="إعدادات الـ API">
                    <i data-lucide="key" class="w-4 h-4"></i>
                </button>
            </div>
        </header>

        <!-- نافذة منبثقة لضبط مفتاح Gemini -->
        <div id="keyModal" class="hidden p-3 bg-amber-950/90 border-b border-amber-700 text-xs text-amber-200 flex flex-col gap-2">
            <span>أدخل مفتاح Google Gemini الخاص بك (يُحفظ بأمان في متصفحك):</span>
            <div class="flex gap-2">
                <input id="apiKeyInput" type="password" placeholder="AIzaSy..." class="flex-1 bg-black/50 px-2 py-1 rounded border border-amber-700 text-white outline-none">
                <button onclick="saveApiKey()" class="bg-amber-600 hover:bg-amber-700 text-black font-bold px-3 py-1 rounded">حفظ</button>
            </div>
        </div>

        <!-- تبويبات الأنشطة السريعة -->
        <nav class="flex border-b border-gray-800 bg-[#161f30] text-xs font-bold text-gray-400">
            <button onclick="switchTab('chat')" id="tab-chat" class="flex-1 py-3 text-center text-red-500 border-b-2 border-red-500">
                💬 المحاور الذكي
            </button>
            <button onclick="switchTab('voice')" id="tab-voice" class="flex-1 py-3 text-center hover:text-gray-200">
                🎙️ تصحيح النطق
            </button>
            <button onclick="switchTab('blitz')" id="tab-blitz" class="flex-1 py-3 text-center hover:text-gray-200">
                ⚡ تحدي الـ 60 ثانية
            </button>
        </nav>

        <!-- 1. قسم المحاور الذكي -->
        <div id="view-chat" class="flex-1 flex flex-col justify-between overflow-hidden">
            <div id="chatMessages" class="flex-1 p-4 overflow-y-auto space-y-3 hide-scrollbar text-sm">
                <div class="flex justify-end">
                    <div class="bg-[#1e293b] p-3 rounded-2xl rounded-tl-none border border-gray-800 max-w-[85%] leading-relaxed">
                        أهلاً بك يا بطل! أنا مدربك التفاعلي لكسر حاجز الخوف من الإنجليزية. اكتب أي جملة أو اسألني وسأساعدك فوراً 🚀
                    </div>
                </div>
            </div>
            
            <div class="p-3 bg-[#161f30] border-t border-gray-800 flex items-center gap-2">
                <input id="chatInput" type="text" placeholder="اكتب بالإنجليزية أو اسأل بالعربي..." class="flex-1 bg-gray-900 text-white px-3.5 py-2.5 rounded-xl border border-gray-700 text-sm outline-none focus:border-red-500">
                <button onclick="sendChatMessage()" class="bg-red-600 hover:bg-red-700 text-white p-2.5 rounded-xl">
                    <i data-lucide="send" class="w-5 h-5 transform -rotate-90"></i>
                </button>
            </div>
        </div>

        <!-- 2. قسم تصحيح النطق الصوتي -->
        <div id="view-voice" class="hidden flex-1 p-5 flex-col items-center justify-between text-center">
            <div class="space-y-4 w-full mt-4">
                <span class="text-xs text-gray-400 font-bold tracking-wider">اقرأ الجملة التالية بصوتك:</span>
                <div class="p-4 bg-gray-900 rounded-2xl border border-gray-800 text-lg font-bold text-red-400 tracking-wide dir-ltr" id="targetSentence">
                    "Practice makes progress, not perfection."
                </div>
                <div class="flex justify-center gap-3">
                    <button onclick="speakText(document.getElementById('targetSentence').innerText)" class="text-xs flex items-center gap-1 text-amber-400 bg-amber-950/40 px-3 py-1.5 rounded-xl border border-amber-800/40">
                        <i data-lucide="volume-2" class="w-4 h-4"></i> استمع للنطق الأصلي
                    </button>
                </div>
            </div>

            <!-- زر التسجيل -->
            <div class="my-auto flex flex-col items-center gap-3">
                <button id="micBtn" onclick="startMicRecognition()" class="w-24 h-24 bg-red-600 hover:bg-red-700 active:scale-95 rounded-full flex items-center justify-center text-white shadow-lg shadow-red-900/40 transition-all">
                    <i data-lucide="mic" class="w-10 h-10"></i>
                </button>
                <span id="micStatus" class="text-xs text-gray-400">اضغط المايك وتحدث بوضوح</span>
            </div>

            <div id="voiceFeedback" class="w-full min-h-[70px] p-3 rounded-2xl bg-gray-900/90 border border-gray-800 text-xs text-gray-300">
                النتيجة وملاحظات اللفظ ستظهر هنا...
            </div>
        </div>

        <!-- 3. قسم تحدي الـ 60 ثانية -->
        <div id="view-blitz" class="hidden flex-1 p-5 flex flex-col justify-between">
            <div class="flex justify-between items-center bg-gray-900 p-3 rounded-2xl border border-gray-800">
                <span class="text-xs text-gray-400 font-bold">سؤال من سوق العمل والـ Freelancing:</span>
                <span class="text-xs bg-red-950 text-red-400 font-bold px-2.5 py-1 rounded-lg">المستوى 1</span>
            </div>

            <div class="my-auto space-y-4">
                <h3 class="text-base font-bold text-center leading-relaxed text-gray-200">
                    كيف تقول لعميل أجنبي باحتراف: <br>
                    <span class="text-amber-400">"سأقوم بتسليم المشروع في الموعد المحدد"</span>؟
                </h3>

                <div class="space-y-2.5 pt-2">
                    <button onclick="checkAnswer(this, true)" class="w-full p-3 text-sm bg-gray-900 hover:bg-gray-800 border border-gray-800 rounded-xl text-right font-medium transition-all">
                        A) I will deliver the project on schedule.
                    </button>
                    <button onclick="checkAnswer(this, false)" class="w-full p-3 text-sm bg-gray-900 hover:bg-gray-800 border border-gray-800 rounded-xl text-right font-medium transition-all">
                        B) I give you the work in the time.
                    </button>
                    <button onclick="checkAnswer(this, false)" class="w-full p-3 text-sm bg-gray-900 hover:bg-gray-800 border border-gray-800 rounded-xl text-right font-medium transition-all">
                        C) Project finish tomorrow sure.
                    </button>
                </div>
            </div>

            <div id="blitzResult" class="text-center text-xs text-gray-400">
                اختر الإجابة الأدق والأكثر احترافية
            </div>
        </div>

    </div>

    <!-- المنطق البرمجي المكتمل -->
    <script>
        lucide.createIcons();

        // استرجاع النقاط والمفتاح
        let currentXP = parseInt(localStorage.getItem('user_xp') || '250');
        let geminiKey = localStorage.getItem('gemini_api_key') || '';
        document.getElementById('xpDisplay').innerText = `${currentXP} XP`;
        if (geminiKey) document.getElementById('apiKeyInput').value = geminiKey;

        function addXP(points) {
            currentXP += points;
            localStorage.setItem('user_xp', currentXP);
            document.getElementById('xpDisplay').innerText = `${currentXP} XP`;
        }
