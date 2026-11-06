# AGL Planner 0.6.0-internal.28 — Windows အသုံးပြုနည်း

[Setup.exe](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.28/AGL-Planner-0.6.0-internal.28-Windows-x64-Setup.exe) · [Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.28/AGL-Planner-0.6.0-internal.28-Windows-x64.zip) · [Release notes](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.28/RELEASE_NOTES.md) · [SHA256](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.28/SHA256SUMS.txt)

## Install / Update

Windows 10/11 x64 နှင့် .NET Framework 4.7.2+ လိုအပ်ပါသည်။ GitHub login၊ Git နှင့် build tools မလိုပါ။

1. ဖွင့်ထားသော AGL Planner ကို ပိတ်ပါ။
2. Setup.exe ကို ဖွင့်ပြီး Install ကိုနှိပ်ပါ။ ယခင် installer ဖြင့် install လုပ်ထားလျှင် တူညီသော install folder ထဲ update လုပ်နိုင်ပါသည်။
3. Desktop / Start Menu မှ AGL Planner ကို ဖွင့်ပြီး INFO တွင် **0.6.0-internal.28** ကို စစ်ပါ။

လက်ရှိ user ၏ `%LOCALAPPDATA%/Programs/AGL Planner` တွင် install လုပ်သည်။ Existing local records၊ profiles နှင့် logs ကို ထိန်းထားသည်။ Git preview shortcut သည် folder သီးခြားကို ညွှန်းနိုင်သဖြင့် installer မှ သွင်းထားသော AGL Planner shortcut ကို အသုံးပြုပါ။

## Flight Records / Flight history

FLY အပေါ် bar မှ Prepare record / Continue setup ဖြင့် pilot၊ Battery ID၊ weather နှင့် AUW ကို စစ်ဖြည့်ပါ။ ရနိုင်သော telemetry ကို အလိုအလျောက် ဖြည့်ပါသည်။ ပျံပြီး Complete Previous Record မှ ကျန်သောအချက်များကို ဖြည့်ပါ။

**FLY → Flight Records → Flight history** တွင် သိမ်းထားသော record များ ပြန်ကြည့်နိုင်ပါသည်။

- Search တွင် Flight No.၊ vehicle၊ pilot သို့မဟုတ် Battery ID ရိုက်ရှာပါ။ Status filter ဖြင့် Plans၊ Recording၊ Needs review၊ Finalized နှင့် Cancelled ကို ရွေးနိုင်သည်။
- Planned / Review details ကို ပြင်ပြီး Save နိုင်သည်။ Recording / Finalized / Cancelled details သည် readonly ဖြစ်ပြီး input cursor / blue selection highlight မပြပါ။
- Record ပြောင်းချိန် တကယ်ပြင်ထားမှ Save / Discard / Cancel မေးသည်။ Revert changes ဖြင့် နောက်ဆုံးသိမ်းထားသော values ကို ပြန်ယူနိုင်သည်။
- Ctrl+S Save၊ Ctrl+F Search၊ F5 Refresh ကို သုံးနိုင်သည်။ ရှာဖွေ/filter လုပ်နေချိန် ရွေးထားသော record နှင့် draft ကို ဆက်ထိန်းထားသည်။
- Flight logs မှ သက်ဆိုင်ရာ `.tlog` / `.bin` ရရှိမှု၊ status နှင့် files ကို ကြည့်နိုင်သည်။

Battery ID ကို အသစ်ရိုက်ထည့်နိုင်သလို saved ID ကို ရွေး၍ type၊ series **S**၊ parallel **P** နှင့် capacity ကို ပြန်ဖြည့်နိုင်သည်။ Physical pack တစ်လုံးအတွက် တူညီသော ID ကို သုံးပါ။ Check usage တွင် completed flights 7–8 ကြိမ် Warning၊ 9 နှင့်အထက် Critical ပြသည်။

## Profiles / Dashboards

SETUP → Vehicle Profile မှ profile ရွေးနိုင်ပြီး Sync now ဖြင့် shared profiles ကို ပြန်ယူနိုင်သည်။ Offline တွင် cache ကို ဆက်သုံးနိုင်သည်။ လက်ရှိ FC UID နှင့် profile တစ်ခုတည်း ကိုက်ပါက Flight Record နှင့် အလိုအလျောက် ချိတ်ပေးသည်။

[Developer dashboard](https://agl-developer.pages.dev/admin) · [Production dashboard](https://agl-dashboard.pages.dev)

## နောက်တစ်ကြိမ် update

Vehicle ကို disconnect လုပ်ပြီး mission ပြင်ဆင်ချက်များ save လုပ်ပါ။ INFO → Check for updates ကို သုံးပါ။ [လက်ရှိ installer အမြဲရယူရန်](https://agl-planner-services.quiz-checker-usage.workers.dev/downloads/windows-x64)။

Version: `0.6.0-internal.28` · Build: `0.6.0-internal.28-a346389e37b3-a3f4d22ee149`

Compiled source: `a346389e37b3c1f53face29e8445d7b7941cd347`

Installer SHA256: `f63032634ac37134ce93d340175bf70025cca5d91428eae6ee2b53a13d0a9936`

Native Windows UI: https://github.com/kakashihatakhae/agl-gcs-downloads/actions/runs/42178906105
