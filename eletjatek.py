import sys, pygame, random

pygame.init()

cell_width=10
cell_height=10
grid=grid_x, grid_y=100,100
size = width, height = cell_width*grid_x, cell_height*grid_y
black = 0, 0, 0
white = 255, 255, 255
##üres grid
grid=[]
for i in range(grid_y):
    grid.append([0]*grid_x)

screen = pygame.display.set_mode(size)
sejt=pygame.image.load("sejt.png")
sejt2=pygame.image.load("sejt2.png")
sejt3=pygame.image.load("sejt3.png")
sejt4=pygame.image.load("sejt4.png")

def foglalt (grid, poz):
    x=poz[0]
    y=poz[1]
    if x in range(grid_x) and y in range(grid_y):
        if grid[x][y]!=0:
            return True
    return False

def szomszéd (grid, poz):
    sz=0
    x=poz[0]
    y=poz[1]

    if foglalt(grid,(x+1,y)):
        sz=sz+1

    if foglalt(grid,(x-1,y)):
        sz=sz+1

    if foglalt(grid,(x+1,y+1)):
        sz=sz+1

    if foglalt(grid,(x+1,y-1)):
        sz=sz+1

    if foglalt(grid,(x-1,y+1)):
        sz=sz+1

    if foglalt(grid,(x-1,y-1)):
        sz=sz+1

    if foglalt(grid,(x,y+1)):
        sz=sz+1

    if foglalt(grid,(x,y-1)):
        sz=sz+1
    return sz
##inicializálás (ősleves)
for x in range(grid_x):
        for y in range(grid_y):
            if random.random()<0.7:
                grid[x][y]=0
            else:
                grid[x][y]=1
          

while 1:
    halottak=[]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    szület=[]
    halott=[]
    for x in range(grid_x):
        for y in range(grid_y):
            szdb=szomszéd(grid,(x,y))
            if foglalt(grid,(x,y)):
                if szdb>3 or szdb<2:
                    halott.append((x,y))
                else:
                    if grid[x][y]<13:
                        grid[x][y]+=1
            else:
                if szomszéd(grid,(x,y))==3:
                    szület.append((x,y))

    for x,y in halott:
        grid[x][y]=0
    for x,y in szület:
        grid[x][y]=1
    
    screen.fill(black)
    for x,oszlop in enumerate(grid):
        for y,s in enumerate(oszlop):
            if s in [1,2,3]:
                screen.blit(sejt, [x*cell_width,y*cell_height])
            elif s in [4,5,6]:
                screen.blit(sejt2, [x*cell_width,y*cell_height])
            elif s in [7,8,9]:
                screen.blit(sejt3, [x*cell_width,y*cell_height])
            elif s>10:
                screen.blit(sejt4, [x*cell_width,y*cell_height])
                
    print(grid)
    pygame.display.flip()
