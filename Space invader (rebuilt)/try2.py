import pygame
import random
import math
from pygame import image
from pygame.constants import K_SPACE
pygame.init()

screen= pygame.display.set_mode((800,600))

# Title and Icon 
pygame.display.set_caption("Space invaders")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
#background
background=pygame.image.load('background.png')
#bullet
bullet=pygame.image.load('bullet.png')
running = True
#player
playerimg = pygame.image.load("space-invaders.png")
playerX=360
playerX_change=0
playerY=450
# enemy
enemyimg = pygame.image.load("ufo.png")
enemyX=random.randint(0,736)
enemyY=random.randint(50,100)
enemyX_change=3
enemyY_change=5


bulletY=450
bulletY_change=5
bulletX_change=5
bulletstate="ready"

def enemy(x,y):
    screen.blit(enemyimg,(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))
def bullet_fire(x,y):
    global bulletstate 
    bulletstate="fire"
    screen.blit(bullet,(x+16,y+10))

while running:
    # RGB (RED,GREEN,BLUE)
    screen.fill((0,0,0))
    # background img
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    # if keystroke is pressed check whether it is right or left
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("left key is pressed")
                playerX_change=-3
            if event.key==pygame.K_RIGHT:
                print("right key is pressed")
                playerX_change=3
            if event.key==pygame.K_SPACE:
                if bulletstate is "ready":
                    bulletX=playerX
                    print("space is pressed")
                    bullet_fire(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
                print("key has been released")
                playerX_change=0
                
    # checking for boundries of spacreship so it doesnt go out of bound
    playerX+=playerX_change
    if playerX<=0  :
        playerX=0
    elif playerX>=736:
        playerX=736
    player(playerX,playerY)
    # Enemy movement
    if enemyX<=0  :
        enemyX_change=3
        enemyY+=enemyY_change
    elif enemyX>=736:
        enemyX_change=-3
        enemyY+=enemyY_change
    enemy(enemyX,enemyY)
    enemyX+=enemyX_change
    #bullet movement
    if bulletY<=0:
        bulletY=480
        bulletstate="ready"
    if bulletstate is "fire" :
        bullet_fire(bulletX,bulletY)
        bulletY-=bulletY_change
        bulletX+=bulletX_change
    

    pygame.display.update()
