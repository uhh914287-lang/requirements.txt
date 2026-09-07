<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أكاديمية السعيدة للإنجليزية الذكية</title>
    <!-- Tailwind CSS & Lucide Icons via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
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

        function toggleKeyModal() {
            document.getElementById('keyModal').classList.toggle('hidden');
        }

        function saveApiKey() {
            const key = document.getElementById('apiKeyInput').value.trim();
            if (key) {
                localStorage.setItem('gemini_api_key', key);
                geminiKey = key;
                alert('تم حفظ المفتاح بنجاح!');
                toggleKeyModal();
            }
        }

        function switchTab(tab) {
            ['chat', 'voice', 'blitz'].forEach(t => {
                document.getElementById(`view-${t}`).classList.add('hidden');
                document.getElementById(`tab-${t}`).className = 'flex-1 py-3 text-center text-gray-400 hover:text-gray-200';
            });
            document.getElementById(`view-${tab}`).classList.remove('hidden');
            document.getElementById(`tab-${tab}`).className = 'flex-1 py-3 text-center text-red-500 border-b-2 border-red-500';
        }

        // 1. المحاور الذكي عبر Gemini API المباشر
        async function sendChatMessage() {
            const input = document.getElementById('chatInput');
            const text = input.value.trim();
            if (!text) return;

            if (!geminiKey) {
                alert('يرجى النقر على أيقونة المفتاح بالأعلى وإدخال مفتاح Gemini الخاص بك للبدء.');
                toggleKeyModal();
                return;
            }

            const chatBox = document.getElementById('chatMessages');
            chatBox.innerHTML += `
                <div class="flex justify-start">
                    <div class="bg-red-600 text-white p-3 rounded-2xl rounded-tr-none max-w-[85%]">${text}</div>
                </div>`;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${geminiKey}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{
                            parts: [{
                                text: `You are an encouraging English coach for Yemeni learners. Reply briefly (under 3 sentences). Correct any grammar gently at the end with a tip. User said: ${text}`
                            }]
                        }]
                    })
                });
                const data = await response.json();
                const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || 'تعذر جلب الرد، تحقق من صحة المفتاح.';

                chatBox.innerHTML += `
                    <div class="flex justify-end">
                        <div class="bg-[#1e293b] p-3 rounded-2xl rounded-tl-none border border-gray-800 max-w-[85%] leading-relaxed">
                            ${reply}
                            <button onclick="speakText(this.parentElement.innerText)" class="mt-2 text-xs flex items-center gap-1 text-amber-400">
                                🔊 استمع للنطق
                            </button>
                        </div>
                    </div>`;
                addXP(15);
                chatBox.scrollTop = chatBox.scrollHeight;
            } catch (err) {
                chatBox.innerHTML += `<div class="text-xs text-red-400 text-center">خطأ بالاتصال، تأكد من مفتاح الـ API.</div>`;
            }
        }

        // النطق الآلي
        function speakText(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const utter = new SpeechSynthesisUtterance(text.replace('🔊 استمع للنطق', ''));
                utter.lang = 'en-US';
                utter.rate = 0.92;
                window.speechSynthesis.speak(utter);
            }
        }

        // 2. فحص النطق بالمايك
        function startMicRecognition() {
            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRec) {
                alert("متصفحك لا يدعم التعرف الصوتي المباشر، يرجى الفتح عبر Chrome.");
                return;
            }
            const rec = new SpeechRec();
            rec.lang = 'en-US';
            const status = document.getElementById('micStatus');
            const feedback = document.getElementById('voiceFeedback');

            status.innerText = '🎙️ جاري الاستماع... اقرأ الآن!';
            rec.start();

            rec.onresult = (e) => {
                const spoken = e.results[0][0].transcript;
                status.innerText = 'اضغط المايك وتحدث بوضوح';
                if (spoken.toLowerCase().includes("practice makes progress")) {
                    feedback.innerHTML = `<span class="text-green-400 font-bold text-sm">🟢 لفظ ممتاز ومتقن! (100%)</span><br>سمعنا: "${spoken}"`;
                    addXP(25);
                } else {
                    feedback.innerHTML = `<span class="text-amber-400 font-bold text-sm">🟡 محاولة جيدة! ركز على نطق مخارج الكلمات بدقة.</span><br>سمعنا: "${spoken}"`;
                }
            };
            rec.onerror = () => { status.innerText = 'تعذر التقاط الصوت، أعد المحاولة'; };
        }

        // 3. التحقق من إجابة التحدي
        function checkAnswer(btn, isCorrect) {
            const res = document.getElementById('blitzResult');
            if (isCorrect) {
                btn.className = 'w-full p-3 text-sm bg-green-950/80 border border-green-600 rounded-xl text-right font-bold text-green-300';
                res.innerHTML = '🎉 إجابة احترافية ممتازة! ربحت +20 XP';
                addXP(20);
            } else {
                btn.className = 'w-full p-3 text-sm bg-red-950/80 border border-red-600 rounded-xl text-right font-bold text-red-300';
                res.innerHTML = '❌ غير دقيقة للتعامل المهني الرسمي، حاول مجدداً.';
            }
        }

        document.getElementById('chatInput').addEventListener('keydown', (e) => {
            if (e.key === 'Enter') sendChatMessage();
        });
    </script>
</body>
</html>
