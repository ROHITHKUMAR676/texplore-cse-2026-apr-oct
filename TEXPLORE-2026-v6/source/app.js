(function(){
const A=window.ASSETS, $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const root=document.documentElement.style;
const totalPages=$$('.pg').length;
root.setProperty('--bgp','url('+A.bg_purple+')');
root.setProperty('--logo','url('+A.logo+')');
$$('[data-a]').forEach(e=>e.src=A[e.dataset.a]);
$$('[data-bg]').forEach(e=>e.style.backgroundImage='url('+A[e.dataset.bg]+')');
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
let guide=!reduce, pf=null, opened=false;

/* ---------- Adhi's voice ---------- */
const TTS='speechSynthesis' in window;const VOX={on:true,voice:null};let vtok=0;
const CONN=window.ADHI_CONN||[''];
const ACR=[[/₹\s?([\d,.]+)\s*lakhs?/gi,'$1 lakh rupees'],[/₹\s?([\d,.]+)/g,'$1 rupees'],[/(\d)\s?–\s?(\d)/g,'$1 to $2'],[/TN-IMPACT/g,'T N Impact'],[/Vigil-X/g,'Vigil X'],[/\bIIITDM\b/g,'I I I T D M'],[/\bIITM\b/g,'I I T M'],[/\bICCDS\b/g,'I triple C D S'],[/\bIEEE\b/g,'I triple E'],[/\bKBAIC\b/g,'K B A I C'],[/\bIWDC\b/g,'I W D C'],[/\bCSE\b/g,'C S E'],[/\bREC\b/g,'R E C'],[/\bHoD\b/g,'H O D'],[/\bGDG\b/g,'G D G'],[/\bSIH\b/g,'S I H'],[/\bFDP\b/g,'F D P'],[/\bAWS\b/g,'A W S'],[/\bTCS\b/g,'T C S'],[/\bHCL\b/g,'H C L'],[/\bVIT\b/g,'V I T'],[/\bSRM\b/g,'S R M'],[/\bKIT\b/g,'K I T'],[/\bUAG\b/g,'U A G'],[/\bASU\b/g,'A S U'],[/\bPSBs\b/g,'P S Bs'],[/\bCoE\b/g,'C O E'],[/\bUiPath\b/g,'Ui Path'],[/\bGUVI\b/g,'Guvi'],[/\bAI\b/g,'A I'],[/\bML\b/g,'M L'],[/\bDSA\b/g,'D S A'],[/\bDEVS\b/g,'Devs'],[/\bGenAI\b/g,'Gen A I'],[/\bGitHub\b/g,'Git Hub'],[/·/g,', '],[/&amp;/g,'and'],[/&/g,'and']];
const spoken=t=>ACR.reduce((s,[r,x])=>s.replace(r,x),t.replace(/\bDr\.(?=\s)/g,'Doctor')).replace(/\bTEXPLORE\b/g,'Texplore');
const vlist=()=>TTS?speechSynthesis.getVoices().filter(v=>/^en/i.test(v.lang)):[];
function vscore(v){const n=v.name+' '+v.lang;let s=0;
  if(/zira/i.test(v.name))s+=1000;
  if(/natural|neural|online|premium|enhanced/i.test(n))s+=50;
  if(/en-IN/i.test(v.lang))s+=18;else if(/en-GB|en-AU/i.test(v.lang))s+=8;else if(/en-US/i.test(v.lang))s+=6;
  if(/female|woman|zira/i.test(n))s+=30;
  if(/google/i.test(n))s+=12;
  if(/espeak|compact|novelty|whisper|bubbles|zarvox|trinoids|bells|boing|cellos|organ|good news|bad news|jester|albert|fred|junior|kathy|ralph|superstar/i.test(n))s-=60;
  return s}
function fillVoices(){
  const all=vlist();if(!all.length)return;
  VOX.voice=all.find(v=>/UK English Female/i.test(v.name))||all.find(v=>/^en-GB/i.test(v.lang)&&/female|woman|hazel/i.test(v.name))||all[0];
}
function stopVoice(){vtok++;if(TTS)speechSynthesis.cancel();$$('.stage.talk').forEach(s=>s.classList.remove('talk'))}
function say2(st,text,id){
  return new Promise(resolve=>{
    if(!VOX.on||!TTS)return resolve(false);
    const my=++vtok,stg=$('.stage',st.pg);let fin=false;
    const done=ok=>{if(fin)return;fin=true;clearTimeout(sf);stg.classList.remove('talk');resolve(ok)};
    const sf=setTimeout(()=>{if(TTS)speechSynthesis.cancel();done(true)},45000);
    const tryTTS=()=>{
      const sents=spoken(text).match(/[^.!?]+[.!?]*/g)||[text];let i=0;
      stg.classList.add('talk');
      const next=()=>{
        if(my!==vtok)return done(true);if(i>=sents.length)return done(true);
        const sentence=sents[i++].trim();
        const enqueue=(preferred=true)=>{
          if(my!==vtok)return done(true);
          const u=new SpeechSynthesisUtterance(sentence);
          if(preferred&&VOX.voice)u.voice=VOX.voice;
          u.lang=(preferred&&VOX.voice?.lang)||'en-IN';u.rate=.96;u.pitch=.9;u.volume=1;
          u.onend=()=>setTimeout(next,160);
          u.onerror=()=>{
            if(my!==vtok)return done(true);
            if(preferred&&VOX.voice){VOX.voice=null;enqueue(false)}else done(true);
          };
          try{speechSynthesis.resume();speechSynthesis.speak(u)}catch(e){
            if(preferred&&VOX.voice){VOX.voice=null;enqueue(false)}else done(true);
          }
        };
        enqueue();};
      next();
    };
    if(window.ADHI_AUDIO){const a=new Audio('audio/'+id+'.mp3');let ok=false;
      a.addEventListener('canplay',()=>{ok=true;stg.classList.add('talk');a.play().catch(()=>{ok=false;tryTTS()})},{once:true});
      a.addEventListener('ended',()=>done(true));a.addEventListener('error',()=>{if(!ok)tryTTS()},{once:true});
      a.load();return;}
    tryTTS();
  });
}
async function talk(st,text,id,my){
  const t0=Date.now();const ok=await say2(st,text,id);if(my!==tok)return;
  const el=Date.now()-t0;
  if(!ok||el<800)await sleep(rt(text));else await sleep(Math.max(0,2200-el)+450);
}
/* ---------- mascot guide (Adhi): one page speaks at a time ---------- */
const FACE={wave:'r',cheer:'r',spin:'r',point:'l',hop:'l',think:'l',peek:'l',idle:'l'};
const DUR={wave:2500,cheer:2600,spin:1400,point:2700,hop:2500,think:2900,peek:2700};
const ctl=new Map();let tok=0,sig='';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const rt=s=>Math.max(3300,Math.min(7600,1900+(s||'').length*55));
let introMusicDone=Promise.resolve();
function playIntroMusic(){
  const Ctx = window.AudioContext || window.webkitAudioContext;
  if(!Ctx) return new Promise(r => setTimeout(r, 10000));
  let ctx;
  try { ctx = new Ctx(); } catch(e) { return Promise.resolve(); }
  ctx.resume().catch(()=>{});

  const now = ctx.currentTime + 0.05;
  const BAR = 2.35;

  // ---- Master chain: soft compressor -> out, with fade in/out ----
  const master = ctx.createGain();
  master.gain.setValueAtTime(0.0001, now);
  master.gain.linearRampToValueAtTime(1.15, now + 1.2);
  master.gain.setValueAtTime(1.15, now + 8.9);
  master.gain.exponentialRampToValueAtTime(0.0001, now + 9.95);
  const comp = ctx.createDynamicsCompressor();
  comp.threshold.value = -20; comp.ratio.value = 3; comp.attack.value = 0.02; comp.release.value = 0.4;
  master.connect(comp); comp.connect(ctx.destination);

  // ---- Reverb (generated impulse response, no files needed) ----
  const irLen = ctx.sampleRate * 3.2;
  const ir = ctx.createBuffer(2, irLen, ctx.sampleRate);
  for(let c = 0; c < 2; c++){
    const d = ir.getChannelData(c);
    for(let i = 0; i < irLen; i++) d[i] = (Math.random()*2-1) * Math.pow(1 - i/irLen, 2.6);
  }
  const reverb = ctx.createConvolver(); reverb.buffer = ir;
  const wet = ctx.createGain(); wet.gain.value = 0.55;
  const dry = ctx.createGain(); dry.gain.value = 0.8;
  const mix = ctx.createGain();
  mix.connect(dry); dry.connect(master);
  mix.connect(reverb); reverb.connect(wet); wet.connect(master);

  // ---- Pad bus with slow, breathing low-pass sweep ----
  const padFilter = ctx.createBiquadFilter();
  padFilter.type = 'lowpass'; padFilter.Q.value = 0.4;
  padFilter.frequency.setValueAtTime(600, now);
  padFilter.frequency.linearRampToValueAtTime(1500, now + 5);
  padFilter.frequency.linearRampToValueAtTime(900, now + 9.5);
  padFilter.connect(mix);

  const panner = (p) => {
    if(!ctx.createStereoPanner) return null;
    const n = ctx.createStereoPanner(); n.pan.value = p; return n;
  };

  // ---- Warm pad: two slightly detuned oscillators per note ----
  function pad(hz, at, len, vol){
    const g = ctx.createGain();
    g.gain.setValueAtTime(0.0001, at);
    g.gain.linearRampToValueAtTime(vol, at + 0.9);
    g.gain.setValueAtTime(vol, at + len - 0.2);
    g.gain.exponentialRampToValueAtTime(0.0001, at + len + 0.9);
    [-7, 7].forEach((cents, i) => {
      const o = ctx.createOscillator();
      o.type = i ? 'triangle' : 'sine';
      o.frequency.value = hz; o.detune.value = cents;
      o.connect(g); o.start(at); o.stop(at + len + 1);
    });
    g.connect(padFilter);
  }

  // ---- Soft sub bass ----
  function bass(hz, at, len){
    const o = ctx.createOscillator(), g = ctx.createGain();
    o.type = 'sine'; o.frequency.value = hz;
    g.gain.setValueAtTime(0.0001, at);
    g.gain.linearRampToValueAtTime(0.12, at + 0.5);
    g.gain.exponentialRampToValueAtTime(0.0001, at + len);
    o.connect(g); g.connect(master); o.start(at); o.stop(at + len + 0.1);
  }

  // ---- Melody: gentle bell / music-box pluck ----
  function bell(hz, at, vol, pan){
    const g = ctx.createGain();
    g.gain.setValueAtTime(0.0001, at);
    g.gain.linearRampToValueAtTime(vol, at + 0.02);
    g.gain.exponentialRampToValueAtTime(0.0001, at + 2.2);
    const o1 = ctx.createOscillator(), o2 = ctx.createOscillator(), g2 = ctx.createGain();
    o1.type = 'sine'; o1.frequency.value = hz;
    o2.type = 'sine'; o2.frequency.value = hz * 2.005; g2.gain.value = 0.18; // shimmer overtone
    o1.connect(g); o2.connect(g2); g2.connect(g);
    const p = panner(pan);
    if(p){ g.connect(p); p.connect(mix); } else { g.connect(mix); }
    o1.start(at); o2.start(at); o1.stop(at + 2.3); o2.stop(at + 2.3);
  }

  // Chords: Cmaj7 -> Am7 -> Fmaj7 -> G6 (calm, hopeful)
  const chords = [
    [130.81, 164.81, 196.00, 246.94],
    [110.00, 130.81, 164.81, 196.00],
    [ 87.31, 110.00, 130.81, 164.81],
    [ 98.00, 146.83, 196.00, 220.00]
  ];
  chords.forEach((notes, i) => {
    const at = now + i * BAR;
    notes.forEach((hz, n) => {
      pad(hz, at, BAR, n === 0 ? 0.040 : 0.027);
      pad(hz * 2, at + 0.05, BAR, 0.011); // airy octave above
    });
    bass(notes[0] / 2, at, BAR + 0.4);
  });

  // Melody (C pentatonic-ish), [bar, offset, Hz, volume, pan]
  const melody = [
    [0, 0.35, 659.25, 0.075, -0.3], [0, 0.95, 783.99, 0.063,  0.2], [0, 1.60, 1046.5, 0.069, -0.1],
    [1, 0.35, 880.00, 0.075,  0.3], [1, 0.95, 1046.5, 0.063, -0.2], [1, 1.60, 1318.5, 0.056,  0.25],
    [2, 0.35, 880.00, 0.075, -0.25],[2, 0.95, 1046.5, 0.063, 0.15], [2, 1.60, 880.00, 0.056, -0.1],
    [3, 0.35, 1174.7, 0.069,  0.2], [3, 0.95, 987.77, 0.063, -0.2], [3, 1.60, 783.99, 0.063,  0.1],
    [3, 2.10, 1046.5, 0.050,  0.0] // soft resolve into the fade
  ];
  melody.forEach(([bar, off, hz, vol, pan]) => bell(hz, now + bar * BAR + off, vol, pan));

  return new Promise(resolve => setTimeout(() => { ctx.close().catch(()=>{}); resolve(); }, 10000));
}
function mk(pg){
  const st={pg,m:$('.mascot',pg),b:$('.bubble',pg),hs:$$('.hs',pg),i:-1,pt:null,mt:null};
  st.m.classList.add('face-l');
  st.hs.forEach((h,k)=>h.addEventListener('click',()=>manual(st,k)));
  st.m.addEventListener('click',e=>{e.stopPropagation();if(!opened)return;
    if(st.hs.length)manual(st,(st.i+1)%st.hs.length);else{tok++;allReset();pose(st,['wave','hop','cheer','spin'][Math.floor(Math.random()*4)]);const tx=st.pg.dataset.intro.split('||')[0];say(st,'Adhi',tx,'');const my=tok;talk(st,tx,'p'+st.pg.dataset.n+'-intro0',my).then(()=>{if(my===tok)reset(st)})}});
  return st;
}
function pose(st,name){
  const m=st.m;clearTimeout(st.pt);
  m.className='mascot';void m.offsetWidth;
  if(FACE[name]==='l')m.classList.add('face-l');
  m.classList.add('p-'+name);
  if(name==='cheer')burst(st);
  st.pt=setTimeout(()=>{m.className='mascot face-l'},DUR[name]||2500);
}
function say(st,t,d,c){
  const b=st.b;b.classList.remove('show');
  $('b',b).textContent=t||'';$('span',b).textContent=d||'';$('i',b).textContent=c||'';
  void b.offsetWidth;b.classList.add('show');
}
function show(st,k){
  st.i=k;const h=st.hs[k];
  st.hs.forEach(x=>x.classList.toggle('on',x===h));
  st.pg.classList.add('has-on');
  say(st,h.dataset.t,h.dataset.d,h.dataset.c);
  pose(st,h.dataset.pose||'point');
}
function reset(st){clearTimeout(st.mt);clearTimeout(st.pt);st.hs.forEach(x=>x.classList.remove('on'));st.pg.classList.remove('has-on');st.b.classList.remove('show');st.m.className='mascot face-l'}
function allReset(){stopVoice();ctl.forEach(reset)}
function manual(st,k){if(!opened)return;const my=++tok;allReset();show(st,k);const h=st.hs[k];talk(st,hs_text(h,k),'p'+st.pg.dataset.n+'-h'+k,my).then(()=>{if(my===tok){st.mt=setTimeout(()=>reset(st),2500)}})}
const hs_text=(h,k)=>CONN[k%CONN.length]+h.dataset.t+'. '+h.dataset.d;
async function speak(st,my){
  const parts=(st.pg.dataset.intro||'').split('||');const n=+st.pg.dataset.n;
  for(let i=0;i<parts.length;i++){
    say(st,n===1&&i===0?'Hi, I’m Adhi!':(i?'Adhi':'Page '+n),parts[i],'');pose(st,i?'think':'wave');
    await talk(st,(n===1&&i===0?'Hi there! ':(i===0?'Page '+n+'. ':''))+parts[i],'p'+n+'-intro'+i,my);if(my!==tok)return false;
  }
  for(let k=0;k<st.hs.length;k++){
    show(st,k);await talk(st,hs_text(st.hs[k],k),'p'+n+'-h'+k,my);if(my!==tok)return false;
  }
  reset(st);return true;
}
async function runSpread(){
  const my=++tok;allReset();if(!opened||!guide)return;
  await introMusicDone;if(my!==tok)return;
  const vis=visiblePages().sort((a,b)=>a.dataset.n-b.dataset.n).map(p=>ctl.get(p));
  for(const st of vis){
    if(!(await speak(st,my)))return;
    await sleep(600);if(my!==tok)return;
  }
  const last=vis[vis.length-1];
  if(last&&+last.pg.dataset.n<totalPages){say(last,'Adhi','Flip the page and I’ll tell you about the next one!','');pose(last,'wave');await talk(last,'Flip the page, and I’ll tell you about the next one!','next-prompt',my);if(my!==tok)return;reset(last)}
}
function burst(st){
  const s=$('.stage',st.pg);const cols=['#ffc21a','#ff3dd2','#fff','#8a5cff'];
  for(let i=0;i<14;i++){const e=document.createElement('span');e.className='spark';e.textContent=i%3?'✦':'★';
    e.style.color=cols[i%4];e.style.right=(8+Math.random()*10)+'cqw';e.style.bottom=(10+Math.random()*8)+'cqw';
    e.style.setProperty('--dx',(-18+Math.random()*10-Math.random()*20)+'cqw');e.style.setProperty('--dy',(-8-Math.random()*22)+'cqw');e.style.setProperty('--rot',(Math.random()*360)+'deg');
    s.appendChild(e);setTimeout(()=>e.remove(),1200);}
}
function visiblePages(){
  const W=innerWidth;
  return $$('.pg').filter(pg=>{const r=pg.getBoundingClientRect();const pe=pg.closest('.page');
    if(!r.width||getComputedStyle(pe).display==='none')return false;
    const cx=r.left+r.width/2;return cx>0&&cx<W&&r.width>40&&r.top<innerHeight&&r.bottom>0;});
}
function sync(){
  const vis=visiblePages();
  $('#book').classList.toggle('cov',vis.length===1&&+vis[0].dataset.n===1);
  const ns=vis.map(p=>+p.dataset.n).sort((a,b)=>a-b);
  $('#pn').textContent=(ns.length?(ns.length>1?ns[0]+'–'+ns[ns.length-1]:ns[0]):'')+' / '+totalPages;
  const s=ns.join(',');if(s!==sig){sig=s;runSpread()}
}
/* ---------- book ---------- */
function initBook(){
  $$('.pg').forEach(pg=>ctl.set(pg,mk(pg)));
  pf=new St.PageFlip($('#book'),{width:700,height:990,size:'stretch',minWidth:260,maxWidth:1100,minHeight:370,maxHeight:1560,
    maxShadowOpacity:.55,showCover:true,mobileScrollSupport:false,flippingTime:1000,usePortrait:true,startZIndex:0,autoSize:true,clickEventForward:true,swipeDistance:30,drawShadow:true});
  pf.loadFromHTML($$('.page'));window.__pf=pf;
  const upd=()=>setTimeout(sync,120);
  pf.on('flip',upd);pf.on('changeState',e=>{if(e.data==='read')upd()});pf.on('changeOrientation',upd);
  addEventListener('resize',upd);
  $$('[data-go]').forEach(a=>a.addEventListener('click',e=>{e.stopPropagation();go(+a.dataset.go)}));
}
function go(n){if(pf){pf.flip(n)}}
function ctrls(){
  $('#prev').onclick=()=>pf&&pf.flipPrev();$('#nxt').onclick=()=>pf&&pf.flipNext();
  $$('#bar [data-j]').forEach(b=>b.onclick=()=>go(+b.dataset.j));
  const g=$('#gd');g.classList.toggle('on',guide);g.onclick=()=>{guide=!guide;g.classList.toggle('on',guide);g.textContent='Mascot guide: '+(guide?'on':'off');
    if(guide)runSpread();else{tok++;allReset()}};
  g.textContent='Mascot guide: '+(guide?'on':'off');
  $('#vx').onclick=()=>{VOX.on=!VOX.on;$('#vx').classList.toggle('on',VOX.on);$('#vx').textContent='Voice: '+(VOX.on?'on':'off');if(!VOX.on)stopVoice()};
  if(TTS){fillVoices();speechSynthesis.onvoiceschanged=fillVoices}else{$('#vx').style.display='none'}
  $('#vx').classList.add('on');
  $('#fs').onclick=()=>{document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen()};
  addEventListener('keydown',e=>{if(!opened)return;if(e.key==='ArrowRight')pf.flipNext();else if(e.key==='ArrowLeft')pf.flipPrev();else if(e.key==='g')g.click();});
}
/* ---------- intro ---------- */
function openBook(){
  if(opened)return;opened=true;
  introMusicDone=playIntroMusic();
  if(TTS){try{const u=new SpeechSynthesisUtterance(' ');u.volume=0;speechSynthesis.speak(u)}catch(e){}}
  $('#intro').classList.add('leave');document.body.classList.add('open');
  setTimeout(()=>{$('#intro').remove()},1300);sig='';sync();
  setTimeout(()=>{const h=$('#hint');h.classList.add('show');setTimeout(()=>h.classList.remove('show'),6500)},2200);
  cancelAnimationFrame(raf);
}
let raf;
function intro(){
  const cv=$('#introCv'),ctx=cv.getContext('2d');let W,H,dpr=Math.min(devicePixelRatio||1,2);
  const rs=()=>{W=innerWidth;H=innerHeight;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0)};rs();addEventListener('resize',rs);
  const T=$('#introTxt');const OFF=reduce?0:4600;const seq=[[2300,'.a'],[3500,'.b'],[4500,'.c'],[5800,'#enter']];
  seq.forEach(([ms,s])=>setTimeout(()=>$(s,T).classList.add('in'),reduce?0:ms+OFF));
  const lr=$('.lr');if(!reduce){setTimeout(()=>lr.classList.add('show'),200);setTimeout(()=>lr.classList.add('expand'),2100);setTimeout(()=>lr.classList.add('out'),4000)}else lr.remove();
  $('#enter').onclick=openBook;$('#skip').onclick=openBook;
  addEventListener('keydown',e=>{if(!opened&&(e.key==='Enter'||e.key===' '))openBook()});
  const img=new Image();img.onload=()=>{
    const sw=150,sh=Math.round(sw*img.height/img.width),oc=document.createElement('canvas');oc.width=sw;oc.height=sh;
    const o=oc.getContext('2d');o.drawImage(img,0,0,sw,sh);const d=o.getImageData(0,0,sw,sh).data;
    const P=[];for(let y=0;y<sh;y+=2)for(let x=0;x<sw;x+=2){if(d[(y*sw+x)*4+3]>140){const nx=x/sw,ny=y/sh;
      const a=Math.random()*6.283,r=Math.max(innerWidth,innerHeight)*(.55+Math.random()*.7);
      P.push({nx,ny,sx:Math.cos(a)*r,sy:Math.sin(a)*r,dl:Math.random()*1.5+(ny)*.5,s:1+Math.random()*1.3,k:Math.random()*6.28,fl:ny<.36&&nx>.24&&nx<.66})}}
    const sparks=[];const t0=performance.now()+OFF;
    const ez=t=>1-Math.pow(1-t,3);
    function frame(now){
      const t=(now-t0)/1000;ctx.clearRect(0,0,W,H);if(t<0){raf=requestAnimationFrame(frame);return}
      const lh=Math.min(H*.5,W*.8),lw=lh*sw/sh,ox=W/2-lw/2,oy=H*.08;
      ctx.globalCompositeOperation='lighter';
      const formed=Math.min(1,Math.max(0,(t-2.2)/1.4));
      if(formed>0){const g=ctx.createRadialGradient(W/2,oy+lh*.2,0,W/2,oy+lh*.2,lh*.7);g.addColorStop(0,'rgba(255,170,40,'+(.38*formed*(.85+.15*Math.sin(t*5)))+')');g.addColorStop(.5,'rgba(190,60,255,'+(.2*formed)+')');g.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);}
      for(const p of P){
        const e=reduce?1:ez(Math.min(1,Math.max(0,(t-p.dl)/2.2)));
        const sw2=(1-e)*Math.sin(t*2+p.k)*lh*.15;
        let x=ox+p.nx*lw+p.sx*(1-e)+sw2,y=oy+p.ny*lh+p.sy*(1-e)-sw2*.5;
        if(e>=1){x+=Math.sin(t*3+p.k)*.7;y+=Math.cos(t*2.6+p.k)*.7;}
        let col='hsla('+(285-p.ny*50)+',100%,'+(70+p.ny*22)+'%,'+(.35+.6*e)+')';
        ctx.fillStyle=col;const s=p.s*(lh/330);ctx.fillRect(x,y,s,s);
              }
      if(formed>.6)for(let q=0;q<2;q++)sparks.push({x:ox+(.3+Math.random()*.28)*lw,y:oy+(.1+Math.random()*.2)*lh,vx:(Math.random()-.5)*40,vy:-50-Math.random()*90,l:1});
      for(let i=sparks.length-1;i>=0;i--){const s=sparks[i];s.x+=s.vx*.016;s.y+=s.vy*.016;s.l-=.012;if(s.l<=0){sparks.splice(i,1);continue}
        ctx.fillStyle='rgba(255,'+(160+s.l*80|0)+',60,'+s.l+')';ctx.fillRect(s.x,s.y,2.4,2.4)}
      if(formed>.5){ctx.globalAlpha=Math.min(.55,(formed-.5)*1.1);ctx.globalCompositeOperation='source-over';ctx.drawImage(img,ox,oy,lw,lh);ctx.globalAlpha=1}
      raf=requestAnimationFrame(frame);
    }
    raf=requestAnimationFrame(frame);
  };img.src=A.logo_s;
}
function bind(r){$$('[data-a]',r).forEach(e=>{if(!e.src)e.src=A[e.dataset.a]})}
function openSheet(id){
  const t=$('#tpl-'+id);if(!t)return;const body=$('#shBody');body.innerHTML='';body.appendChild(t.content.cloneNode(true));bind(body);
  $('#sheet').hidden=false;$('.shcard').scrollTop=0;if(opened){tok++;allReset()}
}
function closeSheet(){$('#sheet').hidden=true;$('#shBody').innerHTML=''}
document.addEventListener('click',e=>{const s=e.target.closest('[data-sheet]');if(s){e.stopPropagation();openSheet(s.dataset.sheet)}});
$('.shx').onclick=closeSheet;$('#sheet').addEventListener('click',e=>{if(e.target.id==='sheet')closeSheet()});
addEventListener('keydown',e=>{if(e.key==='Escape'&&!$('#sheet').hidden)closeSheet()});
ctrls();
function boot(){initBook();intro();}
if(window.St)boot();else addEventListener('load',()=>window.St?boot():(document.title+=' (library failed)'));
})();
