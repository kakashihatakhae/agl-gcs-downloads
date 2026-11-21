# AGL Planner 0.8.0-internal.8 — Windows x64

Windows 10/11 x64 နှင့် .NET Framework 4.7.2 သို့မဟုတ် ပိုသစ်သော version လိုအပ်သည်။

## Download နှင့် install

**[Windows Setup.exe ရယူရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.8/AGL-Planner-0.8.0-internal.8-Windows-x64-Setup.exe)**

[Release notes နှင့် assets](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/tag/v0.8.0-internal.8) · [Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.8/AGL-Planner-0.8.0-internal.8-Windows-x64.zip) · [SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.8/SHA256SUMS.txt)

1. ပြင်ထားသော mission နှင့် record များကို save လုပ်ပြီး AGL Planner ကို ပိတ်ပါ။
2. Setup.exe ကို ဖွင့်ပြီး install သို့မဟုတ် update လုပ်ပါ။
3. Start Menu မှ AGL Planner ကို ဖွင့်ပြီး INFO တွင် `0.8.0-internal.8` ဖြစ်ကြောင်း စစ်ပါ။

Portable ZIP သုံးရန် folder အသစ်ထဲ ဖိုင်အားလုံးဖြည်ပြီး `AGL-Planner-Windows-x64/AGL Planner.exe` ကို ဖွင့်ပါ။

## FLY နှင့် 3D မြေပုံ

- Cockpit နှင့် map ကြား splitter ကို ဆွဲ၍ အကျယ်ညှိပါ။ Cockpit နှင့် Dashboard ကြား splitter ဖြင့် အမြင့်ညှိနိုင်သည်။
- **3D** ကို နှိပ်လျှင် အပေါ် 2D၊ အောက် 3D ပြသည်။ **Pop out** ဖြင့် 3D ကို သီးသန့် window တွင် ချဲ့ကြည့်နိုင်ပြီး **Dock back** ဖြင့် ပြန်ပေါင်းနိုင်သည်။
- စက်ပေါ်မူတည်၍ **3D → ⋯ → Render quality** တွင် **Auto / Performance / Full detail** ရွေးနိုင်သည်။ **Map details** မှ render size နှင့် နောက်ဆုံး frame အချိန်ကို ကြည့်နိုင်သည်။
- Plane၊ Copter၊ Rover နှင့် Boat တို့ကို ယာဉ်အမျိုးအစားအလိုက် ပြသည်။ GPS မရသေးလျှင် `MODEL PREVIEW · NO GPS` ဟု ပြသည်။ **Cached only** ဖြင့် သိမ်းထားသော map နှင့် elevation data ကို offline ကြည့်နိုင်သည်။

## Notifications နှင့် update

အပေါ်ဘားက ခေါင်းလောင်းကို နှိပ်ပြီး update သို့မဟုတ် မပြီးသေးသော flight record ကို တန်းဖွင့်နိုင်သည်။ **Unread** မှ မဖတ်ရသေးသည်များကို ကြည့်ပြီး **×** မှ panel ကို ပိတ်နိုင်သည်။

App စဖွင့်ချိန် အင်တာနက်ရပြီး update အသစ်တွေ့လျှင် install နှင့် restart ပြီးမှ GCS ဖွင့်သည်။ ပထမဆုံး network check မရပါက offline ဆက်သုံးနိုင်သည်။ `0.8.0-internal.5` နှင့် အဟောင်းမှ တင်ရာတွင် app နှင့် updater ပိတ်ပြီး Setup.exe ဖြင့် update လုပ်ပါ။
