# AGL Planner 0.8.0-internal.6 — Windows x64

Windows 10/11 x64 နှင့် .NET Framework 4.7.2 သို့မဟုတ် ပိုသစ်သော version လိုအပ်သည်။ Git၊ Visual Studio နှင့် .NET SDK မလိုပါ။

## Download နှင့် install

**[Windows Setup.exe ရယူရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.6/AGL-Planner-0.8.0-internal.6-Windows-x64-Setup.exe)**

[Release notes နှင့် assets](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/tag/v0.8.0-internal.6) · [SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.6/SHA256SUMS.txt)

1. AGL Planner ကို ပိတ်ပါ။ ပြင်ထားသော mission နှင့် record များကို အရင် save လုပ်ပါ။
2. Setup.exe ကို download လုပ်ပြီး ဖွင့်ကာ install လုပ်ပါ။ ယခင် installer ဖြင့် သွင်းထားလျှင်လည်း update လုပ်နိုင်သည်။
3. Start Menu / Desktop ရှိ AGL Planner ကို ဖွင့်ပါ။ INFO တွင် `0.8.0-internal.6` ဖြစ်ကြောင်း စစ်ပါ။

Portable ZIP ကို သုံးလိုလျှင် folder အသစ်တစ်ခုသို့ ဖိုင်အားလုံး ဖြည်ပြီး `AGL Planner.exe` ကို ဖွင့်ပါ။ Source code ZIP သည် installer မဟုတ်ပါ။

## ဒီတစ်ကြိမ် update ပြုလုပ်ရန်

0.8.0-internal.5 နှင့် အဟောင်းတွင် updater အပြီး process ကျန်နိုင်သဖြင့် app / updater ကို ပိတ်ပြီး ဒီ Setup.exe ဖြင့် update လုပ်ပါ။ ဒီ version တွင် installation တစ်ခုစီအတွက် duplicate startup guard နှင့် verified installer handoff / process exit ပြင်ဆင်ချက် ပါသည်။

## 3D မြေပုံ အသုံးပြုရန်

- FLY → **3D** ကို နှိပ်လျှင် အပေါ် 2D / အောက် 3D ကို ပြသည်။ အလယ် divider ဖြင့် အမြင့်ညှိနိုင်သည်။
- **Pop out** ဖြင့် သီးသန့် window တွင် resize / maximize လုပ်နိုင်သည်။ **Dock back** သို့မဟုတ် window ပိတ်လျှင် မူလ split view သို့ ပြန်ရောက်သည်။ Camera နှင့် data ကို ဆက်ထိန်းသည်။
- Plane တွင် မူရင်း FERONIX၊ multirotor တွင် အစိမ်း arm၊ အဝါ center body / rotor ring ပါသော copter model ကို ပြသည်။ Model နှင့် WP အကွင်းများသည် display scale ဖြစ်ပြီး physical size / acceptance radius မဟုတ်ပါ။
- GPS မရသေးလျှင် `MODEL PREVIEW · NO GPS` ဟု ခွဲပြသည်။ GPS fix ရလျှင် live တည်နေရာသို့ ပြောင်းသည်။
- Current Heading (အနီ)၊ Direct to current WP (လိမ္မော်)၊ Target Heading (အစိမ်း)၊ GPS Track / course-over-ground (အနက်) ကို ပြသည်။ **⋯** menu မှ ဖွင့် / ပိတ်နိုင်ပြီး 2D နှင့် settings တူသည်။
- WP အကွင်းများမှာ မရောက်သေးလျှင် cyan၊ ရောက်ပြီးကြောင်း telemetry ရလျှင် အစိမ်း ဖြစ်သည်။ Home ကို **H** ဖြင့် ပြသည်။
- **Cached only** သည် default ဖြစ်သည်။ ရှိပြီးသား map / elevation data ကို သုံးသည်။ Internet ဖြင့် data ဖြည့်ရန် provider ရွေးပြီး Cached only ကို ပိတ်ကာ Refresh လုပ်နိုင်သည်။ မသိသော elevation ကို အမြင့် 0 ဟု မယူပါ။

## Update

App စဖွင့်ချိန် published version အသစ်ရှိလျှင် download၊ SHA256 စစ်၊ install / restart ပြီးမှ GCS ကို ဖွင့်သည်။ ပထမ network check မရလျှင် အများဆုံး ၆ စက္ကန့်ခန့် စောင့်ပြီး offline ဆက်သုံးနိုင်သည်။ Update အသစ်သိပြီး download မအောင်မြင်ပါက Retry update / Exit app ကို ပြသည်။

## စစ်ဆေးမှု

Native Windows build၊ 3D OpenGL၊ copter geometry / rotor အရေအတွက်၊ Pop out / Dock back / minimize / restore၊ heading line / shared visibility၊ GPS preview၊ WP အကွင်း / Home၊ FPV/OSD၊ startup update နှင့် MAVLink regression များကို စစ်ဆေးထားသည်။ Installer ကို Windows တွင် install / file inventory / shortcut / uninstall စစ်ဆေးပြီးမှ ထုတ်သည်။
