## [0.3.1-internal.3] - 2026-10-22

- **Windows device reporting မစတင်သော startup bug ကို ပြင်ထားပါသည်။** Legacy main window ၏ `OnLoad` သည် base method မခေါ်သဖြင့် Windows တွင် `Shown` event မဖြစ်လာပါ။ ယခင် reporting task ကို ထို event မှ စထားမိသဖြင့် INFO တွင် “Starts automatically in the background” မှာပဲ ကျန်ပြီး database ဆီ report မပို့ပါ။
- Reporting ကို app ready ဖြစ်သောနေရာမှ တိုက်ရိုက်စပါသည်။ Startup delay၊ worker စတင်မှုနှင့် specs ကောက်ယူနေမှုကို status သီးခြား ပြထားပါသည်။ Duplicate worker မဖြစ်စေရန် guard၊ background collection၊ offline queue နှင့် shutdown cancellation ကို ဆက်ထိန်းထားပါသည်။
- Windows app lifecycle ကို တကယ်ဖွင့်၍ reporting worker စကြောင်း စစ်သော regression check ထည့်ထားပါသည်။ Test သည် isolated profile တွင် reporting ကို ပိတ်ထားသဖြင့် CI စက်အချက်အလက်ကို မကောက်/မပို့ပါ။ Verified preview payload ဖြင့် အမြန်စမ်းနိုင်သော workflow dispatch option ပါဝင်ပါသည်။
- Installer နှင့် Git preview နှစ်မျိုးလုံးတွင် fix ပါဝင်ပါသည်။ User စက်၏ end-to-end report အောင်မြင်မှုကို update ပြီး INFO status နှင့် developer dashboard မှ ဆက်စစ်နိုင်ပါသည်။
