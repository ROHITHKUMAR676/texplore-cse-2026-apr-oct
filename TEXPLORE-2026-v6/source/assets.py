import base64, io, json, os
from PIL import Image, ImageDraw, ImageFilter
R='../assets/extracted-from-pdf/'
U='../assets/originals/'
def jpg(im,maxd,q=72):
    im=im.convert('RGB'); im.thumbnail((maxd,maxd),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'JPEG',quality=q,optimize=True,progressive=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
def webp(im,maxd,q=86):
    im=im.copy(); im.thumbnail((maxd,maxd),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=q,method=6)
    return 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
def png(im):
    b=io.BytesIO(); im.save(b,'PNG',optimize=True)
    return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
A={}
# photos: key -> (file, maxdim, crop)
P={
'iwdc':('p-003-008.jpg',800,None),
'glitches':('p-003-007.jpg',800,(0,0,564,300)),
'glitches2':('p-003-011.jpg',800,None),
'vignesh':('p-004-019.jpg',700,None),
'resonance':('p-004-023.jpg',800,None),
'powerbi':('p-004-030.jpg',700,None),
'techdecks':('p-004-033.jpg',800,None),
'xyntra':('p-004-040.jpg',700,None),
'tn':('p-005-045.jpg',800,None),
'press':('p-005-046.jpg',800,None),
'chd1':('p-006-050.jpg',900,None),
'chd2':('p-006-051.jpg',900,None),
'mule1':('p-007-057.jpg',900,None),
'mule2':('p-007-058.jpg',900,None),
'vig1':('p-008-062.jpg',900,None),
'vig2':('p-008-063.jpg',800,None),
'vig3':('p-008-064.jpg',700,None),
'psb':('p-009-068.jpg',700,None),
'nexora':('p-009-069.jpg',800,None),
'kba1':('p-013-087.jpg',800,None),
'kba2':('p-013-088.jpg',900,None),
'kba3':('p-013-089.jpg',800,None),
'kba4':('p-013-091.jpg',560,None),
'devs1':('p-014-095.jpg',700,None),
'devs2':('p-014-096.jpg',700,None),
'intellexa':('p-016-101.jpg',800,None),
'gdg1':('p-016-105.jpg',600,None),
'gdg2':('p-016-106.jpg',600,None),
'gdg3':('p-016-107.jpg',600,None),
'cert':('p-018-122.jpg',650,None),
'bestdept':('p-018-120.jpg',1000,None),
'fdp1':('p-026-172.jpg',900,None),
'fdp2':('p-027-176.jpg',800,None),
'fdp3':('p-027-177.jpg',650,None),
'fdp4':('p-028-183.jpg',700,None),
'fdp5':('p-028-182.jpg',700,None),
'ind1':('p-031-201.jpg',900,None),
'ind2':('p-031-202.jpg',900,None),
'wr1':('p-011-076.jpg',900,None),
'wr2':('p-011-077.jpg',560,None),
'wr3':('p-012-081.jpg',560,None),
'wr4':('p-012-082.jpg',700,None),
'wr5':('p-012-083.jpg',800,None),
'iccds':('p-017-111.jpg',800,None),
'iccds2':('p-017-116.jpg',800,None),
'iccds3':('p-017-113.jpg',600,None),
'iccds4':('p-017-114.jpg',600,None),
'gl1':('p-025-167.jpg',800,None),
'gl2':('p-025-166.jpg',700,None),
'ws1':('p-021-140.jpg',600,None),
'ws2':('p-022-146.jpg',600,None),
'ws3':('p-023-152.jpg',600,None),
'ws4':('p-024-160.jpg',600,None),
'iv1':('p-019-127.jpg',900,None),
'iv2':('p-019-126.jpg',700,None),
'iv3':('p-019-129.jpg',700,None),
'iv4':('p-020-134.jpg',700,None),
'iv5':('p-020-135.jpg',700,None),
'iv6':('p-020-136.jpg',700,None),
'fu1':('p-029-187.jpg',560,None),
'fu2':('p-029-188.jpg',560,None),
'fu3':('p-029-189.jpg',560,None),
'im1':('p-030-193.jpg',560,None),
'im2':('p-030-194.jpg',560,None),
'im3':('p-030-197.jpg',700,None),
}
for k,(f,d,c) in P.items():
    import glob
    num=f.split('-')[2].split('.')[0]
    f=os.path.basename(glob.glob(R+'p-*-'+num+'.*')[0])
    im=Image.open(R+f)
    if c: im=im.crop(c)
    if k=='cert': im=im.rotate(-90,expand=True)
    A[k]=jpg(im,d)
# backgrounds
for k,f in [('bg_purple','1791909783740_image.png'),('bg_white','1791909798848_image.png'),('bg_red','1791909815337_image.png')]:
    A[k]=jpg(Image.open(U+f),640,66)
# logo
lg=Image.open(U+'rec.png').convert('RGBA').crop((270,420,775,1125))
A['logo']=webp(lg,420,90)
lg.thumbnail((200,300)); lg.save('logo_s.png')
A['logo_s']=png(lg)
A['logo_full']=png(Image.open(U+'1791957904595_rec-logo-expanded-white.png').convert('RGBA'))
# mascot
m=Image.open(U+'adhi.png').convert('RGBA'); bb=(114,0,1140,1275); m=m.crop(bb)
W,H=m.size
box=(528,748,737,983)
patch=m.crop(box)
fl=m.transpose(Image.FLIP_LEFT_RIGHT)
mask=Image.new('L',patch.size,0); ImageDraw.Draw(mask).rounded_rectangle((8,8,patch.size[0]-8,patch.size[1]-8),radius=40,fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(7))
fl.paste(patch,(W-box[2],box[1]),mask)
fl.save('m_flip.png')
A['mascot']=webp(m,520,88)
A['mascot_l']=webp(fl,520,88)

# --- new in v3: AllPDF (blockchain) + achievements record proofs
import glob as _g
R2='../assets/extracted-from-AllPDF/'; DM='../assets/extracted-from-achievements-doc/'
BC={'bc0':'b-001-000.jpg','bc1':'b-001-001.png','bc2':'b-002-002.jpg','bc3':'b-002-003.png','bc4':'b-003-004.jpg','bc5':'b-004-005.jpg','bc6':'b-004-006.jpg','bc7':'b-005-007.jpg','bc8':'b-005-008.jpg','bc9':'b-006-009.jpg','bc10':'b-006-010.jpg','bc11':'b-006-011.png','bc12':'b-007-012.jpg','bc13':'b-008-013.jpg','bc14':'b-009-014.jpg','bc15':'b-009-015.jpg'}
for k,f in BC.items():
    A[k]=jpg(Image.open(R2+f),900 if k not in('bc12','bc13') else 1000,70)
for i in range(1,21):
    f=[x for x in os.listdir(DM) if x.startswith('image%d.'%i)][0]
    A['ac%d'%i]=jpg(Image.open(DM+f),800,72)
_h=Image.open(U+'HoD-photo-Dr-J-Manoranjini.png').convert('RGB'); _h=_h.resize((_h.width*4,_h.height*4),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,60,3))
A['hod']=jpg(_h,720,88)
FC={'fc1':'../assets/originals/faculty-coordinator-1-Karthikeyan-N.jpg','fc2':'../assets/originals/faculty-coordinator-2-Balachandar-J.png','fc3':'../assets/originals/faculty-coordinator-3-Poornima-A.jpg','fc4':'../assets/originals/faculty-coordinator-4-Jayapradha.png'}
for k,f in FC.items(): A[k]=jpg(Image.open(f),560,84)
SC={'sc1':'../assets/originals/student-coordinator-1-Rohith-Kumar-S.png','sc2':'../assets/originals/student-coordinator-2-Sarveshvaran-D.png','sc3':'../assets/originals/student-coordinator-3-Gowtham-S.png'}
for k,f in SC.items():
    _s=Image.open(f).convert('RGB'); _s=_s.resize((_s.width*5,_s.height*5),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,50,2)); A[k]=jpg(_s,420,86)
json.dump(A,open('assets.json','w'))
print(len(A), sum(len(v) for v in A.values())/1e6,'MB')
