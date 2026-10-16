import json, html, os, sys
MODE=os.environ.get('MODE','web')
A=json.load(open('assets.json'))
def e(s): return html.escape(s,quote=True)
def fig(key,x,y,w,h,cap=None,t=None,d=None,c='',pose='point',rot=0,pos='50% 50%',fit='cover',cls=''):
    hs=' hs' if t else ''
    at=f' data-t="{e(t)}" data-d="{e(d)}" data-c="{e(c)}" data-pose="{pose}"' if t else ''
    cp=f'<figcaption>{cap}</figcaption>' if cap else ''
    return (f'<figure class="fig{hs} {cls}" style="left:{x}%;top:{y}%;width:{w}%;height:{h}%;--r:{rot}deg"{at}>'
            f'<div class="ph"><img data-a="{key}" alt="" style="object-fit:{fit};object-position:{pos}"></div>{cp}</figure>')
def tx(x,y,w,inner,cls='p',size=None,extra=''):
    s=f'left:{x}%;top:{y}%;width:{w}%;'+(f'font-size:{size}cqw;' if size else '')+extra
    return f'<div class="{cls}" style="{s}">{inner}</div>'
def chip(x,y,w,big,small,rot=-3,t=None,d=None,c='',pose='cheer',size=4.4):
    hs=' hs' if t else ''
    at=f' data-t="{e(t)}" data-d="{e(d)}" data-c="{e(c)}" data-pose="{pose}"' if t else ''
    return f'<div class="chipbig{hs}" style="left:{x}%;top:{y}%;width:{w}%;--r:{rot}deg;font-size:{size}cqw"{at}>{big}<small>{small}</small></div>'
ICON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4.5 4-6.5 8-6.5s7 2 8 6.5"/></svg>'
ICON2='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="m21 17-5-5-8 7"/></svg>'
def slot(x,y,w,h,label,icon=ICON2,t=None,d=None,c='Reserved',pose='think'):
    hs=' hs' if t else ''
    at=f' data-t="{e(t)}" data-d="{e(d)}" data-c="{e(c)}" data-pose="{pose}"' if t else ''
    return f'<div class="slot{hs}" style="left:{x}%;top:{y}%;width:{w}%;height:{h}%"{at}>{icon}{label}</div>'
LOGO='<div class="logo"><i></i><b>RAJALAKSHMI<br><span>ENGINEERING</span><br>COLLEGE</b></div>'
BG={'stu':'bg_purple','fac':'bg_white','dep':'bg_red','front':'bg_purple'}
def page(n,sec,tag,intro,inner,hard=False,cover=False):
    dens='hard' if hard else 'soft'
    tg=f'<div class="tag">{tag}</div>' if tag else ''
    return (f'<div class="page" data-density="{dens}"><div class="pg sec-{sec}" data-n="{n}" data-intro="{e(intro)}">'
      f'<div class="bg" data-bg="{BG[sec]}"></div><div class="shade"></div>'
      f'<header class="hd">{LOGO}{tg}</header>{inner}'
      +('' if cover else f'<div class="folio">TEXPLORE 2026<b>{n:02d}</b></div>')+
      '<div class="stage"><div class="bubble"><em class="eq"><u></u><u></u><u></u><u></u></em><b></b><span></span><i></i></div>'
      '<div class="mascot"><img class="r" data-a="mascot" alt="REC mascot"><img class="l" data-a="mascot_l" alt=""><span class="glint"></span></div></div>'
      '</div></div>')
def H1(txt,y=11.5,size=6,x=6,w=88,cls='h1'): return f'<div class="{cls}" style="left:{x}%;top:{y}%;width:{w}%;font-size:{size}cqw">{txt}</div>'
def KICK(txt,y,x=6,w=88): return f'<div class="kick" style="left:{x}%;top:{y}%;width:{w}%">{txt}</div>'
P=[]
CONN=['']
# 1 cover
TILES=['resonance', 'mule1', 'iwdc', 'vig2', 'kba3', 'fdp2', 'chd1', 'xyntra', 'wr1', 'iv1', 'techdecks', 'im3', 'gdg2', 'bestdept', 'nexora', 'fdp1', 'ind1', 'iccds2', 'mule2', 'vig1', 'chd2', 'gl1', 'powerbi', 'iv4', 'glitches2', 'wr5', 'iccds3', 'ind2', 'kba2', 'fdp4']
SPAN={3:'t2',9:'w2',14:'t2',20:'t2',26:'w2'}
wall='<div class="wall"><div class="wg">'+''.join(f'<figure class="{SPAN.get(i,"")}"><img data-a="{k}" alt=""></figure>' for i,k in enumerate(TILES))+'</div></div><div class="scrim"></div>'
cov=(wall+'<div class="cover-title"><h1 class="sweep">TEXPLORE</h1><h2>2026</h2></div>'
 +'<div class="dept" style="top:44%;font-size:2.55cqw">Department of Computer Science and Engineering</div>'
 +'<div class="h2" style="left:6%;top:59%;font-size:6.2cqw;line-height:1.06;text-shadow:0 .5cqw 2cqw rgba(0,0,0,.6)">Dream big.<br><span style="color:#b9a3ff">Code bold.</span><br><span style="color:#ff6a7d">Innovate.</span></div>'
 +tx(6,82,62,'Turn ideas into technology that changes lives.','p',2.4)
 +'<div class="edn" style="left:50%;top:51.2%">Edition  <i>·</i> VOL 13 ISSUE 8</div>')
P.append(page(1,'front','','I’m Adhi, and I’ll take you through this magazine, one page at a time.||Flip the page whenever you like. I’ll tell you the story of each page, then wait for you.',cov,hard=True,cover=True))
# 2 HoD
hod=(H1('From the desk<br>of the HoD',11.5,5.6)
 +fig('hod',6,26,36,29,'Dr. J. Manoranjini','Dr. J. Manoranjini','Head of the Department of Computer Science and Engineering, with a message on the year’s achievements.','HoD · CSE','wave',-2,pos='50% 18%')
 +'<div class="h1" style="left:44.5%;top:24.6%;font-size:11cqw;color:var(--gold);opacity:.9;line-height:1">“</div>'
 +tx(56,27.5,38,'<span style="font-family:Unbounded,sans-serif;font-weight:800;font-size:3.1cqw;line-height:1.15;display:block;color:#fff">Dr. J. Manoranjini</span><span style="display:block;margin:.8cqw 0 1.8cqw;font-weight:700;color:var(--gold);font-size:2.1cqw">Head of the Department<br>Computer Science and Engineering</span>It is a privilege to present TEXPLORE 2026, a record of a year in which our students, faculty and partners turned ideas into results. The department was honoured with the <b>Best Department Award 2025</b>, and that recognition belongs to every one of you.','p',2.0)
 +tx(6,60,88,'Our students carried the department’s name across the country: <b>first places</b> at the IntelliTrace Hackathon and Acentra Health BUILD TO CARE, <b>third places</b> at the Chandigarh Police Hackathon and SRM Designathon, and a special prize at TN-IMPACT. On 18 July 2026, <b>1,000 computing students built 1,000 agentic AI bots in 120 minutes</b> to set a World Records Union record. Our Centre of Excellence in Blockchain Technology, the Upskill series with 133+ certificates, global sessions with Sunway University, Arizona State University and UAG Mexico, and faculty programmes in Generative and Agentic AI reflect one commitment: learning that prepares our graduates for the world they will build. My thanks to our faculty, students and industry partners. I invite you to read on.','p',2.0)
 +tx(6,79.4,60,'<i style="font-weight:600;color:rgba(246,241,255,.85)">With best wishes,</i><br><b>Dr. J. Manoranjini</b>, Head of the Department, CSE','p',2.0))
