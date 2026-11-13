#Cree le 25 Mars 2024
from kandinsky import fill_rect as fr,draw_string as ds,get_pixel as gp
from random import randint as rd,choice as ch
from ion import keydown as kd
from time import sleep as sl,monotonic as mn
g,ifc=(150,)*3,(255,182,57)
wh,n=(255,)*3,(0,)*3
re,gr,bl=(255,0,0),(0,255,0),(0,0,255)
z,u,bw,bh,dir=0,1,320,222,[(1,0),(-1,0),(0,1),(0,-1)]
ta,tp=0.15,0.3
dc=[wh,re,bl,gr]

def shuffle(lst):
 n=len(lst)
 for i in range(n):
  j=rd(i,n-1)
  lst[i],lst[j]=lst[j],lst[i]
def maze(t=3):
 global dspl,w,h,sw,sh,m,i
 w,h,sw,sh,m,i=bw//t,bh//t,bw%t,bh%t,t,z
 if w%2==z:sw,w=sw+m,w-u
 if h%2==z:sh,h=sh+m,h-u
 dspl=[[u]*h for i in range(w)]
 def dig(x,y):
  global i
  dspl[x][y],id=z,z
#  fr(x*m+sw,y*m+sh,m,m,(255,)*3)
  shuffle(dir)
  for dx,dy in dir:
   nx,ny,id=x+2*dx,y+2*dy,id+u
   if z<=nx<w and z<=ny<h and dspl[nx][ny]==1 and i<115:
    dspl[x+dx][y+dy],i=z,i+u
#    fr((x+dx)*m+sw,(y+dy)*m+sh,m,m,(255,)*3),sl(0.001)
    dig(nx,ny)
   if id==4:i-=u
 sx,sy=rd(z,(w-u)//2)*2,rd(z,(h-u)//2)*2
 dig(sx,sy)
 while dspl[z][z]==u:
  for a in reversed(range(w)):
   for b in reversed(range(h)):
    if dspl[a][b]==z:cx,cy=a,b
  dig(cx,cy)
 dspl[z][z]=2
 while dspl[w-u][h-u]==u:
  for a in range(w):
   for b in range(h):
    if dspl[a][b]==z:cx,cy=a,b
  dig(cx,cy)
 dspl[w-u][h-u]=3
 while dspl[z][h-u]==u:
  for a in reversed(range(w)):
   for b in range(h):
    if dspl[a][b]==z:cx,cy=a,b
  dig(cx,cy)
 while dspl[w-u][z]==u:
  for a in range(w):
   for b in reversed(range(h)):
    if dspl[a][b]==z:cx,cy=a,b
  dig(cx,cy)
 for a in range(w//2+1):
  for b in range(h//2+1):
   if dspl[a*2][b*2]==u:dig(a*2,b*2)

def end():
 sl(2);fr(0,0,320,222,g)
 m,s=int((mn()-c)//60),int((mn()-c)%60)
 ds("Bravo, labyrinthe de",60,72)
 ds(str(w)+" par "+str(h)+", termine",160-((len(str(w))+len(str(h)))*5+70),102)
 if m==0:ds("en "+str(s)+" s !",160-(len(str(s))*5+35),132)
 else:ds("en "+str(m)+" m et "+str(s)+" s !",160-((len(str(m))+len(str(s)))*5+65),132)
 time=mn()
 while time>mn()-5:
  if kd(4):break

def menu():
 global ym,rj,tm
 choix=nc=size=ns=True
 rv=nr=False
 ym,pym,hm,lm=1,1,[42,102,162],[0,55,30]
 fr(0,0,320,222,wh)
 ds("Choisissez votre mode de jeu :",10,hm[0])
 ds("Labyrinthe simple",75,hm[1])
 ds("Labyrinthe a l'aveugle",50,hm[2])
 while choix:
  if nc:
   nc=False
   fr(lm[pym],hm[pym],10,18,wh),fr(310-lm[pym],hm[pym],10,18,wh)
   ds("[",lm[ym],hm[ym],bl),ds("]",310-lm[ym],hm[ym],bl)
   sl(ta)
  if kd(1) and ym>1:pym,ym,nc=ym,ym-1,True
  elif kd(2) and ym<len(hm)-1:pym,ym,nc=ym,ym+1,True
  elif kd(4):choix=False
 if ym==2:
  rj=2
  rv=nr=True
  fr(0,0,320,222,wh)
  ds("Choisissez la taille du rayon",25,hm[0])
  ds("de visibilite lors deplacement :",10,hm[0]+20)
  ds("+",155,130),ds("-",155,170)
  sl(tp)
 while rv:
  if nr:
   nr=False
   fr(150,150,20,18,wh),ds(str(rj),160-5*len(str(rj)),150)
   sl(ta)
  if kd(1) and rj<20:rj,nr=rj+1,True
  elif kd(2) and rj>0:rj,nr=rj-1,True
  elif kd(4):rv=False
 tm=10
 fr(0,0,320,222,wh)
 ds("Choisissez la taille :",50,hm[0]),ds("(3 est le plus grand)",55,hm[0]+20)
 ds("+",155,130),ds("-",155,170)
 sl(tp)
 while size:
  if ns:
   ns=False
   fr(150,150,20,18,wh),ds(str(tm),160-5*len(str(tm)),150)
   sl(ta)
  if kd(1) and tm<30:tm,ns=tm+1,True
  elif kd(2) and tm>3:tm,ns=tm-1,True
  elif kd(4):size=False
 fr(0,0,320,222,wh)
 ds("Labyrinthe en",95,90)
 ds("initialisation...",75,114)
 maze(tm)

def reveal():
 for a in range(-rj,rj+1):
  for b in range(-rj,rj+1):
   bx,by=x+a,y+b
   if not 0<=bx<w or not 0<=by<h or[bx,by]==[x,y]:continue
   if gp(bx*m+sw,by*m+sh)==(148,150,148):
    if dspl[bx][by]!=1:fr(bx*m+sw,by*m+sh,m,m,n)
    elif dspl[bx][by]==3:fr(bx*m+sw,by*m+sh,m,m,gr)

while True:
 menu()
 fr(z,z,bw,sh,ifc),fr(z,z,sw,bh,ifc)
 fr(sw,sh,bw-sw,bh-sh,g)
 if ym==1:
  for a in range(w):
   for b in range(h):
    if dspl[a][b]!=u:fr(a*m+sw,b*m+sh,m,m,dc[dspl[a][b]])
 else:fr((w-1)*m+sw,(h-1)*m+sh,m,m,gr)
 x,y,px,py,s,c=z,z,z,z,0.1,mn()
 game,new=True,True
 while game:
  if new:
   new=False
   fr(px*m+sw,py*m+sh,m,m,dc[dspl[px][py]]),fr(x*m+sw,y*m+sh,m,m,dc[1]),sl(s)
#   fr(px*m+sw,py*m+sh,m,m,g),fr(x*m+sw,y*m+sh,m,m,dc[1]),sl(s)
   if (x,y)==(w-u,h-u):end();game=False
  if kd(0) and x>z and dspl[x-u][y]!=u:x,px,py,new=x-u,x,y,True
  elif kd(1) and y>z and dspl[x][y-u]!=u:y,px,py,new=y-u,x,y,True
  elif kd(2) and y<h-u and dspl[x][y+u]!=u:y,px,py,new=y+u,x,y,True
  elif kd(3) and x<w-u and dspl[x+u][y]!=u:x,px,py,new=x+u,x,y,True
  if ym==2:reveal()
