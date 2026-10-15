import re, html, sys, json
src=open(sys.argv[1],encoding='utf-8').read(); out=sys.argv[2]
conn=json.loads(re.search(r'ADHI_CONN=(\[.*?\]);',src).group(1))
pages=re.split(r'<div class="pg sec-',src)[1:]
lines=['ADHI VOICE SCRIPT — every line Adhi says, with the file name to use if you record/generate your own audio.',
'Save each as audio/<ID>.mp3, then set window.ADHI_AUDIO=true in index.html (see README). Missing files fall back to the browser voice.','']
for pg in pages:
    n=int(re.search(r'data-n="(\d+)"',pg).group(1))
    intro=html.unescape(re.search(r'data-intro="([^"]*)"',pg).group(1)).split('||')
    for i,t in enumerate(intro):
        pre='Hi there! ' if (n==1 and i==0) else ('Page %d. '%n if i==0 else '')
        lines.append(f'p{n}-intro{i}\t{pre}{t}')
    for k,m in enumerate(re.finditer(r'class="[^"]*\bhs\b[^"]*"[^>]*?data-t="([^"]*)" data-d="([^"]*)"',pg)):
        t,d=html.unescape(m.group(1)),html.unescape(m.group(2))
        lines.append(f'p{n}-h{k}\t{conn[k%len(conn)]}{t}. {d}')
lines.append('next-prompt\tFlip the page, and I’ll tell you about the next one!')
open(out,'w',encoding='utf-8').write('\n'.join(lines)+'\n'); print(len(lines))
