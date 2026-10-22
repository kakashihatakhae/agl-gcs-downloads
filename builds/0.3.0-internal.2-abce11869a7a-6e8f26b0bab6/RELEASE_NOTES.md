## [0.3.0-internal.2] - 2026-10-22

- R2 မလိုဘဲ public binary-only `agl-gcs-downloads` repo နှင့် Cloudflare Worker မှ update payload နှင့် Windows installer ကို ပေးပါသည်။ Source repo သည် private အဖြစ် ဆက်ရှိပါသည်။ Installer parts ကို download လုပ်ချိန် `.exe` တစ်ဖိုင်တည်းအဖြစ် stream လုပ်ပါသည်။ SHA256 စစ်ထားသော app files၊ manifest နှင့် update channel ကို Git commit တစ်ခုတည်းဖြင့် တင်ပါသည်။
- Device inventory ကြည့်ရန် password login ပါသော developer dashboard (`/admin`) ထည့်ထားပါသည်။ Installation count၊ နောက်ဆုံး ၇ ရက်အတွင်း report ပို့ထားမှု၊ update version၊ CPU/RAM/GPU/Windows specs၊ search နှင့် pagination ပါဝင်ပါသည်။ Device key/hash ကို dashboard မှ မပြပါ။
- Dashboard တွင် HttpOnly/Secure session၊ login rate limit၊ same-origin form checks နှင့် no-store/CSP headers သုံးပါသည်။ Admin password သည် source/app/installer ထဲ မပါပါ။
- App ၏ public service URL ကို live Worker သို့ ချိတ်ထားပါသည်။ Updater အဟောင်းများအတွက် installer/Git build အသစ်ကို တစ်ကြိမ် update လုပ်ရန် လိုပါသည်။ Native Windows WMI နှင့် Windows စက်အစစ်တွင် updater/install behavior ကို ဆက်စမ်းရန် လိုပါသည်။
