## [0.8.0-internal.6] - 2026-11-16

### Windows installer ရယူရန်

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.6/AGL-Planner-0.8.0-internal.6-Windows-x64-Setup.exe)**

[SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.6/SHA256SUMS.txt) · [မြန်မာအသုံးပြုနည်း](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.6/README-WINDOWS-my.md)

- Update စစ်ခြင်းကို graphics / native initialization မတိုင်မီ ရွှေ့၍ update လုပ်ချိန် မလိုအပ်သော native thread များ မစတော့ပါ။
- Auto Update အပြီး app window ပိတ်သော်လည်း နောက်ခံ process ကျန်ပြီး updater က စောင့်နေသည့် startup handoff ကို ပြင်ထားသည်။ Installer က ဖိုင်များစစ်ပြီး အသင့်ဖြစ်ကြောင်း အတည်ပြုမှ app က ထွက်သည်။ မူလ startup process ကိုယ်တိုင်သာ အဆုံးသတ်ပြီး အခြား app process များကို အတင်းမပိတ်ပါ။
- Installation folder တစ်ခုစီအတွက် application / updater reservation ထည့်၍ update လုပ်နေစဉ် သို့မဟုတ် app ဖွင့်ထားစဉ် ထပ်ဖွင့်ရာမှ မမြင်ရသော process များ မပွားစေတော့ပါ။ Folder မတူသော installation ကို ဆက်သုံးနိုင်သည်။
- Download စစ်ပြီးသော updater အသစ် ရှိလျှင် ၎င်းကို bootstrap အဖြစ် သုံးသည်။ Parent exit စောင့်ခြင်းကို bounded လုပ်ပြီး install / restart အခြေအနေကို staging folder ၏ `update-runner.log` တွင် မှတ်တမ်းတင်သည်။
- Delta download၊ SHA256 / build pin၊ settings / personal files ထိန်းသိမ်းခြင်း၊ rollback နှင့် live connection / recording guard ကို ဆက်ထိန်းသည်။
- Windows တွင် parent process၊ ကူးထားသော updater နှင့် ပြန်ဖွင့်သော EXE အစစ်များဖြင့် end-to-end စမ်းသပ်သည်။ Foreground thread ကျန်နေခြင်း၊ duplicate startup၊ သီးခြား installation၊ verified file replacement၊ settings ထိန်းသိမ်းမှုနှင့် restart working directory ပါဝင်သည်။

**0.8.0-internal.5 နှင့် အဟောင်းမှ ရွှေ့ရန်** — updater အဟောင်းသည် ကိုယ်တိုင် ပိတ်မထွက်နိုင်သော ပြဿနာ ရှိနိုင်သဖြင့် ဒီတစ်ကြိမ် app / updater process များကို ပိတ်ပြီး Setup.exe အသစ်ဖြင့် update လုပ်ပါ။ နောက် update များတွင် handoff ပြင်ဆင်ချက်ကို သုံးမည်။
