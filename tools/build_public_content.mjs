#!/usr/bin/env node
/**
 * FURUSHO OFFICIAL v4: deterministic public HTML section generator.
 * Edit assets/data/public-content.json, then run:
 *   node tools/build_public_content.mjs --write
 * CI checks with --check. Never read private Profile OS content here.
 */
import fs from 'node:fs';
const data = JSON.parse(fs.readFileSync('assets/data/public-content.json', 'utf8'));
const transform = function transform(file,s,data){
 const esc=(x)=>String(x??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
 const attr=esc;
 const mark=(n,t)=>`<!-- BEGIN GENERATED:${n} -->\n${t}\n<!-- END GENERATED:${n} -->`;
 const replace=(n,initial,text)=>{
   const re=new RegExp(`<!-- BEGIN GENERATED:${n} -->[\\s\\S]*?<!-- END GENERATED:${n} -->`);
   if(re.test(s))s=s.replace(re,mark(n,text));
   else if(initial.test(s))s=s.replace(initial,mark(n,text));
   else throw new Error(`Missing anchor for ${file}:${n}`);
 };
 const href=(w)=>`https://www.youtube.com/watch?v=${w.video}`;
 const image=(w)=>`https://img.youtube.com/vi/${w.video}/hqdefault.jpg`;
 const featured=data.works.filter(w=>w.featured);
 if(file==="index.html"){
   const work=data.services.map((v,i)=>`          <article class="v3-work-row"><span class="index">${String(i+1).padStart(2,"0")}</span><h3>${esc(v.title)}</h3><p>${esc(v.summary)}</p><a href="mailto:furushonoritaka@gmail.com?subject=${encodeURIComponent(v.title+"のご相談｜古庄里好")}" aria-label="${attr(v.title)}についてメールで相談する">メールで相談 →</a></article>`).join("\n");
   replace("HOME_SERVICES",/        <div class="v3-work-list">[\s\S]*?<\/div>(?=\s*<div class="v3-studio-note">)/,`        <div class="v3-work-list">\n${work}\n        </div>`);
   const f=(w,cls)=>`          <a class="${cls}" href="${href(w)}" target="_blank" rel="noopener noreferrer"><figure><img src="${image(w)}" alt="${attr(w.title)}の関連映像サムネイル" width="480" height="360" loading="lazy" decoding="async"></figure><div class="v3-feature-copy"><span>${esc(w.kind)}</span><div><h3>${esc(w.title)}</h3><p>${esc(w.detail?w.detail+" / ":"")}${esc(w.year)} / ${esc(w.role)}</p></div></div></a>`;
   replace("HOME_FEATURED_WORKS",/        <div class="v3-feature-grid">[\s\S]*?<\/div>(?=\s*<a class="v3-dark-link")/,`        <div class="v3-feature-grid">\n${f(featured[0],"v3-feature-main")}\n          <div class="v3-feature-side-stack">\n${featured.slice(1).map(w=>f(w,"v3-feature-side")).join("\n")}\n          </div>\n        </div>`);
   const p=data.projects.filter(x=>x.featured);
   const projectRows=p.map((v,i)=>`          <a class="v3-project-row" href="${attr(v.home_url||v.url)}"${(v.home_url||v.url).startsWith("http")?' target="_blank" rel="noopener noreferrer"':""}><span class="index">${String(i+1).padStart(2,"0")}</span><strong>${esc(v.title)}</strong><p>${esc(v.summary)}</p><span class="arrow">${esc(v.label)} →</span></a>`).join("\n");
   replace("HOME_PROJECTS",/        <div class="v3-project-list">[\s\S]*?<\/div>(?=\s*<\/div>\s*<\/section>)/,`        <div class="v3-project-list">\n${projectRows}\n        </div>`);
   const updateRows=data.updates.map(x=>`          <article class="v4-current-item"><p class="v3-label">${esc(x.category)}</p><h3>${esc(x.title)}</h3><p>${esc(x.summary)}</p><a href="${attr(x.url)}" target="_blank" rel="noopener noreferrer">${esc(x.link_label)} →</a></article>`).join("\n");
   const current=`    <section class="v3-section v4-current" id="current-work" aria-labelledby="current-work-heading"><div class="section-shell"><div class="v3-section-head"><div><p class="v3-label">CURRENT WORK</p><h2 id="current-work-heading">いま取り組んでいること。</h2></div><p>指導の現場から、タップダンスの楽しみ方を広げる制作活動まで。</p></div><div class="v4-current-grid">\n${updateRows}\n</div><p class="v4-current-detail"><a class="v3-dark-link" href="activities/">活動について詳しく見る →</a></p></div></section>`;
   replace("HOME_CURRENT_WORK",/    <section class="v4-current"[\s\S]*?<\/section>/,current);
   // On the initial implementation no CURRENT section exists; insert before Projects.
   // The replace above handles subsequent runs with markers. 
   s=s.replace('href="https://rhythmspeaker.stores.jp/" target="_blank" rel="noopener noreferrer">Rhythm Speaker →','href="https://noritap.github.io/rhythmspeaker/" target="_blank" rel="noopener noreferrer">Rhythm Speaker公式サイト →');
   s=s.replace('<link rel="stylesheet" href="assets/css/editorial-photo-library.css">','<link rel="stylesheet" href="assets/css/editorial-photo-library.css">\n  <link rel="stylesheet" href="assets/css/v4-public.css">');
   s=s.replace("Performance / Choreography</h2>","主な出演・振付作品。</h2>");
   s=s.replace('>Careerを詳しく見る →</a>','>出演・振付歴を見る →</a>');
   return s;
 }
 if(file==="career/index.html"){
   const f=(w,cls)=>`          <a class="${cls}" href="${href(w)}" target="_blank" rel="noopener noreferrer"><figure><img src="${image(w)}" alt="${attr(w.title)}の関連映像サムネイル" width="480" height="360" loading="lazy" decoding="async"></figure><div class="career-feature-copy"><span>${esc(w.kind)} · ${esc(w.year)}</span><div><h3>${esc(w.title)}</h3><p>${esc(w.detail?w.detail+" / ":"")}${esc(w.role)}</p></div></div></a>`;
   replace("CAREER_FEATURED_WORKS",/        <div class="career-feature-grid">[\s\S]*?<\/div>(?=\s*<\/div>\s*<\/section>)/,`        <div class="career-feature-grid">\n${f(featured[0],"career-feature-main")}\n          <div class="career-feature-side-stack">\n${featured.slice(1).map(w=>f(w,"career-feature-side")).join("\n")}\n          </div>\n        </div>`);
   const others=data.works.filter(w=>!w.featured).map(w=>`        <a class="career-credit-row" href="${href(w)}" target="_blank" rel="noopener noreferrer"><span class="year">${esc(w.year)}</span><strong>${esc(w.title)}</strong><span>${esc(w.role)}</span><span class="arrow">関連映像 →</span></a>`).join("\n");
   // Preserve the two existing non-video credits as historically documented.
   const archival=`        <div class="career-credit-row"><span class="year">2016</span><strong>RIP SLYME 日本武道館「TOKYO STOMP」</strong><span>出演</span><span class="arrow">LIVE</span></div>\n        <div class="career-credit-row archive-row"><span class="year">2004</span><strong>Chicago Human Rhythm Project「Rhythm World」</strong><span>招聘・出演</span><span class="arrow"><a href="https://www.facebook.com/photo.php?fbid=1236768718491027&amp;set=pb.100064737308832.-2207520000&amp;type=3" target="_blank" rel="noopener noreferrer">ARCHIVE 01</a> / <a href="https://www.facebook.com/photo/?fbid=1236768715157694&amp;set=pb.100064737308832.-2207520000" target="_blank" rel="noopener noreferrer">02</a></span></div>`;
   replace("CAREER_MORE_WORKS",/      <div class="career-credit-list">[\s\S]*?<\/div>(?=\s*<\/section>)/,`      <div class="career-credit-list">\n${others}\n${archival}\n      </div>`);
   return s;
 }
 if(file==="media/index.html"){
   const rows=data.works.map(w=>`      <a href="${href(w)}" target="_blank" rel="noopener noreferrer"><span>${esc(w.kind)} / ${esc(w.role)}</span><strong>${esc(w.media_title||w.title)}</strong><em>関連映像を見る →</em></a>`).join("\n");
   replace("MEDIA_SELECTED_WORKS",/    <div class="media-video-grid">[\s\S]*?<\/div>(?=<p class="media-more">)/,`    <div class="media-video-grid">\n${rows}\n    </div>`);
   s=s.replace('href="https://rhythmspeaker.stores.jp/" target="_blank" rel="noopener noreferrer"><span>03 / STUDIO','href="https://noritap.github.io/rhythmspeaker/" target="_blank" rel="noopener noreferrer"><span>03 / STUDIO');
   return s;
 }
 if(file==="projects/index.html"){
   const groups=[
     {id:"learn",eyebrow:"LEARN / PLAY",title:"学ぶ・楽しむ。",description:"レッスンやゲームで、タップダンスに触れる。"},
     {id:"watch",eyebrow:"WATCH / LISTEN",title:"観る・聴く。",description:"番組、パフォーマンス、音楽を探す。"},
     {id:"vision",eyebrow:"VISION",title:"構想を知る。",description:"活動をつなぐ考え方と、その背景。"},
     {id:"tools",eyebrow:"TOOLS / SHOP",title:"利用する・購入する。",description:"利用者向けサービスと公式ショップ。"}
   ];
   let index=0;
   const str=groups.map((g,gi)=>{
     const links=data.projects.filter(x=>x.group===g.id).map(p=>{index++;let local=!p.url.startsWith("http");return `          <a class="project-row" href="${attr(p.url)}"${local?"":' target="_blank" rel="noopener noreferrer"'}><span class="index">${String(index).padStart(2,"0")}</span><strong>${esc(p.title)}</strong><p>${esc(p.summary)}</p><span class="route">${esc(p.label)} →</span></a>`}).join("\n");
     return `    <section class="projects-section${gi%2===0?" alt":""}"><div class="section-shell"><div class="projects-section-head"><div><p class="projects-label">${esc(g.eyebrow)}</p><h2>${esc(g.title)}</h2></div><p>${esc(g.description)}</p></div><div class="project-list">\n${links}\n        </div></div></section>`;
   }).join("\n\n");
   replace("PROJECT_DIRECTORY",/    <section class="projects-section alt">[\s\S]*?(?=    <section class="projects-why">)/,str+"\n\n");
   s=s.replace("やっていること、<br>ぜんぶ。","活動・プロジェクト。");
   s=s.replace("学ぶ。見る。遊ぶ。使う。","レッスン、番組、音楽、制作、利用者向けサービスを目的から探せます。");
   return s;
 }
 throw Error("Unexpected file: "+file);
};
const expected = ['works', 'services', 'projects', 'updates'];
for (const name of expected) {
  if (!Array.isArray(data[name])) throw new Error('Missing collection: ' + name);
  const ids = data[name].map(x => x.id);
  if (new Set(ids).size !== ids.length) throw new Error('Duplicate id: ' + name);
}
if (data.works.filter(x => x.featured).length !== 3) throw new Error('Exactly 3 featured works required');
for (const p of data.projects) {
  if (!['learn', 'watch', 'vision', 'tools'].includes(p.group)) throw new Error('Invalid project group: '+p.id);
  if (!/^(https:\/\/|(\.\.\/))/.test(p.url)) throw new Error('Invalid project destination: '+p.id);
}
const files = ['index.html', 'career/index.html', 'media/index.html', 'projects/index.html'];
const check = process.argv.includes('--check');
const write = process.argv.includes('--write');
if (check === write) throw new Error('Use either --check or --write');
let drift = [];
for (const file of files) {
  const current = fs.readFileSync(file,'utf8');
  const output = transform(file,current,data);
  if (output !== current) {
    if (check) drift.push(file);
    if (write) fs.writeFileSync(file,output,'utf8');
  }
}
if (drift.length) {
  process.stderr.write('Public content out of sync: '+drift.join(', ')+'\n');
  process.exit(1);
}
process.stdout.write((write ? 'Updated' : 'Verified')+' public content: '+files.join(', ')+'\n');