P.append(page(2,'front','Foreword','A message from our Head of the Department, Dr. J. Manoranjini, on the department’s year.',hod))
# 3 TOC
def grp(color,title,rng,items):
    r=''.join(f'<a data-go="{n+1}"><span>{t}</span><em>{n+2}</em></a>' for t,n in items)
    return f'<div class="grp"><h3><s style="background:{color}"></s>{title}<em>{rng}</em></h3><div class="items">{r}</div></div>'
toc=('<div class="toc" style="font-size:2.3cqw">'
 +grp('#ff3dd2','Student Achievements','6–15',[('Competitions &amp; firsts',4),('Fests &amp; hackathons',5),('TN-IMPACT 2026',6),('Chandigarh Police Hackathon',7),('Mule Scanner AI',8),('Vigil-X',9),('More hackathon wins',10),('Clubs: KBAIC',11),('Clubs: DEVS',12),('Clubs: Intellexa &amp; Google Developer’s Club',13)])
 +grp('#e9ecff','Faculty Achievements','16–17',[('Faculty of the Year',14),('Faculty empowerment',15)])
 +grp('#ff2d4a','Department Achievements','18–24',[('Best Department Award',16),('World record: AI Botathon 1000',17),('Conferences &amp; guest lecture',19),('Workshops',20),('Industrial visits',21),('Global immersion',22)])
 +'<div class="grp"><h3 data-go="24" style="cursor:pointer"><s style="background:#ffc21a"></s>Meet the Team<em>25</em></h3></div></div>')
toc=toc.replace('<div class="toc" style="font-size:2.3cqw">','<div class="toc" style="font-size:2.3cqw">')
P.append(page(3,'front','Contents','Contents are listed here for easy navigation.',H1('Inside<br>this issue',11,5.6)+toc))
# 4
p4=(H1('Student<br>Achievements',11,5.6)+KICK('National &amp; international competitions',24.2)
 +fig('iwdc',6,29,50,25,'IWDC InnovateHer · 1st Prize','Keerthana M G wins 1st Prize','First prize at the IWDC InnovateHer competition conducted at REC.','1st Prize','hop',-2)
 +fig('glitches',60,30,34,19,'Team Glitches','Glitches take the 1st prize','1st prize at the 3rd Project Contest for Design Thinking and Innovation 2025.','1st Prize · 2025','cheer',3)
 +fig('glitches2',58,54,34,21,'Winners with their prizes','The winning moment','The Glitches team with their prize books at the Design Thinking contest.','Design Thinking 2025','wave',-2)
 +tx(6,59,46,'<b>Keerthana M G</b> (220701123) won the 1st Prize at the IWDC InnovateHer competition conducted at REC.')
 +tx(6,70,46,'<b>Glitches</b> won the 1st prize at the 3rd Project Contest for Design Thinking and Innovation 2025.'))
P.append(page(4,'stu','Students','Our students have been busy winning. Here are highlights from the year.',p4))
# 5
p5=(H1('Student<br>Achievements',11,5.6)
 +fig('vignesh',6,25,26,17,'Vignesh','The Recharge website','Vignesh, a third-year CS student, built the Recharge website for the college’s cultural fest.','Student developer','wave',-2,pos='50% 20%')
 +tx(35,25,28,'<b>Recharge website:</b> a third-year Computer Science student took on building the site for the college’s cultural fest.',size=2.1)
 +fig('techdecks',66,25,28,17,'TechDecks · runner-up','TechDecks: runner-up','Runner-up at the HappyFox Hackathon on the theme Campus Connect, 24 Feb 2025.','Runner-up','cheer',3)
 +fig('resonance',6,48,41,17,"Resonance’25",'Resonance’25 tech fest','Intellexa’s flagship fest: Cyber Quest, DSA Battle, Database Design Duel and more.','Tech fest','hop',-2)
 +fig('xyntra',54,48,40,17,"Xyntra’25",'Xyntra’25: 36 hours','IEEE Computer Society REC’s 36-hour national-level hackathon.','36-hour hackathon','think',2)
 +tx(6,69,41,'<b>Resonance’25</b> challenged participants with Cyber Quest, DSA Battle, Database Design Duel, Web Wizard Relay and Pitch Perfect, plus Flutter and 3D design workshops.',size=2.1)
 +tx(54,69,40,'<b>Xyntra’25</b> was not merely a hackathon but a priceless experience. Team: Keerthana M G, Hareesh S S, Jayakanth Sivakumar and Maria Darsha.',size=2.1))
P.append(page(5,'stu','Students','Fests and hackathons, with stories of what our students built.',p5))
# 6
p6=(H1('TN-IMPACT<br>2026',11,6.3)
 +fig('tn',6,27,46,41,None,'Special Prize at TN-IMPACT','Our team stood out among 750+ teams at Tamil Nadu’s largest industrial hackathon.','Top 20 of 750+','cheer',-2,fit='contain',cls='noframe')
 +fig('press',58,40,36,36,'In the press','Making the news','A Tamil newspaper clipping from the department’s achievements file.','Press','think',3,pos='50% 0%')
 +tx(58,26,36,'<b>Special mention</b> at TN-IMPACT 2026, Tamil Nadu’s largest industrial hackathon at KIT. Top 20. 750+ teams. One standout idea.',size=2.3)
 +chip(6,72,46,'Top 20','from 750+ teams',-2,size=4.6))
P.append(page(6,'stu','Students','A special mention among 750+ teams.',p6))
# 7
p7=(H1('Chandigarh<br>Police Hackathon',11,5)
 +fig('chd1',6,28,58,27,'Receiving the ₹50,000 cheque','3rd place, ₹50,000','Raghavan S, Mymoon Beevi, Prajeet V and Prajith S secured 3rd place, with a ₹50,000 cash prize and a ₹5,000 Best Performance Award for every team member.','3rd Place','cheer',-2)
 +fig('chd2',42,51,52,23,'Third rank holders','The team with their trophy','Trophy, certificate and cheque in hand after the hackathon.','Trophy','hop',3)
 +chip(6,58,30,'3rd','place · ₹50,000',-3,size=5.4)
 +tx(6,70,32,'Our students from CSE secured 3rd place in the Chandigarh Police Hackathon, conducted by the Chandigarh Police.',size=2.1))
