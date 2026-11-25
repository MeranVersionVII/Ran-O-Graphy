# -*- coding: utf-8 -*-
"""Kandungan kursus: slide, nota penceramah dan prompt — khusus untuk ejen Coway.

Edit fail ini, kemudian jalankan:  python3 build.py && node render.js
"""

PLATFORM = "Threads"
TEAM = "Tim Coway"
COURSE_TITLE = "Claude AI untuk Ejen Coway: Dari Zero ke Mesin Cari Prospek Threads"
COURSE_SUB = ("Kelas hands-on untuk ejen jualan Coway — dari tak pernah guna AI sampai ada sistem automatik "
              "yang cari prospek penapis air, penapis udara, tilam, mesin basuh dan aircon di Threads.")
DISCLAIMER = "Bahan latihan bebas untuk ejen. Bukan bahan rasmi Coway."

# ---------------------------------------------------------------------------
# PROMPT PACK  (id, tajuk, bila guna, teks prompt)
# Teks dalam [kurungan] = peserta ganti sendiri.
# ---------------------------------------------------------------------------
PROMPTS = [
  ("P01", "Chat pertama: kenalkan diri sebagai ejen Coway", "Hari pertama guna Claude. Untuk nampak apa Claude boleh buat untuk kerja jualan.",
"""Hai Claude. Aku [nama], ejen jualan Coway di [kawasan, cth. Shah Alam].
Aku jual penapis air, penapis udara, tilam, mesin basuh dan aircon Coway.
Aku baru mula guna AI.

Terangkan dalam bahasa mudah 5 cara kau boleh bantu kerja jualan aku setiap hari.
Untuk setiap cara, beri satu contoh yang spesifik untuk ejen Coway."""),

  ("P02", "Template formula P.K.T.F.C (versi Coway)", "Asas untuk SEMUA prompt. Salin, isi kurungan, guna.",
"""Peranan: Kau ialah [cth. copywriter jualan produk rumah dengan pengalaman 10 tahun].
Konteks: Aku ejen Coway di [kawasan]. Produk: [cth. penapis air].
         Audience: [cth. keluarga muda yang baru pindah rumah].
Tugas: [cth. Tulis 3 post Threads tentang kenapa ramai orang pasang penapis air di rumah].
Format: [cth. Bahasa Melayu santai, max 500 aksara, hook di ayat pertama, soalan di hujung].
Contoh: [tampal 1 post kau yang pernah dapat banyak respon]."""),

  ("P03", "Biar Claude tanya dulu", "Bila tak pasti nak minta apa, atau tugas tu besar.",
"""Aku nak [matlamat, cth. dapat 5 prospek tilam minggu ni].

Sebelum kau jawab, tanya aku 5 soalan paling penting untuk faham situasi aku.
Tanya satu soalan pada satu masa, dan tunggu jawapan aku."""),

  ("P04", "Ayat iterasi (baiki jawapan)", "Lepas Claude beri jawapan pertama. Pilih mana-mana satu.",
"""• Pendekkan jadi separuh, kekalkan isi paling penting.
• Tukar tone jadi lebih santai, macam kawan bagi cadangan.
• Beri 5 versi lain, setiap satu dengan hook yang berbeza.
• Apa yang paling lemah dalam jawapan kau tadi? Baiki bahagian tu.
• Buang apa-apa yang bunyi macam iklan atau template."""),

  ("P05", "Brand Brain ejen Coway (arahan Project)", "Tampal dalam 'Project instructions'. Upload juga brosur, senarai harga dan FAQ.",
"""Kau ialah pembantu jualan untuk [nama kau], ejen Coway di [kawasan servis].

TENTANG AKU
- Produk: penapis air, penapis udara, tilam, mesin basuh, aircon Coway
- Model yang aku fokus: [senarai model]
- Pakej: [sewa bulanan / beli tunai / ansuran] — [harga, jika boleh dikongsi]
- Promo semasa: [promo bulan ni + tarikh tamat]
- Servis & jaminan: [ikut polisi semasa Coway]

PELANGGAN AKU
- [cth. keluarga muda, pasangan baru pindah rumah, ibu bapa yang risau kualiti udara]

GAYA BAHASA
- Bahasa Melayu santai dan mesra, macam kawan bagi cadangan
- Panggil pelanggan: [kau / awak / tuan-puan]

PERATURAN
- Sentiasa jujur bahawa aku ejen Coway, bukan akaun rasmi syarikat.
- Jangan buat dakwaan kesihatan (cth. "sembuhkan asma"). Sebut fakta produk sahaja.
- Jangan sebut harga atau promo yang tiada dalam maklumat ni.
- Jangan kutuk jenama lain.
- Kalau tak pasti, tanya aku dulu."""),

  ("P06", "Profil pelanggan ideal untuk setiap produk", "Langkah pertama sebelum cari prospek. Jalankan dalam Project Brand Brain.",
"""Berdasarkan maklumat dalam project ni, bina profil pelanggan ideal untuk SETIAP produk
yang aku jual: penapis air, penapis udara, tilam, mesin basuh, aircon.

Untuk setiap produk, beri dalam jadual:
1. Siapa mereka (umur, situasi hidup)
2. "Detik pencetus" — apa yang berlaku sampai mereka mula cari produk ni
   (cth. pindah rumah, anak selalu bersin, aircon rosak)
3. 5 ayat yang mereka mungkin tulis di Threads bila ada masalah ni (bahasa santai/rojak)
4. Kebimbangan utama sebelum beli (cth. harga, kontrak sewa, servis)"""),

  ("P07", "Kata kunci carian Threads", "Lepas ada profil pelanggan. Hasilnya akan masuk ke RUNBOOK automation.",
"""Berdasarkan jadual profil pelanggan tadi, senaraikan kata kunci carian Threads
untuk cari orang yang SEDANG CARI produk, atau SEDANG ADA MASALAH yang produk aku selesaikan.

- 4 kata kunci untuk setiap produk (penapis air, penapis udara, tilam, mesin basuh, aircon)
- 4 kata kunci umum (cth. "baru pindah rumah")

Guna bahasa yang orang Malaysia betul-betul taip: Melayu, English dan rojak.
Tandakan ⭐ pada 10 yang paling berpotensi.
Elakkan kata kunci yang hanya akan jumpa iklan ejen lain."""),

  ("P08", "Nilai post Threads secara manual", "Lepas cari sendiri di Threads. Tampal beberapa post sekaligus.",
"""Aku akan tampal beberapa post Threads (username, lokasi jika ada, isi post, berapa lama dah post).

Untuk setiap post, beri:
- Skor: 🔥 KUAT / 🟡 SEDERHANA / ⚪ LEMAH / ❌ BUANG
- Produk Coway yang paling sesuai
- Sebab (1 ayat)

Kriteria:
🔥 Jelas sedang cari produk, atau ada masalah yang produk aku selesaikan, di [kawasan servis]
🟡 Ada minat atau masalah, tapi lokasi tak pasti atau keperluan kabur
⚪ Cuma bersembang, tiada niat jelas
❌ Iklan ejen lain / jenama pesaing, post Indonesia, luar kawasan, lebih 7 hari

Post:
[tampal di sini]"""),

  ("P09", "Draf reply pada post Threads", "Untuk prospek 🔥 dan 🟡. Kau yang copy dan reply sendiri.",
"""Tulis draf reply untuk post Threads ini:
Username: [ ]
Post: [ ]
Produk sesuai: [ ]

Peraturan:
- 1–3 ayat, Bahasa Melayu santai (rojak OK)
- Mula dengan respon kepada apa yang dia tulis — tunjuk kau faham masalah dia
- Beri satu tip atau info berguna, kemudian sebut aku ejen Coway di [kawasan]
- Ajak DM dengan lembut
- Tiada harga, tiada dakwaan kesihatan, max 1 emoji, tak bunyi macam template

Beri 3 versi."""),

  ("P10", "Balas bantahan prospek", "Bila prospek kata mahal, dah ada, takut kontrak, nak fikir dulu.",
"""Prospek balas: "[tampal, cth. mahal la sewa bulan-bulan / dah ada filter / takut terikat kontrak]"
Produk: [ ]

Beri 3 cara balas yang:
- jujur dan tak memaksa
- akui kebimbangan mereka dulu
- guna fakta dari maklumat dalam project ni SAHAJA
- ajak ke langkah kecil seterusnya (cth. tengok demo, tanya satu soalan)

Max 60 patah perkataan setiap satu."""),

  ("P11", "Follow-up prospek yang senyap", "Bila prospek dah DM tapi senyap lepas dapat info.",
"""Prospek ni dah DM aku, tapi senyap lepas aku bagi maklumat:
[tampal perbualan]

Tulis 3 mesej follow-up untuk hari ke-2, ke-5 dan ke-10.
Setiap mesej mesti beri nilai baru: tip berguna, testimoni pelanggan sebenar aku
([tampal testimoni]), atau soalan menarik — bukan "dah fikir ke?".
Max 40 patah perkataan setiap satu."""),

  ("P12", "Minta Claude rancang sistem dulu", "Prompt pertama dalam app Claude Desktop, sebelum bina apa-apa.",
"""Aku ejen Coway. Aku nak bina sistem automatik macam ni:

Setiap pagi dan malam, kau cari post di Threads dari orang yang sedang cari
penapis air, penapis udara, tilam, mesin basuh atau aircon di [kawasan].
Tapis yang betul-betul prospek, tulis draf reply untuk setiap satu,
dan hantar report ke group Telegram aku. Aku sendiri yang akan reply di Threads.

Sebelum bina apa-apa, terangkan pelan langkah demi langkah dalam bahasa mudah,
dan senaraikan apa yang aku perlu sediakan sendiri. Anggap aku tak tahu code."""),

  ("P13", "Langkah 1: Simpan info bisnes (offer.md)", "Dalam app Claude Desktop. Fail ni jadi sumber fakta untuk semua draf reply.",
"""Cipta folder projek di [cth. Documents\\coway-lead].

Dalam folder tu, cipta fail offer.md dengan maklumat bisnes aku:
[tampal isi Brand Brain dari P05]

Fail ni ialah sumber fakta untuk semua draf reply.
Jangan sesekali tambah harga, promo atau dakwaan yang tiada dalam fail ni."""),

  ("P14", "Langkah 2: Sambung bot Telegram", "Selepas cipta bot di @BotFather. JANGAN paste token dalam chat.",
"""Aku dah cipta bot Telegram melalui @BotFather. Aku TAK akan paste token dalam chat ni.

1. Cipta fail .env dalam folder projek dengan baris TELEGRAM_BOT_TOKEN= dan
   TELEGRAM_CHAT_ID= yang kosong. Aku akan paste token sendiri.
2. Tulis script untuk cari chat ID aku secara automatik, selepas aku tekan Start pada bot.
3. Tulis script send-report yang hantar fail atau teks ke Telegram,
   pecahkan mesej yang panjang, dan jangan sesekali paparkan token.

Lepas siap, beritahu aku apa yang perlu aku buat,
kemudian uji dengan hantar mesej "Ujian berjaya"."""),

  ("P15", "Langkah 3: Group Telegram dengan Topics", "Selepas cipta group, hidupkan Topics, dan jadikan bot admin.",
"""Aku nak report masuk ke satu group Telegram yang ada Topics:
- 🔎 Prospek Threads — report lead
- 💡 Bank Idea Content — idea post

Aku dah cipta group, hidupkan Topics, jadikan bot admin
(Manage Topics + Post Messages), dan hantar satu mesej dalam group.

Tulis script yang cari group tu, cipta 2 topic di atas, dan simpan ID-nya dalam .env.
Kemas kini send-report supaya boleh pilih topic. Kemudian uji."""),

  ("P16", "Langkah 4: Uji carian Threads", "Ujian pertama. Kau login Threads sendiri dalam browser app Claude.",
"""Buka Threads dalam browser app ni. Aku akan login sendiri — jangan masukkan kata laluan.

Lepas aku login, cari 3 kata kunci ni dengan tapisan "Recent":
[3 kata kunci ⭐ dari P07]

Untuk setiap post yang mungkin prospek, beri:
username, lokasi, berapa lama dah post, ringkasan keperluan, produk sesuai,
link post, skor (🔥/🟡/⚪) dan draf reply ikut offer.md.

Tunjuk dalam chat ni dulu.
JANGAN reply, like, follow atau DM sesiapa di Threads."""),

  ("P17", "Langkah 5: Tulis RUNBOOK (arahan tetap)", "Selepas ujian carian memuaskan. Inilah 'SOP' yang Claude ikut setiap kali run.",
"""Tulis fail RUNBOOK.md dalam folder projek. Ini arahan tetap yang kau ikut setiap kali cari lead.

1. CARI
- Guna browser app ni (Threads dah login), tapisan "Recent".
- Kata kunci, satu-satu, tunggu 3 saat setiap carian:
  [senarai 8–10 kata kunci ⭐]
- Kalau Threads ter-logout: berhenti, hantar amaran ke topic Prospek. Jangan cuba login.

2. TAPIS — simpan orang yang SEDANG CARI atau ADA MASALAH berkaitan produk Coway aku
- ✅ Kawasan [kawasan servis], atau lokasi tak disebut
- ❌ Buang: iklan ejen Coway lain & jenama pesaing, post Indonesia, barang jual,
  post lebih 7 hari, link yang dah ada dalam seen-leads.txt

3. NILAI — 🔥 kuat / 🟡 sederhana / ⚪ lemah, dan produk paling sesuai

4. DRAF REPLY — 1–3 ayat santai, khusus untuk post tu, sebut aku ejen Coway di [kawasan],
   ajak DM. Fakta dari offer.md sahaja. Tiada harga, tiada dakwaan kesihatan.

5. REPORT — simpan dalam reports/TARIKH-pagi.md atau -malam.md, format:
   🔎 Lead Threads: <tarikh> (<n> lead) - Sesi <Pagi/Malam>
   ---
   🔥 1. @username · <lokasi> · <berapa lama> · <produk>
   <ringkasan keperluan>
   🔗 <link>
   👇 Reply:
   ---
   <teks reply SAHAJA, dalam mesej berasingan supaya senang copy>
   ---
   Kalau tiada lead baru, hantar satu baris: "(0 lead) tiada lead baru".
   Hantar ke topic Prospek Threads, kemudian tambah link baru ke seen-leads.txt.

6. IDEA CONTENT (sesi pagi sahaja) — 2 idea post Threads berdasarkan soalan orang hari ni.
   Semak ideas-log.txt supaya tak berulang. Hantar ke topic Bank Idea Content.

PERATURAN: hanya BACA di Threads. Jangan reply, like, follow atau DM. Jangan paparkan token."""),

  ("P18", "Langkah 6: Jadualkan pagi & malam", "Langkah terakhir. Lepas ni sistem jalan sendiri.",
"""Cipta scheduled task bernama "coway-lead-threads" yang jalan setiap hari
pukul 9:00 pagi dan 9:00 malam.

Arahan untuk task:
- Baca RUNBOOK.md dan offer.md dalam folder [folder projek], dan ikut RUNBOOK sepenuhnya.
- Sebelum 3 petang = Sesi Pagi (lead + idea content). Selepas tu = Sesi Malam (lead sahaja).
- Akhiri dengan ringkasan satu baris: berapa lead baru, berapa yang 🔥, dan sama ada hantar berjaya.
- Kalau gagal, hantar mesej ralat ringkas ke topic Prospek.

Kemudian jalankan sekali sekarang sebagai ujian."""),

  ("P19", "Debug: sistem ada masalah", "Bila report tak masuk, lead berulang, atau kualiti lead/reply tak bagus.",
"""Run lead tadi ada masalah: [terangkan — cth. tiada report masuk Telegram /
lead berulang / reply terlalu formal / banyak iklan ejen lain].

Siasat puncanya (semak report, seen-leads.txt dan RUNBOOK),
terangkan dalam bahasa mudah, kemudian betulkan RUNBOOK atau script
supaya run seterusnya okay."""),

  ("P20", "Analisis hasil mingguan", "Setiap hujung minggu, dalam app Claude Desktop.",
"""Baca semua report dalam folder reports untuk minggu ni.
Hasil sebenar aku minggu ni: [cth. 12 reply, 5 DM, 2 closing — penapis air & tilam].

1. Kata kunci mana yang paling banyak beri lead 🔥?
2. Produk mana yang paling banyak permintaan?
3. Cadangkan 3 perubahan pada RUNBOOK (kata kunci, tapisan, gaya reply) untuk minggu depan."""),

  ("P21", "BONUS: Idea post Threads ejen Coway", "Supaya prospek datang sendiri ke ruang reply kau.",
"""Berdasarkan soalan dan masalah yang orang tulis di Threads minggu ni
(baca folder reports), beri 10 idea post Threads untuk ejen Coway — 2 untuk setiap produk.

Untuk setiap idea:
- Ayat hook yang buat orang berhenti scroll
- 3 poin isi (keseluruhan max 500 aksara)
- Soalan penutup yang dorong orang reply

Tiada dakwaan kesihatan. Tiada harga."""),
]

