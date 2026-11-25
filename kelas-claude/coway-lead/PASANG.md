# Pasang sistem lead Coway (guna semula sistem kabinet)

Tampal prompt di bawah dalam app Claude Desktop, dalam sesi yang dibuka di folder `D:\Jaeger\Claude`
(contohnya sesi "Tookang Kabinet - Claude"). Sistem kabinet tak diusik.

```
Aku nak buat sistem lead Threads yang sama macam kabinet-lead, tapi untuk produk Coway
(penapis air, penapis udara, tilam, mesin basuh, aircon). Jangan ubah apa-apa dalam kabinet-lead.

1. Cipta folder D:\Jaeger\Claude\coway-lead. Salin common.ps1, setup-chatid.ps1, setup-group.ps1
   dan send-report.ps1 dari kabinet-lead. Cipta seen-leads.txt dan ideas-log.txt yang kosong, dan folder reports.
2. Cipta .env baru dengan TELEGRAM_BOT_TOKEN= dan TELEGRAM_CHAT_ID= kosong, dan .gitignore yang mengandungi .env.
   Aku akan cipta bot BARU di @BotFather dan paste token sendiri — jangan minta token dalam chat.
3. Tulis offer.md dan RUNBOOK.md ikut kandungan yang aku tampal di bawah.
4. Lepas aku isi token, jalankan setup-chatid.ps1, kemudian bantu aku setup group Telegram baru
   "Coway Lead" dengan Topics, dan cipta 2 topic: 🔎 Prospek Threads dan 💡 Bank Idea Content.
5. Uji: cari 3 keyword pertama dalam RUNBOOK, tunjuk hasil dalam chat dulu. Jangan reply/like/follow/DM di Threads.
6. Uji juga langkah 5 RUNBOOK (hantar ke web app dengan tool ArtifactData). Kalau tool tu tiada dalam sesi ni,
   beritahu aku.
7. Bila aku setuju dengan kualiti lead, cipta scheduled task "coway-lead-threads": setiap hari 9:00 pagi dan
   9:00 malam, baca coway-lead\RUNBOOK.md dan offer.md, ikut sepenuhnya. Sebelum 3 petang = Sesi Pagi
   (lead + idea), selepas tu = Sesi Malam (lead sahaja).

--- offer.md ---
[tampal isi offer.md]

--- RUNBOOK.md ---
[tampal isi RUNBOOK.md]
```

## Sebelum mula
- Isi semua `[kurungan]` dalam `offer.md`.
- Cipta bot Telegram baru di @BotFather. Jangan guna bot kabinet: satu bot untuk satu sistem.
- Web app: https://claude.ai/artifact/44qDCyr3chxVQePemHD79U — buang data contoh dengan butang "Buang data contoh" bila lead sebenar dah masuk.