P.append(page(7,'stu','Students','A podium finish at the Chandigarh Police Hackathon.',p7))
# 8
p8=(H1('Mule Scanner<br>AI',11,5.2)+KICK('IntelliTrace Hackathon 2026 · Indian Bank at VIT Chennai',25)
 +fig('mule1',6,29,58,27,'Presenting at IntelliTrace 2026','Mule Scanner AI on stage','Presented at VIT Chennai as part of the PSBs Hackathon Series 2026, an initiative of the Ministry of Finance, the Department of Financial Services and the Indian Banks’ Association.','Finalist pitch','think',-2)
 +fig('mule2',40,52,54,25,'Receiving the award','1st place at IntelliTrace','Participated on 7 April 2026 and was announced the winner on 8 July 2026, taking home a cash prize of ₹2.5 lakhs.','1st · ₹2.5 lakhs','cheer',3)
 +chip(6,60,28,'1st','place · ₹2.5 lakhs',-3,size=5.4)
 +tx(6,71,32,'Problem statement: Cross-Channel “Mule Account” Detection Graph. Participated 7 April 2026; announced winner 8 July 2026.',size=2))
P.append(page(8,'stu','Students','Mule Scanner AI took first place.',p8))
# 9
p9=(H1('Vigil-X',11,9)+KICK('Acentra Health BUILD TO CARE 2026 · SRM Kattankulathur',22.5)
 +fig('vig2',6,28,60,25,'Winners at BUILD TO CARE 2026','Vigil-X wins 1st place','Winner of the BUILD TO CARE 2026 hackathon finals, announced on 9 October 2026.','1st Place','cheer',-2)
 +fig('vig1',48,47,46,26,'The winning moment','The crowd goes wild','Our students competed in the finals on 8–9 October at SRM Kattankulathur.','Finals · 8–9 Oct','hop',3)
 +fig('vig3',6,56,38,19,'Finalist kit &amp; certificate','Finalists with certificates','Certificates and finalist badges from the Acentra Health Hackathon.','Finalist','think',-3)
 +chip(6,77,30,'1st','place',-3,size=4.4)
 +tx(48,77,26,'Finals on 8–9 Oct; winner announced 9 Oct 2026.',size=1.9))
P.append(page(9,'stu','Students','Vigil-X won the BUILD TO CARE finals.',p9))
# 10
p10=(H1('More hackathon<br>wins',11,5.2)
 +fig('psb',6,27,36,38,'PSBs Hackathon Series 2026 · Grand Finale','Grand Finale, PSBs 2026','The awards ceremony of the IntelliTrace hackathon at VIT Chennai.','Grand Finale','cheer',-2)
 +fig('nexora',46,28,48,25,'NEXORA · 24-hour hackathon','NEXORA 24-hour hackathon','HackHere’s overnight hackathon, 22–23 August 2026 at SNS iNnovation Hub, Coimbatore.','24 hours','point',3)
 +tx(46,57,48,'<b>NEXORA</b>, a 24-hour hackathon by HackHere, 22–23 August 2026, SNS iNnovation Hub, Coimbatore.',size=2.2)
 +tx(46,67,48,'<span style="font-size:3cqw;font-weight:800;line-height:1.15;color:var(--acc)">Students from our department won hackathons conducted by various institutions.</span>'))
P.append(page(10,'stu','Students','More wins and trophies from our students.',p10))
# 11 KBAIC
p11=(H1('KBAIC',11,8.5)+KICK('Kerala Blockchain Academy Club REC · with the CSE department',22.5)
 +fig('kba3',6,28,56,26,'KBAIC Inauguration Ceremony','The club is inaugurated','KBAIC was inaugurated on 19 September 2025 with the CSE department.','19 Sep 2025','cheer',-2)
 +fig('kba4',66,27,28,29,'Inauguration poster','Unlocking the future of blockchain','The inauguration poster for the REC–Kerala Blockchain Innovation club.','Club launch','wave',3)
 +fig('kba2',6,60,44,17,'Club members and guests','Our blockchain community','Students and mentors at REC Tech Lounge.','Community','hop',-2)
 +fig('kba1',54,60,40,17,'Faculty Empowerment Conclave','Faculty Empowerment Conclave','Kerala Blockchain Academy, IIITMK, Technopark, 20 Sep 2025.','20 Sep 2025','think',2,fit='contain',cls='noframe dark')
 +'')
P.append(page(11,'stu','Students · Clubs','Club life: the Kerala Blockchain Academy Club at REC.',p11))
# 12 DEVS
p12=(H1('DEVS Club REC',11,5.2)+KICK('Code. Coffee. Repeat…',17.8)
 +fig('devs1',6,25,40,36,'Hacktivate','Hacktivate: hackathons unplugged','SIH winners share real experiences, real wins, real learning. 20 Jan on Google Meet.','20 Jan','cheer',-2)
 +fig('devs2',54,28,40,36,'Project to Production','Project to Production','Git and GitHub, deploying web, mobile and AI/ML projects. 26 Jan on Google Meet.','26 Jan','point',3)
 +tx(6,67,40,'<b>Hacktivate — Hackathons Unplugged.</b> SIH winners share real experiences, real wins and real learning.',size=2.1)
 +tx(54,70,40,'<b>Project to Production</b> (Titanium 2026): Git and GitHub, and deploying mobile, web and AI/ML projects.',size=2.1))
P.append(page(12,'stu','Students · Clubs','Highlights from DEVS club sessions.',p12))
# 13 Intellexa + GDG
p13=(H1('Intellexa REC',11,4.8)
 +fig('intellexa',6,22,34,38,None,'Intellexa REC newsletter','Photography, prompts and ML','Three events from August 2025: a photography challenge, PROMPTSMITHS and Inside the Black Box.','Aug 2025','think',-2,fit='contain',cls='noframe dark')
 +tx(44,22,50,'<b>Photography Challenge</b>, 19 Aug 2025, for 2nd-year students. <b>PROMPTSMITHS</b>, 18 Aug 2025: language models and in-lab AI creation without GPU or cloud. <b>Inside the Black Box</b>, 23 Aug 2025: how machines actually learn.',size=2.05)
 +H1('Google Developer’s Club',52.5,3.4,44,50,'h2')
 +tx(6,66,34,'<b>Road to SIH</b> session, 21 Aug 2026.',size=2.1)
 +fig('gdg3',44,59,15,19,None,'Road to SIH','Road to SIH','A GDG session preparing students for Smart India Hackathon.','21 Aug 2026','point',-3)
 +fig('gdg2',61,59,16,19,None,'A packed hall','Full house','Students filled the hall for the Google Developer’s Club session.','GDG','hop',2)
 +fig('gdg1',79,57,15,21,None,'Club members','The GDG team','Club members at the event.','GDG','wave',-2))
