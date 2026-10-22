## [0.3.1-internal.1] - 2026-10-22

- FLY → Action tab နှင့် Simple Actions ထဲက ခလုတ်များကို AGL အမှောင်/အဝါ theme သို့ ပြောင်းထားပါသည်။ Normal၊ hover၊ pressed၊ disabled state များကို ညှိပြီး hover/pressed စာသား contrast ကို စစ်ထားပါသည်။ ခလုတ် command နှင့် လုပ်ဆောင်ချက်ကို မပြောင်းပါ။
- Toolbar ရှိ AGL logo အရှည်ကို နှိပ်လျှင် default browser မှ `/agl` စာမျက်နှာကို ဖွင့်ပါသည်။ မူရင်း AGL logo အရှည် အပြည့်အစုံကိုသာ aspect ratio မပျက်ဘဲ ပြထားပါသည်။ Developer dashboard `/admin` ကို ဆက်သုံးနိုင်ပါသည်။
- Device reporting startup error များကို INFO တွင် ပြထားပြီး network timeout ကို ၃၀ စက္ကန့်ထားပါသည်။ Report queue ထဲတွင် HTTP/network failure အကြောင်းရင်းနှင့် retry အချိန်ကို ထိန်းထား၍ စစ်ဆေးရ ပိုလွယ်စေပါသည်။ App ပွင့်ပြီးမှ report ပို့ပါသည်။ Install လုပ်ရုံဖြင့် device စာရင်း မတိုးပါ။
- Backend ingestion နှင့် authenticated dashboard လမ်းကြောင်း အလုပ်လုပ်ကြောင်း စမ်းထားပါသည်။ User ၏ Windows report မရောက်သေးသည့် အကြောင်းရင်းကို INFO status ဖြင့် ဆက်စစ်ရန် လိုပါသည်။ Cloud compatibility စမ်းသပ်မှုသည် native Windows WMI/GUI စမ်းသပ်မှုအတွက် အစားထိုးမဟုတ်ပါ။