# ---------------------------------------------------------------------------
# SLIDE
# ---------------------------------------------------------------------------
from helpers import bullets, cards, flow, table, promptbox, note

TG_EXAMPLE = (
  '<div class="tgwrap">'
  '<div class="tg"><b>🔎 Lead Threads: 26 Nov 2026 (3 lead) - Sesi Pagi</b></div>'
  '<div class="tg">🔥 1. @contoh_ibu2anak · Shah Alam · 3 jam lepas · Penapis air<br>'
  'Baru pindah rumah, air paip keruh, minta recommend water filter.<br>🔗 threads.com/@contoh_ibu2anak/post/…<br>👇 Reply:</div>'
  '<div class="tg reply">Hi! Air keruh lepas pindah memang selalu jadi sebab paip lama. Ramai pasang penapis air terus kat sinki supaya senang. '
  'Saya ejen Coway area Shah Alam, boleh DM kalau nak tengok pilihan yang sesuai 🙂</div>'
  '<div class="tg">🟡 2. @contoh_user · lokasi tak pasti · 1 hari lepas · Tilam …</div>'
  '</div>'
)

SLIDES = [
# ===== PEMBUKAAN =====
dict(layout="cover", title=COURSE_TITLE, body=COURSE_SUB,
  notes=[
    "Perkenalkan diri: siapa kau, berapa lama jual Coway, dan macam mana kau guna Claude setiap hari.",
    "Beritahu peserta: tak perlu tahu apa-apa pasal AI atau code. Kita mula dari kosong, dan Claude yang tulis semua code.",
    "Pastikan semua peserta dah buka laptop dan dah terima PDF Prompt Pack — kita salin prompt dari situ sepanjang kelas.",
    "Tetapkan peraturan: soalan boleh tanya bila-bila masa; latihan hands-on wajib buat sama-sama.",
  ]),

dict(layout="std", kicker="Kenapa kelas ni", title="Cabaran ejen Coway cari prospek",
  body=cards([
    ("Post iklan, senyap", "Post brosur dan promo, tapi tak ada orang tanya."),
    ("Prospek ada, tapi tak nampak", "Setiap hari orang tanya pasal penapis air dan tilam di Threads — tapi tenggelam dalam feed."),
    ("Reply macam template", "\"PM untuk harga\" — orang terus scroll."),
    ("Masa habis scroll", "Cari prospek manual makan berjam-jam, dan esok kena mula semula."),
  ], 2),
  notes=[
    "Tanya peserta: 'Berapa jam seminggu korang habiskan cari prospek online?' Biar 2–3 orang jawab.",
    "Tekankan: prospek SEDANG wujud di Threads — orang tulis 'air rumah keruh', 'aircon rosak', 'tilam buat sakit belakang' setiap hari.",
    "Masalahnya bukan tiada prospek, tapi tiada SISTEM untuk jumpa mereka setiap hari.",
    "Peralihan: 'Sekarang aku tunjuk sistem yang aku guna sendiri.'",
  ]),

dict(layout="accent", kicker="Demo hasil akhir", title="Ini yang korang akan bina",
  body='<div class="big">Setiap pagi &amp; malam, Claude cari prospek Coway di Threads → tapis → tulis draf reply → hantar ke Telegram korang.</div>'
       '<p class="lead-l">DEMO LIVE: tunjuk group Telegram kau dan report lead yang masuk hari ni.</p>',
  notes=[
    "INI SLIDE PALING PENTING — tunjuk hasil akhir DULU supaya peserta nampak destinasi.",
    "Buka Telegram di skrin: tunjuk group dengan 2 topic (🔎 Prospek Threads, 💡 Bank Idea Content).",
    "Tunjuk satu report: lead + link, dan reply dalam mesej berasingan. Demo: tekan lama → Copy → buka link → paste reply di Threads.",
    "Tunjuk scheduled task dalam app Claude Desktop yang jalan pukul 9 pagi & 9 malam.",
    "Tutup dengan: 'Korang tak tulis satu baris code pun. Korang cuma bercakap dengan Claude.'",
  ]),

dict(layout="std", kicker="Peta perjalanan", title="5 bahagian, dari zero ke automation",
  body=table(["Bahagian", "Topik", "Hasil"], [
    ["1", "<b>Kenal Claude</b> — akaun, app desktop, chat pertama", "Akaun siap"],
    ["2", "<b>Seni Prompting</b> — formula, iterasi, Brand Brain", "Claude kenal bisnes Coway korang"],
    ["3", "<b>Kenal prospek Coway</b> — 5 produk, keyword, reply", "Keyword + reply yang laku"],
    ["4", "<b>Asas automation</b> — Trigger → Claude → Tindakan", "Faham komponen sistem"],
    ["5", "<b>Mesin cari prospek</b> — bina 6 langkah", "Sistem jalan sendiri pagi &amp; malam"],
  ]),
  notes=[
    "Logik susunan: buat MANUAL dulu (Bahagian 3), baru automate (Bahagian 4–5).",
    "Sebab: kalau tak faham apa itu prospek yang bagus, automation akan cari benda yang salah.",
    "Nombor prompt tertera di bawah setiap slide — peserta cari dalam PDF Prompt Pack.",
  ]),

# ===== BAHAGIAN 1 =====
dict(layout="section", kicker="Bahagian 1", title="Kenal Claude", body="Dari tak pernah guna AI ke chat pertama"),

dict(layout="std", kicker="Bahagian 1 · Konsep", title="Apa itu Claude?",
  body='<div class="g2c"><div>'
       + bullets([
          "Pembantu AI dari syarikat Anthropic",
          "Faham dan tulis Bahasa Melayu &amp; rojak",
          "Kuat menulis, berfikir, baca brosur PDF &amp; gambar",
          "App desktop boleh buka browser, buat fail &amp; jalan ikut jadual",
        ])
       + '</div><div class="card soft"><h3>Analogi mudah</h3><p>Claude macam <b>pembantu jualan baru yang sangat pandai</b> — tapi hari pertama, dia tak kenal produk Coway, harga, atau gaya korang.</p><p style="margin-top:10px">Makin banyak korang terangkan, makin bagus kerja dia.</p></div></div>',
  notes=[
    "Elak istilah teknikal (LLM, model, token). Guna analogi pembantu jualan baru.",
    "Prompt = arahan kerja. Project = buku panduan produk. Automation = SOP yang pembantu jalankan sendiri ikut jadual.",
    "Sebut had: Claude boleh silap, terutama fakta produk dan harga. Sebab tu kita bagi dia fakta yang betul (Bahagian 2).",
  ]),

dict(layout="std", kicker="Bahagian 1 · Persediaan", title="Apa yang korang perlukan",
  body=table(["", "Bahagian 1–3", "Bahagian 4–5 (automation)"], [
    ["Akaun Claude", "Free pun boleh", "Plan berbayar (Pro / Max)"],
    ["Peranti", "Browser atau app fon", "<b>App Claude Desktop</b> di laptop/PC"],
    ["Akaun lain", "—", "Threads + Telegram"],
    ["Komputer", "—", "Hidup &amp; app terbuka pada waktu jadual"],
  ]) + '<p class="small muted" style="margin-top:16px">Harga, plan &amp; ciri berubah dari masa ke masa — semak claude.ai/pricing dan claude.ai/download.</p>',
  notes=[
    "Jangan paksa upgrade hari ini. Bahagian 1–3 boleh ikut dengan akaun Free.",
    "Untuk automation, mereka perlukan app Claude Desktop (Windows/Mac) dan plan berbayar — sistem ni guna browser terbina dalam app dan scheduled task.",
    "Komputer mesti hidup dan app terbuka pada pukul 9 pagi & 9 malam. Ini had paling penting — terangkan dari awal.",
    "SEMAK harga & ciri terkini sebelum kelas — jangan sebut dari ingatan.",
  ]),

dict(layout="std", kicker="Bahagian 1 · Hands-on", title="Buka akaun &amp; kenal skrin",
  body=flow([
    ("1", "claude.ai", "Daftar guna emel atau akaun Google."),
    ("2", "Kotak chat", "Tempat taip arahan (prompt)."),
    ("3", "Butang +", "Upload brosur, senarai harga, screenshot."),
    ("4", "Projects", "Folder kerja yang Claude 'ingat'."),
    ("5", "App Desktop", "Muat turun untuk Bahagian 4–5."),
  ]),
  notes=[
    "Buat LIVE: buka claude.ai dan tunjuk setiap bahagian skrin.",
    "Bagi peserta 5 minit untuk daftar. Bantu yang tersangkut (biasanya pengesahan emel).",
    "Tunjuk di mana muat turun app Claude Desktop — minta peserta pasang semasa rehat.",
  ]),

dict(layout="std", kicker="Bahagian 1 · Latihan", title="Chat pertama",
  body=promptbox("P01") + note("Latihan 5 minit: salin P01, isi kurungan, hantar. Baca jawapan Claude."),
  prompts=["P01"],
  notes=[
    "Peserta buka PDF Prompt Pack, cari P01, salin dan isi kurungan.",
    "Lepas 5 minit, minta 2–3 peserta kongsi jawapan yang paling mengejutkan mereka.",
    "Titik pengajaran: jawapan spesifik untuk Coway sebab mereka beri konteks.",
  ]),

# ===== BAHAGIAN 2 =====
dict(layout="section", kicker="Bahagian 2", title="Seni Prompting", body="Cara bagi arahan supaya hasil tak hambar"),

dict(layout="std", kicker="Bahagian 2 · Konsep", title="Kenapa output AI selalu hambar?",
  body='<div class="g2c"><div class="card"><div class="lbl bad">Prompt lemah</div><div class="pmini">Tulis post pasal penapis air Coway.</div><p class="muted small" style="margin-top:12px">Claude terpaksa meneka semuanya → bunyi macam iklan biasa.</p></div>'
       '<div class="card"><div class="lbl good">Prompt kuat</div><div class="pmini">Kau copywriter produk rumah. Tulis 3 post Threads untuk keluarga muda yang baru pindah rumah di Shah Alam, tentang kenapa ramai pasang penapis air. Santai, max 500 aksara, hook di ayat pertama, soalan di hujung. Tiada harga.</div></div></div>'
       + '<p class="lead" style="margin-top:22px">Sampah masuk, sampah keluar. <b>Konteks</b> masuk, <b>hasil</b> keluar.</p>',
  notes=[
    "Buat LIVE: hantar kedua-dua prompt, tunjuk beza hasilnya sebelah-menyebelah.",
    "Tanya peserta: 'Mana satu korang akan post?' Biar mereka sendiri nampak beza.",
  ]),

dict(layout="std", kicker="Bahagian 2 · Formula", title="Formula P.K.T.F.C",
  body='<div class="g2c" style="grid-template-columns:1fr 1.3fr">'
       + bullets([
          "<b>P</b>eranan — siapa Claude patut jadi",
          "<b>K</b>onteks — produk, kawasan, audience",
          "<b>T</b>ugas — apa sebenarnya nak dibuat",
          "<b>F</b>ormat — panjang, bahasa, gaya",
          "<b>C</b>ontoh — post lama yang laku",
        ]) + promptbox("P02", compact=True) + '</div>',
  prompts=["P02"],
  notes=[
    "Terangkan setiap huruf dengan contoh Coway.",
    "'Contoh' paling kerap dilupakan tapi paling berkesan — tampal post lama yang pernah dapat banyak respon.",
    "Latihan 5 minit: peserta guna P02 untuk satu produk yang mereka paling banyak jual.",
  ]),

dict(layout="std", kicker="Bahagian 2 · Teknik", title="Rahsia sebenar: iterasi",
  body='<div class="g2c">' + promptbox("P03", compact=True) + promptbox("P04", compact=True) + '</div>',
  prompts=["P03", "P04"],
  notes=[
    "Prompt pertama jarang sempurna — itu normal. Berbual dengan Claude 3–5 pusingan.",
    "P03: bila tak tahu nak minta apa, suruh Claude TANYA dulu.",
    "P04: tunjuk LIVE — ambil jawapan tadi, guna 2 ayat dari P04.",
  ]),

dict(layout="std", kicker="Bahagian 2 · Hands-on", title="Project 'Brand Brain' ejen Coway",
  body='<div class="g2c" style="grid-template-columns:1fr 1.3fr"><div>'
       + bullets([
          "<b>Projects → Create project</b>",
          "Nama: <i>Coway [nama kau] Brand Brain</i>",
          "Tampal P05 dalam <b>Project instructions</b>",
          "Upload: brosur produk, senarai harga, FAQ, testimoni",
          "Semua chat dalam project ni = Claude dah kenal bisnes kau",
        ], small=True) + '</div><div>' + promptbox("P05", hide_body=True)
       + table(["Bahagian P05", "Isi"], [
          ["Tentang aku", "Produk, model, pakej, promo, servis"],
          ["Pelanggan aku", "Siapa yang biasa beli"],
          ["Gaya bahasa", "Santai, cara panggil pelanggan"],
          ["Peraturan", "Jujur sebagai ejen · tiada dakwaan kesihatan · tiada harga tak sah · tak kutuk jenama lain"],
        ], small=True) + '</div></div>',
  prompts=["P05"],
  notes=[
    "Project = buku panduan produk untuk pembantu baru.",
    "Bagi 10 minit isi P05. Ini ASAS untuk semua bahagian seterusnya — dan nanti jadi fail offer.md dalam automation.",
    "Tekankan 3 peraturan: jujur sebagai ejen (bukan akaun rasmi), tiada dakwaan kesihatan, tiada harga yang tak disahkan.",
    "Ujian: dalam project tu, tanya 'Apa promo aku bulan ni?' — Claude patut jawab tepat, atau cakap tak tahu.",
  ]),

# ===== BAHAGIAN 3 =====
dict(layout="section", kicker="Bahagian 3", title="Kenal Prospek Coway", body="Buat secara manual dulu — baru kita automate"),

dict(layout="std", kicker="Bahagian 3 · Peta prospek", title="5 produk, 5 jenis prospek",
  body=table(["Produk", "Detik pencetus", "Contoh ayat di Threads"], [
    ["💧 Penapis air", "Pindah rumah, air keruh, risau kualiti air", "\"Air paip rumah baru keruh, nak pasang filter apa?\""],
    ["🌬️ Penapis udara", "Rumah berhabuk, jerebu, ada bayi", "\"Rumah selalu berhabuk, air purifier berbaloi tak?\""],
    ["🛏️ Tilam", "Tidur tak lena, tilam lama", "\"Tilam dah 10 tahun, recommend tilam bagus?\""],
    ["🧺 Mesin basuh", "Mesin rosak, keluarga bertambah", "\"Mesin basuh rosak lagi, nak tukar brand apa?\""],
    ["❄️ Aircon", "Panas, bil elektrik tinggi, aircon rosak", "\"Aircon bilik tak sejuk, baiki ke beli baru?\""],
  ], small=True) + note("Prospek terbaik ialah orang yang <b>sendiri</b> tulis masalah mereka — mereka dah 'angkat tangan'."),
  notes=[
    "Terangkan konsep 'detik pencetus': orang tak cari penapis air setiap hari — mereka cari bila sesuatu berlaku.",
    "Tanya peserta: 'Produk mana paling laku untuk korang? Apa yang biasanya buat pelanggan mula tanya?'",
    "Contoh ayat dalam jadual ialah rekaan; minta peserta tambah ayat sebenar yang pernah mereka dengar dari pelanggan.",
  ]),

dict(layout="std", kicker="Bahagian 3 · Langkah 1–2", title="Profil pelanggan &amp; kata kunci Threads",
  body='<div class="g2c">' + promptbox("P06", compact=True) + promptbox("P07", compact=True) + '</div>',
  prompts=["P06", "P07"],
  notes=[
    "P06 dalam Project Brand Brain: profil pelanggan untuk setiap produk.",
    "P07: kata kunci carian. SIMPAN 10 kata kunci ⭐ — ini akan masuk terus ke RUNBOOK automation nanti.",
    "Amaran: kata kunci seperti 'Coway' atau 'promo penapis air' kebanyakannya jumpa iklan ejen lain. Cari ayat MASALAH, bukan nama produk.",
  ]),

dict(layout="std", kicker="Bahagian 3 · Langkah 3", title="Cari sendiri di Threads &amp; nilai",
  body='<div class="g2c" style="grid-template-columns:1fr 1.3fr"><div>'
       + '<div class="score hot">🔥 KUAT<span>Jelas cari produk / ada masalah, dalam kawasan</span></div>'
       + '<div class="score warm">🟡 SEDERHANA<span>Ada minat, lokasi atau keperluan kabur</span></div>'
       + '<div class="score cold">⚪ LEMAH<span>Sembang sahaja, tiada niat jelas</span></div>'
       + '<p class="small muted">❌ Buang: iklan ejen lain, post Indonesia, luar kawasan, &gt; 7 hari</p>'
       + '</div>' + promptbox("P08", compact=True) + '</div>',
  prompts=["P08"],
  notes=[
    "Latihan 15 minit: buka Threads, cari 3 kata kunci ⭐, tab 'Recent'. Salin 5–10 post ke P08.",
    "Bincang: setuju tak dengan skor Claude? Kalau tak, beritahu Claude kenapa.",
    "Kriteria yang mereka betulkan di sini akan masuk ke RUNBOOK (P17).",
    "Ingatkan: banyak post datang dari ejen Coway lain — itu bukan prospek.",
  ]),

dict(layout="std", kicker="Bahagian 3 · Langkah 4", title="Reply pada post — bukan spam DM",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div>'
       + bullets([
          "Reply pada post orang tu — dia yang mula bertanya",
          "Respon kepada masalah dia dulu, baru sebut Coway",
          "Satu tip berguna &gt; seribu \"PM untuk harga\"",
          "Jujur: \"Saya ejen Coway area ___\"",
          "Ajak DM dengan lembut",
        ], small=True)
       + '</div>' + promptbox("P09", compact=True) + '</div>',
  prompts=["P09"],
  notes=[
    "Peraturan emas: reply yang bantu, bukan reply yang jual.",
    "Peserta jalankan P09 untuk 3 prospek 🔥 mereka, kemudian pilih versi terbaik.",
    "Tekankan: KORANG yang reply sendiri. Claude tulis draf; korang sesuaikan dan hantar.",
    "Tiada dakwaan kesihatan (cth. 'elak penyakit', 'sembuhkan asma') — boleh buat masalah dengan syarikat dan undang-undang.",
  ]),

dict(layout="std", kicker="Bahagian 3 · Langkah 5", title="Bila prospek DM: bantahan &amp; follow-up",
  body='<div class="g2c">' + promptbox("P10", compact=True) + promptbox("P11", compact=True) + '</div>',
  prompts=["P10", "P11"],
  notes=[
    "Bantahan biasa ejen Coway: mahal, dah ada, takut kontrak sewa, nak tanya suami/isteri dulu.",
    "Minta peserta senaraikan 3 bantahan paling kerap mereka dengar, dan jalankan P10 untuk setiap satu.",
    "P11: kebanyakan jualan berlaku selepas follow-up ke-2 atau ke-3. Testimoni pelanggan sebenar paling berkesan.",
    "Peralihan: 'Korang dah buat semua ni manual. Sekarang bayangkan Claude buat bahagian cari, tapis dan tulis draf — setiap pagi dan malam.'",
  ]),

# ===== BAHAGIAN 4 =====
dict(layout="section", kicker="Bahagian 4", title="Asas Automation", body="Satu konsep, lima komponen"),

dict(layout="std", kicker="Bahagian 4 · Konsep", title="Trigger → Claude → Tindakan",
  body=flow([
    ("⏰", "TRIGGER", "Jadual: setiap hari pukul 9 pagi &amp; 9 malam."),
    ("🧠", "CLAUDE", "Cari di Threads, tapis, nilai, tulis draf reply."),
    ("📲", "TINDAKAN", "Hantar report ke group Telegram korang."),
  ], arrows=True, big=True) + '<p class="lead" style="margin-top:28px">Korang tak perlu buka Threads untuk cari — korang cuma buka Telegram dan reply.</p>',
  notes=[
    "Ini satu-satunya konsep yang mereka MESTI faham. Ulang 2–3 kali.",
    "Automation = SOP yang pembantu jalankan sendiri, tanpa disuruh setiap kali.",
    "Minta peserta beri 1 lagi contoh kerja harian dalam bentuk Trigger → Claude → Tindakan.",
  ]),

dict(layout="std", kicker="Bahagian 4 · Komponen", title="5 komponen sistem",
  body=table(["Komponen", "Fungsi", "Analogi"], [
    ["<b>App Claude Desktop</b>", "Tempat Claude bekerja di komputer korang", "Pejabat"],
    ["<b>Browser dalam app</b>", "Claude buka Threads dengan akaun korang (dah login)", "Mata"],
    ["<b>Fail projek</b>", "offer.md (fakta), RUNBOOK.md (SOP), seen-leads.txt (rekod)", "Buku panduan"],
    ["<b>Bot Telegram</b>", "Hantar report ke group dengan Topics", "Posmen"],
    ["<b>Scheduled task</b>", "Jalankan semua ni pukul 9 pagi &amp; 9 malam", "Jam loceng"],
  ]),
  notes=[
    "Terangkan setiap komponen dengan analogi. Jangan masuk detail teknikal.",
    "Penting: semua ni berjalan di KOMPUTER korang. Komputer mesti hidup dan app terbuka pada waktu jadual.",
    "Nama menu dalam app Claude Desktop mungkin berubah — semak versi terkini sebelum kelas.",
  ]),

dict(layout="std", kicker="Bahagian 4 · Prinsip", title="Korang tak tulis code — korang bercakap",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div>'
       + bullets([
          "Claude tulis semua script &amp; fail",
          "Korang terangkan apa yang korang nak, dalam Bahasa Melayu",
          "Minta Claude <b>rancang dulu</b>, baru bina",
          "Bina satu langkah, uji, baru langkah seterusnya",
          "Token &amp; kata laluan: korang masukkan sendiri, <b>jangan paste dalam chat</b>",
        ], small=True)
       + '</div>' + promptbox("P12", compact=True) + '</div>',
  prompts=["P12"],
  notes=[
    "Ini perubahan minda paling besar: automation bukan untuk programmer sahaja lagi.",
    "Buat LIVE: jalankan P12 dalam app Claude Desktop. Tunjuk Claude terangkan pelan dan senaraikan apa yang peserta perlu sediakan.",
    "Prinsip 'bina satu, uji satu' — kalau rosak, senang tahu di mana.",
  ]),

# ===== BAHAGIAN 5 =====
dict(layout="section", kicker="Bahagian 5", title="Mesin Cari Prospek", body="Bina langkah demi langkah dalam app Claude Desktop"),

dict(layout="std", kicker="Bahagian 5 · Peta", title="6 langkah bina sistem",
  body=flow([
    ("1", "Info bisnes", "offer.md (P13)"),
    ("2", "Bot Telegram", "BotFather + script (P14)"),
    ("3", "Group &amp; Topics", "Prospek + Idea (P15)"),
  ]) + '<div style="height:16px"></div>' + flow([
    ("4", "Uji carian", "Login Threads + cari (P16)"),
    ("5", "RUNBOOK", "SOP tetap (P17)"),
    ("6", "Jadual", "9 pagi &amp; 9 malam (P18)"),
  ]),
  notes=[
    "Tunjuk semula demo dari awal kelas — sekarang peserta akan faham setiap bahagian.",
    "Setiap langkah = satu prompt. Peserta salin prompt, Claude buat kerja, kita uji, baru teruskan.",
    "Masa: kira-kira 60–90 minit untuk semua 6 langkah.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Langkah 1", title="Simpan info bisnes",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div>'
       + bullets([
          "Buka app Claude Desktop",
          "Pilih folder kerja (cth. Documents)",
          "Salin P13, tampal isi Brand Brain (P05)",
          "Hasil: folder <code>coway-lead</code> + fail <code>offer.md</code>",
        ], small=True)
       + note("offer.md = satu-satunya sumber fakta. Kalau promo bertukar, kemas kini fail ni.")
       + '</div>' + promptbox("P13", compact=True) + '</div>',
  prompts=["P13"],
  notes=[
    "Kenapa fail ni penting: scheduled task jalan tanpa korang. Claude mesti ada fakta yang betul dalam fail, bukan dalam ingatan chat.",
    "Ingatkan: kemas kini offer.md setiap kali promo atau harga berubah.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Langkah 2", title="Cipta &amp; sambung bot Telegram",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div class="card"><h3>Buat sendiri di Telegram</h3>'
       + bullets([
          "Cari <b>@BotFather</b> (tanda biru ✔️)",
          "Taip <code>/newbot</code>, beri nama &amp; username (mesti berakhir dengan <i>bot</i>)",
          "Simpan <b>token</b> — rahsia!",
          "Buka bot baru → tekan <b>Start</b>",
          "Guna bot BARU, bukan bot ChatGPT/lain",
        ], small=True)
       + '</div>' + promptbox("P14", compact=True) + '</div>',
  prompts=["P14"],
  notes=[
    "Buat LIVE di Telegram: cipta bot dengan BotFather.",
    "Token = kunci rumah. JANGAN paste dalam chat Claude. Claude cipta fail .env, korang buka fail tu dan paste token sendiri.",
    "Kenapa bot baru: satu bot hanya boleh 'dengar' satu sistem. Kongsi bot dengan ChatGPT atau tool lain boleh buat kedua-duanya rosak.",
    "Kejayaan: peserta terima mesej 'Ujian berjaya' dari bot mereka.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Langkah 3", title="Group Telegram dengan Topics",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div class="card"><h3>Buat sendiri di Telegram</h3>'
       + bullets([
          "New Group → tambah bot",
          "Edit group → hidupkan <b>Topics</b>",
          "Administrators → jadikan bot admin",
          "Tanda ✅ <b>Manage Topics</b> &amp; <b>Post Messages</b>",
          "Hantar satu mesej dalam group",
        ], small=True)
       + '</div>' + promptbox("P15", compact=True) + '</div>',
  prompts=["P15"],
  notes=[
    "Kenapa group dengan Topics: report lead dan idea content tak bercampur.",
    "Masalah biasa: bila Topics dihidupkan, Telegram 'upgrade' group dan hak admin bot kadang-kadang hilang. Semak semula hak admin bot.",
    "Kejayaan: 2 topic muncul dalam group, dicipta oleh bot sendiri.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Langkah 4", title="Login Threads &amp; uji carian",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div>'
       + bullets([
          "Claude buka Threads dalam browser app",
          "Korang <b>login sendiri</b> — sekali sahaja, login kekal",
          "Claude cari 3 kata kunci, tab <b>Recent</b>",
          "Hasil ditunjuk dalam chat dulu",
          "Nilai: lead betul? Reply sedap?",
        ], small=True)
       + '</div>' + promptbox("P16", compact=True) + '</div>',
  prompts=["P16"],
  notes=[
    "Langkah paling menarik untuk peserta — mereka nampak Claude 'scroll' Threads sendiri.",
    "Kalau browser pane tersembunyi, tunjuk cara paparkannya dalam app.",
    "Jangan teruskan ke langkah 5 selagi kualiti lead dan reply belum memuaskan. Guna P04 untuk baiki gaya reply.",
    "Tekankan: Claude hanya BACA. Tiada reply, like, follow atau DM automatik.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Langkah 5", title="RUNBOOK: SOP yang Claude ikut setiap kali",
  body='<div class="g2c"><div>'
       + table(["Bahagian", "Isi"], [
          ["1. Cari", "8–10 kata kunci ⭐, tab Recent, satu-satu"],
          ["2. Tapis", "Kawasan servis; buang ejen lain, Indonesia, &gt; 7 hari, lead lama"],
          ["3. Nilai", "🔥 / 🟡 / ⚪ + produk sesuai"],
          ["4. Reply", "Ikut offer.md, tiada harga &amp; dakwaan kesihatan"],
          ["5. Report", "Format Telegram, reply dalam mesej berasingan"],
          ["6. Idea", "2 idea post (sesi pagi)"],
        ], small=True)
       + '</div><div>' + promptbox("P17", hide_body=True)
       + note("Prompt P17 panjang — salin penuh dari Prompt Pack, isi kata kunci ⭐ dan kawasan servis korang.")
       + '</div></div>',
  prompts=["P17"],
  notes=[
    "RUNBOOK = SOP. Scheduled task baca fail ni setiap kali, jadi hasil konsisten.",
    "Peserta isi 2 bahagian sendiri: senarai kata kunci ⭐ dari P07, dan kawasan servis.",
    "seen-leads.txt menyimpan setiap link yang dah dihantar — sesi malam takkan ulang lead sesi pagi.",
    "Bila nak ubah apa-apa (keyword, gaya reply), cakap dengan Claude: 'kemas kini RUNBOOK supaya …'.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Hasil", title="Rupa report dalam Telegram",
  body='<div class="g2c" style="grid-template-columns:1.2fr 1fr">' + TG_EXAMPLE + '<div>'
       + bullets([
          "Tajuk: tarikh, bilangan lead, <b>Sesi Pagi/Malam</b>",
          "Mesej lead: siapa, kawasan, produk, link",
          "Mesej reply <b>berasingan</b> → tekan lama → Copy",
          "Buka link → paste → sesuaikan → reply",
          "Tiada lead? Satu baris sahaja",
        ], small=True) + '</div></div>',
  notes=[
    "Tunjuk report sebenar dari Telegram kau sebagai perbandingan.",
    "Kenapa reply dalam mesej berasingan: bila tekan lama → Copy, yang tersalin cuma teks reply.",
    "Rutin harian: buka Telegram, reply 5–10 lead 🔥, selesai dalam 15 minit.",
    "Contoh dalam slide ni rekaan — username dan post bukan orang sebenar.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Langkah 6", title="Jadualkan &amp; kawal dari fon",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div>'
       + table(["", "9:00 pagi", "9:00 malam"], [
          ["Cari lead", "✅", "✅"],
          ["Report → 🔎 Prospek", "✅", "✅"],
          ["2 idea → 💡 Idea", "✅", "—"],
        ], small=True)
       + '<p class="small" style="margin-top:14px"><b>Kenapa 9 malam?</b> Waktu paling aktif di Threads selepas kerja.<br><b>Kenapa tak lebih kerap?</b> Carian berulang nampak macam bot.</p>'
       + '<p class="small muted" style="margin-top:10px">Remote Control: kawal sesi Claude di komputer dari app Claude di fon.</p>'
       + '</div>' + promptbox("P18", compact=True) + '</div>',
  prompts=["P18"],
  notes=[
    "Selepas P18, Claude jalankan ujian sekali. Semak report masuk ke Telegram.",
    "Syarat: komputer hidup dan app Claude terbuka pada waktu jadual. Tetapkan komputer supaya tak sleep.",
    "Kalau app tertutup pada pukul 9, task akan jalan bila app dibuka semula.",
    "Remote Control: tunjuk cara buka sesi dari app Claude di fon — boleh suruh 'cari lead sekarang' dari luar rumah.",
  ]),

dict(layout="accent", kicker="Demo &amp; build", title="Jom bina sama-sama",
  body='<div class="big">6 langkah, satu prompt setiap langkah — uji sebelum teruskan.</div><p class="lead-l">Checkpoint: angkat tangan bila mesej masuk ke Telegram korang.</p>',
  notes=[
    "Sesi paling panjang (60–90 minit). Buat LIVE, satu langkah pada satu masa, tunggu semua siap.",
    "Checkpoint selepas setiap langkah: Langkah 2 = mesej ujian sampai. Langkah 3 = 2 topic muncul. Langkah 4 = lead keluar dalam chat. Langkah 6 = report masuk Telegram.",
    "Guna P19 bila ada masalah — ajar peserta minta Claude debug sendiri.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Masalah biasa", title="Bila sistem tak jalan",
  body=table(["Masalah", "Punca biasa", "Penyelesaian"], [
    ["Tiada report pukul 9", "Komputer sleep / app tertutup", "Tetapkan sleep: Never, biar app terbuka"],
    ["Amaran \"Threads logged out\"", "Sesi login tamat", "Login semula dalam browser app"],
    ["Bot tak boleh hantar ke topic", "Bot hilang hak admin", "Beri semula Manage Topics + Post Messages"],
    ["Lead berulang", "seen-leads.txt tak dikemas kini", "P19"],
    ["Banyak iklan ejen lain", "Kata kunci terlalu umum", "Tukar ke ayat masalah, tambah tapisan"],
  ], small=True) + promptbox("P19", hide_body=True, style="margin-top:16px"),
  prompts=["P19"],
  notes=[
    "Kebanyakan masalah bukan code — tapi komputer sleep atau hak admin bot.",
    "Untuk masalah lain, P19: terangkan masalah dalam Bahasa Melayu biasa, biar Claude siasat dan betulkan.",
  ]),

dict(layout="dark", kicker="Penting", title="Etika, syarikat &amp; keselamatan akaun",
  body=cards([
    ("Claude hanya baca", "Tiada auto-reply, like, follow atau DM. Korang yang reply, 5–10 sehari."),
    ("Jujur sebagai ejen", "Jangan guna nama/logo seolah-olah akaun rasmi Coway. Ikut garis panduan syarikat."),
    ("Tiada dakwaan kesihatan", "Sebut fakta produk sahaja. Jangan janji \"sembuh\" atau \"elak penyakit\"."),
    ("Data &amp; token", "Hormati PDPA. Token bot &amp; kata laluan jangan dikongsi atau di-paste dalam chat."),
  ], 2),
  notes=[
    "Jangan langkau slide ni. Satu akaun yang disekat, atau satu aduan kepada syarikat, boleh hapuskan semua hasil.",
    "Carian kecil, berjadual, dengan akaun sendiri — sama macam korang cari sendiri. Elak tool 'scraper' yang melanggar terma Meta.",
    "Semak dengan pengurus/syarikat tentang garis panduan pemasaran ejen di media sosial.",
    "Akta Perlindungan Data Peribadi 2010 (PDPA) terpakai bila simpan data orang untuk tujuan jualan.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Ukur", title="Ukur hasil setiap minggu",
  body=cards([
    ("Lead 🔥 seminggu", "Kualiti kata kunci korang."),
    ("Reply dihantar", "Disiplin harian."),
    ("DM masuk", "Kualiti reply korang."),
    ("Closing", "Ikut produk."),
  ], 4) + promptbox("P20", compact=True, style="margin-top:20px"),
  prompts=["P20"],
  notes=[
    "Automation bukan 'set and forget'. Semak sekali seminggu.",
    "Lead 🔥 sikit → baiki kata kunci. DM sikit → baiki gaya reply dalam RUNBOOK.",
    "Peserta catat hasil sendiri (reply, DM, closing) — Claude tak nampak apa berlaku selepas mereka reply.",
  ]),

dict(layout="accent", kicker="Penutup", title="Tugasan 7 hari",
  body=bullets([
    "Hari 1: Lengkapkan Brand Brain &amp; offer.md (P05, P13)",
    "Hari 2: Pastikan sistem jalan pagi &amp; malam",
    "Hari 3–6: Reply 5–10 lead 🔥 sehari, follow-up DM (P10, P11)",
    "Hari 7: Analisis hasil (P20) &amp; kongsi dalam group",
    "BONUS: Post 1 idea dari Bank Idea Content setiap hari (P21)",
  ], light=True),
  prompts=["P21"],
  notes=[
    "Beri tugasan konkrit supaya ilmu jadi tabiat.",
    "Minta peserta kongsi screenshot report Telegram dan hasil minggu pertama dalam group support.",
    "P21: post yang betul buat prospek datang sendiri — gabungkan dengan reply harian untuk hasil terbaik.",
    "Tutup dengan sesi soal jawab dan ingatkan tentang group support.",
  ]),
]
