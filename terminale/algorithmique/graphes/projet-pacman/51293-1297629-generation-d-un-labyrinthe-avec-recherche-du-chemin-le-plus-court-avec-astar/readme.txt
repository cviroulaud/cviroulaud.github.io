Génération d'un labyrinthe avec recherche du chemin le plus court avec astar----------------------------------------------------------------------------
Url     : http://codes-sources.commentcamarche.net/source/51293-generation-d-un-labyrinthe-avec-recherche-du-chemin-le-plus-court-avec-astarAuteur  : mehdichertiDate    : 05/09/2013
Licence :
=========

Ce document intitulé « Génération d'un labyrinthe avec recherche du chemin le plus court avec astar » issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis à disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fixées par la licence, tant que cette note
apparaît clairement.

Description :
=============

ce programme permet de:
<br />
<br />- g&eacute;n&eacute;rer un labyrinthe al&
eacute;atoire
<br />- utilisation de l'algorithme astar pour trouver le chemin 
le plus court (m&ecirc;me si dans le cas du labyrinthe parfait il y a un seul ch
emin possible l'algorithme utilis&eacute; trouve le meilleur chemin possible)
<
br />La s&eacute;lection de la destination est faite avec le souris
<br />
<br
 />D&eacute;pendances : pygame
<br /><a name='source-exemple'></a><h2> Source /
 Exemple : </h2>
<br /><pre class='code' data-mode='basic'>
# -*- coding: utf
8 -*-
&quot;&quot;&quot;
Laby , par Mehdi Cherti 2010 (mehdidc): 
	- generati
on d'un labyrinthe
	- utilisation de l'algorithme astar pour trouver le chemin 
le plus court (selection de la destination avec la souris)
&quot;&quot;&quot;

from  random import randint , choice
import pygame
from pygame.locals import *

import def_const
from math import sqrt

const = def_const.def_const ()
&qu
ot;&quot;&quot; definitions des constantes &quot;&quot;&quot;

# Couleurs
con
st.white  = (255 , 255 , 255)
const.pink   = (255 , 0 , 255)
const.black  = (0
 , 0 , 0)
const.yellow = (255 , 255 , 0)

#directions 
const.right = 0
cons
t.left = 1
const.up = 2
const.down = 3

# autres

const.wc = 20 # width d'
un seul carreau du laby
const.hc = 20# height d'un seul carreau du laby

cons
t.perso_radius = const.wc/2 # rayon du personnage (qui est un cercle)
const.tim
e_perso = 50 # temps en ms avant chaque test du clavier pour les touches qui con
cernent le perso
const.time_perso_poll = 50 # temps en ms avant chaque mise a j
our de la position du perso
&quot;&quot;&quot; fin definitions des constantes&q
uot;&quot;&quot;

class Point:
	def __init__ (self,xy):
		self.x = xy[0]
		
self.y = xy[1]

&quot;&quot;&quot; Definition de la classe cellule de labyrint
he&quot;&quot;&quot;
class cellule:
	def __init__(self):
		self.state = False

		self.portes = [True , True , True , True] # Droite , Gauche , Haut , Bas
		

&quot;&quot;&quot; distance : retourne la distance euclidienne entre deux poin
ts &quot;&quot;&quot;
def distance (p1 , p2):
	return sqrt((p1[0]-p2[0])**2 + 
(p1[1]-p2[1])**2)

&quot;&quot;&quot; classe Personnage &quot;&quot;&quot;
cl
ass Perso:
	def __init__ (self,lab):
		self.x = 1
		self.y = 1
		self.chemin
 =None
		self.laby = lab
		self.color = const.yellow
	&quot;&quot;&quot; affi
chage &quot;&quot;&quot;	
	def show(self,buffer):
		a,b = const.perso_radius ,
 const.perso_radius
		pygame.draw.circle (buffer, self.color , (a+self.laby.sx+
self.x*self.laby.wc,b+self.laby.sy+self.y*self.laby.hc) , 
		const.perso_radius
)
		
	&quot;&quot;&quot; mouvement selon la direction&quot;&quot;&quot;
	def 
move (self,dir):
			
		if not self.laby.get_cell (self.x , self.y).portes[dir]
:
			if dir == const.right and self.x+1 &lt; self.laby.w :
				self.x += 1
		
	if dir == const.left and self.x-1 &gt;=0:
				self.x -= 1
			if dir == const.
up and self.y-1 &gt;=0:
				self.y -= 1
			if dir == const.down and self.y+1 &
lt; self.laby.h:
				self.y += 1
				
	&quot;&quot;&quot; fonction utilisée p
ar astar pour traiter une des cases adjacentes&quot;&quot;&quot;
	def traitemen
t (self ,  liste_fermee , liste_ouverte , x ,  y , dir ,parent ,dest):
		if par
ent.portes[dir] : return
		c = self.laby.get_cell (x,y)
		if c in liste_fermee
 : return
		
		if c in liste_ouverte:
			G = distance ( (x,y) , (parent.x , p
arent.y))
			c.dir = self.laby.notdir (dir)
			if G &lt; c.G:
				c.G = G
		
		c.F = c.H + c.G
				c.parent = parent
		else:
			c.parent = parent
			c.di
r = self.laby.notdir (dir)
			c.G = distance ( (x,y) , (parent.x , parent.y))

			c.H = distance ( (x,y) , (dest.x ,dest.y))
			c.F = c.G + c.H
			liste_ouve
rte.append (c)
	&quot;&quot;&quot; retourne , après avoir trouvé le chemin avec
 astar , un tableau contenant le chemin&quot;&quot;&quot;
	def  get_astar (self
, csource , cdest):
		
		source = self.laby.get_cell (csource[0] , csource[1])

		dest = self.laby.get_cell (cdest[0] , cdest[1])
		cur=dest
		chemin = []

		while cur and (cur.x != source.x or cur.y != source.y):
			if cur.x == cur.pa
rent.x-1 :
				chemin.append (const.right)
			if cur.x == cur.parent.x+1:
			
	chemin.append (const.left)
			if cur.y == cur.parent.y+1:
				chemin.append (
const.up)
			if cur.y == cur.parent.y-1:
				chemin.append (const.down)
			cu
r = cur.parent
		
		ret = []
		id = len(chemin) - 1
		while id&gt;=0:
			re
t.append (self.laby.notdir(chemin[id]))
			id-=1
		return ret
		
	&quot;&quo
t;&quot; mise a jour de la position du personnage &quot;&quot;&quot;
	def poll(
self):
		if self.chemin:
			self.move (self.chemin.pop (0))
			
	&quot;&quot
;&quot; permet de se deplacer selon le chemin &quot;&quot;&quot;
	def aller(sel
f,chemin):
		self.chemin = chemin
			
	&quot;&quot;&quot;
	algorithme de pat
hfinding Astar , desti represente le tuple de la destination
	&quot;&quot;&quot
;
	def astar (self , desti):
		dest = Point(desti)
		liste_ouverte = []
		li
ste_fermee = []

		debut = self.laby.get_cell (self.x , self.y)
		liste_ouver
te.append (debut)
		debut.F = distance ((self.x,self.y) , (dest.x,dest.y))
		d
ebut.G = 0
		debut.H = debut.F
		debut.parent = None
		
		
		while 1:
			i
f len(liste_ouverte) &lt;= 0 : 
				break
			min , min_id= liste_ouverte[0].F,
0
					
			for id,v in enumerate(liste_ouverte[1:]):
				if v &lt; min :
			
		min = v
					min_id = id +1
			liste_fermee.append (liste_ouverte[min_id])

			
			if liste_ouverte[min_id].x == dest.x and liste_ouverte[min_id].y == dest
.y : break
			
			self.traitement (liste_fermee,liste_ouverte,liste_ouverte[mi
n_id].x +  1 , liste_ouverte[min_id].y , const.right , liste_ouverte[min_id] , d
est)
			self.traitement (liste_fermee,liste_ouverte,liste_ouverte[min_id].x -  
1 , liste_ouverte[min_id].y , const.left , liste_ouverte[min_id] , dest)
			sel
f.traitement (liste_fermee,liste_ouverte,liste_ouverte[min_id].x  , liste_ouvert
e[min_id].y-1 , const.up , liste_ouverte[min_id] , dest)
			self.traitement (li
ste_fermee,liste_ouverte,liste_ouverte[min_id].x  , liste_ouverte[min_id].y+1 , 
const.down , liste_ouverte[min_id] , dest)
			liste_ouverte.remove (liste_ouver
te[min_id])

&quot;&quot;&quot; classe du labyrinthe &quot;&quot;&quot;
class
 laby:
	def __init__ (self,w,h,sx=0,sy=0):
		self.w = w
		self.h = h
		self.
cellules = []
		self.wc = const.wc
		self.hc = const.hc
		self.sx = sx
		sel
f.sy = sy
		&quot;&quot;&quot; initialisation des cellules , pour chaque cellul
e , il initialise sa position dans le labyrinthe &quot;&quot;&quot;
		for v in 
range(self.w*self.h):
			a = cellule()
			a.x = v % self.w
			a.y = v / self.
w
			self.cellules.append (a)
	&quot;&quot;&quot; retourne la cellule correspo
ndante à la position (x,y) &quot;&quot;&quot;
	def get_cell (self,x,y):
		retu
rn self.cellules[x +  y * self.w]
	&quot;&quot;&quot; retourne direction de sen
s contraire d'une direction &quot;&quot;&quot;
	def notdir(self,dir):
		if dir
 == const.right : return const.left
		if dir == const.left : return const.right

		if dir == const.up : return const.down
		if dir == const.down : return cons
t.up
		
	&quot;&quot;&quot; generation du labyrinthe &quot;&quot;&quot;
	def 
generate_laby (self,x=-1,y=-1):
		if x==-1:
			x = randint(0,self.w-1)
			y =
 randint(0,self.h-1)
		cell_act = self.get_cell (x,y)
		
		if not cell_act.st
ate :
			cell_act.state = True
			tab = []
			if x+1&lt;self.w and not self.g
et_cell(x+1,y).state : tab.append((x+1,y,const.right))
			if x-1&gt;=0  and not
 self.get_cell(x-1,y).state    : tab.append((x-1,y,const.left))
			if y-1&gt;=0
  and not self.get_cell(x,y-1).state   : tab.append((x  ,y-1,const.up))
			if y
+1&lt;self.h and not self.get_cell(x,y+1).state : tab.append((x  ,y+1,const.down
))
			if tab:
				
				while tab:
					C = choice (tab)
					if not self.ge
t_cell(C[0] , C[1]).state:
						
						cell = self.get_cell (C[0] , C[1])
		
				cell_act.portes[C[2]] = False
						cell.portes[self.notdir(C[2])] = False

						self.generate_laby (C[0] , C[1])
					tab.remove (C)
				return True
	
		else : 
				return False
		
	&quot;&quot;&quot; affiche le labyrinthe &quot
;&quot;&quot;
	def show(self,buffer):
		W,H = self.wc , self.hc
		sx,sy = sel
f.sx , self.sy
		for y in range(self.h-1):
			for x in range(self.w-1):
				c
 = self.get_cell (x,y)
				if c.portes[const.right] :
					pygame.draw.line (b
uffer , const.white , (sx+(x+1)*W,sy+y*H),(sx+(x+1)*W,sy+(y+1)*H))
				if c.por
tes[const.down] :
					pygame.draw.line (buffer , const.white , (sx+(x)*W,sy+(y
+1)*H),(sx+(x+1)*W,sy+(y+1)*H))

		x = self.w - 1

		for y in range(self.h-1
):
			c = self.get_cell (x , y)
			if c.portes[const.down]:
				pygame.draw.l
ine (buffer , const.white , (sx+x*W,sy+(y+1)*H),(sx+(x+1)*W,sy+(y+1)*H) )

		y
 = self.h - 1
		for x in range(self.w-1):
			c = self.get_cell (x , y)
			if 
c.portes[const.right]:
				pygame.draw.line (buffer , const.white , (sx+(x+1)*W
,sy+(y)*H),(sx+(x+1)*W,sy+(y+1)*H) )
		pygame.draw.rect (buffer , const.pink , 
(sx , sy , W * self.w , H * self.h),2)
		

if __name__ == &quot;__main__&quot
;:
	
	mylaby = laby(20,20) # création d'un labyrinthe de 20x20 cellules
	pyga
me.init ()
	pygame.display.set_mode ( (640,480))
	screen = pygame.display.get_
surface ()
	
	mylaby.generate_laby() # géneration aléatoire du labyrinthe

	
perso = Perso (mylaby)
	keys = None
	move_time = 0
	perso_time = 0

	while 
True:
		screen.fill (const.black)
		events = pygame.event.get ()
		
		for ev
ent in events:
		
			&quot;&quot;&quot; click de la souris &quot;&quot;&quot;

			if event.type == MOUSEBUTTONDOWN:
				mx , my = pygame.mouse.get_pos ()
		
		x = (mx - mylaby.sx) / mylaby.wc
				y = (my - mylaby.sy) / mylaby.hc
				if
 x&gt;=0 and y&gt;=0 and x &lt; mylaby.w and y &lt; mylaby.h:
					perso.astar 
((x,y)) # trouve le chemin avec astar
					chemin = perso.get_astar ((perso.x,p
erso.y) , (x,y)) # reçoit le chemin en tableau qui donne les directions à prendr
e sequentiellement
					perso.aller (chemin) # ordonne au personnage d'aller au
 chemin sans arrêter la boucle principale
					
		keys = pygame.key.get_presse
d ()
		
		&quot;&quot;&quot; Mouvement du personnage &quot;&quot;&quot;
		if 
pygame.time.get_ticks () - move_time &gt;= const.time_perso:
			move_time = pyg
ame.time.get_ticks ()	
			if keys[pygame.K_RIGHT]:
				perso.move (const.right
)
			if keys[pygame.K_LEFT]:
				perso.move (const.left)
			if keys[pygame.K_
UP]:
				perso.move (const.up)
			if keys[pygame.K_DOWN]:
				perso.move (con
st.down)
			
		if keys[pygame.K_ESCAPE] :
			break
			
		&quot;&quot;&quot;
 mise a jour de la position du personnage &quot;&quot;&quot;
		if pygame.time.g
et_ticks () - perso_time &gt;= const.time_perso_poll:
			perso_time = pygame.ti
me.get_ticks ()
			perso.poll ()
			
		&quot;&quot;&quot; affichage &quot;&qu
ot;&quot;
		mylaby.show (screen)
		perso.show (screen)
		pygame.display.flip 
()
</pre>
