# AGL Planner 0.8.0-internal.35 — Windows x64

Windows 10/11 x64 နှင့် .NET Framework 4.7.2 သို့မဟုတ် ပိုသစ်သော version လိုအပ်ပါတယ်။

## Install လုပ်ပုံ

[Windows Setup.exe ရယူရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.35/AGL-Planner-0.8.0-internal.35-Windows-x64-Setup.exe) · [Portable ZIP](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.35/AGL-Planner-0.8.0-internal.35-Windows-x64.zip)

1. လက်ရှိ mission နဲ့ flight record တွေကို သိမ်းပြီး AGL Planner ပိတ်ပါ။
2. Setup.exe ကို ဖွင့်ပြီး install သို့မဟုတ် update လုပ်ပါ။
3. Start Menu ကနေ AGL Planner ဖွင့်ပြီး **INFO** မှာ `0.8.0-internal.35` ပေါ်တာကို စစ်ပါ။

Portable ZIP သုံးရင် folder အသစ်ထဲ ဖိုင်အားလုံးဖြည်ပြီး `AGL-Planner-Windows-x64/AGL Planner.exe` ကို ဖွင့်ပါ။

## Offline map နဲ့ 3D survey

- **FLY / PLAN → Map Layers** ကနေ MBTiles၊ KMZ သို့မဟုတ် orthophoto GeoTIFF ထည့်ပါ။ ထည့်ထားတဲ့ layer ကို ဖွင့်ပိတ်တာ၊ opacity ညှိတာနဲ့ layer ဆီ zoom လုပ်တာတွေ ဒီနေရာကနေ လုပ်နိုင်ပါတယ်။
- **FLY → 3D → Layers** ကနေ ODM ZIP၊ GLB သို့မဟုတ် elevation GeoTIFF ထည့်ပါ။ GLB ရဲ့ မူရင်း ODM coordinates လိုရင် **Add coords.txt…** မှာ `odm_georeferencing/coords.txt` ရွေးပါ။
- **Fit model to terrain** ဖွင့်ရင် survey ရဲ့ အမြင့်နဲ့ စောင်းပုံကို ရရှိထားတဲ့ elevation data နဲ့ ညှိပေးပါတယ်။ GPS position မရှိဘဲ survey ကြည့်ချိန် အစွန်းတွေကို နောက်ခံမြေပုံနဲ့ ဖြည်းဖြည်းချင်း ရောပြပါတယ်။
- **⋯ → Render quality → Auto** မှာ survey ကြည့်နေချိန် camera ရပ်သွားရင် view ကို resolution အပြည့်နဲ့ ပြပေးပါတယ်။ **Cached only** ဖွင့်ထားချိန် နောက်ခံမြေပုံရဲ့ ကြည်လင်မှုက သိမ်းထားတဲ့ tiles ပေါ် မူတည်ပါတယ်။

[Release notes နှင့် assets](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/tag/v0.8.0-internal.35) · [SHA256 စစ်ဆေးရန်](https://github.com/kakashihatakhae/agl-gcs-downloads/releases/download/v0.8.0-internal.35/SHA256SUMS.txt)
