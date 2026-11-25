# -*- coding: utf-8 -*-
"""Kandungan kursus: slide, nota penceramah dan prompt.

Edit fail ini, kemudian jalankan:  python3 build.py && node render.js
"""

PLATFORM = "TikTok"
COURSE_TITLE = "Claude AI: Dari Zero ke Mesin Cari Prospek"
COURSE_SUB = "Kelas hands-on Tim Kowe — dari tak pernah guna AI sampai automation cari prospek di " + PLATFORM

# ---------------------------------------------------------------------------
# PROMPT PACK  (id, tajuk, bila guna, teks prompt)
# Teks dalam [kurungan] = peserta ganti sendiri.
# Teks dalam {{kurungan berganda}} = pembolehubah yang diisi oleh tool automation.
# ---------------------------------------------------------------------------
PROMPTS = [
  ("P01", "Kenalkan bisnes kau kepada Claude", "Chat pertama. Untuk nampak apa Claude boleh buat untuk bisnes sendiri.",
"""Hai Claude. Aku [nama], aku jual [produk/servis] kepada [siapa pelanggan aku].
Aku baru mula guna AI.

Terangkan dalam bahasa mudah 5 cara kau boleh bantu bisnes aku setiap hari.
Untuk setiap cara, beri satu contoh yang spesifik untuk bisnes aku."""),

  ("P02", "Template formula P.K.T.F.C", "Asas untuk SEMUA prompt. Salin, isi kurungan, guna.",
"""Peranan: Kau ialah [peranan pakar, cth. copywriter jualan 10 tahun].
Konteks: [Info bisnes, siapa audience, apa situasinya].
Tugas: [Apa sebenarnya yang perlu dibuat].
Format: [Panjang, struktur, bahasa, gaya — cth. max 80 patah perkataan, Bahasa Melayu santai].
Contoh: [1–2 contoh gaya yang kau suka]."""),

  ("P03", "Biar Claude tanya dulu", "Bila kau sendiri tak pasti nak minta apa, atau tugas tu besar.",
"""Aku nak [matlamat aku].

Sebelum kau jawab, tanya aku 5 soalan paling penting untuk faham situasi aku.
Tanya satu soalan pada satu masa, dan tunggu jawapan aku."""),

  ("P04", "Ayat iterasi (baiki jawapan)", "Lepas Claude beri jawapan pertama. Pilih mana-mana satu.",
"""• Pendekkan jadi separuh, kekalkan isi paling penting.
• Tukar tone jadi lebih santai, macam cakap dengan kawan.
• Beri 5 versi lain, setiap satu dengan hook yang berbeza.
• Apa yang paling lemah dalam jawapan kau tadi? Baiki bahagian tu.
• Tulis semula untuk orang yang tak pernah dengar pasal produk ni."""),

  ("P05", "Brand Brain (arahan Project)", "Tampal dalam 'Project instructions' supaya Claude ingat bisnes kau setiap kali chat.",
"""Kau ialah pembantu bisnes untuk [nama bisnes].

TENTANG KAMI
- Produk/servis: [apa yang kami jual]
- Harga: [julat harga]
- Kelebihan utama: [3 sebab orang beli dari kami]

PELANGGAN KAMI
- Siapa: [umur, pekerjaan, lokasi]
- Masalah utama: [masalah yang produk kami selesaikan]

GAYA BAHASA
- Bahasa Melayu harian, [santai / profesional]
- Panggil pelanggan: [kau / korang / anda / tuan-puan]

PERATURAN
- Jangan janji benda yang kami tak tawarkan.
- Kalau tak pasti, tanya aku dulu sebelum menjawab."""),

  ("P06", "Bina profil pelanggan ideal (ICP)", "Langkah pertama sebelum cari prospek. Guna dalam Project Brand Brain.",
"""Berdasarkan maklumat bisnes dalam project ni, bina profil pelanggan ideal (ICP) aku.

Sertakan:
1. Demografi (umur, pekerjaan, lokasi, pendapatan)
2. 3 masalah utama yang mereka hadapi
3. Apa yang mereka tonton dan cari di TikTok
4. Ayat yang mereka selalu taip dalam komen bila ada masalah ni
5. Tanda-tanda mereka dah sedia untuk membeli

Beri dalam bentuk jadual, kemudian ringkaskan ICP dalam 2 ayat."""),

  ("P07", "Cari lokasi prospek di TikTok", "Lepas ada ICP. Untuk tahu di mana nak cari.",
"""Untuk ICP di atas, senaraikan:
- 15 hashtag TikTok yang prospek aku selalu guna atau tengok
- 10 jenis akaun/creator yang pengikutnya mungkin prospek aku
- 10 kata kunci carian TikTok

Untuk setiap satu, terangkan dalam satu ayat kenapa ia sesuai.
Tandakan 5 yang paling berpotensi dengan ⭐."""),

  ("P08", "Nilai senarai prospek (manual)", "Lepas kumpul prospek dalam sheet. Tampal beberapa baris sekaligus.",
"""Aku akan tampal senarai prospek dari TikTok (username, bio, komen yang mereka tulis).

Untuk setiap prospek, beri:
- Skor: PANAS / SUAM / SEJUK
- Sebab (1 ayat)
- Masalah yang mereka mungkin ada

Guna ICP dalam project ni sebagai rujukan.
Susun dalam jadual, PANAS di atas sekali.

Senarai:
[tampal di sini]"""),

  ("P09", "Mesej DM pertama yang personal", "Untuk prospek PANAS dan SUAM.",
"""Tulis mesej DM pertama untuk prospek ini:
Username: [ ]
Bio: [ ]
Komen mereka: [ ]

Peraturan:
- Max 50 patah perkataan
- Sebut sesuatu yang spesifik dari bio atau komen mereka
- Jangan terus jual atau letak link
- Akhiri dengan satu soalan ringan

Beri 3 versi dengan gaya berbeza."""),

  ("P10", "Urutan follow-up", "Bila prospek tak balas mesej pertama.",
"""Prospek ni tak balas mesej pertama aku:
[tampal mesej pertama]

Tulis 3 mesej follow-up untuk hari ke-2, ke-5 dan ke-10.
Setiap mesej mesti beri nilai baru (tip berguna, testimoni ringkas, atau soalan menarik)
— jangan cuma tanya "dah baca ke?".
Max 40 patah perkataan setiap satu."""),

  ("P11", "Balas bantahan prospek", "Bila prospek kata mahal, nanti dulu, tak perlu, dsb.",
"""Prospek balas: "[tampal balasan mereka, cth. mahal sangat la]"

Beri 3 cara balas yang:
- jujur dan tak memaksa
- faham kebimbangan mereka dulu
- ajak mereka ke langkah kecil seterusnya

Max 60 patah perkataan setiap satu."""),

  ("P12", "Claude sebagai perunding automation", "Sebelum bina automation. Untuk dapat pelan langkah demi langkah.",
"""Aku nak automate kerja ni:
[terangkan kerja manual kau langkah demi langkah]

Aku guna [Zapier / Make / n8n / Google Sheets / lain-lain].

Pecahkan jadi: TRIGGER → LANGKAH → TINDAKAN.
Untuk setiap langkah, beritahu modul/aplikasi yang perlu dan apa yang perlu diisi.
Anggap aku langsung tak tahu code. Guna bahasa mudah."""),

  ("P13", "Automation pertama: balas borang (dalam modul AI)", "Latihan automation pertama: Google Form → Claude → emel.",
"""Kau pembantu untuk [nama bisnes].
Seseorang baru isi borang dengan maklumat ini:
Nama: {{nama}}
Minat: {{minat}}
Mesej: {{mesej}}

Tulis emel balasan dalam Bahasa Melayu santai, max 120 patah perkataan:
1. Ucap terima kasih dengan nama mereka
2. Jawab mesej mereka secara ringkas
3. Ajak mereka [langkah seterusnya, cth. WhatsApp kami di 01X-XXX XXXX]

Tulis isi emel sahaja, tanpa subjek dan tanpa tandatangan."""),

  ("P14", "Kata kunci untuk tapis komen", "Untuk langkah 'Tapis' dalam automation, supaya Claude tak proses komen sampah.",
"""Senaraikan 30 kata kunci/frasa dalam Bahasa Melayu dan bahasa rojak yang menunjukkan
seseorang di komen TikTok sedang ada masalah [masalah utama ICP]
atau berminat dengan [produk/servis].

Kemudian senaraikan 15 kata kunci yang menunjukkan komen TAK relevan
(spam, promo orang lain, troll).

Beri setiap senarai dalam satu baris, dipisahkan koma, supaya aku boleh tampal terus dalam filter."""),

  ("P15", "Penilai prospek automatik → JSON (enjin utama)", "Prompt dalam modul Claude/AI di automation. Output JSON supaya boleh dimasukkan terus ke Google Sheets.",
"""Kau penilai prospek untuk [nama bisnes] yang menjual [produk/servis]
kepada [ICP ringkas, cth. ibu bekerja 25–40 yang nak kurus selepas bersalin].

Nilai prospek TikTok ini:
Username: {{username}}
Bio: {{bio}}
Komen: {{komen}}
Video sumber: {{video_sumber}}

Kriteria PANAS: [cth. sebut masalah secara terus, tanya harga, minta cadangan]
Kriteria SEJUK: [cth. akaun pesaing, komen tak berkaitan, spam]

Jawab HANYA dalam JSON yang sah, tanpa teks lain:
{
  "skor": "PANAS" atau "SUAM" atau "SEJUK",
  "sebab": "1 ayat",
  "masalah": "masalah utama yang mungkin mereka ada",
  "mesej_dm": "mesej pertama max 50 patah perkataan, personal, tanpa terus jual, akhiri dengan soalan"
}"""),

  ("P16", "Ringkasan harian ke WhatsApp/Telegram", "Langkah notifikasi di hujung automation.",
"""Ini senarai prospek baru hari ini:
{{senarai_prospek}}

Tulis ringkasan untuk aku baca di telefon:
- Jumlah PANAS / SUAM / SEJUK
- 3 prospek PANAS teratas, dengan sebab ringkas
- Satu cadangan tindakan untuk hari ini

Max 100 patah perkataan. Guna emoji secukupnya supaya mudah dibaca."""),

  ("P17", "Debug: automation gagal", "Bila ada langkah automation yang merah / error.",
"""Automation aku gagal.
Tool: [Zapier / Make / n8n]
Langkah yang gagal: [nama langkah]
Mesej ralat: [tampal mesej ralat penuh]
Setting langkah tu: [tampal atau terangkan]

Terangkan dalam bahasa mudah apa puncanya,
dan beri langkah demi langkah untuk betulkan."""),

  ("P18", "Analisis hasil mingguan", "Setiap minggu. Tampal data dari Google Sheets.",
"""Ini data prospek minggu ni dari Google Sheets:
[tampal data — termasuk kolum Skor dan Status]

1. Kira kadar balas dan kadar closing ikut skor (PANAS / SUAM / SEJUK).
2. Apa corak yang kau nampak? (jenis komen, jenis mesej, hari/masa)
3. Beri 3 cadangan spesifik untuk tingkatkan kadar balas minggu depan."""),

  ("P19", "BONUS: Content TikTok yang tarik prospek", "Supaya prospek datang sendiri ke ruang komen kau.",
"""Berdasarkan 3 masalah utama ICP aku, beri 10 idea video TikTok
yang akan buat prospek ideal aku komen.

Untuk setiap idea:
- Hook 3 saat pertama
- Isi ringkas (3 poin)
- Soalan CTA yang dorong orang komen (cth. "Komen 'NAK' kalau kau pun ...")"""),
]

