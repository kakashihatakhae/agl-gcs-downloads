## [0.6.0-internal.28] - 2026-11-06

Windows 10/11 x64 အတွက် internal pre-release ဖြစ်ပါသည်။ ယခင် `0.6.0-internal.25` မှနောက်ပိုင်း Flight Records tab နှင့် Flight history ၏ အသုံးပြုရလွယ်ကူမှု ပြင်ဆင်ချက်များ ပါဝင်ပါသည်။

### Windows installer ရယူရန်

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန် (69.5 MB)](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.28/AGL-Planner-0.6.0-internal.28-Windows-x64-Setup.exe)**

[Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.28/AGL-Planner-0.6.0-internal.28-Windows-x64.zip) · [SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.28/SHA256SUMS.txt) · [မြန်မာအသုံးပြုနည်း](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.28/README-WINDOWS-my.md)

AGL Planner ကို ပိတ်ပြီး Setup.exe ဖြင့် install/update လုပ်ပါ။ ယခင် installer ဖြင့် install လုပ်ထားလျှင် တူညီသော install folder ထဲ update လုပ်နိုင်ပါသည်။ လက်ရှိ user အတွက် install လုပ်ပြီး administrator ခွင့်ပြုချက် မလိုပါ။ GitHub login၊ Git၊ Visual Studio နှင့် .NET SDK မလိုပါ။ .NET Framework 4.7.2+ လိုအပ်ပါသည်။ Install ပြီး INFO တွင် **0.6.0-internal.28** ကို စစ်ပါ။

### Flight history — Record ပြောင်းကြည့်ခြင်းနှင့် Save

- Record တစ်ခုမှ တစ်ခု ပြောင်းကြည့်ရုံဖြင့် Save dialog မပေါ်တော့ပါ။ မူလတန်ဖိုး ပြန်ထားခြင်း၊ တူညီသော ကိန်းဂဏန်းကို format ပြောင်းရေးခြင်း၊ passive telemetry နှင့် theme/layout refresh တို့ကို လူကပြင်သော edit အဖြစ် မမှတ်တော့ပါ။
- တကယ်ပြင်ထားမှ **Save / Discard / Cancel** မေးပါသည်။ Save ပြီး ရွေးထားသော နောက် record ဆီ ဆက်သွားပါသည်။ Cancel၊ validation error နှင့် revision conflict ဖြစ်လျှင် လက်ရှိ record နှင့် ရိုက်ထားသော draft ကို ထိန်းထားပါသည်။
- **Revert changes** ဖြင့် သိမ်းပြီးသား value ကို ပြန်ယူနိုင်ပြီး ပြောင်းလဲမှုမရှိချိန် Save ကို disabled ပြပါသည်။ မသိမ်းနိုင်သောအကြောင်းရင်းကို form ထဲတွင် ပြပါသည်။

### History ရှာခြင်းနှင့် Context actions

- Flight No.၊ vehicle၊ pilot နှင့် Battery ID ဖြင့် ရှာနိုင်ပြီး status အလိုက် filter လုပ်နိုင်ပါသည်။ Result count၊ date/duration၊ empty state နှင့် full reference tooltip ပါဝင်ပါသည်။ Filter ပြောင်းခြင်းက ရိုက်ထားသော draft ကို မပျောက်စေပါ။
- Summary နှင့် ခလုတ်များသည် ရွေးထားသော record အတိုင်း လုပ်ဆောင်ပါသည်။ အခြား record ကြည့်နေချိန် live recording ကို မတော်တဆ end/confirm မလုပ်နိုင်အောင် ကာကွယ်ထားပါသည်။
- အဓိကခလုတ်ကို ညာဘက်အောက်တွင် စုစည်းပြီး square filled/outlined button၊ hover/focus/disabled state နှင့် section underline ကို ညှိထားပါသည်။ **Ctrl+S** Save၊ **Ctrl+F** Search နှင့် **F5** Refresh shortcuts ပါဝင်ပါသည်။
- Flight Records tab မှ Flight logs ကို current/review flight မရှိချိန် နောက်ဆုံးသိမ်းထားသော flight မှ ဖွင့်နိုင်ပါသည်။ ရှည်သော reference စာသားများကို tab width အလိုက် wrap ပြပါသည်။