P.append(page(13,'stu','Students · Clubs','Intellexa and the Google Developer’s Club.',p13))
# 14 Faculty
p14=(H1('Faculty<br>Achievements',11,5.4)
 +fig('cert',6,27,43,23,'Faculty of the Year 2025',fit='contain',cls='noframe')
 +fig('karthik',55,27,22,29,'Dr. V. Karthik','Dr. V. Karthik','Dr. V. Karthik was named Faculty of the Year 2025, recognised for his contributions to teaching, evaluation, research and publication.','Faculty of the Year 2025','cheer',0,fit='cover',cls='noframe')
 +fig('fdp1',6,59,46,22,'Agentic AI faculty programme','Faculty learn Agentic AI','Empowering faculty to build the next generation of autonomous AI systems, by the TCS CoE in AI.','TCS CoE in AI','point',2)
 +tx(56,59,36,'<b>Agentic AI:</b> empowering faculty to build the next generation of autonomous AI systems, organised by the TCS Centre of Excellence in AI.',size=2))
P.append(page(14,'fac','Faculty','Our faculty set the pace.',p14))
# 15
p15=(H1('Faculty<br>Empowerment',11,5.4)+KICK('Programmes by the Department of CSE',24.5)
 +fig('fdp3',6,29,30,34,'GenAI &amp; Applied AI','GenAI and Applied AI, with HCL GUVI','Faculty programme on Generative AI and Applied AI, 22–24 June 2026.','22–24 Jun 2026','cheer',-3,pos='50% 20%')
 +fig('fdp2',40,28,54,24,'Faculty participants','The faculty cohort','Faculty gathered at ANEW101 for three days of Generative AI and Applied AI, organised with HCL GUVI and the Institution’s Innovation Council.','HCL GUVI','hop',2)
 +fig('fdp4',40,56,54,22,'Java FDP · 24–28 Jun 2025','Mastering OOP with Java','A five-day faculty development programme, 24 to 28 June 2025, coordinated by Dr. V. Masilamani of IIITDM and sponsored by the Institution’s Innovation Council.','5-day FDP','think',-2)
 +tx(6,68,31,'Also: a Java FDP (24–28 Jun 2025) and a quality-improvement orientation (14 Jun 2025).',size=2))
P.append(page(15,'fac','Faculty','Faculty empowerment programmes and their highlights.',p15))
# 16
p17=(H1('Department<br>Achievements',11,5.2)
 +fig('bestdept',6,27,62,28,'Annual College Day 2026','Best Department Award 2025','The Department of CSE received the Best Department Award at Annual College Day.','Best Department','cheer',-2)
 +chip(72,29,22,'Best Dept.','Award 2025',3,size=3.4)
 +tx(6,60,62,'The Department of Computer Science and Engineering received the <b>Best Department Award – 2025</b>.',size=2.3)
 +tx(6,69,34,'<b>Industry interactions</b> on campus, 4 Feb 2026.',size=2.2)
 +fig('ind1',44,66,24,13.5,None,'Industry interaction','Industry meets campus','Industry interaction held at REC on 4 February 2026.','4 Feb 2026','point',-2)
 +fig('ind2',72,66,22,13.5,None,'Industry interaction','Talking shop','Faculty and industry leaders in discussion.','Industry','think',2))
P.append(page(16,'dep','Department','Our department and its achievements.',p17))
# 17
p18=(H1('World Record',11,6.4)+KICK('AI Botathon 1000 · AI Nexus 2026 · 18 July 2026',22.2)
 +fig('wr1',6,27,66,27,'AI Nexus 2026, an AI tech summit','A record-setting day','The department organised the world record setting AI Botathon 1000.','18 Jul 2026','cheer',-2)
 +fig('wr2',76,25,18,27,None,'AI Nexus poster','AI Nexus 2026','An AI tech summit with the Agentic AI Botathon at its heart.','AI Nexus','wave',3)
 +fig('wr3',76,56,18,22,None,'Botathon 1000','Agentic AI Botathon 1000','1000 bots, 1000 students, 120 minutes.','1000 bots','hop',-3)
 +tx(6,60,66,'The Department of Computer Science and Engineering organised the world record setting event <b>AI Botathon 1000</b> on 18 July 2026.',size=2.4))
P.append(page(17,'dep','Department','Let me tell you about the world record!',p18))
# 18
p19=(H1('We made<br>history.',11,6)
 +fig('wr4',6,27,42,35,'World Records Union certificate','Record certified','Highest number of fully functional Agentic AI bots developed simultaneously within two hours.','World Record','cheer',-2)
 +fig('wr5',52,27,42,36,None,'We coded. We tested. We built.','Every bot built independently','A verified, official World Records Union attempt.','Verified','hop',3)
 +chip(6,70,28,'1000','computing students',-2,'1000 students','Computing students took part in the record attempt.','1000','wave',4.6)
 +chip(36,68,28,'1000','functional agentic AI bots',2,'1000 bots','Every bot was built, tested and submitted independently.','1000 bots','cheer',4.6)
 +chip(66,70,28,'120','minutes',-3,'120 minutes','All bots were developed within a continuous 120 minutes.','120 min','hop',4.6))
P.append(page(18,'dep','Department','1000 students, 1000 bots, 120 minutes.',p19))
# 19
p20=(H1('Conferences',11,6)+KICK('2nd IEEE International Conference on Computing and Data Science (ICCDS 2025)',19.2,w=88)
 +fig('iccds',6,27,44,27,'ICCDS 2025 · 24 July 2025','ICCDS 2025','The 2nd IEEE International Conference on Computing and Data Science, 24 July 2025.','IEEE · 24 Jul 2025','cheer',-2)
 +fig('iccds2',54,27,40,14,'Opening session','Conference in session','Delegates and chief guests at ICCDS 2025.','ICCDS','point',2)
 +fig('iccds3',54,45,19,9,None,'Audience','The audience','A full audience at the conference.','ICCDS','wave',-2)
 +fig('iccds4',75,45,19,9,None,'Chief guest','Chief guest','A guest is felicitated.','ICCDS','think',2)
 +tx(6,59,88,'IEEE pre-conference workshop on 23 July 2025, followed by ICCDS 2025 on 24 July.',size=2.1)
 +fig('gl1',6,67,38,15,'International Guest Lecture','International guest lecture','20 Jan 2026, with the Centre of Excellence in Blockchain Technology.','20 Jan 2026','hop',-2)
 +tx(50,66,44,'<b>International Guest Lecture</b>, 20 Jan 2026: AI-enabled blockchain innovations and research writing, with Dr. Shyamala Devi Munisamy; by CSE and the CoE in Blockchain Technology.',size=2))
