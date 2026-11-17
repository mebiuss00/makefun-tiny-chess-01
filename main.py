import json,os,time,urllib.request as U
V=[0,100,320,330,500,900,0]
CF=[0,1,3,3,0,1,-4]
EV=[[0]*128 for _ in range(13)]
for s in range(128):
 if s&0x88:continue
 r,f=s>>4,s&7
 ce=min(f,7-f)+min(r,7-r)
 for t in range(1,7):
  w=V[t]+ce*CF[t]+(6*r if t<2 else 24 if t>5 else 0)
  EV[t+6][s]=w
  EV[6-t][s]=-V[t]-ce*CF[t]-(6*(7-r) if t<2 else 24 if t>5 else 0)
ND=[31,33,14,18,-31,-33,-14,-18]
BD=[15,17,-15,-17]
RD=[1,-1,16,-16]
KD=BD+RD
CM={0:13,7:14,4:12,112:7,119:11,116:3}
CT=[(1,4,1),(2,4,-1),(4,116,1),(8,116,-1)]
MATE=60000;INF=10**6;CAP=14000
B=[0]*128;ks={};stk=[]
nd=0;cp=CAP
T0=time.monotonic()
def tk():
 global nd
 nd+=1
 if nd>cp:raise ValueError
def at(s,by):
 for ds,t in (((-15*by,-17*by),1),(ND,2),(KD,6)):
  for d in ds:
   x=s+d
   if not x&0x88 and B[x]==t*by:return 1
 for ds,ts in ((BD,(3,5)),(RD,(4,5))):
  for d in ds:
   x=s+d
   while not x&0x88:
    p=B[x]
    if p:
     if p*by in (ts[0],5):return 1
     break
    x+=d
def gen():
 for s in range(128):
  if s&0x88:continue
  p=B[s]
  if not p or (p>0)!=(tm>0):continue
  t=abs(p)
  if t==1:
   d=16*tm;r=s>>4
   p7=r==(6 if tm>0 else 1)
   o=s+d;tg=[]
   if not B[o]:tg.append(o)
   for dd in (d-1,d+1):
    x=s+dd
    if not x&0x88 and (B[x] and (B[x]>0)!=(tm>0) or x==ep):tg.append(x)
   for x in tg:
    if p7:
     for pr in (5,2,3,4):yield s|x<<7|pr<<14
    else:yield s|x<<7
   if tg and tg[0]==o and r==(1 if tm>0 else 6) and not B[o+d]:yield s|(o+d)<<7
  else:
   for d in (ND,BD,RD,KD,KD)[t-2]:
    x=s
    while 1:
     x+=d
     if x&0x88:break
     q=B[x]
     if not q:
      yield s|x<<7
     else:
      if (q>0)!=(tm>0):yield s|x<<7
      break
     if t in (2,6):break
   if t==6:
    for rb,kq,dr in CT:
     if s==kq and cs&rb and all(not B[kq+i*dr] for i in (1,2,3) if i<3 or dr<0) and all(not at(kq+i*dr,-tm) for i in (0,1,2)):yield kq|(kq+2*dr)<<7
def mk(m):
 global tm,cs,ep,sc
 stk.append((B[:],tm,cs,ep,sc,ks[1],ks[-1]))
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 p=B[f];cap=B[t];cq=t
 if not cap and ep==t and abs(p)==1 and (f&7)!=(t&7):
  cq=t-16*tm;cap=B[cq]
 sc-=EV[p+6][f];B[f]=0
 if cap:sc-=EV[cap+6][cq];B[cq]=0
 if pr:p=pr*tm
 B[t]=p;sc+=EV[p+6][t]
 if abs(p)==6:
  ks[tm]=t
  if abs(t-f)==2:
   rf,rt=(f+3,f+1) if t>f else (f-4,f-1)
   B[rt]=B[rf];B[rf]=0
   sc+=EV[4*tm+6][rt]-EV[4*tm+6][rf]
 cs &= CM.get(f,15)&CM.get(t,15)
 ep=f+16*tm if abs(p)==1 and abs(t-f)==32 else -1
 tm=-tm
def um():
 global tm,cs,ep,sc
 B[:],tm,cs,ep,sc,a,b=stk.pop()
 ks[1]=a;ks[-1]=b
def sr(d,a,b):
 if d<=0:return sc*tm+8
 tk()
 v=-INF
 for m in gen():
  mk(m)
  if at(ks[-tm],tm):
   um();continue
  s=-sr(d-1,-b,-a)
  um()
  if s>v:v=s
  if s>a:
   a=s
   if a>=b:break
 if v<=-INF:return -MATE if at(ks[tm],-tm) else 0
 return v
def uci(m):
 s=chr(97+(m&7))+str((m>>4&7)+1)+chr(97+((m>>7)&7))+str((m>>11&7)+1)
 if m>>14:s+="nbrq"[m>>14-2]
 return s
def sf(fen):
 global tm,cs,ep,sc
 ps=fen.split()
 B[:]=[0]*128;stk.clear()
 sc=0;i=112
 for c in ps[0]:
  if c=="/":i-=24
  elif c.isdigit():i+=int(c)
  else:
   p="pnbrqk".find(c.lower())+1
   sg=1-2*c.islower()
   B[i]=sg*p;sc+=EV[sg*p+6][i]
   if p==6:ks[sg]=i
   i+=1
 tm=1-2*(ps[1]=="b")
 cs=sum({"K":1,"Q":2,"k":4,"q":8}.get(c,0) for c in ps[2])
 ep=-1 if ps[3]=="-" else (int(ps[3][1])-1)*16+ord(ps[3][0])-97
def fm(lg):
 global nd,cp
 cd=[m for m in gen() if (mk(m),not at(ks[-tm],tm),um())[1]]
 if len(cd)==1:return cd[0]
 el=time.monotonic()-T0
 cp=(CAP>>((el>600)+(el>1000)+(el>1400))) if el<=1650 else 2000
 nd=0;best=cd[0]
 for dep in range(1,99):
  loc=0;cur=-INF;a=-INF
  try:
   for m in cd:
    mk(m);s=-sr(dep-1,-INF,-a);um()
    if s>cur:cur=s;loc=m
    if s>a:a=s
  except ValueError:break
  if loc:best=loc
  if nd>=cp:break
 return best
def main():
 url=os.environ["MAKEFUN_ENV_URL"]
 post=lambda p,b:json.load(U.urlopen(U.Request(url+p,data=json.dumps(b).encode())))
 while 1:
  g=post("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   sf(g["fen"])
   g=post("/move",{"game":g["game"],"move":uci(fm(g["legal_moves"]))})
if __name__=="__main__":main()
