import json,os,urllib.request as U
P="aaaakkkkccegbbcfaaaeb98abcc6aaaa024426aa4acd4bde4ade4bcd26ab0244"
H=[[int(c,21)*5-50 for c in P[i:i+32]]for i in(0,32)]
V=[0,100,320,330,500,900,0]
S=[s for s in range(128)if not s&136]
E=[[0]*128 for _ in[0]*13]
for s in S:
 r,f=s>>4,s&7;m=f if f<4 else 7-f
 for t in range(1,7):
  w=V[t]+(H[t-1][(7-r)*4+m]if t<3 else 0);E[t+6][s]=w;E[6-t][s]=-V[t]-(H[t-1][r*4+m]if t<3 else 0)
N=[31,33,14,18,-31,-33,-14,-18];D=[15,17,-15,-17];R=[1,-1,16,-16];K=D+R
C={0:13,7:14,4:12,112:7,119:11,116:3}
CAP=30000
B=[0]*128;un=[];T0=os.times()[4]
def at(s,by):
 for ds,t in(((-15*by,-17*by),1),(N,2),(K,6),(D,3),(R,4)):
  for d in ds:
   x=s+d
   while not x&136:
    p=B[x]
    if p:
     if p==t*by or t>2 and p==5*by:return 1
     break
    if t>4 or t<3:break
    x+=d
def g():
 for s in S:
  p=B[s]
  if p*tm<=0:continue
  t=abs(p)
  if t==1:
   d=16*tm;r=s>>4;o=s+d;tg=[]
   if not B[o]:tg.append(o)
   for dd in(d-1,d+1):
    x=s+dd
    if not x&136 and(B[x]and B[x]*tm<0 or x==ep):tg.append(x)
   for x in tg:
    if r==(6 if tm>0 else 1):
     for pr in(5,2,3,4):yield s|x<<7|pr<<14
    else:yield s|x<<7
   if o in tg and r==(1 if tm>0 else 6)and not B[o+d]:yield s|(o+d)<<7
  else:
   for d in(N,D,R,K,K)[t-2]:
    x=s
    while 1:
     x+=d
     if x&136:break
     q=B[x]
     if not q:yield s|x<<7
     else:
      if q*tm<0:yield s|x<<7
      break
     if t in(2,6):break
   if t==6 and s in(4,116):
    for rb,dr in((1,1),(2,-1))if s<9 else((4,1),(8,-1)):
     if cs&rb and all(not B[s+i*dr]for i in(1,2,3)if i<3 or dr<0)and all(not at(s+i*dr,-tm)for i in(0,1,2)):yield s|(s+2*dr)<<7
def rm(a,b):
 global sc;p=B[a];B[b]=p;B[a]=0;sc+=E[p+6][b]-E[p+6][a]
def mu(m=0):
 global tm,cs,ep,sc
 if m:
  f=m&127;t=(m>>7)&127;p=B[f];w=B[t];q=t
  if ep==t and p*p==1 and f%8!=t%8:q=t-16*tm;w=B[q]
  un.append((m,w,q,cs,ep));sc-=E[p+6][f];B[f]=0
  if w:sc-=E[w+6][q];B[q]=0
  if m>>14:p=(m>>14)*tm
  B[t]=p;sc+=E[p+6][t]
  if p*p==36 and abs(t-f)==2:rm(f+3,f+1)if t>f else rm(f-4,f-1)
  cs&=C.get(f,15)&C.get(t,15);ep=f+16*tm if p*p==1 and t-f in(32,-32)else-1;tm=-tm
 else:
  m,w,q,cs,ep=un.pop();tm=-tm;f=m&127;t=(m>>7)&127;p=B[t];sc-=E[p+6][t]
  if m>>14:p=tm
  sc+=E[p+6][f];B[f]=p;B[t]=0
  if w:B[q]=w;sc+=E[w+6][q]
  if p*p==36 and abs(t-f)==2:rm(f+1,f+3)if t>f else rm(f-1,f-4)
def o(m):
 c=B[(m>>7)&127];r=m>>14
 return(V[abs(c)]or 100)*32-V[abs(B[m&127])]+V[r]if c or r else 0
def sr(d,a,b,pl):
 global nd,bst;nd+=1
 if nd>cp:1/0
 ic=at(B.index(6*tm),-tm);v=-1e6
 if d<=0 and not ic:
  v=sc*tm+8
  if v>=b:return v
 vm=0
 for m in sorted(g(),key=o)[::-1]:
  t=(m>>7)&127
  if d<=0 and not ic and not(B[t]or m>>14 or ep==t):continue
  mu(m)
  if at(B.index(-6*tm),tm):mu();continue
  s=-sr(d-1,-b,-a,pl+1);mu()
  if s>v:v=s;vm=m
  if s>a:
   a=s
   if a>=b:break
 if not pl:bst=vm
 return v if v>-1e6 else-6e4 if ic else 0
def u(m):
 return"%c%d%c%d"%(97+(m&7),(m>>4&7)+1,97+((m>>7)&7),(m>>11&7)+1)+("nbrq"[(m>>14)-2]if m>>14 else"")
def f(fen):
 global tm,cs,ep,sc,un
 ps=fen.split();B[:]=[0]*128;un*=0;sc=0;i=112
 for c in ps[0]:
  if c=="/":i-=24
  elif c.isdigit():i+=int(c)
  else:
   p="pnbrqk".find(c.lower())+1;w=1-2*c.islower();B[i]=w*p;sc+=E[w*p+6][i];i+=1
 tm=1-2*(ps[1]=="b");cs=sum(1<<"KQkq".find(c)for c in ps[2]if c>"-");ep=-1 if ps[3]=="-"else int(ps[3][1])*16-16+ord(ps[3][0])-97
def fm(lg):
 global nd,cp,bst
 cd=[m for m in g()if(mu(m),not at(B.index(-6*tm),tm),mu())[1]]
 if len(cd)==1:return cd[0]
 el=os.times()[4]-T0;cp=CAP>>((el>600)+(el>1000)+(el>1400))if el<=1650 else 2000;nd=0;bst=cd[0]
 for dep in range(1,99):
  try:sr(dep,-1e6,1e6,0)
  except:break
  if nd>=cp:break
 return bst
def main():
 url=os.getenv("MAKEFUN_ENV_URL");post=lambda p,b:json.load(U.urlopen(url+p,data=json.dumps(b).encode()))
 while 1:
  g=post("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":f(g["fen"]);g=post("/move",{"game":g["game"],"move":u(fm(g["legal_moves"]))})
if __name__=="__main__":main()
