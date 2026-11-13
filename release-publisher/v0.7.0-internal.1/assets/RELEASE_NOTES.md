## [0.7.0-internal.1] - 2026-11-13

### Windows installer

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.7.0-internal.1/AGL-Planner-0.7.0-internal.1-Windows-x64-Setup.exe)**

[Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.7.0-internal.1/AGL-Planner-0.7.0-internal.1-Windows-x64.zip) · [SHA256](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.7.0-internal.1/SHA256SUMS.txt)

### FPV View နှင့် OSD

- FLY ရှိ Flight Record ဘေးက **FPV View** သည် သီးသန့် window ကို ဖွင့်ပေးသည်။ မူလ cockpit၊ map နှင့် dashboard ကို ဆက်သုံးနိုင်ပြီး window ကို resize/maximize သို့မဟုတ် အခြား monitor ဆီ ရွှေ့နိုင်သည်။
- **Edit OSD** တွင် element search/visibility စာရင်း၊ draggable preview နှင့် settings ဟူ၍ ၃ ကော်လံ ပါသည်။ Keyboard နေရာရွှေ့ခြင်း၊ text size၊ Sample/Live preview၊ grid/safe-area guides၊ Reset၊ Save/Cancel နှင့် local layout persistence ပါသည်။
- Video မရှိချိန် သို့မဟုတ် ပိတ်ထားချိန်တွင် compressed aerial background ကို ပြသည်။ **DEFAULT AERIAL** အဖြစ် ခွဲပြထားပြီး live video ဟု မပြပါ။ အင်တာနက် မလိုပါ။
- **Start video / Stop video** ဖြင့် USB camera၊ MJPEG နှင့် GStreamer/HereLink inputs ကို ဖွင့်/ပိတ်နိုင်သည်။ ရွေးထားသော source ကို Start နှိပ်၍ ပြန်ဖွင့်နိုင်သည်။ Stop လုပ်ပြီးနောက် နောက်ကျရောက်လာသော frame များကို မပြတော့ပါ။
- အလယ် marker ကို theme နှင့်ကိုက်သော အဝါရောင် တြိဂံအသေးအဖြစ် ပြောင်းထားသည်။ OSD editor မှ နေရာရွှေ့/ဖျောက်နိုင်သည်။
- MJPEG HTTP read ကို Stop က abort လုပ်ပြီး EOF ဖြစ်လျှင် loop မပတ်တော့ပါ။ GStreamer worker မစခင် Stop နှိပ်သော race ကိုလည်း ပြင်ထားသည်။ Native cleanup ကို background တွင် လုပ်၍ main UI ဆက်နှိပ်နိုင်သည်။ Telemetry connection ကို မပိတ်ပါ။
- HUD finalizer မှ context မရှိဘဲ OpenGL texture ဖျက်ခြင်းကြောင့် Windows ပိတ်ချိန် crash ဖြစ်နိုင်မှုကို ပြင်ထားသည်။ Small screen များတွင် Save/Cancel က taskbar နောက် မရောက်အောင် window size ကို ညှိသည်။

### Pi / server API

- Developer dashboard ရှိ Integrations မှ scoped read-only API token ထုတ်ပြီး Flight Records၊ Profiles၊ Installations၊ Batteries နှင့် private logs ကို Pi/server မှ ဖတ်နိုင်သည်။ Expiry / revoke၊ pagination၊ changes feed နှင့် Python client ပါသည်။

### Update နှင့် စမ်းသပ်မှု

App ကို ပိတ်ပြီး installer ဖြင့် update လုပ်နိုင်သလို **INFO → Check for updates → Install & Restart** မှလည်း update လုပ်နိုင်သည်။ User records၊ profiles နှင့် logs ကို ထိန်းထားသည်။ ဤ release သည် optional update ဖြစ်သည်။

Native Windows build၊ startup၊ FPV/OSD usability၊ Start/Stop နှင့် MJPEG cancellation regression၊ MAVLink protocol နှင့် installer install/uninstall စမ်းသပ်မှု အောင်မြင်သော package ကိုသာ publish လုပ်သည်။ Camera/receiver hardware နှင့် real flight video operation ကို သက်ဆိုင်ရာစက်ပေါ်တွင် စမ်းရန် လိုသည်။ Windows x64 internal pre-release ဖြစ်ပြီး macOS မပါဝင်သေးပါ။
