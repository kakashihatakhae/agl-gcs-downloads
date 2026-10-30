# AGL Planner — Native macOS ARM64 development preview

Windows release **0.4.0-internal.2** ကနေ ခွဲထားသော native macOS port ဖြစ်ပါသည်။ Product version က `0.4.0-internal.2.mac.1` ဖြစ်ပြီး Windows release နှင့် feature အပြည့် မတူသေးပါ။ Windows release နှင့် updater ကို မပြောင်းပါ။

## စက်နှင့် runtime

- Apple Silicon ARM64၊ macOS 14 သို့မဟုတ် အထက်ကို target ထားသည်။ M1–M6 မျိုးဆက်အတွက် architecture target တူသော်လည်း model/OS အားလုံးတွင် စမ်းပြီးကြောင်း မဆိုလိုပါ။ စမ်းသပ်ထားသော OS/architecture ကို build artifact ၏ `results/environment.txt` တွင် ကြည့်ပါ။
- ARM64 app host၊ ARM64 .NET runtime နှင့် native libraries ပါဝင်ပါသည်။ Rosetta၊ Wine၊ Windows၊ သီးသန့် .NET install မလိုပါ။
- AppKit window ကို Avalonia 12 ဖြင့် ဖန်တီးပြီး UI/HUD/map ကို native Skia ဖြင့် ဆွဲပါသည်။ Windows WinForms project နှင့် discontinued Xamarin.Mac project ကို မသုံးပါ။

## Install နှင့် စမ်းသပ်နည်း

DMG ကိုဖွင့်၍ **AGL Planner.app** ကို **Applications** ထဲ ဆွဲထည့်ပါ။ ဤ development build သည် ad-hoc signed ဖြစ်ပြီး Developer ID notarization မရှိသေးပါ။ macOS က မအတည်ပြုနိုင်ကြောင်း ပြလျှင် System Settings → Privacy & Security မှ ယခု app အတွက် **Open Anyway** ကို သုံးနိုင်ပါသည်။ System တစ်ခုလုံး၏ Gatekeeper ကို ပိတ်ရန် မလိုပါ။

ပထမဆုံး existing SITL/simulator နှင့် စမ်းပါ။ လက်ရှိ preview တွင် flight command/arming control မပါဝင်ပါ။

- **UDP listen:** `14550` ကိုရွေး၊ CONNECT နှိပ်ပြီး simulator/vehicle က Mac ရဲ့ IP:14550 ဆီ MAVLink ပို့ပါ။ ပထမဆုံး valid autopilot heartbeat ရဲ့ vehicle/component ကို lock လုပ်ပါသည်။ အခြား UDP peer/vehicle data ကို မရောပါ။
- **TCP:** `127.0.0.1`၊ `5760` နှင့် CONNECT ဖြင့် existing local SITL ကို ချိတ်နိုင်ပါသည်။ Simulator ကို app က download/start မလုပ်ပါ။
- **Serial:** SETUP မှ Refresh serial devices နှိပ်၍ `/dev/cu.*` device ကို header တွင် ထည့်ပါ။ Port field တွင် baud rate (ဥပမာ `115200`) ထည့်ပါ။ USB adapter အချို့သည် vendor driver လိုနိုင်သည်။
- **FLY:** HUD၊ telemetry 4×3 grid၊ freshness status၊ map၊ message history နှင့် telemetry preflight checks ပါဝင်ပါသည်။ Data မရသေးလျှင် `—`၊ stale ဖြစ်လျှင် value မှိန်ပြပါသည်။ Disarmed state ကို Ready to Arm အဖြစ် မသတ်မှတ်ပါ။
- **PLAN:** Vehicle mission download၊ map ပေါ် local waypoint ဆွဲခြင်း၊ QGC WPL 110 import/export၊ local clear-all confirmation ပါဝင်ပါသည်။ ပထမ map click သည် HOME row 0 ဖြစ်သည်။ Vehicle mission upload မပါသေးပါ။ Unsupported local coordinate frames ကို import/export မှာ ပယ်ချသည်။ Vehicle read တွင် မူရင်း command/parameter/frame ကို ထိန်းထားသည်။
- **CONFIG:** Parameter download၊ filter နှင့် ArduPilot parameter write ပါဝင်ပါသည်။ ရွေးထားသော parameter အမည်၊ မူလ value၊ အသစ်နှင့် vehicle ID ကို confirmation တွင် ပြသည်။ Vehicle က value ပြန်အတည်ပြုမှ success ပြသည်။ Unsupported parameter types ကို မပို့ပါ။

## မပါသေးသော Windows workflows

Mission upload၊ firmware flash၊ radio/sensor calibration၊ video၊ log analysis၊ MAVFTP၊ MAVLink signing/authentication setup၊ auto-updater နှင့် device reporting ကို ဆက် port လုပ်ရန် လိုသည်။ ဤ preview ကို full Windows parity release အဖြစ် မသုံးပါနှင့်။

## Build နှင့် tests

Repository root မှ .NET 10 SDK ဖြင့်:

```sh
dotnet build NativeMac/AglPlanner.Mac/AglPlanner.Mac.csproj -c Release
dotnet run --project NativeMac/AglPlanner.Tests/AglPlanner.Tests.csproj -c Release
dotnet publish NativeMac/AglPlanner.Mac/AglPlanner.Mac.csproj -c Release -r osx-arm64 --self-contained true -o artifacts/native-mac
```

`NativeMac/package.py` သည် .app staging နှင့် file inventory ကို တည်ဆောက်သည်။ `ci/finish-macos.sh` သည် ARM64 Mac ပေါ်တွင် native-library architecture၊ signature၊ local UDP protocol tests၊ GUI startup/navigation နှင့် DMG packaging ကို စစ်သည်။ Linux UI smoke pass ကို native Mac pass အဖြစ် မယူပါ။ Hardware serial၊ live vehicle၊ macOS permissions၊ keyboard/mouse usability နှင့် model/OS matrix ကို လက်တွေ့ စမ်းရန် ကျန်ပါသည်။

## License နှင့် map data

Mission Planner/MAVLink source နှင့် notices သည် GPLv3 အတိုင်းဖြစ်သည်။ App ထဲက `COPYING.txt` ကို ကြည့်ပါ။ Avalonia/.NET/Skia နှင့် dependency များတွင် မူရင်း licenses သက်ဆိုင်သည်။ Source: https://github.com/kakashihatakhae/agl-gcs (NativeMac directory and recorded source revision)။ Map tiles သည် OpenStreetMap မှဖြစ်ပြီး attribution ကို အမြဲပြသည်။ Visible tiles ကိုပဲ request လုပ်၍ cache 7 ရက်နှင့် bounded memory/concurrency သုံးသည်။