P.append(page(19,'dep','Department','Conferences and a guest lecture from abroad.',p20))
# 20
p21=(H1('Workshops',11,6.6)+KICK('Hands-on sessions with industry experts',20.5)
 +fig('ws1',6,25,30,30,'Cyber Security','GenAI &amp; Agentic AI for cyber security','A value-added course, 18–25 Aug 2026, by CSE and CSE (Cyber Security).','18–25 Aug 2026','think',-2,fit='contain',cls='noframe dark')
 +fig('ws2',38,25,28,30,'UiPath','Autonomous enterprise agents','Agentic AI with UiPath, with the TCS AI CoE, 11–17 Aug 2026.','11–17 Aug 2026','cheer',2,fit='contain',cls='noframe dark')
 +fig('ws3',6,59,30,23,'AI at the Edge','Deploying AI at the Edge','A hands-on edge AI workshop, from development to deployment, on 27 July 2026, with Ramesh N, AI developer at Altsense.','27 Jul 2026','hop',2,fit='contain',cls='noframe dark')
 +fig('ws4',38,59,28,23,'AWS Cloud Launchpad','AWS Cloud Launchpad','Zero to deployment on AWS on 10 August 2026, led by Jayanesh D and Vijay Kumar V, programmer analysts at Cognizant.','10 Aug 2026','point',-2,fit='contain',cls='noframe dark')
 +tx(69,25,26,'<b>Cyber Security</b><br>GenAI and Agentic AI, 18–25 Aug 2026<br><br><b>UiPath</b><br>Enterprise agents, 11–17 Aug 2026<br><br><b>Edge AI</b><br>Ramesh N, Altsense, 27 Jul 2026<br><br><b>AWS Cloud</b><br>Cognizant speakers, 10 Aug 2026',size=1.95))
P.append(page(20,'dep','Department','Four workshops and the skills our students explored.',p21))
# 21
p22=(H1('Industrial<br>Visits',11,5.6)
 +fig('iv1',6,26,52,27,'IIITDM Kanchipuram · 15 Sep 2026','III-year at IIITDM Kanchipuram','Third-year students toured IIITDM on 15 September 2026.','15 Sep 2026','cheer',-2)
 +fig('iv2',62,27,32,17,None,'Lab visit','Hands-on in the lab','Students look at hardware in the lab.','IIITDM','think',3)
 +fig('iv3',62,47,32,14,None,'Group photo','Group photo','The batch with their faculty.','IIITDM','wave',-2)
 +tx(6,58,52,'<b>III-year students</b> visited IIITDM Kanchipuram on 15 September 2026.',size=2.1)
 +tx(6,64,88,'<b>II-year students</b> visited IITM Research Park on 8 October 2026.',size=2.1)
 +fig('iv4',6,68,28,12,None,'IITM Research Park','IITM Research Park','Second-year students at IITM Research Park, 8 October 2026.','8 Oct 2026','hop',-2)
 +fig('iv5',36,68,28,12,None,'Talk','An industry talk','Students listen to a talk in the auditorium.','IITM RP','point',2)
 +fig('iv6',64,68,26,12,None,'Batch','The II-year batch','The whole batch together.','IITM RP','wave',-2))
P.append(page(21,'dep','Department','Industrial visits that brought learning beyond the classroom.',p22))
# 22
p23=(H1('Global<br>Immersion',11,5.6)+KICK('Cintana Global Signature Course 2026 · foreign university interaction',24)
 +fig('fu1',6,29,28,25,'Sunway University, Malaysia','Robots and memory with Sunway','Online sessions with Sunway University Malaysia on 11 Sep and 7 Oct 2026.','Malaysia','hop',-2,fit='contain',cls='noframe dark')
 +fig('fu2',36,29,28,25,'Arizona State University','Co-lecturing with ASU','Two days of co-lecturing with ASU faculty, 8–9 October 2026.','8–9 Oct 2026','cheer',2,fit='contain',cls='noframe dark')
 +fig('fu3',66,29,28,25,'UAG, Mexico','Data with UAG Mexico','Database design and data analysis sessions on 1 and 5 October 2026.','Mexico','wave',-2,fit='contain',cls='noframe dark')
 +H1('Immersion Programme: Code. Create. Connect.',58,3.2,6,88,'h2')
 +fig('im2',6,63,20,20,None,'Immersion','Code. Create. Connect.','A diploma immersion programme at REC, from the Centre of Excellence in Blockchain Technology.','Immersion','point',-2,fit='contain',cls='noframe dark')
 +fig('im3',30,64,32,14,None,'Hands-on','Hands-on learning','Visiting students learn decentralised systems hands-on.','Hands-on','think',2)
 +fig('im1',66,63,16,16,None,'Welcome','Welcome to REC','Visiting students with their hosts.','REC','hop',-2))
P.append(page(22,'dep','Department','Global classrooms and international collaborations.',p23))
# 23 team
FCS=[('fc1','Mr. Karthikeyan N','Assistant Professor'),('fc2','Mr. Balachandar J','Assistant Professor (SS)'),('fc3','Ms. Poornima A','Assistant Professor'),('fc4','Ms. Jayapradha','Assistant Professor (SS)')]
poses=['wave','hop','cheer','think']
slots=''
for i,(k,n,r) in enumerate(FCS):
    col=i%2;row=i//2;x=6+col*47;y=25+row*18.5
    slots+=f'<div class="tcard" style="left:{x}%;top:{y}%;width:41%;height:15.5%"></div>'
    slots+=fig(k,x+1.6,y+1.1,14.5,13.3,None,t=n,d=f'{r}, Department of Computer Science and Engineering, and one of our faculty coordinators.',c='Faculty Coordinator',pose=poses[i],rot=0,pos='50% 18%')
    slots+=tx(x+18,y+3.4,21.5,f'<b style="font-size:2.3cqw;color:#fff;line-height:1.2;display:block">{n}</b><span style="color:var(--gold);font-weight:700;font-size:1.9cqw;display:block;margin:.5cqw 0">{r}</span><span style="font-size:1.8cqw;opacity:.85">Department of CSE</span>','p')
SCS=[('sc1','Rohith Kumar S'),('sc2','Sarveshvaran D'),('sc3','Gowtham S')]
slots+='<div class="kick" style="left:6%;top:60.4%;width:88%">Student coordinators</div>'
for i,(k,n) in enumerate(SCS):
    x=6+i*30;y=64
    slots+=f'<div class="tcard" style="left:{x}%;top:{y}%;width:28%;height:12.6%"></div>'
    slots+=fig(k,x+1.3,y+1.4,10.5,9.4,None,t=n,d='Student coordinator for TEXPLORE 2026.',c='Student Coordinator',pose=['hop','wave','cheer'][i],rot=0,pos='50% 25%')
    slots+=tx(x+12.6,y+3.2,15,f'<b style="font-size:1.9cqw;color:#fff;line-height:1.2;display:block">{n}</b><span style="color:var(--gold);font-weight:700;font-size:1.75cqw;display:block;margin-top:.5cqw">Student Coordinator</span>','p')
p24=(H1('Meet the<br>Team',11,6.2)+KICK('Faculty coordinators',22)+slots)
P.append(page(23,'front','Team','Meet our faculty coordinators and student coordinators.',p24))
# 24
p25=('<div class="h1" style="left:6%;top:15%;font-size:10.5cqw;color:#fff;filter:drop-shadow(0 .9cqw 0 #5b1a8f)">Thank<br>you</div>'
 +'<div class="h1" style="left:6%;top:31%;font-size:7.4cqw;background:linear-gradient(180deg,#fff,#ffcf4d 60%,#ff9d00);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 .6cqw 0 #5b1a8f)">TEXPLORE<br>2026</div>'
 +'<div class="h2" style="left:6%;top:48%;font-size:4.2cqw;line-height:1.1">Dream big.<br><span style="color:#b9a3ff">Code bold.</span><br><span style="color:#ff6a7d">Innovate.</span></div>'
 +'<div class="edn" style="left:6%;top:43.6%;transform:none">Edition <i>·</i> VOL 13 ISSUE 8</div>'
 +'<div class="p" style="left:6%;top:64%;width:60%;font-size:2.4cqw">Department of Computer Science and Engineering<br><b>Rajalakshmi Engineering College</b><br>TEXPLORE 2026</div>'
 +'<div class="chipbig hs" data-go="0" style="left:6%;top:76%;font-size:2.4cqw;cursor:pointer;--r:-2deg" data-t="Back to the cover" data-d="Tap here to start the magazine again." data-c="Page 1" data-pose="wave">Back to cover<small>Click to flip to the start</small></div>')
