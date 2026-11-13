#Cree le 16 Mai 2025
from kandinsky import fill_rect as fr,draw_string as ds,get_pixel as gp
from random import randint as rd,choice as ch
from ion import keydown as kd
from time import sleep as sl,monotonic as mn
g,ifc=(148,150,148),(255,182,57)
wh,n=(255,)*3,(0,)*3
re,gr,bl=(255,0,0),(0,255,0),(0,0,255)
z,u,bw,bh,dir=0,1,320,222,[(1,0),(-1,0),(0,1),(0,-1)]
s=0.1
dc=[wh,re,bl,gr]
mr=500
sm=30
tc=True

def rc(x,y):
 cl=gp(x*m+sw,y*m+sh)
 if cl==g:return u
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
 if w%2==z:sw,w=sw+m,w-u
 if h%2==z:sh,h=sh+m,h-u
 fr(z,z,bw,sh,ifc),fr(z,z,sw,bh,ifc)
 fr(sw,sh,bw-sw,bh-sh,g)
 def dig(x, y):
  sk=[(x,y,z)]
  while sk:
   cx,cy,d=sk[-u]
   fr(cx*m+sw,cy*m+sh,m,m,dc[z])
   if d>mr:sk.pop();continue
   shuffle(dir)
   for dx,dy in dir:
    nx,ny=cx+2*dx,cy+2*dy
    if z<=nx<w and z<=ny<h and rc(nx,ny)==u:
     fr((cx+dx)*m+sw,(cy+dy)*m+sh,m,m,dc[z])
     #sl(0.0001)
     sk.append((nx,ny,d+u))
     break
   else:sk.pop()
 sx,sy=rd(z,(w-u)//2)*2,rd(z,(h-u)//2)*2
 dig(sx,sy)
 while rc(z,z)==u:
  for a in range(w):
   for b in range(h):
    if rc(a,b)==z:cx,cy=a,b;break
   if rc(a,b)==z:break
  dig(cx,cy)
 fr(sw,sh,m,m,dc[2])
 while rc(w-u,h-u)==u:
  for a in reversed(range(w)):
   for b in reversed(range(h)):
    if rc(a,b)==z:cx,cy=a,b;break
   if rc(a,b)==z:break
  dig(cx,cy)
 fr(bw-m,bh-m,m,m,dc[3])
 while rc(z,h-u)==u:
  for a in range(w):
   for b in reversed(range(h)):
    if rc(a,b)==z:cx,cy=a,b;break
   if rc(a,b)==z:break
  dig(cx,cy)
 while rc(w-u,z)==u:
  for a in reversed(range(w)):
   for b in range(h):
    if rc(a,b)==z:cx,cy=a,b;break
   if rc(a,b)==z:break
  dig(cx,cy)
 for a in range(w//2+u):
  for b in range(h//2+u):
   if rc(a*2,b*2)==u:dig(a*2,b*2)

def end():
 sl(2);fr(z,z,320,222,g)
 m,s=int((mn()-c)//60),int((mn()-c)%60)
 ds("Bravo, labyrinthe de",60,72)
 ds(str(w)+" par "+str(h)+", termine",160-((len(str(w))+len(str(h)))*5+70),102)
 if m==0:ds("en "+str(s)+" s !",160-(len(str(s))*5+35),132)
 else:ds("en "+str(m)+" m et "+str(s)+" s !",160-((len(str(m))+len(str(s)))*5+65),132)
 time=mn()
 while time>mn()-5:
  if kd(4):break

def menu():
 global ym,rj,tm,tc
 size=ns=True
 hm=[42,102,162]
 tm=int(sm*2/3)
 sl(s)
 fr(z,z,320,222,wh)
 ds("Choisissez la taille :",50,hm[z])
 ds("+",155,130),ds("-",155,170)
 while size:
  if ns:
   ns=False
   fr(150,150,20,18,wh),ds(str(tm),160-5*len(str(tm)),150)
   sl(s)
  if kd(u) and tm<sm:tm,ns=tm+u,True
  elif kd(2) and tm>u:tm,ns=tm-u,True
  elif kd(4) or kd(52):size=False
 trc=nt=True
 fr(z,z,320,222,wh)
 ds("Dessiner le tracé du passage",20,hm[z])
 ds("<",131,150),ds(">",179,150)
 while trc:
  if nt:
   nt=False
   fr(151,150,18,18,n),fr(152,151,16,16,dc[3]if tc else dc[u])
   sl(s)
  if kd(z)and tc:tc=False;nt=True
  if kd(3)and not tc:tc=nt=True
  if kd(4)or kd(52):trc=False
 fr(z,z,320,222,wh)
 ds("Labyrinthe en",95,90)
 ds("initialisation...",75,114)
 maze(sm+u-tm)

while True:
 menu()
 x,y,px,py,c=z,z,z,z,mn()
 game,new=True,True
 while game:
  if new:
   new=False
   fr(px*m+sw,py*m+sh,m,m,dc[0]if not tc else n)
#   fr(px*m+sw,py*m+sh,m,m,g),fr(x*m+sw,y*m+sh,m,m,dc[1]),sl(s) #Erase your path in your back
   if(px,py)==(z,z):fr(sw,sh,m,m,dc[2])
   fr(x*m+sw,y*m+sh,m,m,dc[1])
   sl(s)
   if (x,y)==(w-u,h-u):end();game=False
  if kd(0) and x>z and rc(x-u,y)!=u:x,px,py,new=x-u,x,y,True
  elif kd(1) and y>z and rc(x,y-u)!=u:y,px,py,new=y-u,x,y,True
  elif kd(2) and y<h-u and rc(x,y+u)!=u:y,px,py,new=y+u,x,y,True
  elif kd(3) and x<w-u and rc(x+u,y)!=u:x,px,py,new=x+u,x,y,True
