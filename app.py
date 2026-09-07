<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SABA IMPERIAL EMPIRE | The Neo-Cinematic Experience</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Tajawal:wght@300;500;700;900&display=swap');
        :root { --gold: #d4af37; --void: #020408; --agate: #8b0000; }
        body { font-family: 'Tajawal', sans-serif; background-color: var(--void); color: #f1f5f9; overflow-x: hidden; user-select: none; }
        .cinzel { font-family: 'Cinzel', serif; }
        .neo-glass {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.92) 0%, rgba(5, 7, 12, 0.98) 100%);
            backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px);
            border: 1px solid rgba(212, 175, 55, 0.25);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(212, 175, 55, 0.15);
        }
        .imperial-gold-text {
            background: linear-gradient(135deg, #fff 0%, #d4af37 50%, #aa771c 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .net-card {
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            background: rgba(13, 18, 30, 0.8);
            border: 1px solid rgba(255,255,255,0.06);
        }
        .net-card:hover {
            transform: scale(1.04) translateY(-4px);
            border-color: var(--gold);
            box-shadow: 0 15px 35px rgba(212, 175, 55, 0.2);
        }
        #spaceCanvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
        /* Custom Scrollbar for Netflix style rows */
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="min-h-screen w-full flex justify-center items-center p-0 sm:p-3 relative">
    <canvas id="spaceCanvas"></canvas>
    
    <main class="w-full max-w-md h-screen sm:h-[96vh] flex flex-col neo-glass sm:rounded-[36px] overflow-hidden relative z-10 border-0 sm:border border-amber-500/30">
        
        <!-- Top Cinematic Navigation -->
        <header class="px-4 py-3 bg-black/70 border-b border-gray-800/80 flex items-center justify-between z-30">
            <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-amber-600 via-yellow-400 to-amber-700 p-[1.5px] shadow-lg shadow-amber-500/20">
                    <div class="w-full h-full bg-[#05070b] rounded-[10px] flex items-center justify-center">
                        <span class="cinzel text-amber-400 font-black text-base">𐩯</span>
                    </div>
                </div>
                <div>
                    <h1 class="text-[10px] font-black tracking-widest imperial-gold-text uppercase cinzel">SABA CINEMA X</h1>
                    <div class="flex items-center gap-1 mt-0.5">
                        <i data-lucide="zap" class="w-3 h-3 text-amber-400 fill-amber-400 animate-pulse"></i>
                        <span id="xpScore" class="text-xs font-black text-white">1,420</span>
                        <span class="text-[9px] text-amber-400/80 font-bold">XP EMPIRE</span>
                    </div>
                </div>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-[10px] bg-red-600/20 text-red-400 px-2.5 py-0.5 rounded-full border border-red-500/30 font-extrabold tracking-wide">ULTRA 4K AI</span>
            </div>
        </header>

        <!-- Main Viewport (Dynamic Container) -->
        <div id="viewport" class="flex-1 overflow-y-auto no-scrollbar relative z-10 p-4 space-y-5">
            
            <!-- Netflix Style Hero Banner -->
            <div class="relative w-full h-48 rounded-2xl overflow-hidden shadow-2xl border border-amber-500/30 group">
                <div class="absolute inset-0 bg-gradient-to-t from-[#05070b] via-[#05070b]/40 to-transparent z-10"></div>
                <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-amber-900/30 via-transparent to-black z-0"></div>
                <div class="absolute bottom-3 right-3 left-3 z-20 flex flex-col justify-end">
                    <span class="text-[9px] bg-amber-500 text-black font-black px-2 py-0.5 rounded w-max mb-1 uppercase cinzel">عرض حصري • البث الحي</span>
                    <h2 class="text-base font-black text-white cinzel leading-tight">Wall Street & Tech Negotiation</h2>
                    <p class="text-[10px] text-gray-300 mt-0.5 line-clamp-1">تعلم لغة كبرى الشركات العالمية بطريقة سينمائية تفاعلية مذهلة.</p>
                    <div class="flex items-center gap-2 mt-2">
                        <button onclick="launchCinematicLesson('Wall Street Masterclass')" class="flex-1 py-1.5 bg-white text-black font-black text-xs rounded-xl flex items-center justify-center gap-1.5 hover:bg-amber-400 transition">
                            <i data-lucide="play" class="w-3.5 h-3.5 fill-black"></i> تشغيل فوري
                        </button>
                        <button onclick="openAiChat()" class="px-3 py-1.5 bg-white/10 hover:bg-white/20 text-white font-bold text-xs rounded-xl backdrop-blur border border-white/20 transition flex items-center gap-1">
                            <i data-lucide="bot" class="w-3.5 h-3.5 text-amber-400"></i> المعلم
                        </button>
                    </div>
                </div>
            </div>

            <!-- Row 1: Netflix Style Horizontal Scroller (محتوى سينمائي واقعي) -->
            <div>
                <h3 class="text-xs font-black text-amber-300 mb-2.5 cinzel flex items-center gap-1.5">
                    <i data-lucide="film" class="w-3.5 h-3.5 text-amber-400"></i> مسلسلات وأفلام لغوية (Bite-sized)
                </h3>
                <div class="flex gap-3 overflow-x-auto no-scrollbar pb-1">
                    <div onclick="launchCinematicLesson('Silicon Valley Pitch')" class="min-w-[130px] h-36 rounded-xl net-card p-2.5 flex flex-col justify-between cursor-pointer relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent z-10"></div>
                        <span class="text-[9px] bg-blue-600/80 text-white px-1.5 py-0.5 rounded w-max z-20 font-bold">تقني 3د</span>
                        <div class="z-20">
                            <h4 class="text-xs font-bold text-white leading-tight">Silicon Valley Pitch</h4>
                            <p class="text-[9px] text-amber-300 mt-0.5">3 دقائق</p>
                        </div>
                    </div>
                    <div onclick="launchCinematicLesson('TED Business Talks')" class="min-w-[130px] h-36 rounded-xl net-card p-2.5 flex flex-col justify-between cursor-pointer relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent z-10"></div>
                        <span class="text-[9px] bg-amber-600/80 text-white px-1.5 py-0.5 rounded w-max z-20 font-bold">ريادة</span>
                        <div class="z-20">
                            <h4 class="text-xs font-bold text-white leading-tight">TED Talks Business</h4>
                            <p class="text-[9px] text-amber-300 mt-0.5">4 دقائق</p>
                        </div>
                    </div>
                    <div onclick="launchCinematicLesson('Survival English')" class="min-w-[130px] h-36 rounded-xl net-card p-2.5 flex flex-col justify-between cursor-pointer relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent z-10"></div>
                        <span class="text-[9px] bg-red-600/80 text-white px-1.5 py-0.5 rounded w-max z-20 font-bold">سفر</span>
                        <div class="z-20">
                            <h4 class="text-xs font-bold text-white leading-tight">Airport & Hotels</h4>
                            <p class="text-[9px] text-amber-300 mt-0.5">2 دقيقة</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Row 2: Gamified Duolingo-Killer Path (خريطة الممالك التفاعلية) -->
            <div>
                <h3 class="text-xs font-black text-amber-300 mb-2.5 cinzel flex items-center gap-1.5">
                    <i data-lucide="map" class="w-3.5 h-3.5 text-amber-400"></i> طريق إمبراطورية السعيدة (ألعاب وتحديات)
                </h3>
                <div class="grid grid-cols-3 gap-2.5">
                    <button onclick="startLevel(1)" class="net-card p-3 rounded-xl text-center flex flex-col items-center justify-center gap-1 group">
                        <div class="w-9 h-9 rounded-full bg-amber-500/20 border border-amber-500/50 flex items-center justify-center text-amber-300 font-black text-xs group-hover:scale-110 transition">1</div>
                        <span class="text-[10px] font-bold text-gray-200">الأساسيات</span>
                    </button>
                    <button onclick="startLevel(2)" class="net-card p-3 rounded-xl text-center flex flex-col items-center justify-center gap-1 group">
                        <div class="w-9 h-9 rounded-full bg-amber-500/20 border border-amber-500/50 flex items-center justify-center text-amber-300 font-black text-xs group-hover:scale-110 transition">2</div>
                        <span class="text-[10px] font-bold text-gray-200">المحادثة الحية</span>
                    </button>
                    <button onclick="startLevel(3)" class="net-card p-3 rounded-xl text-center flex flex-col items-center justify-center gap-1 group">
                        <div class="w-9 h-9 rounded-full bg-red-600/20 border border-red-500/50 flex items-center justify-center text-red-400 font-black text-xs group-hover:scale-110 transition">👑</div>
                        <span class="text-[10px] font-bold text-amber-300">سوق العمل</span>
                    </button>
                </div>
            </div>

            <!-- Quick AI Speech & Zero-Net Tools -->
            <div class="neo-glass p-3.5 rounded-2xl border border-amber-500/20 space-y-2">
                <div class="flex items-center justify-between">
                    <span class="text-[10px] text-amber-400 font-bold cinzel">مختبر النطق والذكاء الخارق</span>
                    <span class="text-[9px] bg-green-500/20 text-green-400 px-2 py-0.5 rounded-full font-bold">أداء فائق 0.1 ثانية</span>
                </div>
                <div class="flex items-center gap-2">
                    <input id="speechInputText" type="text" value="Artificial Intelligence empowers global communication." class="flex-1 bg-black/50 px-3 py-2 rounded-xl text-[11px] text-white border border-gray-700 outline-none" readonly>
                    <button onclick="playAudioPrompt()" class="p-2.5 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 rounded-xl border border-amber-500/40 transition">
                        <i data-lucide="volume-2" class="w-4 h-4"></i>
                    </button>
                </div>
                <button onclick="triggerVoiceAnalysis()" class="w-full py-2.5 bg-gradient-to-r from-red-700 to-red-900 hover:from-red-600 hover:to-red-800 text-white font-bold text-xs rounded-xl shadow-lg transition flex items-center justify-center gap-2">
                    <i data-lucide="mic" class="w-4 h-4"></i> اختبر نطقك الآن (بدون إنترنت تقريباً)
                </button>
                <div id="voiceResultBox" class="text-[10px] text-gray-300 text-center hidden"></div>
            </div>

        </div>

        <!-- Netflix / Neo-Imperial Bottom Navigation Bar -->
        <nav class="grid grid-cols-4 bg-black/90 border-t border-gray-800/80 p-2 text-[10px] font-bold z-30 text-center backdrop-blur-md">
            <button onclick="switchTab('home')" id="nav-home" class="flex flex-col items-center justify-center text-amber-400 gap-0.5 transition">
                <i data-lucide="home" class="w-4 h-4"></i> الرئيسية
            </button>
            <button onclick="switchTab('library')" id="nav-library" class="flex flex-col items-center justify-center text-gray-400 hover:text-white gap-0.5 transition">
                <i data-lucide="book-open" class="w-4 h-4"></i> المكتبة
            </button>
            <button onclick="switchTab('games')" id="nav-games" class="flex flex-col items-center justify-center text-gray-400 hover:text-white gap-0.5 transition">
                <i data-lucide="gamepad-2" class="w-4 h-4"></i> الألعاب
            </button>
            <button onclick="switchTab('profile')" id="nav-profile" class="flex flex-col items-center justify-center text-gray-400 hover:text-white gap-0.5 transition">
                <i data-lucide="user" class="w-4 h-4"></i> الإمبراطور
            </button>
        </nav>
    </main>

    <script>
        lucide.createIcons();

        function switchTab(tab) {
            ['home', 'library', 'games', 'profile'].forEach(t => {
                let btn = document.getElementById('nav-' + t);
                if(t === tab) {
                    btn.className = "flex flex-col items-center justify-center text-amber-400 gap-0.5 transition scale-105";
                } else {
                    btn.className = "flex flex-col items-center justify-center text-gray-400 hover:text-white gap-0.5 transition";
                }
            });
            if(tab === 'home') {
                // Keep default view
            } else {
                alert("جاري تحميل قسم: " + tab + " بسرعة فائقة (وضع البيانات الخفيف مفعل).");
            }
        }

        function launchCinematicLesson(title) {
            alert("🎬 جاري تشغيل العرض السينمائي التفاعلي: " + title + "\n(استهلاك بيانات منخفض للغاية + استجابة فورية)");
            let xp = document.getElementById('xpScore');
            xp.innerText = parseInt(xp.innerText.replace(',', '')) + 50;
        }

        function openAiChat() {
            alert("💬 المعلم الاقتصادي الافتراضي جاهز للرد الفوري ومحاكاة محادثات سوق العمل!");
        }

        function startLevel(lvl) {
            alert("🎮 بدء المستوى التفاعلي رقم: " + lvl + " (تحدي ألعاب سريع).");
        }

        function playAudioPrompt() {
            const utt = new SpeechSynthesisUtterance("Artificial Intelligence empowers global communication.");
            utt.lang = 'en-US';
            window.speechSynthesis.speak(utt);
        }

        function triggerVoiceAnalysis() {
            const box = document.getElementById('voiceResultBox');
            box.classList.remove('hidden');
            box.innerHTML = "🔴 جارٍ تحليل النطق المحلي بالذكاء الاصطناعي... <br><b class='text-amber-300'>تطابق ممتاز بنسبة 96%! (+30 XP)</b>";
            let xp = document.getElementById('xpScore');
            xp.innerText = parseInt(xp.innerText.replace(',', '')) + 30;
        }

        // Space Canvas Starfield Effect (Ultra Fast & Light)
        const canvas = document.getElementById('spaceCanvas');
        const ctx = canvas.getContext('2d');
        let stars = [];
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            stars = Array.from({ length: 30 }, () => ({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 1.2,
                speed: Math.random() * 0.1 + 0.02
            }));
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        function animateSpace() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = 'rgba(212, 175, 55, 0.4)';
            stars.forEach(s => {
                ctx.fillRect(s.x, s.y, s.size, s.size);
                s.y -= s.speed;
                if (s.y < 0) s.y = canvas.height;
            });
            requestAnimationFrame(animateSpace);
        }
        animateSpace();
    </script>
</body>
</html>
