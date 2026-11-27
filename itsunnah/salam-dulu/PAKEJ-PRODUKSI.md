# Itsunnah · Storyboard 01: "Salam Dulu" — pakej produksi

Video menegak 9:16 · 24 saat · Amir & Hana · rumah Melayu moden, cahaya pagi hangat.

Fail dalam folder ini:
- `salam-dulu-animatic.mp4` — animatic 9:16 dari panel storyboard (masa, teks, subtitle). **Bukan video animasi akhir.** Watak tidak bergerak; kamera sahaja yang bergerak perlahan.
- `panels/1.jpg` … `6.jpg` — panel storyboard tanpa label, untuk dijadikan frame permulaan dalam alat imej-ke-video.
- `subtitle.srt` — subtitle BM.

## Cara hasilkan video animasi sebenar

Watak mesti kekal sama, jadi **jangan jana watak dari teks**. Guna setiap panel sebagai **frame permulaan** dalam alat imej-ke-video (cth. Kling, Veo, Runway, Luma), satu klip bagi setiap babak, kemudian sambung dalam CapCut.

1. Muat naik `panels/N.jpg` sebagai gambar permulaan.
2. Tampal prompt babak N (di bawah). Pilih nisbah 9:16 dan tempoh yang tertera (pilih 5 saat jika alat tak benarkan 3–4 saat; potong dalam CapCut).
3. Jana 2–3 versi, pilih yang muka dan pakaian paling kekal.
4. Kalau muka berubah: kurangkan gerakan dalam prompt ("subtle", "minimal movement") — gerakan besar paling kerap merosakkan muka.

Prompt ditulis dalam Bahasa Inggeris sebab kebanyakan alat video lebih tepat dengan BI.

### Babak 1 · 0:00–0:03 · Wide
- Panel: `panels/1.jpg`
- Teks skrin: **"Bila sampai rumah…"**
- Prompt:
  > 3D animated children's film style. Wide shot, warm morning sunlight. A young Malay boy in a white kopiah and sage-green baju Melayu, and a young Malay girl in an apricot hijab covering her hair, ears, neck and chest, cream tunic and sage-green trousers, walk calmly along the stone path toward the green front door of a simple modern Malay house. Slow steady camera push-in. Gentle breeze in the plants. Keep faces, outfits and art style exactly as in the image. No extra characters, no text, no watermark.

### Babak 2 · 0:03–0:06 · Loceng
- Panel: `panels/2.jpg`
- SFX: loceng pintu (ding-dong) pada ~0:04
- Prompt:
  > 3D animated children's film style. Medium close-up at the front door. The boy politely presses the doorbell once with his index finger, then lowers his hand. The girl stands beside him calmly with her hands together, smiling softly. Subtle, minimal movement. Static camera. Keep faces, outfits and art style exactly as in the image. No extra characters, no text, no watermark.

### Babak 3 · 0:06–0:10 · Salam
- Panel: `panels/3.jpg`
- Teks skrin: **"1. Beri salam"**
- Dialog: Amir — "Assalamualaikum!" · Hana — "Assalamualaikum."
- Prompt:
  > 3D animated children's film style. Two-shot of the boy and girl facing the closed front door, waiting patiently. The boy says a greeting with a cheerful open mouth, then the girl says a softer greeting. Gentle natural lip movement, friendly expressions, small head nods. Static camera. Keep faces, outfits and art style exactly as in the image. No extra characters, no text, no watermark.

### Babak 4 · 0:10–0:14 · Jemput
- Panel: `panels/4.jpg`
- Teks skrin: **"2. Tunggu dengan sopan"**
- Dialog: Ibu — "Waalaikumsalam. Jemput masuk."
- Prompt:
  > 3D animated children's film style. Over-the-shoulder shot from inside the house. A kind Malay mother in a mauve hijab and floral baju kurung opens the green door, smiles warmly and gestures with an open palm inviting the children in, speaking gently. The children stand still and polite in the foreground. Slow subtle camera drift. Keep faces, outfits and art style exactly as in the image. No extra characters, no text, no watermark.

### Babak 5 · 0:14–0:19 · Masuk
- Panel: `panels/5.jpg`
- Teks skrin: **"Salam dulu 🤍"**
- Narator: "Salam dulu, baru masuk."
- Prompt:
  > 3D animated children's film style. Medium shot. The boy and girl each place their right hand on their chest respectfully and walk slowly through the open door into a warm, tidy living room, smiling. Calm, child-paced movement. Slow steady camera follow. Keep faces, outfits and art style exactly as in the image. No extra characters, no text, no watermark.

### Babak 6 · 0:19–0:24 · End card
- Panel: `panels/6.jpg`
- Dialog: Amir — "Jom cuba hari ini!"
- Teks skrin: **"Itsunnah · Adab kecil, kesan besar"** (+ logo)
- Prompt:
  > 3D animated children's film style. Medium shot in a cozy living room with warm lamp light. The boy and girl smile and wave cheerfully at the camera; the boy speaks one short happy line. Gentle, friendly movement. Static camera with slight slow push-in. Keep faces, outfits and art style exactly as in the image. No extra characters, no text, no watermark.

## Suara & audio
| Masa | Siapa | Ayat | Nada |
|---|---|---|---|
| 0:06.3 | Amir | "Assalamualaikum!" | Ceria, jelas |
| 0:08.1 | Hana | "Assalamualaikum." | Lembut, sopan |
| 0:10.4 | Ibu | "Waalaikumsalam. Jemput masuk." | Mesra, tenang |
| 0:14.6 | Narator | "Salam dulu, baru masuk." | Hangat, perlahan |
| 0:19.2 | Amir | "Jom cuba hari ini!" | Bersemangat |

- Rakam suara kanak-kanak sebenar (dengan izin ibu bapa) atau guna suara AI yang dibenarkan untuk kegunaan komersial.
- Muzik latar: lembut, tanpa alat muzik jika itu garis panduan jenama — guna nasyid/vokal sahaja atau bunyi alam.
- SFX: loceng pintu (0:04), pintu dibuka (0:10.5), langkah kaki perlahan (0:15).

## Arahan editing (CapCut)
1. Kanvas 9:16 (1080×1920), 30 fps.
2. Susun 6 klip ikut masa di atas; peralihan *dissolve* 0.3 saat, tiada peralihan bergaya.
3. Teks skrin: kotak bulat krim (#FFFAF0), tulisan hijau gelap tebal, di bahagian atas; muncul 0.3 saat selepas babak bermula. Rujuk `salam-dulu-animatic.mp4` untuk kedudukan dan masa.
4. Import `subtitle.srt` (atau guna auto-caption dan semak ejaan).
5. Babak 6: tambah logo Itsunnah di bawah tagline.
6. Eksport 1080×1920, 30 fps. Semak: tiada watermark alat AI, tiada watak tambahan, aurat Hana dan Ibu kekal tertutup dalam setiap frame.
