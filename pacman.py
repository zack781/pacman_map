import pygame
import random


pygame.init()

width = 570
height = 630

Screen = pygame.display.set_mode((width,height))

#variables
game = True

#colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
wall = (0,128,248)

#kinematic
pacx = 30*1
pacy = 30*1
vx1=1
vy1=0
vx2=0
vy2=0
speed=7
#ghosts' kinematic
gx=None
gy=None
r = random.randrange(0,3)
if r==0:
    gx=8*30
    gy=9*30
elif r==1:
    gx=9*30
    gy=9*30
elif r==2:
    gx=10*30
    gy=9*30

gvx1=0
gvy1=0
gvx2=0
gvy2=0


#map
mapp = ("00000000000000000000        0        00 00 000 0 000 00 00                 00 00 0 00000 0 00 00    0   0   0    00000 000 0 000 00000000 0       0 00000000 0 00 00 0 00000      0   0      00000 0 00000 0 00000000 0       0 00000000 0 00000 0 00000        0        00 00 000 0 000 00 00  0           0  000 0 0 00000 0 0 000    0   0   0    00 000000 0 000000 00                 00000000000000000000")

key = None

clock = pygame.time.Clock()

def ghosts():
    global gx,gy,gvx1,gvy1,gvx2,gvy2
    
    pygame.draw.rect(Screen, black, (gx,gy,30,30))

    r = random.randrange(0,4)

    if r==0:
        #UP
        gvx1=0
        gvy1=-1
    elif r==1:
        #DOWN
        gvx1=0
        gvy1=1
    elif r==2:
        #LEFT
        gvx1=1
        gvy1=0
    elif r==3:
        #RIGHT
        gvx1=-1
        gvy1=0
        
    if mapp[(int(gx/30)+gvx1)+ ((int(gy/30)+gvy1)*19)] != "0":  
        gvx2=gvx1
        gvy2=gvy1
    
    if mapp[(int(gx/30)+gvx2)+ ((int(gy/30)+gvy2)*19)] != "0":
        gx+=(gvx2*30)
        gy+=(gvy2*30)
    


while game:
    counter=0 
    Screen.fill(white) 
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                vx1=0
                vy1=-1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                vx1=0
                vy1=1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                vx1=-1
                vy1=0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                vx1=1
                vy1=0

    #drawing
    #map
    for h in range(21):
        
        for w in range(19):
            if mapp[counter] == "0":
                pygame.draw.rect(Screen, red, (w*30,h*30,30, 30))
            counter+=1
    
    #character        
    pygame.draw.rect(Screen, blue, (pacx,pacy,30, 30))
    ghosts()


    #velocity

    if mapp[(int(pacx/30)+vx1)+ ((int(pacy/30)+vy1)*19)] != "0":
        vx2=vx1
        vy2=vy1
    
    if mapp[(int(pacx/30)+vx2)+ ((int(pacy/30)+vy2)*19)] != "0":
        pacx+=(vx2*30)
        pacy+=(vy2*30)

        
    
    pygame.display.flip()
    
    pygame.display.update()
    
    clock.tick(6)

pygame.quit()
quit()
