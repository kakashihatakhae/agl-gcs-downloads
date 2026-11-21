# AGL Planner 0.8.0-internal.16 — Windows x64

Windows 10/11 x64 နှင့် .NET Framework 4.7.2 သို့မဟုတ် ပိုသစ်သော version လိုအပ်သည်။

## Download နှင့် install

**[Windows Setup.exe ရယူရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.16/AGL-Planner-0.8.0-internal.16-Windows-x64-Setup.exe)**

[Release notes နှင့် assets](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/tag/v0.8.0-internal.16) · [Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.16/AGL-Planner-0.8.0-internal.16-Windows-x64.zip) · [SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.16/SHA256SUMS.txt)

1. ပြင်ထားသည့် mission နှင့် record များကို သိမ်းပြီး AGL Planner ပိတ်ပါ။
2. Setup.exe ကို ဖွင့်ပြီး install သို့မဟုတ် update လုပ်ပါ။
3. Start Menu မှ AGL Planner ကို ဖွင့်ပြီး **INFO** တွင် `0.8.0-internal.16` ပြကြောင်း စစ်ပါ။

Portable ZIP သုံးလိုပါက folder အသစ်ထဲ ဖိုင်အားလုံးဖြည်ပြီး `AGL-Planner-Windows-x64/AGL Planner.exe` ကို ဖွင့်ပါ။

## FLY cockpit နှင့် မြေပုံ

- HUD ၏ ဘယ်ဘက်တွင် Airspeed၊ ညာဘက်တွင် Altitude ဖတ်နိုင်သည်။ Box မြှားသည် သက်ဆိုင်ရာ scale ပေါ်တွင် လက်ရှိတန်ဖိုးကို ညွှန်သည်။
- **Wind** card တွင် `From W · 270°` ဆိုလျှင် အနောက်ဘက်မှ လေတိုက်လာသည်။ မြှားက လေရွေ့ရာဘက်ကို ညွှန်ပြီး အမြန်နှုန်းကို `m/s` ဖြင့်ပြသည်။ Flight controller မှ wind estimate ပေးရန် လိုသည်။
- **3D** ကို နှိပ်လျှင် မြေပုံကို အပေါ် 2D၊ အောက် 3D ခွဲပြသည်။ **Pop out** မှ သီးသန့် window တွင် ချဲ့ကြည့်ပြီး **Dock back** ဖြင့် ပြန်ပေါင်းနိုင်သည်။

## Flight Record

- **Prepare Record** တွင် သိမ်းထားသော Vehicle Profile ကို ရှာရွေးနိုင်သည်။ ချိတ်ထားသည့်ယာဉ်နှင့် profile မကိုက်လျှင် record မစခင် အတည်ပြုပါ။
- **Complete Previous Record** မှ ကျန်နေသည့် field များနှင့် flight outcome ကို ဖြည့်ပါ။ အခြားအချက်များကို **Show all details** မှ ပြန်ကြည့်နိုင်သည်။

## App update

အင်တာနက်ရချိန် app စဖွင့်သည့်အခါ update စစ်ပြီး အသစ်ရှိလျှင် install နှင့် restart လုပ်ပေးသည်။ `0.8.0-internal.5` နှင့် အဟောင်းမှ တင်ရာတွင် app နှင့် updater ကိုပိတ်ပြီး Setup.exe သုံးပါ။
