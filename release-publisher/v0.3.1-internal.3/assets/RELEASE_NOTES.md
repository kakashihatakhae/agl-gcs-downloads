## [0.3.1-internal.3] - 2026-10-22

Windows 10/11 x64 အတွက် internal testing release ဖြစ်ပါသည်။ ယခင် 0.2.7 release မှ လက်ရှိအထိ အတည်ပြုထားသော ပြင်ဆင်ချက်များကို စုစည်းထားပါသည်။

### Windows installer ရယူရန်

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန် (70 MB)](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.3.1-internal.3/AGL-Planner-0.3.1-internal.3-Windows-x64-Setup.exe)**

[Installer နှင့် ZIP SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.3.1-internal.3/SHA256SUMS.txt) · [လက်ရှိ installer ကို GitHub login မလိုဘဲ ရယူရန်](https://agl-planner-services.quiz-checker-usage.workers.dev/downloads/windows-x64)

ဖွင့်ထားသော AGL Planner ကို ပိတ်ပြီး Setup.exe ကို ဖွင့်ကာ install လုပ်ပါ။ ယခင် installer ဖြင့် သွင်းထားသော app ကို update လုပ်နိုင်ပါသည်။ Git၊ Visual Studio နှင့် .NET SDK မလိုပါ။ .NET Framework 4.7.2+ လိုပါသည်။ Source code ZIP သည် application installer မဟုတ်ပါ။ Private GitHub release download အတွက် repo access ရှိသော GitHub account ဖြင့် default browser မှ login ဝင်ထားရပါမည်။

### FLY နှင့် app branding

- Cockpit တွင် **TimeInAir** ကို Ready to Arm အပေါ်၌ အဝါဖျော့နောက်ခံ၊ အမည်းစာသား box ဖြင့် `HH:mm:ss` ပုံစံ ပြထားပါသည်။ Map coordinate selector ၏ default သည် **MGRS** ဖြစ်ပါသည်။
- Action နှင့် Simple Actions ခလုတ်များ၏ normal၊ hover၊ pressed နှင့် disabled အရောင်များကို AGL theme နှင့် ညှိထားပါသည်။ ခလုတ် command များကို မပြောင်းပါ။
- Toolbar ရှိ AGL logo အရှည်ကို နှိပ်လျှင် default browser မှ [AGL logo webpage](https://agl-planner-services.quiz-checker-usage.workers.dev/agl) ကို ဖွင့်ပါသည်။ Logo အရှည်ကို စာသားအပြည့်အစုံနှင့် aspect ratio မှန်စွာ ပြထားပါသည်။

### Update နှင့် developer dashboard

- Private source repo အတွက် updater 404 ပြဿနာကို ဖြေရှင်းရန် Cloudflare Worker နှင့် public binary-only downloads repo ကို သုံးထားပါသည်။ **INFO → Update AGL Planner** မှ update လုပ်နိုင်ပြီး R2 မလိုပါ။ Developer credentials သည် app/installer ထဲ မပါပါ။
- Password ဖြင့် ဝင်ရသော [Developer dashboard](https://agl-planner-services.quiz-checker-usage.workers.dev/admin) တွင် report ပို့ထားသော installation များ၊ version၊ Windows/CPU/RAM/GPU၊ report အချိန်၊ search နှင့် pagination ကို ကြည့်နိုင်ပါသည်။
- Windows app ဖွင့်ပြီး background မှ basic device report ပို့ပါသည်။ App/Windows version၊ CPU/architecture/count၊ RAM၊ GPU နှင့် random installation ID ကိုသာ ပါဝင်စေပြီး username၊ hostname၊ hardware serial၊ GPS နှင့် flight logs မပါပါ။ INFO မှ automatic reporting ကို ပိတ်နိုင်ပါသည်။ Offline queue နှင့် retry ပါဝင်ပါသည်။
- **Windows reporting startup bug ကို ပြင်ထားပါသည်။** မဖြစ်လာသော `Shown` event ကို စောင့်မနေတော့ဘဲ main window ready ဖြစ်ချိန်မှ worker ကို စပါသည်။ INFO တွင် status သီးသန့်နှင့် **Copy reporting status** ပါဝင်ပြီး startup၊ collection၊ error နှင့် retry အခြေအနေကို မြင်နိုင်ပါသည်။

### စမ်းသပ်မှု

- အသုံးပြုသူက `0.3.1-internal.3` ကို Windows တွင် update လုပ်စမ်းပြီး reporting ပြဿနာ အဆင်ပြေပြီဟု အတည်ပြုထားပါသည်။
- Cloud desktop build၊ GUI/startup regression checks၊ .NET reporting/updater checks၊ backend ingestion/dashboard tests နှင့် live service round trip ကို စစ်ထားပါသည်။ Logo webpage ကို desktop/mobile နှစ်မျိုး စစ်ထားပါသည်။
- Installer နှင့် ZIP ၏ sizes/SHA256၊ installer archive နှင့် NSIS CRC ကို စစ်ထားပါသည်။ ဤ release သည် user စမ်းပြီးသော installer နှင့် application bytes တူညီပါသည်။
- GitHub Actions Windows runner သည် account payment/spending-limit ကြောင့် job မစနိုင်ခဲ့ပါ။ Automated native Windows install/uninstall၊ WMI နှင့် UI/DPI test အားလုံး pass ဟု မသတ်မှတ်ပါ။ Installer သည် unsigned ဖြစ်ပြီး macOS installer မပါဝင်ပါ။

Installer SHA256: `f4a40976ea80d2517b886e3a92bf4fdabc04fe9d5e1a495c96a4fe8e0f143427`

Compiled source: `93bf38f602402212cda1ffe84f025d4c9bf8c860` · Build: `0.3.1-internal.3-93bf38f60240-64e17a7120c3`

Source release: https://github.com/kakashihatakhae/agl-gcs/releases/tag/v0.3.1-internal.3 · `release` branch