### ပြင်ခွင့်ရှိသော / မရှိသော Record

- **Planned / Review** record ၏ details ကို ပြင်ပြီး Save လုပ်နိုင်ပါသည်။ **Recording / Finalized / Cancelled** record ကို Flight history တွင် ကြည့်ရုံသာ ရပါသည်။
- Readonly input ထဲ click လုပ်လျှင် cursor မဝင်တော့ဘဲ Tab ဖြင့်လည်း ကျော်သွားပါသည်။ အရင် field ၏ focus ကို record အသစ်တွင် ပြန်မယူတော့ပါ။ Planned / Review ပြန်ရွေးလျှင် editing နှင့် Save ကို ဆက်သုံးနိုင်ပါသည်။
- Readonly **Battery ID** တွင် အပြာရောင် selected highlight ကျန်နေနိုင်သော bug ကို ပြင်ပါသည်။ Record ပြန်ဖွင့်ခြင်း၊ catalog refresh၊ Battery section ပိတ်/ပြန်ဖွင့်ခြင်းနှင့် native control ပြန်တည်ဆောက်ခြင်း နောက်တွင်လည်း ရှင်းပေးပါသည်။
- Battery ID မပြောင်းဘဲ field မှထွက်ချိန် newer catalog specification က အဟောင်း flight ၏ battery values ကို ပြန်ရေးနိုင်ခြင်းကို ပြင်ပါသည်။ Saved ID ရွေးခြင်း၊ manual typing၊ specification autofill နှင့် editable field ၏ user text selection ကို ဆက်သုံးနိုင်ပါသည်။

### Update လုပ်ခြင်း

**INFO → Check for updates → Install & Restart** မှ update လုပ်နိုင်ပါသည်။ Update မလုပ်မီ vehicle ကို disconnect လုပ်ပြီး mission ပြင်ဆင်ချက်များ save လုပ်ထားပါ။ အဟောင်းမှ update မရလျှင် အပေါ်က Setup.exe ကို သုံးပါ။ ယခင် local records၊ profiles နှင့် logs ကို ထိန်းထားပါသည်။ ဤ release သည် **optional update** ဖြစ်ပြီး Force update flag ကို မဖွင့်ထားပါ။

### စမ်းသပ်မှု

- [Native Windows UI / core စမ်းသပ်မှု](https://github.com/kakashihatakhae/agl-gcs-downloads/actions/runs/42178906105) အောင်မြင်ပါသည်။ History navigation၊ Save/Discard/Cancel၊ validation/conflict recovery၊ search/filter၊ readonly mouse/keyboard behavior နှင့် compact layout ကို စစ်ထားပါသည်။
- Recording / Finalized / Cancelled သုံးမျိုးလုံးတွင် Battery ID highlight မကျန်ကြောင်း native Windows screenshots ဖြင့် စစ်ထားပါသည်။ Editable Battery ID selection၊ type/S/P/capacity autofill၊ usage၊ shared profiles နှင့် updater guards များလည်း အောင်မြင်ပါသည်။
- Application files **1,223** ခု၏ Git hashes သည် user အတည်ပြုထားသော preview package နှင့် ကိုက်ညီပါသည်။ Publication workflow က exact installer ကို Windows တွင် install/uninstall လုပ်ပြီး file hashes၊ shortcut/registry နှင့် user-file preservation စစ်ပြီးမှ public assets ထုတ်ပါသည်။

Installer SHA256: `f63032634ac37134ce93d340175bf70025cca5d91428eae6ee2b53a13d0a9936`

Compiled source: `a346389e37b3c1f53face29e8445d7b7941cd347` · Build: `0.6.0-internal.28-a346389e37b3-a3f4d22ee149`
