# AGL Planner 0.6.0-internal.21 — Windows အသုံးပြုနည်း

## Download / install / update

[Setup.exe ရယူရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.21/AGL-Planner-0.6.0-internal.21-Windows-x64-Setup.exe) · [Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.21/AGL-Planner-0.6.0-internal.21-Windows-x64.zip) · [SHA256](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.21/SHA256SUMS.txt)

Windows 10/11 x64 နှင့် .NET Framework 4.7.2+ လိုအပ်ပါသည်။ GitHub login၊ Git နှင့် build tools မလိုပါ။

1. ဖွင့်ထားသော AGL Planner ကို ပိတ်ပါ။
2. Setup.exe ကို ဖွင့်ပြီး Install ကိုနှိပ်ပါ။ ယခင် installer ဖြင့် သွင်းထားလျှင် တူညီသော install folder ထဲ update လုပ်နိုင်ပါသည်။
3. Desktop / Start Menu မှ AGL Planner ကို ဖွင့်ပါ။ INFO တွင် `0.6.0-internal.21` ဖြစ်ကြောင်း စစ်ပါ။

Install folder သည် `%LOCALAPPDATA%\Programs\AGL Planner` ဖြစ်ပါသည်။ Administrator ခွင့်ပြုချက် မလိုပါ။ Windows Settings → Apps မှ uninstall လုပ်နိုင်ပြီး user-created files ကို ထိန်းထားပါသည်။ Internal installer သည် code signing မရှိသေးပါ။ Windows warning ပေါ်လျှင် filename နှင့် SHA256 ကို စစ်ပါ။

Installer integrity error ပေါ်လျှင် ဖိုင်အဟောင်းကို ဖယ်ပြီး download ပြန်ယူပါ။ SHA256 မကိုက်သောဖိုင်ကို မသုံးပါနှင့်။

## PLAN — Terrain Profile

မြေပုံအောက်ပိုင်းရှိ glass panel ကို ခေါက်/ဖြန့်နိုင်သည်။ ရွှေဝါမျဉ်းက planned altitude၊ မီးခိုးရောင်က terrain၊ အနီရောင်က terrain အောက်ရောက်သောအပိုင်း ဖြစ်ပါသည်။ Hover ဖြင့် distance/terrain/plan/clearance ကြည့်ပြီး click ဖြင့် မြေပုံပေါ်က အဲဒီနေရာသို့ သွားနိုင်သည်။ R / refresh icon ဖြင့် data ကို ပြန်စစ်နိုင်သည်။

Home/waypoint ပြင်ခြင်း၊ mission ဖွင့်/ဖျက်ခြင်းနောက် profile ကို အလိုအလျောက် ပြန်တွက်သည်။ Cached SRTM/GeoTIFF/DTED data ရှိလျှင် offline ကြည့်နိုင်သည်။ Data မရသောနေရာကို 0 m ဟု မယူဘဲ unknown gap ပြထားသည်။ Relative altitude သည် PLAN Home AMSL ကို သုံးပြီး Global/Terrain frame ကို သီးခြားခွဲတွက်သည်။

DEM resolution နှင့် sampling ကြောင့် peak/obstacle အားလုံးကို မသိနိုင်ပါ။ Graph သည် planning estimate ဖြစ်ပြီး flight clearance အတည်ပြုချက် မဟုတ်ပါ။

## Vehicle Profile နှင့် Flight Record

SETUP sidebar → Vehicle Profile တွင် vehicle name/type၊ Plane Pusher/Tractor၊ controller ID နှင့် firmware ကို သိမ်းနိုင်သည်။ Controller UID match ရှိလျှင် FLY record ကို အဲဒီ profile နှင့် ချိတ်၍ အချက်အလက်များကို ဖြည့်ပေးသည်။

- မပျံခင် FLY အပေါ်ဘက် **Prepare next flight / Continue setup** မှ လိုအပ်သည့်အချက်များ ဖြည့်ပါ။ Telemetry ရနိုင်သောအချက်များကို အလိုအလျောက် ဖြည့်သည်။
- Pilot၊ Battery ID၊ weather နှင့် AUW တို့ကို စစ်ပါ။ Battery ID သည် physical pack တစ်လုံးချင်းကို သတ်မှတ်ရန် ဖြစ်သည်။
- Flight recording အတွင်း telemetry/logs ကို သိမ်းပေးသည်။ ပျံပြီးနောက် **Complete Previous Record** မှ လူဖြည့်ရန်ကျန်သောအချက်များကို ဖြည့်ပြီး complete လုပ်ပါ။ Flight No. ဖြင့် record ကို ပြန်သိနိုင်သည်။
- FLY → **Flight Records** တွင် history နှင့် Flight logs ကို ပြန်ကြည့်နိုင်သည်။ `.tlog` သည် telemetry coverage ပေါ်မူတည်ပြီး `.bin` သည် FC တွင် ရနိုင်/မရနိုင်မှုနှင့် matching ပေါ်မူတည်သည်။ မရသေးသော file ကို status တွင် ပြထားသည်။

Local record များကို offline သိမ်းနိုင်သည်။ Internet ရချိန် profile metadata၊ record နှင့် သက်ဆိုင်ရာ logs များကို cloud သို့ sync လုပ်သည်။ Authorized dashboard account ဖြင့် record detail၊ update history နှင့် private log downloads ကို ကြည့်နိုင်သည်။

## နောက်တစ်ကြိမ် update

Vehicle ကို disconnect လုပ်ပြီး mission ပြင်ဆင်ချက်များကို save လုပ်ပါ။ INFO → Check for updates ကို သုံးပါ။ Update မရလျှင် လက်ရှိ installer ကို [ဒီလင့်ခ်](https://agl-planner-services.quiz-checker-usage.workers.dev/downloads/windows-x64) မှ ရယူနိုင်သည်။

## Build / verification

Version: `0.6.0-internal.21` · Build: `0.6.0-internal.21-1ad700a9a423-e1152422a106`

Compiled source: `1ad700a9a423278685c2b742ce32bcf5b5366b3e`

Installer SHA256: `4a63ea3d4bf46291843a80f8abe46cba5ac90a5666f82fda43d0bc6c1d97e266`

Native UI test: https://github.com/kakashihatakhae/agl-gcs-downloads/actions/runs/41638630438

ဤ publication သည် Windows x64 internal pre-release ဖြစ်သည်။ macOS native development ကို ခဏရပ်ထားဆဲဖြစ်သည်။
