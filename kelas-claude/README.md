# Kelas Claude AI — Tim Kowe

| Fail | Guna untuk |
|---|---|
| `slides.pdf` | Slide 14 muka untuk present kelas / pitch kepada tim |
| `slides.html` | Sumber slide — edit teks di sini, kemudian jana semula PDF |
| `sales-page/index.html` | Sales page + borang daftar + aliran bayaran |

## 1. Ubah tetapan sales page

Buka `sales-page/index.html` dan cari blok `CONFIG` di bahagian atas. Ubah:

- `hargaBiasa`, `hargaEarlyBird`, `tarikhTutupEarlyBird` — harga & tarikh tutup early bird (harga bertukar automatik selepas tarikh ini)
- `tarikhKelas`, `lokasi`, `kuotaTempat`
- `bank` — nama bank, no. akaun, nama akaun
- `whatsapp` — nombor untuk terima resit (cth. `60123456789`)
- `linkBayaranOnline` — link bayaran dari ToyyibPay / Billplz / Stripe Payment Link. Jika kosong, hanya pilihan pindahan bank dipaparkan.
- `googleSheetWebhook` — (pilihan) untuk simpan setiap pendaftaran ke Google Sheets (lihat bawah)

## 2. Aliran pendaftaran

1. Peserta isi borang (nama, emel, telefon, tahap, matlamat)
2. Sistem jana nombor rujukan (cth. `KOWE-AB12CD`)
3. **Bayaran online** → terus ke link ToyyibPay/Billplz/Stripe
   **Pindahan bank** → papar maklumat akaun + butang WhatsApp yang siap berisi maklumat peserta & rujukan
4. Anda sahkan bayaran, kemudian hantar link kelas + group support

## 3. (Pilihan) Simpan pendaftaran ke Google Sheets

1. Buat Google Sheet baru → **Extensions → Apps Script**
2. Tampal kod ini:

```js
function doPost(e) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const d = JSON.parse(e.postData.contents);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(["Masa", "Rujukan", "Nama", "Emel", "Telefon", "Tahap", "Matlamat", "Bayaran", "Harga", "Status"]);
  }
  sheet.appendRow([d.masa, d.rujukan, d.nama, d.emel, d.telefon, d.tahap, d.matlamat, d.bayaran, d.harga, "Belum sah"]);
  return ContentService.createTextOutput("ok");
}
```

3. **Deploy → New deployment → Web app**, "Execute as: Me", "Who has access: Anyone"
4. Salin URL web app ke `googleSheetWebhook` dalam `CONFIG`

## 4. Online-kan sales page (percuma)

Mana-mana satu:
- **Netlify Drop** — seret folder `sales-page` ke https://app.netlify.com/drop
- **GitHub Pages** — Settings → Pages → pilih branch & folder
- **Vercel** — import repo, set root directory ke `kelas-claude/sales-page`

## 5. Jana semula PDF selepas edit slide

```bash
node -e "
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/kelas-claude/slides.html');
  await p.pdf({ path: 'kelas-claude/slides.pdf', width: '1280px', height: '720px', printBackground: true });
  await b.close();
})();"
```

Atau buka `slides.html` dalam Chrome → Print → Save as PDF (Background graphics: hidup, Margin: tiada).
