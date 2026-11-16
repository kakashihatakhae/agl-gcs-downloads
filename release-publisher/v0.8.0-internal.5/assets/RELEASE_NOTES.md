## [0.8.0-internal.5] - 2026-11-16

### Windows installer ရယူရန်

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.5/AGL-Planner-0.8.0-internal.5-Windows-x64-Setup.exe)**

[SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.5/SHA256SUMS.txt) · [မြန်မာအသုံးပြုနည်း](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.5/README-WINDOWS-my.md) · [လက်ရှိ installer အမြဲရယူရန်](https://agl-planner-services.quiz-checker-usage.workers.dev/downloads/windows-x64)

AGL Planner ကို ပိတ်ပြီး Setup.exe ဖြင့် install / update လုပ်ပါ။ Windows 10/11 x64၊ .NET Framework 4.7.2+ လိုအပ်သည်။ GitHub login မလိုပါ။

### ယခင် 0.7.0-internal.2 မှ ပြောင်းလဲမှုများ

- **FLY 2D / 3D split map**၊ resize divider၊ သီးခြား camera zoom၊ Follow / Orbit နှင့် မူရင်း FERONIX STL ကို GPS / MSL / attitude အတိုင်း ပြသည်။
- **Pop out / Dock back** ဖြင့် သီးသန့် resize / maximize လုပ်နိုင်သော 3D window ပါသည်။ Camera / data ကို ဆက်ထိန်းပြီး renderer တစ်ခုတည်း သုံးသည်။ Minimize ချိန် ရပ်ကာ 2D ပြန်ရွေးခြင်း / FLY မှထွက်ခြင်းက GPU resources ကို ပြန်လွှတ်သည်။
- **Copter 3D model** တွင် အစိမ်း arm၊ အဝါ center body / rotor ring၊ charcoal propeller နှင့် အဖြူ front chevron ပါသည်။ Vehicle type အလိုက် rotor အရေအတွက် ရွေးသည်။ Plane တွင် FERONIX ကို ဆက်သုံးသည်။
- **Navigation lines** — Current Heading အနီ၊ Direct to current WP လိမ္မော်၊ Target Heading အစိမ်း၊ GPS Track / course-over-ground အနက်။ 2D နှင့် show/hide settings တူပြီး ⋯ menu မှလည်း ရွေးနိုင်သည်။
- **WP နံပါတ် / အကွင်း / Home H** — မရောက်သေးသော အကွင်း cyan၊ telemetry က ရောက်ပြီးဟု အတည်ပြုသော အကွင်း အစိမ်း။ အကွင်းကို ၃၀% သေးထားသည်။ Target ခုန်ရွေးခြင်းကို ရောက်ပြီးဟု မမှတ်ပါ။
- **GPS မရသေးချိန် model preview** ကို မီးခိုးရောင်နှင့် `MODEL PREVIEW · NO GPS` ဟု ခွဲပြပြီး fix ရလျှင် live တည်နေရာသို့ ပြောင်းသည်။ Missing terrain / attitude နှင့် terrain အောက်ကွယ်နိုင်သော အခြေအနေများတွင်လည်း model မြင်သာရေးကို ပြင်ထားသည်။ Telemetry GPS / MSL ကို မပြောင်းပါ။
- **Startup update** — Internet ရချိန် GCS / auto-connect မစခင် published update စစ်၍ version အသစ်ကို download / SHA256 စစ် / install / restart လုပ်သည်။ ပထမ check တွင် offline / timeout ဖြစ်လျှင် offline ဆက်သုံးနိုင်သည်။ Update အသစ်သိပြီးနောက် မအောင်မြင်ပါက Retry / Exit state ကို ဆက်ထိန်းသည်။ Version ဟောင်းဆီ downgrade မလုပ်ပါ။
- Cached-only terrain၊ bounded map / elevation samples၊ lazy renderer နှင့် cached labels ဖြင့် Windows ပေါ်တွင် ပေါ့ပါးစေရန် ထိန်းထားသည်။

### စစ်ဆေးမှု

Native Windows build၊ 3D OpenGL / copter / navigation line / window lifecycle၊ WP အကွင်း / Home / GPS preview၊ FPV/OSD၊ startup updater နှင့် MAVLink regression checks အောင်မြင်ပြီး Windows installer install / file inventory / shortcut / uninstall စစ်ဆေးမှုများ ပါဝင်သည်။
