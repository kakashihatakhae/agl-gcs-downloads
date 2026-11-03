## [0.6.0-internal.21] - 2026-11-03

Windows 10/11 x64 အတွက် internal pre-release ဖြစ်ပါသည်။ ယခင် `0.4.0-internal.2` မှနောက်ပိုင်း Vehicle Profile၊ Flight Record၊ private flight logs၊ dashboard နှင့် PLAN Terrain Profile ပြင်ဆင်ချက်များ ပါဝင်ပါသည်။

### Windows installer ရယူရန်

**[AGL Planner Windows Setup.exe ကို download လုပ်ရန် (69.5 MB)](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.21/AGL-Planner-0.6.0-internal.21-Windows-x64-Setup.exe)**

[Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.21/AGL-Planner-0.6.0-internal.21-Windows-x64.zip) · [SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.21/SHA256SUMS.txt) · [မြန်မာအသုံးပြုနည်း](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.6.0-internal.21/README-WINDOWS-my.md)

GitHub login၊ Git၊ Visual Studio နှင့် .NET SDK မလိုပါ။ App အဟောင်းကို ပိတ်ပြီး Setup.exe ဖြင့် install/update လုပ်ပါ။ .NET Framework 4.7.2+ လိုအပ်ပါသည်။ Install ပြီး INFO တွင် **0.6.0-internal.21** ဖြစ်ကြောင်း စစ်ပါ။ Installer သည် လက်ရှိ Windows user အတွက် install လုပ်ပြီး administrator ခွင့်ပြုချက် မလိုပါ။

### ပါဝင်သော အဓိကပြောင်းလဲမှုများ

- **PLAN → Terrain Profile** — ရွှေဝါရောင် planned altitude၊ မီးခိုးရောင် terrain၊ မြေအောက်ရောက်သောအပိုင်း အနီရောင်၊ route length၊ terrain peak နှင့် waypoint နံပါတ်များကို တွဲပြပါသည်။ Hover ဖြင့် distance/altitude/clearance ကြည့်နိုင်ပြီး graph ကိုနှိပ်၍ မြေပုံက အဲဒီနေရာသို့ သွားနိုင်ပါသည်။
- Terrain Profile ကို cockpit Flight Mode ကဲ့သို့ **dark glass နောက်ခံ** ပြောင်းထားပါသည်။ ခေါက်/ဖြန့်နိုင်ပြီး hover အချိန် map backdrop ကို cache မှ သုံးပါသည်။ Map center နှင့် attribution မဖုံးစေရန် layout ကို ညှိထားပါသည်။
- Relative / Global / Terrain altitude frame များကို ခွဲတွက်ပြီး cached SRTM/GeoTIFF/DTED data ကို သုံးပါသည်။ Data မရသောနေရာကို unknown gap အဖြစ်ပြပါသည်။ Samples ကို ကန့်သတ်၍ နောက်ခံတွင် တွက်ပြီး mission ပြောင်းချိန် result အဟောင်း ပြန်ဝင်ခြင်းကို ကာကွယ်ပါသည်။
- **SETUP → Vehicle Profile** — local profile သိမ်းခြင်း၊ Plane Pusher/Tractor ရွေးခြင်း၊ flight controller UID ဖြင့် profile match လုပ်ခြင်းနှင့် profile metadata online sync ပါဝင်ပါသည်။ သက်ဆိုင်ရာ profile value များကို Flight Record တွင် အလိုအလျောက် ဖြည့်ပေးပါသည်။
- **FLY → Flight Records** — Prepare/Continue setup → recording → Complete Previous Record workflow၊ မှတ်မိလွယ်သော Flight No.၊ telemetry autofill၊ မဖြည့်ရသေးသောအချက်များပြခြင်း၊ record history နှင့် status အရောင်များ ပါဝင်ပါသည်။ Battery ID/usage၊ AUW၊ GNSS၊ weather၊ camera weight၊ crash findings နှင့် notes များကို သိမ်းနိုင်ပါသည်။
- **Flight logs** — flight တစ်ကြိမ်ချင်းနှင့် `.tlog` / onboard `.bin` ကို ဆက်စပ်သိမ်းပြီး online ရချိန် private storage သို့ sync လုပ်ပါသည်။ Dashboard login ဝင်ထားသူများက download ရနိုင်ပါသည်။ မရသေးသော BIN ကို ရပြီးသားဟု မပြပါ။
- FC watchdog/reset နှင့် onboard log backend ပိတ်ထားသောအခြေအနေများတွင် မလိုအပ်သော log cleanup request ပို့ခြင်းကို ကာကွယ်ထားပါသည်။
- Flight Record buttons ၏ primary/secondary priority၊ square corners၊ alignment၊ scroll/maximize၊ theme refresh နှင့် Battery type dropdown/manual override ပြဿနာများကို ပြင်ထားပါသည်။ Flight time မရလျှင် source label နှင့်အတူ 0 ကို ထားပါသည်။
- Developer/production dashboard များတွင် account login/profile၊ record edit history/user attribution၊ delayed-response/conflict/retry ကာကွယ်မှုများနှင့် developer-only keyword-protected record deletion ပါဝင်ပါသည်။

### App ထဲမှ update လုပ်ရန်

Vehicle ကို disconnect လုပ်ပြီး ပြင်ထားသော mission များကို save လုပ်ပါ။ **INFO → Check for updates** မှ update ကို စစ်နိုင်ပါသည်။ အဟောင်းမှ update မရလျှင် အပေါ်က Setup.exe ကို သုံးပါ။

### စမ်းသပ်မှုနှင့် အတိုင်းအတာ

- Native Windows တွင် Terrain Profile၊ glass compositing/cache၊ map interaction၊ Flight Record workflow နှင့် mouse/keyboard checks အောင်မြင်ပါသည်။ [Native Windows စမ်းသပ်မှုမှတ်တမ်း](https://github.com/kakashihatakhae/agl-gcs-downloads/actions/runs/41638630438)။
- Record core suites 8 မျိုးကို Windows timezone 5 မျိုးဖြင့် စစ်ထားပါသည်။ Full app UI compatibility checks၊ web API tests 32 ခုနှင့် developer/production browser workflow checks အောင်မြင်ထားပါသည်။
- ဤ release publication တွင် installer install/uninstall၊ ဖိုင် hash၊ shortcut/registry နှင့် user ဖိုင်မဖျက်ခြင်းကို native Windows job မှ စစ်ပြီးမှ public assets ကို publish လုပ်ပါသည်။
- Terrain Profile သည် sampled straight-leg DEM estimate ဖြစ်ပြီး obstacles/buildings၊ loiter orbit၊ RTL path နှင့် firmware ၏ dynamic flight path မပါပါ။ Physical FC/USB နှင့် flight စမ်းသပ်မှုအားလုံးကို အတည်ပြုပြီးဟု မသတ်မှတ်ပါ။ macOS development သည် pause အဖြစ် ဆက်ရှိပါသည်။

Installer SHA256: `4a63ea3d4bf46291843a80f8abe46cba5ac90a5666f82fda43d0bc6c1d97e266`

Compiled source: `1ad700a9a423278685c2b742ce32bcf5b5366b3e` · Build: `0.6.0-internal.21-1ad700a9a423-e1152422a106`
