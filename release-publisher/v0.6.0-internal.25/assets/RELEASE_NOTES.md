## [0.6.0-internal.25] - 2026-11-05

Windows 10/11 x64 အတွက် internal pre-release ဖြစ်ပါသည်။ ယခင် `0.6.0-internal.21` မှနောက်ပိုင်း Battery library၊ across-device Vehicle Profiles၊ unique Flight No. နှင့် developer-controlled update ပြင်ဆင်ချက်များ ပါဝင်ပါသည်။

### Windows installer ရယူရန်

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန် (69.5 MB)](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.25/AGL-Planner-0.6.0-internal.25-Windows-x64-Setup.exe)**

[Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.25/AGL-Planner-0.6.0-internal.25-Windows-x64.zip) · [SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.25/SHA256SUMS.txt) · [မြန်မာအသုံးပြုနည်း](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.25/README-WINDOWS-my.md)

App အဟောင်းကို ပိတ်ပြီး Setup.exe ဖြင့် install/update လုပ်ပါ။ GitHub login၊ Git၊ Visual Studio နှင့် .NET SDK မလိုပါ။ .NET Framework 4.7.2+ လိုအပ်ပါသည်။ လက်ရှိ Windows user အတွက် install လုပ်ပြီး administrator ခွင့်ပြုချက် မလိုပါ။ Install ပြီး INFO တွင် **0.6.0-internal.25** ဖြစ်ကြောင်း စစ်ပါ။

### Battery ID နှင့် Battery library

- **Prepare / View record** နှင့် **Flight history → Battery & Power** တွင် Battery ID ကို ရိုက်ထည့်နိုင်သလို သိမ်းထားသော physical pack ID များထဲက ရွေးနိုင်ပါသည်။ ရွေးထားသော pack ၏ Type၊ series cells **S**၊ parallel count **P** နှင့် capacity ကို ပြန်ဖြည့်ပေးသည်။ ယခင် flight voltage/percentage ကို မကူးပါ။
- **Parallel count (P)** field အသစ်ကို Windows form၊ local/cloud records၊ CSV၊ dashboard detail နှင့် correction editor တွင် ထည့်ထားပါသည်။ မသိသော P ကို blank ထားနိုင်ပြီး ထည့်ပါက positive whole number ဖြစ်ရပါသည်။
- Battery ID ထည့်ပြီး **Check usage** နှိပ်၍ အသုံးပြုပြီးသော flight အရေအတွက်ကို စစ်နိုင်ပါသည်။ **7–8 ကြိမ် Warning**၊ **9 နှင့်အထက် Critical** ဖြစ်သည်။ Online တွင် synced devices နှင့် local records ကို ထပ်မရေတွက်ဘဲ ပေါင်းစစ်ပြီး offline တွင် **This computer only** ဟု ပြပါသည်။ Plans၊ cancelled၊ deleted နှင့် confirmation-pending records များကို completed use အဖြစ် မတွက်ပါ။
- Developer နှင့် production dashboard နှစ်ခုလုံးတွင် **Batteries** page ပါဝင်ပါသည်။ Battery ID/usage level ဖြင့် စစ်ထုတ်ခြင်း၊ S/P/capacity၊ last updated၊ linked flight history၊ voltage source နှင့် သက်ဆိုင်ရာ record ကို တိုက်ရိုက်ဖွင့်ခြင်း ပါဝင်ပါသည်။
- Online မှ Battery ID/specifications များကို cache သိမ်း၍ offline တွင် ပြန်ရွေးနိုင်သည်။ Dropdown အတွက် operator၊ location၊ log files နှင့် voltage history ကို မယူပါ။ Background catalog refresh က ရိုက်နေသောစာနှင့် popup selection ကို မရေးကျော်ပါ။ Native Windows editable dropdown event အစီအစဉ်ကြောင့် specifications မပြန်ဖြည့်နိုင်သော bug ကို ပြင်ထားပါသည်။

### Vehicle Profiles နှင့် Flight Records

