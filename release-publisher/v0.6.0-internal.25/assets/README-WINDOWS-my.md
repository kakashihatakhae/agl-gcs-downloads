# AGL Planner 0.6.0-internal.25 — Windows အသုံးပြုနည်း

## Download / install / update

[Setup.exe](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.25/AGL-Planner-0.6.0-internal.25-Windows-x64-Setup.exe) · [Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.25/AGL-Planner-0.6.0-internal.25-Windows-x64.zip) · [SHA256](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.25/SHA256SUMS.txt)

Windows 10/11 x64 နှင့် .NET Framework 4.7.2+ လိုအပ်ပါသည်။ GitHub login၊ Git နှင့် build tools မလိုပါ။

1. ဖွင့်ထားသော AGL Planner ကို ပိတ်ပါ။
2. Setup.exe ကို ဖွင့်ပြီး Install ကိုနှိပ်ပါ။ ယခင် installer ဖြင့် သွင်းထားလျှင် တူညီသော install folder ထဲ update လုပ်နိုင်ပါသည်။
3. Desktop / Start Menu မှ AGL Planner ကို ဖွင့်ပြီး INFO တွင် **0.6.0-internal.25** ကို စစ်ပါ။

Installer သည် လက်ရှိ user ၏ LocalAppData/Programs/AGL Planner တွင် install လုပ်သည်။ Existing local records၊ profiles နှင့် logs ကို ထိန်းထားသည်။ Git preview shortcut သည် folder သီးခြားကို ညွှန်းနိုင်သဖြင့် installer ဖြင့် သွင်းပြီး shortcut target သည် install folder ဖြစ်ကြောင်း စစ်ပါ။

## Flight record နှင့် Battery

- FLY အပေါ် bar မှ Prepare record / Continue setup ဖြင့် pilot၊ Battery ID၊ weather နှင့် AUW ကို စစ်ဖြည့်ပါ။ ရနိုင်သော telemetry values ကို အလိုအလျောက် ဖြည့်သည်။
- Battery ID ကို အသစ်ရိုက်ထည့်နိုင်သလို saved ID ကို ရွေး၍ Type၊ S/P နှင့် capacity ကို ပြန်ဖြည့်နိုင်သည်။ Physical pack တစ်လုံးအတွက် ID တစ်ခုတည်းကို စက်အားလုံးတွင် သုံးပါ။
- Check usage တွင် completed flights 7–8 ကြိမ် Warning၊ 9 နှင့်အထက် Critical ပြသည်။ Counts သည် measured health/charge cycle မဟုတ်ပါ။
- ပျံပြီး Complete Previous Record မှ လူဖြည့်ရန်ကျန်သောအချက်များကို ဖြည့်ပါ။ FLY → Flight Records မှ history နှင့် logs ကို ပြန်ကြည့်နိုင်သည်။
- `.tlog` သည် telemetry coverage နှင့် `.bin` သည် FC မှ ရရှိ/ကိုက်ညီမှုအပေါ် မူတည်သည်။ မရသေးသောဖိုင်ကို status တွင် ပြထားသည်။

## Shared profiles နှင့် dashboards

SETUP → Vehicle Profile မှ profile ရွေးနိုင်ပြီး Sync now ဖြင့် စက်အားလုံးက ပို့ထားသော profiles ကို ပြန်ယူနိုင်သည်။ Offline တွင် cache ကို ဆက်သုံးနိုင်သည်။ လက်ရှိ FC UID နှင့် unique profile ကိုက်ပါက Flight Record တွင် အလိုအလျောက် ချိတ်ပေးသည်။

[Developer dashboard](https://agl-developer.pages.dev/admin) · [Production dashboard](https://agl-dashboard.pages.dev)

Login ဝင်၍ Vehicle Profiles၊ Flight Records နှင့် Batteries ကို ကြည့်နိုင်သည်။ Flight record detail မှ history၊ corrections နှင့် private flight logs ကို ကြည့်/download လုပ်နိုင်သည်။

## နောက်တစ်ကြိမ် update

Vehicle ကို disconnect လုပ်ပြီး mission ပြင်ဆင်ချက်များ save လုပ်ပါ။ INFO → Check for updates ကို သုံးပါ။ [လက်ရှိ installer အမြဲရယူရန်](https://agl-planner-services.quiz-checker-usage.workers.dev/downloads/windows-x64)။

## Build / verification

Version: `0.6.0-internal.25` · Build: `0.6.0-internal.25-6b634354d7da-6ba122cc4690`

Compiled source: `6b634354d7dade1fb0ee564dd5ad2c6165f44271`

Installer SHA256: `37a1cc1d68a9f822b821c5a90dbebb97a992f5f661cb69fbabe96250a2d30dd1`

Native Windows UI: https://github.com/kakashihatakhae/agl-gcs-downloads/actions/runs/42013658257
