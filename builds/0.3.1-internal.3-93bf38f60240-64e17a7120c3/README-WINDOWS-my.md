# AGL Planner — Release

ဒီ branch သည် AGL Planner release များအတွက် သီးသန့် source၊ Windows package နှင့် မှတ်တမ်းများကို ထိန်းသိမ်းထားသော `release` branch ဖြစ်ပါသည်။

<!-- release-version:start -->
**Version: `0.3.1-internal.3`** · **Tag: `v0.3.1-internal.3`**

Installer: `AGL-Planner-0.3.1-internal.3-Windows-x64-Setup.exe`

Portable ZIP: `AGL-Planner-0.3.1-internal.3-Windows-x64.zip`
<!-- release-version:end -->

လက်ရှိ version သည် internal testing အတွက် Pre-release ဖြစ်ပါသည်။ GitHub Pre-release label သည် private access သတ်မှတ်ချက် မဟုတ်ပါ။

## Download / Install

[လက်ရှိ Windows installer ကို download လုပ်ရန်](https://agl-planner-services.quiz-checker-usage.workers.dev/downloads/windows-x64)။

GitHub မှာ publish လုပ်ပြီးသော package များကို [Releases](https://github.com/kakashihatakhae/agl-gcs/releases) မှ ရယူနိုင်ပါသည်။ ပုံမှန် install လုပ်သုံးရန် **`AGL-Planner-<VERSION>-Windows-x64-Setup.exe`** ကို download လုပ်ပါ။ GitHub ရဲ့ **Source code (zip)** သည် developer source ဖြစ်ပြီး install လုပ်ရန် ဖိုင်မဟုတ်ပါ။

1. App ဖွင့်ထားလျှင် ပိတ်ပြီး **Setup.exe** ကို ဖွင့်ပါ။
2. License ကိုဖတ်ပြီး Install ကိုနှိပ်ပါ။ လက်ရှိ Windows user ရဲ့ `%LOCALAPPDATA%\Programs\AGL Planner` ထဲ install လုပ်ပါမည်။ Administrator ခွင့်ပြုချက် မလိုပါ။
3. Desktop သို့မဟုတ် Start Menu မှ **AGL Planner** ကို ဖွင့်ပါ။ Settings → Apps → Installed apps မှ uninstall လုပ်နိုင်ပါသည်။ ကိုယ်တိုင်ထည့်ထားသော mission၊ log နှင့် အခြား user ဖိုင်များကို uninstaller က မဖျက်ပါ။

Internal installer သည် code signing မလုပ်ရသေးပါ။ Windows က unknown publisher အဖြစ် သတိပေးနိုင်ပါသည်။ `SHA256SUMS.txt` တွင် Setup.exe နှင့် portable ZIP နှစ်မျိုးလုံးအတွက် checksum ပါသည်။

Install မလုပ်ဘဲ portable သုံးလိုလျှင် **`AGL-Planner-<VERSION>-Windows-x64.zip`** ကို folder အသစ်ထဲ **အပြည့် extract** လုပ်ပြီး `AGL-Planner-Windows-x64/AGL Planner.exe` ကို ဖွင့်ပါ။ DLL နှင့် အခြားဖိုင်များကို app နှင့်အတူ ထားပါ။

Windows 10/11 x64 နှင့် .NET Framework 4.7.2 သို့မဟုတ် ပိုသစ်သော version လိုပါသည်။ Git၊ Visual Studio နှင့် .NET SDK မလိုပါ။

## Branch များ

| Branch | ရည်ရွယ်ချက် |
| --- | --- |
| `release` | Version သတ်မှတ်ပြီးသော release source၊ release README/notes နှင့် Windows package |
| `import/mission-planner` | လက်ရှိ application development |
| `preview/windows-ui-test` | လက်ရှိ UI / Mission Validation / PreFlight စမ်းသပ်ခြင်း |
| `main` | Project မိတ်ဆက်နှင့် လမ်းညွှန် |

Release branch ရဲ့ Windows package သည် `bin/release/AGL-Planner-Windows-x64` ထဲတွင် ရှိပါသည်။ ရှိပြီးသား source checkout မှ Git ဖြင့် ရယူလိုလျှင် app ကို ပိတ်ပြီး ဒီ command များကို သုံးနိုင်ပါသည်။

```powershell
git fetch origin release
git restore --source=FETCH_HEAD --worktree -- bin/release/AGL-Planner-Windows-x64
& ".\bin\release\AGL-Planner-Windows-x64\AGL Planner.exe"
```

## လက်ရှိ UI / Mission checks စမ်းသပ်ရန်

App ကိုပိတ်ပြီး project folder မှာ အောက်ပါ command များကို သုံးပါ။ Installer အသစ် download မလိုပါ။ ဒီ test branch သည် `release` channel နှင့် သီးခြားဖြစ်ပါသည်။

```powershell
git fetch origin preview/windows-ui-test
if ($LASTEXITCODE -ne 0) { throw "Git fetch failed" }
git -c core.autocrlf=false restore --source=FETCH_HEAD --worktree -- bin/preview/AGL-GCS-Windows-dev
if ($LASTEXITCODE -ne 0) { throw "App update failed" }
$aglTestDir = (Resolve-Path ".\bin\preview\AGL-GCS-Windows-dev").Path
Start-Process -FilePath "$aglTestDir\AGL Planner.exe" -WorkingDirectory $aglTestDir
```

PLAN → **Validate mission** နှင့် FLY → **PreFlight** တွင် စမ်းပါ။ [Mission checks အသုံးပြုပုံနှင့် စစ်ဆေးသည့်အတိုင်းအတာ](Desktop/MISSION-CHECKS.md) ကို ဖတ်နိုင်ပါသည်။

## Version စည်းမျဉ်း

`MAJOR.MINOR.PATCH` စနစ်ကို အသုံးပြုပါသည်။

| အမျိုးအစား | တိုးမည့်အခြေအနေ | ဥပမာ |
| --- | --- | --- |
| MAJOR | ရှိပြီးသားအသုံးပြုပုံ/API နှင့် မကိုက်ညီသော အပြောင်းအလဲကြီး | `1.2.3` → `2.0.0` |
| MINOR | Feature အသစ် ထပ်တိုးပြီး လက်ရှိ behavior နှင့် ကိုက်ညီနေခြင်း | `1.2.3` → `1.3.0` |
| PATCH | Bug fix နှင့် feature မတိုးသော ပြင်ဆင်မှု | `1.2.3` → `1.2.4` |

- `0.x` သည် အစောပိုင်းဖွံ့ဖြိုးဆဲ အဆင့် ဖြစ်ပါသည်။
- Internal build များတွင် `-internal.1`, `-internal.2` ကဲ့သို့ suffix ထည့်ပါသည်။ ဥပမာ `0.1.0-internal.1`။
- အတည်ပြုပြီးသော build တွင် suffix ဖြုတ်၍ `0.1.0` ကဲ့သို့ ထုတ်နိုင်ပါသည်။
- Git tag သည် `v` + version ဖြစ်ပါသည်။ ဥပမာ `v0.1.0-internal.1`။
- `VERSION` သည် version အတွက် မူရင်းတစ်နေရာတည်း ဖြစ်ပါသည်။ Splash၊ product version၊ package၊ manifest နှင့် tag တို့ကို တိုက်စစ်ပါသည်။ .NET numeric assembly/file version သည် `MAJOR.MINOR.PATCH.0` ဖြစ်ပါသည်။

[Release notes](https://github.com/kakashihatakhae/agl-gcs/blob/release/RELEASE_NOTES.md) တွင် release တိုင်း၏ အပြောင်းအလဲနှင့် validation ကို ဖော်ပြပါသည်။ Release tag နှင့် ထုတ်ပြီးသား asset ကို အစားမထိုးဘဲ version အသစ် ထုတ်ပါသည်။

## App ထဲမှ update

Private repository အတွက် GitHub login မလိုသော သီးသန့် update service နှင့် automatic basic device reporting setup ကို [Cloudflare service လမ်းညွှန်](Services/README-my.md) တွင် ကြည့်ပါ။ R2 မသုံးဘဲ public binary-only GitHub downloads repo နှင့် Worker ဖြင့် installer/update files ကို ပေးပြီး password login ပါသော developer dashboard နှင့် D1 device database ကို သုံးထားပါသည်။

**INFO → Update AGL Planner → Download update → Install & Restart** ကို သုံးပါ။ ဒီ build သည် Cloudflare service ၏ Windows update channel ကို ယူပါသည်။ Development preview branch ကို မယူပါ။ Restart မလုပ်မီ edited mission ကို save လုပ်ပြီး vehicle links ကို disconnect လုပ်ထားပါ။

တူညီသော build ကို နှိုင်းယှဉ်စမ်းရန် tag အလိုက် ZIP ကို ဆက်သုံးနိုင်ပါသည်။ Updater သည် service ၏ နောက်ဆုံး published Windows package သို့ ပြောင်းပေးပါသည်။

## Internal စမ်းသပ်မှု

Build၊ Windows PE/ZIP checks၊ package hashes နှင့် Linux/Mono GUI စမ်းသပ်မှုများကို စစ်ပြီး package ထုတ်ပါသည်။ လက်ရှိ internal build အတွက် native Windows launch၊ updater install/restart၊ serial/vehicle operation နှင့် full native test suite တို့ကို ဆက်အတည်ပြုရန် လိုပါသည်။ Code signing မပါဝင်သေးပါ။ macOS package သည် ယခု release တွင် မပါဝင်ပါ။

Bug report မှာ app version/build၊ Windows version၊ resolution/DPI၊ ပြန်ဖြစ်စေရန်အဆင့်များ၊ screenshot နှင့် သက်ဆိုင်ရာ log တို့ကို ထည့်ပေးပါ။

Maintainer အတွက် [release ထုတ်နည်း](https://github.com/kakashihatakhae/agl-gcs/blob/release/Desktop/RELEASING.md) ကို ကြည့်ပါ။ မူရင်း Mission Planner provenance ကို [UPSTREAM.md](https://github.com/kakashihatakhae/agl-gcs/blob/release/UPSTREAM.md)၊ GPLv3 နှင့် original author notices ကို [COPYING.txt](https://github.com/kakashihatakhae/agl-gcs/blob/release/COPYING.txt) တွင် ထိန်းသိမ်းထားပါသည်။
