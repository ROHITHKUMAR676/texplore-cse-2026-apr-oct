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
  const sel=$('#vs'),all=vlist();if(!all.length||!sel)return;
  const preferred=all.find(v=>/UK English Female/i.test(v.name))||all.find(v=>/^en-GB/i.test(v.lang)&&/female|woman|hazel/i.test(v.name))||all[0],vs=[preferred];
  let saved=null;try{saved=localStorage.getItem('adhiVoice')}catch(e){}
  const zira=vs.find(v=>/zira/i.test(v.name));const keep=vs.find(v=>v.name===saved);VOX.voice=zira||keep||vs[0];
  sel.innerHTML=vs.slice(0,14).map(v=>'<option value="'+v.name.replace(/"/g,'')+'">'+v.name.replace(/^(Microsoft|Google)\s/,'').replace(/ Online \(Natural\)/,' (Natural)')+' · '+v.lang+'</option>').join('');
  if(!vs.slice(0,14).includes(VOX.voice))VOX.voice=vs[0];
  sel.value=VOX.voice.name.replace(/"/g,'');
}
function stopVoice(){vtok++;if(TTS)speechSynthesis.cancel();$$('.stage.talk').forEach(s=>s.classList.remove('talk'))}
function say2(st,text,id){
  return new Promise(resolve=>{
    if(!VOX.on||!TTS||!VOX.voice)return resolve(false);
    const my=++vtok,stg=$('.stage',st.pg);let fin=false;
    const done=ok=>{if(fin)return;fin=true;clearTimeout(sf);stg.classList.remove('talk');resolve(ok)};
    const sf=setTimeout(()=>{if(TTS)speechSynthesis.cancel();done(true)},45000);
    const tryTTS=()=>{
      const sents=spoken(text).match(/[^.!?]+[.!?]*/g)||[text];let i=0;
      stg.classList.add('talk');
      const next=()=>{
        if(my!==vtok)return done(true);if(i>=sents.length)return done(true);
        const u=new SpeechSynthesisUtterance(sents[i++].trim());u.voice=VOX.voice;u.lang=VOX.voice.lang;u.rate=.96;u.pitch=.9;u.volume=1;
        u.onend=()=>setTimeout(next,160);u.onerror=()=>done(true);speechSynthesis.speak(u);};
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
  const Ctx=window.AudioContext||window.webkitAudioContext;if(!Ctx)return new Promise(r=>setTimeout(r,10000));
  let ctx;try{ctx=new Ctx()}catch(e){return Promise.resolve()}
  const now=ctx.currentTime,master=ctx.createGain(),filter=ctx.createBiquadFilter();filter.type='lowpass';filter.frequency.value=900;filter.Q.value=.35;master.gain.setValueAtTime(.0001,now);master.gain.linearRampToValueAtTime(.72,now+.9);master.gain.setValueAtTime(.72,now+9.1);master.gain.exponentialRampToValueAtTime(.0001,now+9.95);filter.connect(master);master.connect(ctx.destination);ctx.resume().catch(()=>{});
  const chords=[[130.81,164.81,196,246.94],[110,130.81,164.81,196],[87.31,110,130.81,164.81],[98,146.83,196,220]];
  chords.forEach((notes,index)=>notes.forEach((hz,note)=>{
    const at=now+index*2.35,osc=ctx.createOscillator(),warm=ctx.createOscillator(),gain=ctx.createGain();osc.type='sine';osc.frequency.value=hz;warm.type='sine';warm.frequency.value=hz*2;gain.gain.setValueAtTime(.0001,at);gain.gain.linearRampToValueAtTime(note === 0 ? .014 : .009,at+.8);gain.gain.setValueAtTime(note === 0 ? .014 : .009,at+2.35);gain.gain.exponentialRampToValueAtTime(.0001,at+3.05);osc.connect(gain);warm.connect(gain);gain.connect(filter);osc.start(at);warm.start(at);osc.stop(at+3.1);warm.stop(at+3.1);
  }));
  return new Promise(resolve=>setTimeout(()=>{ctx.close().catch(()=>{});resolve()},10000));
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
  $('#vs').onchange=e=>{const v=vlist().find(x=>x.name===e.target.value);if(!v)return;VOX.voice=v;try{localStorage.setItem('adhiVoice',v.name)}catch(er){}if(guide){runSpread()}};
  if(TTS){fillVoices();speechSynthesis.onvoiceschanged=fillVoices}else{$('#vx').style.display='none';$('#vs').style.display='none'}
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
