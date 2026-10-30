# agl-gcs-downloads
for public releases

<!-- agl-downloads:start -->
## Windows installer

[AGL Planner Setup.exe ကို download လုပ်ရန်](https://agl-planner-services.quiz-checker-usage.workers.dev/downloads/windows-x64)

Download ပြီး Setup.exe ကို ဖွင့်၍ install လုပ်ပါ။ App အဟောင်းမှ service updater ပါသော build အသစ်သို့ တစ်ကြိမ် ပြောင်းရန် လိုပါသည်။

Installer SHA256: `f286e457f7dcd84ce58cd2d4d0829da2a97e6276c6d2475192fd85fdbaa75a24`

ဤ repo တွင် compiled Windows update files နှင့် installer parts သာ ပါဝင်ပါသည်။ Source repo သည် private အဖြစ် ဆက်ရှိပါသည်။
<!-- agl-downloads:end -->

## Versioned release downloads

[AGL Planner v0.3.1-internal.3 — Windows installer နှင့် portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/tag/v0.3.1-internal.3)

Release Assets ထဲမှ Setup.exe ကို download လုပ်၍ install လုပ်နိုင်ပါသည်။ SHA256SUMS.txt နှင့် မြန်မာ release notes ပါဝင်ပါသည်။ Source release သည် private `agl-gcs` repo ၏ `release` branch တွင် ရှိပါသည်။ ဤ repo သည် compiled downloads နှင့် download publication workflow အတွက် ဖြစ်ပါသည်။

## Native macOS Apple Silicon preview

[AGL Planner 0.4.0-internal.2.mac.1 — macOS ARM64 DMG ကို download လုပ်ရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/raw/refs/heads/main/installers/macos-native/0.4.0-internal.2.mac.1/AGL-Planner-0.4.0-internal.2.mac.1-macOS-arm64.dmg)

macOS 14+ Apple Silicon အတွက် development preview ဖြစ်ပြီး Windows release နှင့် feature အပြည့် မတူသေးပါ။ Wine/Rosetta မလိုပါ။ DMG ကိုဖွင့်၍ app ကို Applications ထဲ ဆွဲထည့်ပါ။ Ad-hoc signed ဖြစ်ပြီး notarization မရှိသေးပါ။

[အသုံးပြုနည်းနှင့် မပါသေးသော features](installers/macos-native/0.4.0-internal.2.mac.1/README-my.md) · [SHA256](installers/macos-native/0.4.0-internal.2.mac.1/AGL-Planner-0.4.0-internal.2.mac.1-macOS-arm64.dmg.sha256) · [Build/test မှတ်တမ်း](installers/macos-native/0.4.0-internal.2.mac.1/BUILD-INFO.json)
