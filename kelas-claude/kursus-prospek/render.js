// Jana PDF dari HTML:  node render.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = __dirname;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('file://' + path.join(dir, 'slides.html'));
  await p.pdf({ path: path.join(dir, 'slides.pdf'), width: '1280px', height: '720px', printBackground: true });

  // Semak kandungan yang melimpah ke kawasan footer
  const over = await p.$$eval('.slide', ss => ss.map((s, i) => {
    const limit = s.querySelector('.foot').getBoundingClientRect().top - 6;
    let max = 0;
    s.querySelectorAll('.body > *, .body *').forEach(e => { max = Math.max(max, e.getBoundingClientRect().bottom); });
    return max > limit ? i + 1 : null;
  }).filter(Boolean));
  if (over.length) console.log('AMARAN — slide melimpah:', over.join(', '));

  // Thumbnail untuk nota penceramah
  fs.mkdirSync(path.join(dir, 'thumbs'), { recursive: true });
  const slides = await p.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(dir, 'thumbs', String(i + 1).padStart(2, '0') + '.png') });
  }

  for (const f of ['nota-penceramah', 'prompt-pack']) {
    const q = await b.newPage();
    await q.goto('file://' + path.join(dir, f + '.html'));
    await q.pdf({ path: path.join(dir, f + '.pdf'), format: 'A4', printBackground: true,
      displayHeaderFooter: true, headerTemplate: '<span></span>',
      footerTemplate: '<div style="font-size:8px;color:#8f8677;width:100%;text-align:center;font-family:Inter">Kelas Claude AI · Tim Coway · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
      margin: { top: '16mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  }
  console.log('Siap:', slides.length, 'slide');
  await b.close();
})();