P.append(page(24,'front','','Thank you for reading TEXPLORE 2026!',p25,hard=True))

import re as _re
def lead(n,y,text,x=6,w=88,size=2.0,intro=True):
    global P
    P[n-1]=P[n-1].replace('<div class="folio">',tx(x,y,w,text,'p',size)+'<div class="folio">',1)
    if intro:
        P[n-1]=_re.sub(r'(data-intro=")([^"]*)(")',lambda m:m.group(1)+m.group(2)+'||'+e(_re.sub('<[^>]+>','',text))+m.group(3),P[n-1],1)
def block(n,html_):
    P[n-1]=P[n-1].replace('<div class="folio">',html_+'<div class="folio">',1)
def pill(x,y,w,label,sheet):
    return f'<div class="shpill" data-sheet="{sheet}" style="left:{x}%;top:{y}%;width:{w}%">{label}</div>'
lead(4,19.2,'From design-thinking contests to national hackathons, our students competed across the country this year. Here is what they brought home.')
lead(5,19.2,'<b>Fests, hackathons &amp; firsts.</b> Our students do not just compete, they build: websites, tech fests and 36-hour hackathons run for the whole campus.')
lead(6,20.8,'Also: <b>Top 10</b> at the AICCI National Startup Summit 2026 and <b>13th</b> at CIH Hackathon’26 (Sam Devaraja J, Saiprashanth V, Vishal S, Thivyaa P).',size=2.0)
lead(7,19.6,'<b>Team:</b> Raghavan S, Mymoon Beevi, Prajeet V and Prajith S from CSE. <b>Prize:</b> ₹50,000 cash award plus a ₹5,000 Best Performance Award for every member. Hosted by Chandigarh Police with UIET, Panjab University.')
lead(10,20.2,'<b>Project Excellence Award</b> in two categories at Robovanta’26 (Pixor Robotics, Dindigul) for Sam Devaraja J, and <b>2nd place</b> at a 6-hour hackathon at SA College of Engineering for Monisha S.',size=1.95)
block(10,tx(6,69.5,37,'<b>Designathon 2026: Crack the Complexity.</b> 3rd place for Team Intelliroute (Keerthanaa S, Kiran Raj G, Padma Sree M) at SRM Institute of Science and Technology, 4–5 Aug 2026.',size=1.85)
 +tx(46,77.2,27,'<b>24-hour hackathon at REC:</b> 1st place for Rohith Kumar S, Roshan A and Arunraj M.',size=1.85)
 +pill(6,80.2,37,'Full student achievement record ›','stu'))
P[9]=_re.sub(r'(data-intro=")([^"]*)(")',lambda m:m.group(1)+m.group(2)+'||'+e('Two more podiums on this page. Designathon 2026 at SRM, third place for Team Intelliroute. And a first place at our own twenty four hour hackathon here at R E C. The full record of every achievement is one tap away.')+m.group(3),P[9],1)
block(5,tx(6,79.2,66,'<b>Also this year:</b> Rithika R, Rakshitha S and Roshan M took on Invente Hackinfinity’26, a 24-hour hackathon at SSN College of Engineering.',size=1.9))
block(11,tx(6,80,66,'Formation of Kerala Blockchain Academy (KBA) at REC and the BIC onboarding session, 19 Nov 2025.',size=1.85)+'')
block(12,tx(6,78.6,66,'<b>Club team:</b> Gokulakrishnan K (President), Dhanvin PR and Mithesh Tharun S (Vice Presidents), Meenakshi G (Secretary), Hursun SS (Mentor).',size=1.85))
lead(14,21.3,'Dr. V. Karthik was recognised at College Day 2026 for commendable overall performance in teaching, evaluation, research, publication and other professional pursuits (2025–26).',intro=False)
lead(16,20.3,'Highlights of the year: the <b>Best Department Award 2025</b>, a <b>World Records Union</b> world record, and <b>133+ blockchain certificates</b> completed in Season 1 of the Upskill series by the CoE in Blockchain Technology.',size=1.95)
block(17,tx(6,68.6,66,'<b>How it worked.</b> Every bot was built independently. Over a continuous 120 minutes, 1000 computing students designed, developed, tested and submitted fully functional Agentic AI bots in a transparent, verified process. The World Records Union certified the record, set at Rajalakshmi Engineering College, Chennai, on 18 July 2026.',size=2.0))
block(20,tx(69,58,26,'<b>Decode Blockchain</b><br>Unlock the Future of Decentralization, a BIC workshop.<br><br><b>Upskill Season 1</b><br>133+ blockchain certificates completed.',size=1.85)+pill(69,76,25,'Blockchain at REC ›','bc'))
block(13,tx(44,39.5,50,'Intellexa REC is also the team behind <b>Resonance’25</b>, the department’s flagship tech fest.',size=2.05)+tx(6,73,34,'The Google Developer’s Club ran <b>Road to SIH</b> to help students gear up for the Smart India Hackathon.',size=1.95))
block(14,tx(6,52.5,43,'The certificate of appreciation is signed by Principal Dr. S. N. Murugesan and Chairperson Dr. (Mrs.) Thangam Meganathan.',size=1.45))
block(15,tx(6,77.5,31,'The Java FDP, sponsored by IIC, built a culture of continuous improvement.',size=1.9))
lead(21,19.8,'Visits to IIITDM Kanchipuram and IITM Research Park gave our students first-hand exposure to labs, research and industry.')
# TOC extras
block(3,'<div class="toc2"><b>Extras</b><br><a data-sheet="stu">Full student achievement record</a><a data-sheet="bc">Blockchain at REC: KBA, BIC, CoE, CBA and Upskill</a></div>')

assert len(P)==24

