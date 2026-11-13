#Cree le 16 Août 2024
from kandinsky import fill_rect as fr,draw_string as ds,get_pixel as gp
from random import randint as rd,choice as ch
from ion import keydown as kd
from time import sleep as sl,monotonic as mn

wh,gr,ifc=(255,)*3,(148,150,148),(255,182,57)
bw,bh,dr=320,222,[(1,0),(-1,0),(0,1),(0,-1)]
dc=[wh,(255,0,0),(0,0,255),(0,255,0)]
tl=lambda a:len(str(a))*5
ml,mr=30,500

def rc(x,y):
 cl=gp(x*m+sw,y*m+sh)
 if cl==gr:return 1
 for i in range(4):
  if cl==dc[i]:return i

def shuffle(lst):
 n=len(lst)
 for i in range(n):
  j=rd(i,n-1)
  lst[i],lst[j]=lst[j],lst[i]
def maze(t=3):
 global w,h,sw,sh,m
 w,h,sw,sh,m=bw//t,bh//t,bw%t,bh%t,t
 if w%2==0:sw,w=sw+m,w-1
 if h%2==0:sh,h=sh+m,h-1
 fr(0,0,bw,sh,ifc),fr(0,0,sw,bh,ifc)
 fr(sw,sh,bw-sw,bh-sh,gr)
 def dig(x, y):
  sk=[(x,y,0)]
  while sk:
   cx,cy,d=sk[-1]
   fr(cx*m+sw,cy*m+sh,m,m,dc[0])
   if d>mr:sk.pop();continue
   shuffle(dr)
   for dx,dy in dr:
    nx,ny=cx+2*dx,cy+2*dy
    if 0<=nx<w and 0<=ny<h and rc(nx,ny)==1:
     fr((cx+dx)*m+sw,(cy+dy)*m+sh,m,m,dc[0])
     #sl(0.0001)
     sk.append((nx,ny,d+1))
     break
   else:sk.pop()
 sx,sy=rd(0,(w-1)//2)*2,rd(0,(h-1)//2)*2
 dig(sx,sy)
 while rc(0,0)==1:
  for a in range(w):
   for b in range(h):
    if rc(a,b)==0:cx,cy=a,b;break
   if rc(a,b)==0:break
  dig(cx,cy)
 fr(sw,sh,m,m,dc[2])
 while rc(w-1,h-1)==1:
  for a in reversed(range(w)):
   for b in reversed(range(h)):
    if rc(a,b)==0:cx,cy=a,b;break
   if rc(a,b)==0:break
  dig(cx,cy)
 fr(bw-m,bh-m,m,m,dc[3])
 while rc(0,h-1)==1:
  for a in range(w):
   for b in reversed(range(h)):
    if rc(a,b)==0:cx,cy=a,b;break
   if rc(a,b)==0:break
  dig(cx,cy)
 while rc(w-1,0)==1:
  for a in reversed(range(w)):
   for b in range(h):
    if rc(a,b)==0:cx,cy=a,b;break
   if rc(a,b)==0:break
  dig(cx,cy)
 for a in range(w//2+1):
  for b in range(h//2+1):
   if rc(a*2,b*2)==1:dig(a*2,b*2)

def end():
 d=mn()-c
 sl(3);fr(0,0,320,222,gr)
 m,s,dx,ct=int(d//60),int(d%60),int((d*10)%10),int((d*100)%10)
 ds("Bravo, labyrinthe de",60,72)
 ds(str(w)+" par "+str(h)+", termine",160-((len(str(w))+len(str(h)))*5+70),102)
 if dx==s==m==0:
  ds("en "+str(ct)+" ct !",160-tl(ct)-40,132)
 elif s==m==0:
  ds("en "+str(dx)+" dx et "+str(ct)+" ct !",160-tl(dx)-tl(ct)-75,132)
 elif m==0:
  ds("en "+str(s)+" s, "+str(dx)+" dx",160-tl(s)-tl(dx)-50,132)
  ds("et "+str(ct)+" ct !",160-tl(ct)-40,152)
 else:
  ds("en "+str(m)+" m, "+str(s)+" s,",160-tl(m)-tl(s)-50,132)
  ds(str(dx)+" dx et "+str(ct)+" ct !",160-tl(dx)-tl(ct)-60,152)
 sl(5)

def menu():
 global tm
 size=ns=True
 tm=int(ml*2/3)
 fr(0,0,320,222,wh)
 ds("Choisissez la taille :",50,42)#,ds("(3 est le plus grand)",55,42+20)
 ds("+",155,130),ds("-",155,170)
 while size:
  if ns:
   ns=False
   fr(150,150,20,18,wh),ds(str(tm),160-5*len(str(tm)),150)
   sl(0.15)
  if kd(1) and tm<ml:tm,ns=tm+1,True
  elif kd(2) and tm>1:tm,ns=tm-1,True
  elif kd(4)or kd(52):size=False
 fr(0,0,320,222,wh)
 ds("Labyrinthe en",95,90)
 ds("initialisation...",75,114)
 maze(ml+1-tm)

while True:
 dspl,os=[],[]
 menu()
 fr(0,0,bw,sh,ifc),fr(0,0,sw,bh,ifc)
 #fr(sw,sh,bw-sw,bh-sh,gr)
 #for a in range(w):
 # for b in range(h):
 #  if dspl[a][b]!=1:fr(a*m+sw,b*m+sh,m,m,dc[dspl[a][b]])
 del dspl
 x,y,px,py,c=0,0,0,0,mn()
 game,new=True,True
 while game:
  os.append([0,0,0,w+h-2])
  while os:
   lv=w*h
   for i in range(len(os)):
    fc=os[i][2]+os[i][3]
#    fc=os[i][3]
    if fc<lv:lv,ix=fc,i
   x,y,gc=os[ix][0],os[ix][1],os[ix][2]
   if(x,y)==(w-1,h-1):break
   os.remove(os[ix])
   for a,b in[(1,0),(0,-1),(-1,0),(0,1)]:
    dx,dy=x+a,y+b
    if gp(sw+dx*m,sh+dy*m)==gr:continue
    nx,ny=x+2*a,y+2*b
    if not 0<=nx<w or not 0<=ny<h or gp(sw+nx*m,sh+ny*m)==dc[1]:continue
    gc,hc=gc+1,w-1-x+h-1-y
    os.append([nx,ny,gc,hc])
#    dspl[ny][nx]=5
    fr(sw+dx*m,sh+dy*m,m,m,dc[1])
    fr(sw+nx*m,sh+ny*m,m,m,dc[1])
  if (x,y)==(w-1,h-1):
   end()
   game=False