# ---------------------------------------------------------------------------
# SLIDE
#   layout: cover | section | std | dark | accent
#   body: HTML (guna helper di build.py)
#   notes: list ayat untuk penceramah
#   prompts: senarai id prompt yang dirujuk
# ---------------------------------------------------------------------------
from helpers import bullets, cards, flow, table, promptbox, note

SLIDES = [
# ===== PEMBUKAAN =====
dict(layout="cover", title=COURSE_TITLE, body=COURSE_SUB,
  notes=[
    "Perkenalkan diri: siapa kau, apa bisnes kau, dan kenapa kau guna Claude setiap hari.",
    "Beritahu peserta: tak perlu tahu apa-apa pasal AI atau code. Kita mula dari kosong.",
    "Pastikan semua peserta dah buka laptop dan dah terima PDF Prompt Pack — kita akan salin prompt dari situ sepanjang kelas.",
    "Tetapkan peraturan: soalan boleh tanya bila-bila masa; latihan hands-on wajib buat sama-sama.",
  ]),

dict(layout="std", kicker="Kenapa kelas ni", title="Cari prospek cara lama",
  body=cards([
    ("Scroll berjam-jam", "Buka TikTok, cari komen, salin nama satu-satu."),
    ("DM yang sama", "Copy-paste mesej sama kepada semua orang. Kadar balas rendah."),
    ("Lupa follow-up", "Prospek panas jadi sejuk sebab tak ada sistem."),
    ("Tak tahu mana berkesan", "Tak ada data — tak tahu apa yang perlu diperbaiki."),
  ], 2),
  notes=[
    "Tanya peserta: 'Berapa jam seminggu korang habiskan cari prospek?' Biar 2–3 orang jawab.",
    "Kongsi pengalaman kau sendiri sebelum guna automation — berapa jam, berapa penat, berapa yang terlepas.",
    "Tekankan: masalahnya bukan kurang usaha, tapi tak ada SISTEM.",
    "Peralihan: 'Sekarang aku tunjuk macam mana benda ni nampak bila dah ada sistem.'",
  ]),

dict(layout="accent", kicker="Demo hasil akhir", title="Ini yang korang akan bina",
  body='<div class="big">Prospek masuk sendiri → Claude nilai &amp; tulis DM → tersusun dalam Google Sheets → ringkasan sampai ke telefon.</div>'
       '<p class="lead-l">DEMO LIVE: tunjuk automation kau berjalan.</p>',
  notes=[
    "INI SLIDE PALING PENTING — tunjuk hasil akhir DULU supaya peserta nampak destinasi.",
    "Tukar ke skrin: tunjuk automation kau berjalan dari mula sampai hujung (2–3 minit sahaja).",
    "Tunjuk Google Sheets yang penuh dengan prospek, skor PANAS/SUAM/SEJUK, dan mesej DM yang Claude tulis.",
    "Tunjuk notifikasi ringkasan di telefon kau.",
    "Tutup dengan: 'Habis kelas ni, korang boleh buat versi korang sendiri.' Jangan terangkan cara buat lagi — itu nanti.",
  ]),

dict(layout="std", kicker="Peta perjalanan", title="5 bahagian, dari zero ke automation",
  body=table(["Bahagian", "Topik", "Hasil"], [
    ["1", "<b>Kenal Claude</b> — akaun, skrin, chat pertama", "Akaun siap &amp; chat pertama"],
    ["2", "<b>Seni Prompting</b> — formula, iterasi, Projects", "Project 'Brand Brain'"],
    ["3", "<b>Kenal &amp; nilai prospek</b> — ICP, skor, DM", "10 prospek dinilai + DM"],
    ["4", "<b>Asas automation</b> — Trigger → Claude → Tindakan", "Automation pertama jalan"],
    ["5", "<b>Mesin cari prospek</b> — bina 5 blok", "Automation prospek sendiri"],
  ]),
  notes=[
    "Terangkan logik susunan: kita buat SECARA MANUAL dulu (Bahagian 3), baru automate (Bahagian 4–5).",
    "Sebab: kalau tak faham proses manual, automation akan automate benda yang salah.",
    "Setiap bahagian ada latihan dan prompt dalam PDF peserta — nombor prompt tertera di bawah slide.",
  ]),

# ===== BAHAGIAN 1 =====
dict(layout="section", kicker="Bahagian 1", title="Kenal Claude", body="Dari tak pernah guna AI ke chat pertama"),

dict(layout="std", kicker="Bahagian 1 · Konsep", title="Apa itu Claude?",
  body='<div class="g2c"><div>'
       + bullets([
          "Pembantu AI dari syarikat Anthropic",
          "Faham dan tulis dalam Bahasa Melayu &amp; rojak",
          "Kuat menulis, berfikir, analisis fail &amp; gambar",
          "Boleh disambung ke Gmail, Drive, Sheets &amp; tool lain",
        ])
       + '</div><div class="card soft"><h3>Analogi mudah</h3><p>Claude macam <b>pekerja baru yang sangat pandai</b> — tapi hari pertama kerja, dia tak kenal bisnes kau langsung.</p><p style="margin-top:10px">Makin banyak kau terangkan, makin bagus kerja dia.</p></div></div>',
  notes=[
    "Elak istilah teknikal (LLM, model, token). Guna analogi pekerja baru.",
    "Terangkan analogi: pekerja baru yang pandai tapi tak tahu konteks — sebab tu arahan (prompt) kita penting.",
    "Analogi ni akan kita guna sepanjang kelas: Prompt = arahan kerja, Project = buku panduan syarikat, Automation = SOP yang jalan sendiri.",
    "Sebut juga had: Claude boleh silap. Kita sentiasa semak hasilnya, terutama fakta dan angka.",
  ]),

dict(layout="std", kicker="Bahagian 1 · Hands-on", title="Buka akaun &amp; kenal skrin",
  body=flow([
    ("1", "Pergi ke claude.ai", "Daftar guna emel atau akaun Google."),
    ("2", "Kotak chat", "Tempat taip arahan (prompt)."),
    ("3", "Butang +", "Upload fail, gambar, PDF, screenshot."),
    ("4", "Projects", "Folder kerja yang Claude 'ingat'."),
  ]),
  notes=[
    "Buat LIVE di skrin: buka claude.ai dan tunjuk setiap bahagian skrin.",
    "Bagi peserta 5 minit untuk daftar. Bantu yang tersangkut (biasanya pengesahan emel).",
    "Tunjuk di mana sejarah chat, cara mula chat baru, dan di mana menu Projects.",
    "Sebut app telefon juga wujud — sesuai untuk guna di luar, tapi kelas ni guna laptop.",
  ]),

dict(layout="std", kicker="Bahagian 1 · Konsep", title="Free atau berbayar?",
  body=table(["", "Free", "Pro / Max (berbayar)"], [
    ["Untuk siapa", "Cuba-cuba, guna sekali-sekala", "Guna setiap hari untuk bisnes"],
    ["Had penggunaan", "Rendah — cepat habis", "Jauh lebih tinggi"],
    ["Projects &amp; connectors", "Terhad", "Penuh"],
    ["Untuk automation", "Tak sesuai", "Disyorkan"],
  ]) + '<p class="small muted" style="margin-top:16px">Harga &amp; ciri berubah dari masa ke masa — semak claude.ai/pricing.</p>',
  notes=[
    "Jangan paksa upgrade hari ini. Bahagian 1–3 boleh buat dengan akaun Free.",
    "Untuk automation (Bahagian 4–5), mereka perlukan sama ada plan berbayar ATAU kredit API (bergantung tool). Terangkan bila sampai nanti.",
    "SEMAK harga terkini di claude.ai/pricing sebelum kelas — jangan sebut harga dari ingatan.",
  ]),

dict(layout="std", kicker="Bahagian 1 · Latihan", title="Chat pertama",
  body=promptbox("P01") + note("Latihan 5 minit: salin P01, isi kurungan, hantar. Baca jawapan Claude."),
  prompts=["P01"],
  notes=[
    "Minta semua peserta buka PDF Prompt Pack, cari P01, salin dan isi kurungan.",
    "Lepas 5 minit, minta 2–3 peserta kongsi jawapan yang paling mengejutkan mereka.",
    "Titik pengajaran: jawapan lebih bagus sebab mereka beri konteks (nama, produk, pelanggan).",
    "Peralihan: 'Sekarang kita belajar cara bagi arahan yang lebih power.'",
  ]),

# ===== BAHAGIAN 2 =====
dict(layout="section", kicker="Bahagian 2", title="Seni Prompting", body="Cara bagi arahan supaya hasil tak hambar"),

dict(layout="std", kicker="Bahagian 2 · Konsep", title="Kenapa output AI selalu hambar?",
  body='<div class="g2c"><div class="card"><div class="lbl bad">Prompt lemah</div><div class="pmini">Tulis caption untuk produk aku.</div><p class="muted small" style="margin-top:12px">Claude terpaksa meneka semuanya → jawapan generik.</p></div>'
       '<div class="card"><div class="lbl good">Prompt kuat</div><div class="pmini">Kau copywriter F&amp;B. Tulis 3 caption IG untuk sambal bilis premium, audience ibu bekerja 25–40, promo 11.11. Bahasa santai, max 80 patah perkataan, hook kuat di baris pertama, CTA di hujung.</div></div></div>'
       + '<p class="lead" style="margin-top:22px">Sampah masuk, sampah keluar. <b>Konteks</b> masuk, <b>hasil</b> keluar.</p>',
  notes=[
    "Buat LIVE: hantar kedua-dua prompt dalam Claude, tunjuk beza hasilnya sebelah-menyebelah.",
    "Tanya peserta: 'Apa beza yang korang nampak?' Biar mereka sendiri cakap 'yang kedua lebih spesifik'.",
    "Kaitkan dengan analogi pekerja baru: kalau bos cakap 'buat caption', pekerja baru pun bingung.",
  ]),

dict(layout="std", kicker="Bahagian 2 · Formula", title="Formula P.K.T.F.C",
  body='<div class="g2c" style="grid-template-columns:1fr 1.2fr">'
       + bullets([
          "<b>P</b>eranan — siapa Claude patut jadi",
          "<b>K</b>onteks — bisnes, audience, situasi",
          "<b>T</b>ugas — apa sebenarnya nak dibuat",
          "<b>F</b>ormat — panjang, struktur, bahasa",
          "<b>C</b>ontoh — gaya yang kau suka",
        ]) + promptbox("P02", compact=True) + '</div>',
  prompts=["P02"],
  notes=[
    "Terangkan setiap huruf dengan satu contoh ringkas. Tulis di whiteboard jika ada.",
    "Tak semua prompt perlukan 5 elemen. Tapi makin penting tugas, makin lengkap formula.",
    "'Contoh' paling kerap dilupakan tapi paling berkesan — bagi caption lama kau yang laku sebagai contoh.",
    "Latihan 5 minit: peserta guna P02 untuk satu kerja sebenar mereka minggu ni.",
  ]),

dict(layout="std", kicker="Bahagian 2 · Teknik", title="Rahsia sebenar: iterasi",
  body='<div class="g2c">' + promptbox("P03", compact=True) + promptbox("P04", compact=True) + '</div>',
  prompts=["P03", "P04"],
  notes=[
    "Prompt pertama jarang sempurna — dan itu normal. Pakar pun 'berbual' dengan Claude 3–5 pusingan.",
    "P03: bila tak tahu nak minta apa, suruh Claude TANYA dulu. Ini teknik paling mudah untuk pemula.",
    "P04: ayat-ayat pendek untuk baiki jawapan. Tunjuk LIVE: ambil jawapan tadi, guna 2 ayat dari P04.",
    "Mesej utama: jangan terima jawapan pertama bulat-bulat. Bentuk dia.",
  ]),

dict(layout="std", kicker="Bahagian 2 · Hands-on", title="Projects: 'Brand Brain' bisnes kau",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div>'
       + bullets([
          "Klik <b>Projects → Create project</b>",
          "Namakan: <i>[Nama bisnes] Brand Brain</i>",
          "Tampal P05 dalam <b>Project instructions</b>",
          "Upload fail: katalog, senarai harga, FAQ",
          "Semua chat dalam project ni = Claude dah kenal bisnes kau",
        ]) + '</div>' + promptbox("P05", compact=True) + '</div>',
  prompts=["P05"],
  notes=[
    "Kaitkan dengan analogi: Project = buku panduan syarikat untuk pekerja baru.",
    "Buat LIVE langkah demi langkah. Tunjuk di mana 'Project instructions' dan butang upload fail.",
    "Bagi peserta 10 minit isi P05 dengan info bisnes mereka. Ini ASAS untuk semua bahagian seterusnya.",
    "Ujian: dalam project tu, tanya 'Siapa pelanggan aku?' — Claude patut jawab tepat tanpa diberitahu lagi.",
    "Semua latihan selepas ini dibuat DALAM project ni.",
  ]),

# ===== BAHAGIAN 3 =====
dict(layout="section", kicker="Bahagian 3", title="Kenal &amp; Nilai Prospek", body="Buat secara manual dulu — baru kita automate"),

dict(layout="std", kicker="Bahagian 3 · Langkah 1", title="Siapa prospek ideal kau (ICP)?",
  body='<div class="g2c" style="grid-template-columns:1fr 1.25fr"><div>'
       + '<p class="lead">ICP = <b>Ideal Customer Profile</b>.<br>Kalau tak tahu siapa yang dicari, automation pun tak tahu.</p>'
       + bullets(["Demografi", "3 masalah utama", "Apa mereka tengok di TikTok", "Ayat yang mereka taip dalam komen", "Tanda sedia membeli"])
       + '</div>' + promptbox("P06", compact=True) + '</div>',
  prompts=["P06"],
  notes=[
    "ICP ialah asas automation. Kriteria PANAS/SUAM/SEJUK nanti datang dari sini.",
    "Paling penting: point 4 — 'ayat yang mereka taip dalam komen'. Inilah kata kunci yang automation akan cari.",
    "Peserta jalankan P06 dalam Project Brand Brain mereka. Minta mereka simpan hasilnya (copy ke dokumen atau upload ke project).",
    "Tanya 1–2 peserta kongsi ICP mereka — betulkan jika terlalu umum ('semua orang' bukan ICP).",
  ]),

dict(layout="std", kicker="Bahagian 3 · Langkah 2", title="Di mana prospek berada di TikTok?",
  body=cards([
    ("💬 Ruang komen", "Komen di video yang bincang masalah ICP kau."),
    ("#️⃣ Hashtag", "Hashtag niche yang ICP selalu tonton."),
    ("🎯 Akaun pesaing", "Orang yang tanya soalan di video pesaing."),
    ("🔴 LIVE", "Penonton yang aktif bertanya semasa live."),
  ], 4) + promptbox("P07", compact=True, style="margin-top:20px"),
  prompts=["P07"],
  notes=[
    "Prospek terbaik ialah orang yang SENDIRI sebut masalah mereka dalam komen — mereka dah 'angkat tangan'.",
    "Komen di video pesaing ialah lombong emas: mereka dah berminat dengan kategori produk kau.",
    "Peserta jalankan P07, kemudian buka TikTok dan cari 3 hashtag ⭐ yang Claude cadangkan.",
  ]),

dict(layout="std", kicker="Bahagian 3 · Langkah 3", title="Kumpul prospek dalam Google Sheets",
  body=table(["Tarikh", "Username", "Bio", "Komen", "Video sumber", "Skor", "Mesej DM", "Status"], [
    ["25/11", "@kak_ani", "Ibu 2 anak, KL", "Macam mana nak turun 5kg ni 😭", "link", "", "", "Belum DM"],
    ["25/11", "@miza.h", "Cikgu | Johor", "Berapa harga set ni?", "link", "", "", "Belum DM"],
    ["…", "", "", "", "", "", "", ""],
  ], small=True) + note("Latihan: kumpul 10 prospek secara manual (15 minit). Biarkan kolum Skor &amp; Mesej DM kosong."),
  notes=[
    "Tunjuk template Google Sheets ni. Kongsi link template dengan peserta (buat salinan dulu sebelum kelas).",
    "Kolum ni SAMA dengan apa yang automation akan isi nanti — jadi mereka faham struktur data dari awal.",
    "Bagi 15 minit untuk kumpul 10 prospek secara manual dari TikTok.",
    "Tanya selepas itu: 'Berapa lama korang ambil?' — ini akan jadi perbandingan bila automation jalan.",
    "Contoh dalam jadual ialah rekaan; ganti dengan contoh dari niche kau sendiri.",
  ]),

dict(layout="std", kicker="Bahagian 3 · Langkah 4", title="Claude nilai prospek",
  body='<div class="g2c" style="grid-template-columns:1fr 1.3fr"><div>'
       + '<div class="score hot">PANAS<span>Sebut masalah terus / tanya harga</span></div>'
       + '<div class="score warm">SUAM<span>Ada minat, belum ada niat jelas</span></div>'
       + '<div class="score cold">SEJUK<span>Tak berkaitan / spam / pesaing</span></div>'
       + '</div>' + promptbox("P08", compact=True) + '</div>',
  prompts=["P08"],
  notes=[
    "Terangkan sistem 3 warna. Masa terhad — fokus pada PANAS dulu.",
    "Peserta salin 10 baris dari Google Sheets mereka, tampal dalam P08.",
    "Bincang: setuju tak dengan skor Claude? Kalau tak, beritahu Claude kenapa — dia akan belajar dalam chat tu.",
    "Kriteria yang mereka betulkan di sini akan dimasukkan ke dalam prompt automation nanti (P15).",
  ]),

dict(layout="std", kicker="Bahagian 3 · Langkah 5", title="Claude tulis DM yang personal",
  body='<div class="g2c">' + promptbox("P09", compact=True) + '<div>' + promptbox("P10", compact=True) + promptbox("P11", compact=True, style="margin-top:14px", hide_body=True) + '</div></div>',
  prompts=["P09", "P10", "P11"],
  notes=[
    "Peraturan emas DM: personal, pendek, tak terus jual, akhiri dengan soalan.",
    "Peserta jalankan P09 untuk 3 prospek PANAS mereka.",
    "P10 untuk follow-up — kebanyakan jualan berlaku selepas follow-up ke-2 atau ke-3.",
    "P11 untuk bila prospek bantah (mahal, nanti dulu). Tunjuk satu contoh live.",
    "Tekankan: HANTAR DM SECARA MANUAL. Claude tulis draf, kau yang hantar dan sesuaikan.",
    "Peralihan: 'Sekarang korang dah buat semua ni manual. Bayangkan kalau langkah kumpul, nilai dan tulis DM ni jalan sendiri…'",
  ]),

# ===== BAHAGIAN 4 =====
dict(layout="section", kicker="Bahagian 4", title="Asas Automation", body="Satu konsep yang buka semua pintu"),

dict(layout="std", kicker="Bahagian 4 · Konsep", title="Trigger → Claude → Tindakan",
  body=flow([
    ("⚡", "TRIGGER", "Sesuatu berlaku. Cth: borang baru diisi, baris baru di Sheets, jadual setiap pagi."),
    ("🧠", "CLAUDE", "Berfikir &amp; menulis. Cth: nilai, ringkaskan, tulis balasan."),
    ("✅", "TINDAKAN", "Hasil dihantar. Cth: hantar emel, isi Sheets, notifikasi Telegram."),
  ], arrows=True, big=True) + '<p class="lead" style="margin-top:28px">Semua automation — dari yang paling mudah sampai yang paling canggih — ikut corak ni.</p>',
  notes=[
    "Ini satu-satunya konsep yang mereka MESTI faham. Ulang 2–3 kali.",
    "Kaitkan dengan analogi: automation = SOP yang pekerja baru jalankan sendiri, tanpa kau suruh setiap kali.",
    "Minta peserta beri 1 contoh kerja harian mereka dalam bentuk Trigger → Claude → Tindakan. Tulis 2–3 di whiteboard.",
  ]),

dict(layout="std", kicker="Bahagian 4 · Tool", title="Pilih tool automation",
  body=table(["Tool", "Kelebihan", "Sesuai untuk"], [
    ["<b>Zapier</b>", "Paling mudah, banyak integrasi", "Pemula yang nak cepat"],
    ["<b>Make</b>", "Visual, lebih murah untuk volume tinggi", "Aliran yang ada banyak langkah"],
    ["<b>n8n</b>", "Paling fleksibel, boleh self-host", "Yang nak kawalan penuh"],
    ["<b>Cowork</b>", "Dalam app desktop Claude, tanpa setup integrasi", "Kerja pada fail &amp; folder komputer"],
    ["<b>Claude Code</b>", "Paling berkuasa, Claude bina skrip sendiri", "Yang selesa sedikit teknikal"],
  ]) + note("Dalam kelas ni kita guna: <b>[tool yang kau guna]</b>"),
  notes=[
    "Jangan buat peserta pening — beritahu terus tool yang kelas ni guna (tool yang automation kau guna).",
    "Sebut tool lain sekadar supaya mereka tahu wujud; konsep Trigger → Claude → Tindakan sama di semua tool.",
    "Terangkan kos: tool automation biasanya ada plan percuma terhad, dan langkah Claude mungkin perlukan kunci API Anthropic (bayar ikut guna).",
    "SEMAK harga & had plan percuma setiap tool sebelum kelas.",
  ]),

dict(layout="std", kicker="Bahagian 4 · Latihan", title="Automation pertama: balas borang",
  body=flow([
    ("1", "Google Form", "Pelanggan isi nama, minat, mesej."),
    ("2", "Claude (P13)", "Tulis emel balasan personal."),
    ("3", "Gmail", "Emel dihantar automatik."),
  ], arrows=True) + promptbox("P13", compact=True, style="margin-top:20px"),
  prompts=["P13"],
  notes=[
    "Kenapa mula dengan ini: paling mudah, nampak hasil dalam 20 minit, bina keyakinan.",
    "Buat LIVE langkah demi langkah di tool kau. Peserta ikut serentak.",
    "Tunjuk cara masukkan pembolehubah {{nama}}, {{minat}}, {{mesej}} dari borang ke dalam prompt.",
    "Uji: isi borang sendiri, tunjuk emel sampai. Raikan bila peserta pertama berjaya!",
    "Kalau ada yang tersangkut, guna P17 (debug) — ini peluang tunjuk Claude bantu betulkan automation.",
  ]),

dict(layout="std", kicker="Bahagian 4 · Konsep", title="Prompt untuk automation ≠ prompt untuk chat",
  body=table(["", "Prompt chat", "Prompt automation"], [
    ["Siapa baca output", "Manusia", "Mesin (Sheets, Zapier, dll.)"],
    ["Format jawapan", "Bebas", "<b>Tetap &amp; ketat</b> — selalunya JSON"],
    ["Boleh tanya balik?", "Ya", "Tak — mesti lengkap sekali jalan"],
    ["Data", "Ditaip sendiri", "Pembolehubah <code>{{username}}</code>"],
  ]) + '<p class="lead" style="margin-top:20px">Peraturan: suruh Claude jawab <b>HANYA dalam format yang ditetapkan</b>.</p>',
  notes=[
    "Konsep penting sebelum Bahagian 5. Dalam automation, tiada manusia untuk betulkan jawapan.",
    "JSON = format data yang mesin faham. Tak perlu faham teknikal — cukup tahu ia 'borang' yang Claude isi.",
    "Tunjuk contoh JSON ringkas dan bagaimana setiap 'kotak' (skor, sebab, mesej_dm) masuk ke kolum Sheets yang berbeza.",
  ]),

# ===== BAHAGIAN 5 =====
dict(layout="section", kicker="Bahagian 5", title="Mesin Cari Prospek", body="Gabungkan semua yang dah dipelajari"),

dict(layout="std", kicker="Bahagian 5 · Senibina", title="5 blok mesin cari prospek",
  body=flow([
    ("1", "Ambil data", "Komen/prospek dari TikTok masuk ke sistem."),
    ("2", "Tapis", "Buang spam &amp; komen tak relevan."),
    ("3", "Claude nilai", "Skor + sebab + DM (P15)."),
    ("4", "Simpan", "Satu baris baru di Google Sheets."),
    ("5", "Notifikasi", "Ringkasan ke telefon (P16)."),
  ], arrows=True),
  notes=[
    "Tunjuk semula demo dari awal kelas — sekarang peserta akan nampak 5 blok ni dengan jelas.",
    "Setiap blok = satu langkah dalam tool automation. Kita bina satu-satu.",
    "Kaitkan dengan Bahagian 3: blok 3 ialah P08 + P09 yang mereka buat manual tadi, cuma sekarang automatik.",
    "Gantikan perincian blok 1 dengan cara sebenar automation kau ambil data.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Blok 1–2", title="Ambil data &amp; tapis",
  body='<div class="g2c"><div class="card"><h3>Blok 1 · Ambil data</h3>'
       + bullets(["<b>[Terangkan sumber data dalam automation kau]</b>", "Pilihan: senarai manual di Sheets, borang, atau tool pengumpul data", "Setiap prospek = 1 rekod: username, bio, komen, video"], small=True)
       + '</div><div class="card"><h3>Blok 2 · Tapis</h3>'
       + bullets(["Tapis guna kata kunci (P14)", "Buang komen terlalu pendek / emoji sahaja", "Buang duplikat (prospek yang sama)", "Jimat kos — Claude hanya proses yang berpotensi"], small=True)
       + '</div></div>' + promptbox("P14", compact=True, style="margin-top:18px", hide_body=True),
  prompts=["P14"],
  notes=[
    "Blok 1: TUNJUK cara automation kau ambil data. Ini bahagian yang paling berbeza antara setup — terangkan setup kau sendiri.",
    "Ingatkan: ikut terma penggunaan platform. Jangan guna kaedah yang boleh menyebabkan akaun disekat.",
    "Blok 2: tapis SEBELUM hantar ke Claude — jimat kos dan hasil lebih bersih.",
    "Peserta jalankan P14 untuk dapat senarai kata kunci, kemudian tampal dalam modul filter.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Blok 3", title="Enjin utama: Claude nilai &amp; tulis DM",
  body=promptbox("P15", compact=True),
  prompts=["P15"],
  notes=[
    "Ini 'otak' mesin. Gabungan P06 (ICP) + P08 (skor) + P09 (DM) dalam satu prompt.",
    "Terangkan setiap bahagian: konteks bisnes → data prospek {{}} → kriteria → format JSON.",
    "Peserta MESTI ganti kriteria PANAS/SEJUK dengan kriteria yang mereka betulkan dalam Bahagian 3.",
    "Uji dulu dalam chat biasa dengan 3 prospek — pastikan output JSON betul — baru masukkan ke tool automation.",
    "Tunjuk cara petakan setiap medan JSON ke kolum Google Sheets.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Blok 4–5", title="Simpan &amp; notifikasi",
  body='<div class="g2c"><div class="card"><h3>Blok 4 · Google Sheets</h3>'
       + bullets(["Tambah baris baru untuk setiap prospek", "Skor, Sebab, Mesej DM diisi dari JSON", "Status mula dengan 'Belum DM'", "Susun/tapis ikut PANAS"], small=True)
       + '</div><div class="card"><h3>Blok 5 · Notifikasi</h3>'
       + bullets(["Sekali sehari (cth. 9 pagi)", "Claude ringkaskan prospek baru (P16)", "Hantar ke Telegram / emel / WhatsApp", "Kau buka telefon → terus tahu siapa nak DM"], small=True)
       + '</div></div>' + promptbox("P16", compact=True, style="margin-top:18px", hide_body=True),
  prompts=["P16"],
  notes=[
    "Blok 4: guna template Sheets yang sama dari Bahagian 3 — peserta dah kenal strukturnya.",
    "Blok 5: notifikasi harian buat sistem ni jadi tabiat. Tanpa notifikasi, Sheets akan dilupakan.",
    "Notifikasi ialah automation kedua (trigger ikut jadual), berasingan dari aliran utama.",
  ]),

dict(layout="accent", kicker="Demo &amp; build", title="Jom bina sama-sama",
  body='<div class="big">Bina 5 blok dalam [tool kau], langkah demi langkah.</div><p class="lead-l">Uji dengan 5 prospek sebenar → semak Sheets → betulkan dengan P17.</p>',
  prompts=["P17"],
  notes=[
    "Sesi paling panjang (45–60 minit). Buat LIVE, satu blok pada satu masa, tunggu semua peserta siap sebelum ke blok seterusnya.",
    "Ada 'checkpoint' selepas setiap blok: 'Angkat tangan kalau dah nampak data masuk.'",
    "Ralat biasa: pembolehubah salah petakan, JSON tak sah, kunci API tak diisi, kebenaran Google tak diberi.",
    "Guna P17 bila ada ralat — ajar peserta minta Claude bantu debug, bukan bergantung pada kau.",
    "Akhir sesi: setiap peserta jalankan automation sekali dan tunjuk Sheets mereka.",
  ]),

dict(layout="dark", kicker="Penting", title="Etika &amp; keselamatan akaun",
  body=cards([
    ("Ikut terma platform", "Jangan guna kaedah ambil data yang dilarang TikTok — akaun boleh disekat."),
    ("Hantar DM secara manual", "Claude tulis draf; manusia hantar. Had DM sehari supaya tak dianggap spam."),
    ("Personal, bukan spam", "Setiap mesej mesti relevan dengan komen orang tu."),
    ("Lindungi data (PDPA)", "Simpan data dengan selamat, guna untuk tujuan jualan sahaja, padam bila diminta."),
  ], 2),
  notes=[
    "Jangan langkau slide ni. Satu akaun yang disekat boleh hapuskan semua hasil.",
    "Akta Perlindungan Data Peribadi 2010 (PDPA) Malaysia terpakai bila kita simpan data orang untuk tujuan komersial.",
    "Prinsip: automation untuk CARI dan TULIS DRAF; hubungan dengan prospek tetap dibuat oleh manusia.",
    "Jika kau tak pasti tentang terma platform terkini, nasihatkan peserta semak sendiri.",
  ]),

dict(layout="std", kicker="Bahagian 5 · Ukur", title="Ukur hasil setiap minggu",
  body=cards([
    ("Prospek baru", "Berapa yang masuk seminggu?"),
    ("% PANAS", "Kualiti sumber data kau."),
    ("Kadar balas", "Berapa % balas DM?"),
    ("Kadar closing", "Berapa % jadi pelanggan?"),
  ], 4) + promptbox("P18", compact=True, style="margin-top:20px"),
  prompts=["P18"],
  notes=[
    "Automation bukan 'set and forget'. Semak sekali seminggu.",
    "Kalau % PANAS rendah: baiki sumber data atau kata kunci tapis. Kalau kadar balas rendah: baiki gaya DM dalam P15.",
    "P18: tampal data minggu ni, biar Claude cari corak dan cadang penambahbaikan.",
  ]),

dict(layout="accent", kicker="Penutup", title="Tugasan 7 hari",
  body=bullets([
    "Hari 1: Lengkapkan Project Brand Brain (P05, P06)",
    "Hari 2–3: Jalankan mesin cari prospek setiap hari",
    "Hari 4–6: DM 5 prospek PANAS sehari + follow-up (P09, P10)",
    "Hari 7: Analisis hasil (P18) &amp; kongsi dalam group",
    "BONUS: Buat content yang tarik prospek (P19)",
  ], light=True),
  prompts=["P19"],
  notes=[
    "Beri tugasan konkrit supaya ilmu jadi tabiat.",
    "Minta peserta kongsi screenshot Sheets dan hasil minggu pertama dalam group support.",
    "Sebut P19 sebagai bonus: content yang betul buat prospek datang sendiri ke ruang komen — automation jadi lebih berkesan.",
    "Tutup dengan sesi soal jawab, dan ingatkan tentang group support.",
  ]),
]
