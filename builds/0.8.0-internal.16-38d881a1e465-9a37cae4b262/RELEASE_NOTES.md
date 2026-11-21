## [0.8.0-internal.16] - 2026-11-21

### Windows installer ရယူရန်

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.16/AGL-Planner-0.8.0-internal.16-Windows-x64-Setup.exe)**

[Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.16/AGL-Planner-0.8.0-internal.16-Windows-x64.zip) · [SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.16/SHA256SUMS.txt) · [မြန်မာအသုံးပြုနည်း](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.16/README-WINDOWS-my.md)

Windows 10/11 x64 နှင့် .NET Framework 4.7.2+ လိုအပ်သည်။ Download အတွက် GitHub login မလိုပါ။

### 0.8.0-internal.8 မှ ပြောင်းလဲမှုများ

- **Complete Previous Record** တွင် ဖြည့်စရာကျန်သည့် field အရေအတွက်နှင့် အသေးစိတ်စာရင်းကို ကြည့်နိုင်သည်။ Postflight outcome ကို ရွေးပြီး **Show all details** မှ သိမ်းထားသည့်အချက်များကို ပြန်ကြည့်၊ ပြင်နိုင်သည်။ Telemetry မှ flight time မရလျှင် `0` ဖြည့်ပြီး data ရရှိမှုအခြေအနေကို ပြသည်။
- **Prepare Record** တွင် local နှင့် sync လုပ်ထားသည့် Vehicle Profile များကို ရှာပြီး offline ရွေးနိုင်သည်။ ရွေးထားသည့် profile နှင့် ချိတ်ထားသည့်ယာဉ် မကိုက်လျှင် record မစခင် အတည်ပြုနိုင်သည်။
- **FLY cockpit** တွင် fighter HUD ပုံစံဖြင့် heading၊ pitch၊ roll၊ airspeed နှင့် altitude ဖတ်နိုင်သည်။ Airspeed box မြှားက ဘယ်ဘက် speed scale ကို ညွှန်ပြီး **AIRSPEED** စာတန်းကို ဖုံးနေသည့် မျဉ်းများကို ဖယ်ထားသည်။
- **Wind card** က FLY မြေပုံပေါ်မှာ လေအမြန်နှုန်းကို `m/s` ဖြင့်ပြသည်။ `From` က လေတိုက်လာသည့်အရပ်ကို ပြပြီး မြှားက လေရွေ့သွားသည့်အရပ်ကို ညွှန်သည်။ လေငြိမ်ခြင်း၊ estimate မရသေးခြင်းနှင့် estimate ဟောင်းခြင်းကို ခွဲပြထားသည်။
- FLY tab၊ tab ရွှေ့မြှား၊ Map နှင့် MGRS dropdown၊ Zoom spinner၊ connection toolbar နှင့် title bar တို့ကို AGL dark theme နှင့် ညှိထားသည်။

App စဖွင့်ချိန် အင်တာနက်ရပြီး update အသစ်တွေ့လျှင် download၊ စစ်ဆေး၊ install နှင့် restart လုပ်ပြီးမှ GCS ဖွင့်သည်။ `0.8.0-internal.5` နှင့် အဟောင်းမှ တင်ရာတွင် app နှင့် updater ပိတ်ပြီး Setup.exe ဖြင့် update လုပ်ပါ။