- စက်အားလုံးက sync ပို့ထားသော Vehicle Profiles ကို **SETUP → Vehicle Profile** နှင့် **Flight history → Vehicle profile** တွင် ပြန်ရွေးသုံးနိုင်ပါသည်။ Offline cache၊ source installation reference နှင့် concurrent-edit protection ပါဝင်ပါသည်။
- လက်ရှိ FC UID နှင့် profile တစ်ခုတည်းကိုက်ပါက Flight Record တွင် အလိုအလျောက် ချိတ်ပြီး captured profile values များကို ထိန်းထားပါသည်။ Production dashboard တွင် အခြားစက်မှ shared profile နှင့် flight record ဆက်စပ်မှုကိုလည်း မှန်ကန်စွာ ပြပါသည်။
- အသစ်ဖန်တီးသော automatic Flight No. တွင် record GUID ၏ bit အပြည့်ကို အသုံးပြု၍ စက်များအကြား reference တူနိုင်မှုကို လျှော့ချထားပါသည်။ ရှိပြီးသား Flight No.၊ records နှင့် logs ဆက်စပ်မှုကို ထိန်းထားပါသည်။

### Update လုပ်ခြင်း

- **INFO → Check for updates → Install & Restart** ဖြင့် update လုပ်နိုင်ပါသည်။ Vehicle ကို disconnect လုပ်ပြီး ပြင်ထားသော mission များကို save လုပ်ထားပါ။ အဟောင်းမှ update မရလျှင် Setup.exe ကို သုံးပါ။
- Developer dashboard → **Release channel** တွင် published Windows build တစ်ခုအတွက် **Force update** နှင့် message သတ်မှတ်နိုင်ပါသည်။ ဤ release ကို ပုံမှန် optional update အဖြစ် ထုတ်ထားပြီး force flag ကို မဖွင့်ထားပါ။
- Required update ကို client က idle startup တွင်သာ download/verify/install လုပ်သည်။ Vehicle ချိတ်ထားခြင်း၊ recording/recovery သို့မဟုတ် user လုပ်ဆောင်နေခြင်းရှိလျှင် နောက် launch သို့ ရွှေ့သည်။ Offline/download failure ဖြစ်လျှင် လက်ရှိ app ကို ဆက်သုံးနိုင်သည်။ Required-update bootstrap မပါသော version အဟောင်းများသည် ပုံမှန် update ကို တစ်ကြိမ်လုပ်ရန် လိုပါသည်။

### စမ်းသပ်မှုနှင့် အတိုင်းအတာ

- [Native Windows UI နှင့် core စမ်းသပ်မှု](https://github.com/kakashihatakhae/agl-gcs-downloads/actions/runs/42013658257) အောင်မြင်ပါသည်။ Battery ID ကို mouse ဖြင့် ရွေးခြင်း၊ Type/S/P/capacity ပြန်ဖြည့်ခြင်း၊ current-flight readings ထိန်းခြင်း၊ save/history၊ shared profiles၊ usage boundaries နှင့် updater guards ကို စစ်ထားပါသည်။
- Web API tests **41 ခု**၊ developer/production browser workflow checks၊ mobile-width layout၊ retry၊ authentication နှင့် live synthetic-fixture checks အောင်မြင်ပါသည်။ Preview မှ application files **1,223** ခု၏ Git hashes သည် ဤ package နှင့် ကိုက်ညီပါသည်။
- Publication workflow သည် native Windows တွင် installer install/uninstall၊ installed file hashes၊ shortcut/registry နှင့် user-file preservation ကို စစ်ပြီးမှ public assets ထုတ်ပါသည်။
- Battery usage count သည် charge cycle သို့မဟုတ် measured battery health မဟုတ်ပါ။ အခြားစက်၏ မပို့ရသေးသော offline records ကို sync ပြီးမှ မြင်နိုင်ပါသည်။ Physical FC/USB နှင့် field-flight အခြေအနေအားလုံးကို စမ်းပြီးဟု မသတ်မှတ်ပါ။

Installer SHA256: `37a1cc1d68a9f822b821c5a90dbebb97a992f5f661cb69fbabe96250a2d30dd1`

Compiled source: `6b634354d7dade1fb0ee564dd5ad2c6165f44271` · Build: `0.6.0-internal.25-6b634354d7da-6ba122cc4690`
