
import sys, pygame, random

pygame.init()

size = width, height = 100, 100
speed = [0, 0]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

def foglalt (screen, poz):
    if poz[0] in range(width) and poz[1] in range(height):
        if screen.get_at(poz)==white:
            return True
    return False

def szomszéd (screen, poz):
    sz=0
    x=poz[0]
    y=poz[1]

    if foglalt(screen,(x+1,y)):
        sz=sz+1

    if foglalt(screen,(x-1,y)):
        sz=sz+1

    if foglalt(screen,(x+1,y+1)):
        sz=sz+1

    if foglalt(screen,(x+1,y-1)):
        sz=sz+1

    if foglalt(screen,(x-1,y+1)):
        sz=sz+1

    if foglalt(screen,(x-1,y-1)):
        sz=sz+1

    if foglalt(screen,(x,y+1)):
        sz=sz+1

    if foglalt(screen,(x,y-1)):
        sz=sz+1
    return sz
##inicializálás (ősleves)
for x in range(width):
        for y in range(height):
            if random.random()<0.7:
                screen.set_at((x,y),black)
            else:
                screen.set_at((x,y),white)

while 1:
    halottak=[]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    szület=[]
    halott=[]
    for x in range(width):
        for y in range(height):
            szdb=szomszéd(screen,(x,y))
            if foglalt(screen,(x,y)):
                if szdb>3 or szdb<2:
                    halott.append((x,y))
            else:
                if szomszéd(screen,(x,y))==3:
                    szület.append((x,y))

    for a in halott:
        screen.set_at(a,black)
    for a in szület:
        screen.set_at(a,white) 
    
    pygame.display.flip()