# ---- NEW PAGES ----
about=(H1('About the<br>Department',11.5,5.6)
 +tx(6,20.6,88,'The <b>Department of Computer Science and Engineering</b> at Rajalakshmi Engineering College prepares students to turn ideas into working technology. Learning here goes well beyond the classroom: students build software, take part in hackathons, join clubs and work with industry and universities across the world, guided by a faculty that keeps learning too.','p',2.1)
 +fig('bestdept',6,32,56,24,'Best Department Award 2025','Best Department Award 2025','The Department of CSE received the Best Department Award at Annual College Day.','Best Department','cheer',-2)
 +chip(68,32,26,'1000','AI bots in 120 min',3,'World record','The department organised the world record setting AI Botathon 1000 on 18 July 2026.','Record','cheer',3.2)
 +chip(68,44,26,'133+','blockchain certificates',-3,size=3.2)
 +tx(6,62,41,'<b>Learning that builds.</b> Industry-led workshops, value-added courses and hands-on projects in AI, cyber security, cloud, blockchain and full-stack development sit alongside the curriculum.','p',2.0)
 +tx(53,62,41,'<b>Research and recognition.</b> From IEEE conferences and guest lectures to the Centre of Excellence in Blockchain Technology and the TCS CoE in AI programmes, the department keeps raising its own bar.','p',2.0)
 +tx(6,74.4,41,'<b>A community of clubs.</b> Intellexa, DEVS, KBAIC and the Google Developer’s Club run fests, sessions and hackathons for the whole campus.','p',2.0)
 +tx(53,74.4,22,'<b>Global classrooms.</b> Sessions with Sunway, ASU and UAG Mexico.','p',2.0)
 +'<div class="h2" style="left:6%;top:86%;font-size:3.4cqw;line-height:1.1;color:#fff">Dream big. <span style="color:#b9a3ff">Code bold.</span> <span style="color:#ff6a7d">Innovate.</span></div>')
ABOUT=page(0,'front','About','Let me introduce the Department of Computer Science and Engineering at Rajalakshmi Engineering College, the team behind this magazine.',about)

ED_N=[('fc1','Mr. Karthikeyan N','Assistant Professor'),('fc2','Mr. Balachandar J','Assistant Professor (SS)'),('fc3','Ms. Poornima A','Assistant Professor'),('fc4','Ms. Jayapradha','Assistant Professor (SS)')]
es=''
for i,(k,n,r) in enumerate(ED_N):
    col=i%2;row=i//2;x=6+col*47;y=25+row*16.5
    es+=f'<div class="tcard" style="left:{x}%;top:{y}%;width:41%;height:14%"></div>'
    es+=fig(k,x+1.6,y+1.0,14.5,12,None,t=n,d=f'{r}, Department of Computer Science and Engineering, and one of the faculty editors of TEXPLORE 2026.',c='Faculty Editor',pose=poses[i],rot=0,pos='50% 18%')
    es+=tx(x+18,y+3.0,21.5,f'<b style="font-size:2.3cqw;color:#fff;line-height:1.2;display:block">{n}</b><span style="color:var(--gold);font-weight:700;font-size:1.9cqw;display:block;margin:.5cqw 0">{r}</span><span style="font-size:1.8cqw;opacity:.85">Faculty Editor</span>','p')
editor_message=(
 '<b>Dear Readers,</b><br><br>'
 'It gives me immense pleasure to present the March–October 2026 edition of <b>TEXPLORE</b>, the magazine of the <b>Department of Computer Science, Rajalakshmi Engineering College</b>.<br><br>'
 'TEXPLORE serves as a platform to showcase the achievements, innovative ideas, technical knowledge, and creative talents of our students and faculty members. This edition highlights the department’s activities and accomplishments over the past few months, including industrial visits, Faculty Development Programmes (FDPs), workshops, guest lectures, and other academic and extracurricular initiatives.<br><br>'
 'I extend my sincere gratitude to our Head of the Department, <b>Dr. J. Manoranjini</b>, for her constant encouragement, guidance, and unwavering support, which have been instrumental in bringing this edition to life. I also thank all the faculty members and students who have contributed their valuable efforts and creativity to make this magazine a success.<br><br>'
 'I hope you enjoy reading TEXPLORE and find it both informative and inspiring. Your valuable feedback and suggestions are always welcome as we strive to make future editions even more engaging and enriching.<br><br>'
 '<b>Happy Reading!</b>')
edit=(H1('From the<br>Editors’ Desk',11.5,5.6)+KICK('Faculty editors · TEXPLORE 2026',22)+es
 +tx(8,56.5,84,editor_message,'p',1.45,'line-height:1.25;'))
EDITOR=page(0,'front','Editors','A message to our readers from the faculty editors of TEXPLORE 2026.',edit)
P[1:2]=[ABOUT,P[1],EDITOR]
assert len(P)==26
import re as _r2
for i,pg in enumerate(P,1):
    pg=_r2.sub(r'data-n="\d+"',f'data-n="{i}"',pg,1)
    pg=_r2.sub(r'(<div class="folio">TEXPLORE 2026<b>)\d+(</b>)',lambda m:m.group(1)+f'{i:02d}'+m.group(2),pg,1)
    P[i-1]=pg

def acard(imgs,title,tag,who,org,note=''):
    im=''.join(f'<img data-a="{k}" alt="">' for k in imgs)
    ph=f'<div class="shph n{len(imgs)}">{im}</div>' if imgs else ''
    return f'<article class="ac">{ph}<div class="shtx"><i>{tag}</i><h4>{title}</h4><p class="who">{who}</p><p>{org}</p>'+(f'<p class="nt">{note}</p>' if note else '')+'</div></article>'
F4='Sam Devaraja J, Saiprashanth V, Vishal S, Thivyaa P'
STU=('<h2>Student Achievement Record</h2><p class="shlead">Every entry from the department’s achievement record, sorted by result. Proof certificates and photos are shown where available.</p>'
 '<h3><s style="background:#ffc21a"></s>Podium finishes</h3><div class="grid">'
 +acard(['ac14','ac15'],'Chandigarh Police Hackathon','3rd Place','Raghavan S, Mymoon Beevi, Prajeet V, Prajith S','Chandigarh Police / UIET, Panjab University','₹50,000 cash prize and a ₹5,000 Best Performance Award per team member.')
 +acard(['ac1','ac20'],'Designathon 2026: Crack the Complexity','3rd Place','Team Intelliroute: Keerthanaa S, Kiran Raj G, Padma Sree M','SRM Institute of Science and Technology, Kattankulathur','National-level 24-hour hackathon, 4–5 August 2026.')
 +acard(['ac3'],'24-hour Hackathon','1st Place','Rohith Kumar S, Roshan A, Arunraj M','Rajalakshmi Engineering College')
 +acard([],'6-hour Hackathon','2nd Place','Monisha S','SA College of Engineering')
 +acard(['ac11','ac10'],'Robovanta’26 · Project Excellence Award','2 Categories','Sam Devaraja J','Pixor Robotics, Dindigul','National robotics and innovation fest. Certificate of participation in the hackathon also earned.')
 +'</div><h3><s style="background:#ff3dd2"></s>National rankings</h3><div class="grid">'
 +acard(['ac6'],'AICCI National Startup Summit 2026','Top 10',F4,'AICCI')
 +acard(['ac4','ac5'],'CIH Hackathon’26','13th Place',F4,'Rathinam Technical Campus','24-hour hackathon.')
 +'</div><h3><s style="background:#8a5cff"></s>Participation &amp; certificates</h3><div class="grid">'
 +acard(['ac7','ac8'],'INFOGRAM-26','Certificate of Excellence','Sam Devaraja J, Santhosh Priyan T N','C. Abdul Hakeem College of Engineering and Technology (CAHCET)','National level technical symposium by the Department of IT; hackathon participation.')
 +acard(['ac9'],'Workshop cum Hackathon','Participation','Sam Devaraja J, Santhosh Priyan T N','KCG College of Technology, Chennai','Organised with CADD Centre.')
 +acard(['ac2'],'Adobe Hackathon','Participation','Roshan VS','Adobe, on Unstop','9 August 2026.')
 +acard([],'Invente Hackinfinity’26','24-hour Hackathon','Rithika R, Rakshitha S, Roshan M','SSN College of Engineering')
 +acard(['ac16','ac17','ac18','ac19'],'Technical symposia','Participation','Manisha V and Monisha S','SA College of Engineering (Nakshatra’26), SIMATS Engineering College, Loyola-ICAM College of Engineering and Technology','Manisha V: hackathon and two technical events. Monisha S: technical event at SIMATS.')
 +'</div><h3><s style="background:#35e0ff"></s>Highlights from the magazine</h3><ul class="shul"><li><b>Mule Scanner AI</b>, 1st place, IntelliTrace Hackathon 2026 (Indian Bank, VIT Chennai), ₹2.5 lakhs</li><li><b>Vigil-X</b>, 1st place, Acentra Health BUILD TO CARE 2026 (SRM Kattankulathur)</li><li><b>IWDC InnovateHer</b>, 1st prize, Keerthana M G</li><li><b>Glitches</b>, 1st prize, 3rd Project Contest for Design Thinking and Innovation 2025</li><li><b>TN-IMPACT 2026</b>, special mention, top 20 of 750+ teams</li><li><b>TechDecks</b>, runner-up, HappyFox Hackathon (Campus Connect)</li></ul>')
