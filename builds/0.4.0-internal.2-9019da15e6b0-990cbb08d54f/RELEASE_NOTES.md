## [0.4.0-internal.2] - 2026-10-30

- FLY တွင် အတည်ပြုထားသော **Live Mission Progress** ကို ထည့်ထားပါသည်။ လက်ရှိ waypoint၊ အတည်ပြုပြီးရောက်ရှိသော waypoint အရေအတွက်/ရာခိုင်နှုန်း၊ target အကွာအဝေး၊ ကျန်လမ်းကြောင်း၊ ခန့်မှန်း transit time နှင့် cross-track တို့ကို ပြပါသည်။ Panel ကို ချုံ့/ချဲ့နိုင်ပြီး map တွင် လက်ရှိ leg/target ကို highlight လုပ်ထားပါသည်။
- `ITEM 00` ကဲ့သို့ မရှင်းလင်းသောစာသားအစား **Home၊ Takeoff၊ Land၊ Return to launch** နှင့် mission command အမျိုးအစားကို ခွဲပြပါသည်။ Data မရသေးချိန်၊ mission မဖတ်ရသေးချိန်နှင့် stale state တို့တွင် အကြောင်းရင်း/ဆက်လုပ်ရမည့်အချက်ကို ပြထားပါသည်။ `—` သည် သုညမဟုတ်ဘဲ data မရရှိခြင်းကို ဆိုလိုပါသည်။
- Metric တစ်ခုချင်း၊ progress/timeline၊ ချုံ့/ချဲ့နှင့် display limit ခလုတ်တို့တွင် hover ရှင်းလင်းချက်များ ပါဝင်ပါသည်။ ETA သည် arrival clock time မဟုတ်ဘဲ လက်ရှိ groundspeed အရ transit duration ဖြစ်ကြောင်း၊ L/R နှင့် display threshold တို့၏ အဓိပ္ပာယ်ကို ရှင်းပြထားပါသည်။
- Waypoint history မပြည့်စုံလျှင် အတည်ပြုနိုင်သော reached count ကိုသာ ပြ၍ မသေချာသော ရာခိုင်နှုန်းကို မပြပါ။ Stale/disconnect/pause၊ mission ပြောင်းခြင်း၊ command/branch နှင့် log replay များကို ခွဲပြထားပါသည်။ Vehicle setting နှင့် flight command မပြောင်းပါ။
- ယခင် PLAN theme ပြင်ဆင်ချက်များလည်း ပါဝင်ပါသည်။ Polygon vertices၊ edit handles၊ boundary၊ measurement၊ ROI/geofence pin များကို theme နှင့် ညှိထားပါသည်။
- Cloud desktop build၊ offline telemetry/model နှင့် GUI/layout/hover checks ဖြင့် စစ်ထားပါသည်။ User က ယခင် preview ၏ feature အလုပ်လုပ်ကြောင်း အတည်ပြုထားပါသည်။ Native Windows/macOS UI/DPI နှင့် တကယ့် vehicle/SITL flight ကို ဆက်စမ်းရန် လိုပါသည်။
