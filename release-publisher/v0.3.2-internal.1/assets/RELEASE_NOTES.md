## [0.3.2-internal.1] - 2026-10-22

Windows 10/11 x64 အတွက် internal update ဖြစ်ပါသည်။ FLY နှင့် PLAN မြေပုံရှိ vehicle icon ပြင်ဆင်ချက်များ ပါဝင်ပါသည်။

### Windows installer ရယူရန်

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန် (70 MB)](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.3.2-internal.1/AGL-Planner-0.3.2-internal.1-Windows-x64-Setup.exe)**

[Installer နှင့် ZIP SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.3.2-internal.1/SHA256SUMS.txt) · [လက်ရှိ Windows installer ရယူရန်](https://agl-planner-services.quiz-checker-usage.workers.dev/downloads/windows-x64)

ဖွင့်ထားသော AGL Planner ကို ပိတ်ပြီး Setup.exe ကို ဖွင့်ကာ install လုပ်ပါ။ ယခင် installer ဖြင့် သွင်းထားသော app ကို update လုပ်နိုင်ပါသည်။ Git၊ Visual Studio နှင့် .NET SDK မလိုပါ။ .NET Framework 4.7.2+ လိုအပ်ပါသည်။

### App ထဲမှ update လုပ်ရန်

Vehicle connection ကို disconnect လုပ်ပြီး ပြင်ထားသော mission များကို save လုပ်ပါ။ **INFO → Update AGL Planner → Check for updates** မှ update ကို စစ်၍ download/install လုပ်ပါ။ App ပြန်ပွင့်ချိန် INFO တွင် **0.3.2-internal.1** ဖြစ်ကြောင်း စစ်နိုင်ပါသည်။ Public update service ကို သုံးသဖြင့် GitHub login မလိုပါ။

### ပြောင်းလဲမှုများ

- **VTOL၊ Copter၊ Helicopter၊ Rover၊ Boat၊ Submarine နှင့် Unknown** map icon များကို အတည်ပြုထားသော အဝါ/charcoal concept အတိုင်း vector ပုံစံ ပြောင်းထားပါသည်။ **FLY နှင့် PLAN** နှစ်ခုလုံးတွင် သုံးပါသည်။
- **Copter arm လေးချောင်းကို အစိမ်းရောင် (`#26DC7E`)** ပြောင်း၍ အဝါရောင် body/propellers နှင့် ကွဲပြားမြင်သာစေပါသည်။
- **Plane အတွက် FERONIX Delta Wing** ကို ဆက်သုံးပါသည်။ VTOL ကို rotor ပါသော lift+cruise icon သီးသန့်ဖြင့် ပြပါသည်။ 3D model ကို မပြောင်းပါ။
- Heading နှင့် map bearing အလိုက် လှည့်ခြင်း၊ GPS location၊ tooltip၊ system ID၊ inactive hidden/transparent display နှင့် Copter avoidance circles များကို ထိန်းထားပါသည်။
- Vehicle type ပြောင်းချိန် marker အဟောင်းကို မှားပြီး ပြန်သုံးခြင်းကို ပြင်ထားပါသည်။

### စစ်ဆေးမှု

Desktop compatibility build၊ GDI/Skia rendering၊ rotation/bounds၊ invalid heading၊ inactive states၊ marker type transitions နှင့် Copter danger-ring regression checks အောင်မြင်ပါသည်။ GUI smoke suite၊ package inventory/SHA256 နှင့် installer NSIS CRC ကို စစ်ထားပါသည်။ Windows စက်အစစ်၏ install/update/restart နှင့် UI/DPI စမ်းသပ်မှုအားလုံး pass ဟု မသတ်မှတ်ပါ။

Installer SHA256: `015486b2186d4629805a9a19da097b1e198e12323d534fe7a5594ca5495c9a9a`

Compiled source: `0914c403fedc76036708741a0c5a0567a117065d` · Build: `0.3.2-internal.1-0914c403fedc-2ac00d3fb485`