BCS=('<h2>Blockchain at REC</h2><p class="shlead">Kerala Blockchain Academy, the Blockchain Innovation Club (BIC) and the Centre of Excellence in Blockchain Technology, in photos and milestones.</p>'
 '<h3><s style="background:#ffc21a"></s>Formation of Kerala Blockchain Academy (KBA)</h3><div class="grid">'
 +acard(['bc0'],'REC Tech Lounge','Formation','Students, faculty and guests','Rajalakshmi Engineering College')
 +acard(['bc1'],'KBAIC Inauguration Ceremony','Unlocking the Future of Blockchain','Organised by Kerala Blockchain Academy Club REC, with CSE','Community partner: Perplexity · Industrial partners: Olive IoT, Jerry, Yaazh')
 +'</div><h3><s style="background:#ff3dd2"></s>Inauguration of BIC (KBA)</h3><div class="grid">'
 +acard(['bc2'],'A full house','Inauguration','Students and mentors in the audience','Rajalakshmi Engineering College')
 +acard(['bc3'],'On the podium','Inauguration','Speaker at the inauguration','Rajalakshmi Engineering College')
 +'</div><h3><s style="background:#8a5cff"></s>Decode Blockchain: Unlock the Future of Decentralization</h3><div class="grid">'
 +acard(['bc4','bc7'],'Hands-on workshop','Workshop','Students learning blockchain on their own laptops','')
 +acard(['bc5','bc8','bc6'],'BIC workshop team','Workshop','Organisers, mentors and participants','')
 +'</div><h3><s style="background:#35e0ff"></s>Centre of Excellence for Blockchain Technology</h3><div class="grid">'
 +acard(['bc11','bc9','bc10'],'Centre of Excellence','CoE','Blockchain Technology','Rajalakshmi Engineering College')
 +'</div><h3><s style="background:#ffc21a"></s>Certified Blockchain Associate (CBA) Program</h3><div class="grid">'
 +acard(['bc12'],'CBA certificates','CBA','Kerala Blockchain Academy certificates earned by our students','BIC REC')
 +acard(['bc13'],'Upskill Program: Blockchain Foundation','Season 1 · 133+ certificates completed','Ethereum, Hyperledger Fabric and Bitcoin','Lifetime access, certification and assessments')
 +'</div><h3><s style="background:#ff3dd2"></s>Club Membership Overview</h3><div class="grid">'
 +acard(['bc14','bc15'],'BIC Onboarding Session','19 Nov 2025','New recruit onboarding on Google Meet','Blockchain Innovation Club REC, with the Centre of Excellence in Blockchain Technology')
 +'</div>')
SHEETHTML=('<div id="sheet" hidden><div class="shcard" role="dialog" aria-modal="true"><button class="shx" aria-label="Close">×</button><div id="shBody"></div></div></div>'
 '<template id="tpl-stu">'+STU+'</template><template id="tpl-bc">'+BCS+'</template>')

nav=lambda i,l:f'<button data-j="{i}">{l}</button>'
body=('<div id="stage"></div>'+SHEETHTML+
 '<div id="intro"><div class="smk"></div><div class="smk2"></div><div id="logoReveal"><div class="lr"><div class="lri"><img data-a="logo_full" alt="Rajalakshmi Engineering College"></div></div></div><canvas id="introCv"></canvas><button id="skip">Skip intro</button>'
 '<div id="introTxt"><div class="a">RAJALAKSHMI <span>ENGINEERING</span> COLLEGE</div><div class="b">Department of Computer Science and Engineering presents</div><div class="c">TEXPLORE 2026</div><button id="enter">Open the magazine</button></div></div>'
 '<div id="bookwrap"><div id="book">'+''.join(P)+'</div></div>'
 '<div id="bar"><button id="prev" aria-label="Previous page">‹ Prev</button><span class="pn" id="pn">1 / 26</span><button id="nxt" aria-label="Next page">Next ›</button><span class="sep hide-s"></span>'
 +nav(0,'Cover')+nav(1,'About')+nav(4,'Contents')+nav(5,'Students')+nav(15,'Faculty')+nav(17,'Department')+nav(24,'Team')
 +'<span class="sep hide-s"></span><button data-sheet="stu">Achievements</button><button data-sheet="bc">Blockchain</button><button id="gd">Mascot guide: on</button><button id="vx">Voice: on</button><button id="fs" class="hide-s">Fullscreen</button></div>'
 '<div id="hint">Drag a page corner or use ← → to flip · tap photos to meet the stories</div>')
FONTS=('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&family=Unbounded:wght@700;800;900&display=swap">' if MODE=='web' else '<link rel="stylesheet" href="fonts/fonts.css">')
LIB=('<script src="https://cdn.jsdelivr.net/npm/page-flip@2.0.7/dist/js/page-flip.browser.js"></script>' if MODE=='web' else '<script src="vendor/page-flip.browser.js"></script>')
css=open('style.css').read(); js=open('app.js').read()
out=('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>TEXPLORE 2026 · REC CSE Magazine</title>'
 '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'+FONTS+
 '<style>'+css+'</style></head><body>'+body+LIB+
 '<script>window.ADHI_AUDIO=false;window.ADHI_CONN='+json.dumps(CONN)+';window.ASSETS='+json.dumps(A)+';</script><script>'+js+'</script></body></html>')
import os
OUT=os.environ.get('OUT','../index.html')
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,'w').write(out)
print(len(out)/1e6,'MB')
