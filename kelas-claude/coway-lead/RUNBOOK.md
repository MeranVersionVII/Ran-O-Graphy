# Runbook: carian lead Threads (ejen Coway)

Folder: folder projek ini (cth. `D:\Jaeger\Claude\coway-lead`). Info bisnes: `offer.md` dalam folder yang sama. Baca `offer.md` dulu, setiap kali.

## 1. Cari di Threads (browser dalam app Claude, dah login)
- URL: `https://www.threads.com/search?q=<keyword>&serp_type=default&filter=recent`
- Kalau page tunjuk "Log in" atau tiada hasil untuk SEMUA keyword: berhenti, dan hantar mesej ringkas ke topic `prospek`: "Threads ter-logout, sila login semula dalam browser app Claude." Jangan cuba login.
- Selepas setiap navigate, tunggu 3 saat, kemudian ekstrak post dengan `javascript_tool`:
  ```js
  const o=[];const s=new Set();for(const a of document.querySelectorAll('a[href*="/post/"]')){if(!a.querySelector('time'))continue;const u=a.href.split('?')[0];if(s.has(u))continue;s.add(u);let e=a;for(let i=0;i<12&&e.parentElement;i++){e=e.parentElement;if(e.innerText.length>60&&e.querySelectorAll('a[href*="/post/"] time').length===1)break}o.push(a.querySelector('time').getAttribute('datetime').slice(0,10)+' | '+u+' | '+e.innerText.replace(/\s+/g,' ').slice(0,300))}o.join('\n')
  ```
- Kata kunci (ikut urutan; tukar ikut hasil P07 / analisis mingguan):
  1. penapis air recommend
  2. air paip keruh
  3. water filter rumah
  4. air purifier recommend
  5. rumah berhabuk
  6. recommend tilam
  7. tilam sakit belakang
  8. mesin basuh rosak
  9. aircon tak sejuk
  10. baru pindah rumah
- Rentak macam manusia: satu carian pada satu masa, tidak lebih daripada senarai ini setiap run.
- Tutup tab Threads bila selesai.

## 2. Tapis — simpan prospek sebenar sahaja
Lead = orang yang SEDANG MENCARI, atau SEDANG ADA MASALAH yang diselesaikan oleh penapis air, penapis udara, tilam, mesin basuh atau aircon.
- ✅ Kawasan servis dalam `offer.md`, atau lokasi tak disebut.
- ❌ Buang: iklan ejen Coway lain dan jenama pesaing, link Shopee/affiliate, post Indonesia, barang jual/sewa, cerita tak berkaitan.
- ❌ Buang post lebih 7 hari.
- ❌ Buang URL yang dah ada dalam `seen-leads.txt` (satu URL satu baris). Selepas report dihantar, tambah URL baru ke fail tu.

Skor: 🔥 kuat (jelas cari produk / ada masalah, dalam kawasan) · 🟡 sederhana (minat atau masalah, lokasi/keperluan kabur) · ⚪ lemah (kabur).
Produk: `penapis-air`, `penapis-udara`, `tilam`, `mesin-basuh`, `aircon`, atau `lain`.

## 3. Draf reply
Untuk setiap lead, satu reply dalam Bahasa Melayu santai (rojak OK), 1–3 ayat, khusus untuk post tu:
- Respon kepada apa yang dia tulis dulu, beri satu tip berguna, kemudian sebut "saya ejen Coway area <kawasan>", dan ajak DM.
- Fakta dari `offer.md` SAHAJA. Tiada harga atau promo kecuali tertulis dalam `offer.md`.
- Tiada dakwaan kesihatan (jangan "sembuhkan", "elak penyakit", "bebas kuman 100%"). Jangan kutuk jenama lain.
- Tak bunyi macam template. Maksimum satu emoji.

## 4. Tulis report & hantar ke Telegram
- Simpan dalam `reports/YYYY-MM-DD-pagi.md` atau `reports/YYYY-MM-DD-malam.md`, ikut format ini.
  Baris yang hanya mengandungi `---` memulakan mesej Telegram baru. **Draf reply mesti dalam mesej sendiri, tiada benda lain**, supaya boleh tekan lama dan salin reply sahaja:
  ```
  🔎 Lead Threads: <tarikh> (<n> lead) - Sesi <Pagi/Malam>
  ---
  🔥 1. @username · <lokasi> · <berapa lama> · <produk>
  <ringkasan keperluan satu baris>
  🔗 <url>
  👇 Reply:
  ---
  <teks draf reply sahaja>
  ---
  🟡 2. @username · ...
  ```
- Kalau 0 lead baru, hantar satu baris: "🔎 Lead Threads: <tarikh> (0 lead) - Sesi <Pagi/Malam>: tiada lead baru."
- Hantar: `powershell -File send-report.ps1 -File reports\<fail>.md -Topic prospek` (jalankan dari folder ini).

## 5. Hantar ke web app Hub Prospek Ejen
Selepas Telegram, masukkan lead yang sama ke web app dengan tool `ArtifactData`:
- `action: "batch"`, `url: "https://claude.ai/artifact/44qDCyr3chxVQePemHD79U"`
- Satu entry `{"op": "set", "collection": "leads", "doc_id": <id>, "data": {...}}` untuk setiap lead (maksimum 50 setiap batch).
- `doc_id`: `<username>-<id post dari URL>`, hanya huruf, nombor, `-` dan `_`.
- `data`:
  ```json
  {"username": "...", "score": "kuat|sederhana|lemah", "product": "penapis-air|penapis-udara|tilam|mesin-basuh|aircon|lain",
   "location": "...", "postedAge": "3 jam lepas", "summary": "...", "reply": "...", "url": "https://www.threads.com/...",
   "status": "baru", "session": "Pagi|Malam", "foundAt": "<masa sekarang ISO, UTC>"}
  ```
- Jangan tulis semula lead yang dah ada (dah dalam `seen-leads.txt`), supaya status yang aku tanda tak hilang.
- Kalau tool `ArtifactData` tiada atau gagal, teruskan sahaja — Telegram tetap jadi rekod utama. Sebut kegagalan tu dalam ringkasan akhir.

## 6. Idea content (sesi pagi sahaja)
- 2 idea post Threads berdasarkan soalan atau masalah yang orang tulis dalam carian hari ini.
- Setiap idea: satu ayat hook + 2–3 poin isi. Semak `ideas-log.txt` supaya tak berulang, kemudian tambah idea baru ke fail tu.
- Hantar ke Telegram: `powershell -File send-report.ps1 -Text "<idea>" -Topic idea`
- Hantar juga ke web app: `ArtifactData` `set`, `collection: "ideas"`, `doc_id: <tarikh>-<1|2>`, `data: {"hook": "...", "points": ["...", "..."], "product": "...", "status": "idea", "source": "threads", "createdAt": "<ISO>"}`.

## Peraturan
- Hanya BACA di Threads. Jangan reply, like, follow atau DM.
- Jangan paparkan atau log token bot.
