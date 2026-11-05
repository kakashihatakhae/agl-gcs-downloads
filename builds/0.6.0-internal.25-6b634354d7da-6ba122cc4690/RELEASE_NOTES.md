## [0.6.0-internal.25] - 2026-11-05

- Windows **Prepare / View record** နှင့် **Flight history → Battery & Power** တွင် Battery ID ကို ရိုက်ထည့်နိုင်သလို သိမ်းထားပြီးသား ID များထဲမှလည်း ရွေးနိုင်ပါသည်။ ရွေးသော pack ၏ battery type၊ series cells **S**၊ parallel count **P** နှင့် capacity ကို ပြန်ဖြည့်ပေးသည်။ ယခင် flight ၏ voltage / percentage ကို မကူးပါ။
- **Parallel count (P)** ကို battery equipment fields၊ local record/CSV၊ cloud record၊ dev/production record detail နှင့် correction editor တွင် ထည့်ထားပါသည်။ မှတ်တမ်းအဟောင်းများ၏ မသိရသေးသော P ကို 1 ဟု မခန့်မှန်းပါ။
- Developer နှင့် Production dashboard နှစ်ခုလုံးတွင် **Batteries** page အသစ် ပါဝင်ပါသည်။ Battery ID ဖြင့်ရှာခြင်း၊ usage level filter၊ S/P/capacity၊ last updated၊ အသုံးပြုထားသော flight များနှင့် ဆက်စပ် flight record history ကို ကြည့်နိုင်သည်။ History မှ သက်ဆိုင်ရာ record ကို တိုက်ရိုက်ဖွင့်နိုင်ပါသည်။
- Completed flight **7–8** ကြိမ်တွင် **Warning**၊ **9 နှင့်အထက်** တွင် **Critical** ပြပါသည်။ Planned၊ cancelled၊ deleted၊ confirmation မပြီးသေးသော record များကို အသုံးပြုမှုအဖြစ် မတွက်ပါ။ Charge cycle သို့မဟုတ် battery health စစ်ဆေးမှု မဟုတ်ပါ။
- Online ရှိလျှင် synced record များထဲက Battery ID နှင့် specifications များကို Windows ရွေးချယ်စရာတွင် ထည့်ပေးပြီး local cache သိမ်းသည်။ Offline တွင် local history / ယခင် cache နှင့် manual entry ကို ဆက်သုံးနိုင်ပါသည်။ Flight record အပြည့်နှင့် voltage history ကို Battery dropdown အတွက် download မလုပ်ပါ။
- ဤသည် development preview ဖြစ်ပြီး published release / public updater payload ကို မပြောင်းထားပါ။
