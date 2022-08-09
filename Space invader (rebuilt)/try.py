# import math
# print(math.pi)
# print(math.sin(math.pi/6))
# print(math.degrees(math.pi/6))
# print(math.radians(30))
import pygame
import math 
import random
from pygame import image
from pygame import mixer
from pygame.constants import K_LEFT, K_RIGHT, QUIT
pygame.init()

# background
background=pygame.image.load('background.png')
#bullet
bullet=pygame.image.load('bullet.png')
# Screen display
screen = pygame.display.set_mode((800, 600)) 

# spaceship
spaceship_img=pygame.image.load('space-invaders.png')
PlayerX=368
PlayerY=500
PlayerX_change=0
PlayerY_change=0
def spaceship(x,y):
    screen.blit(spaceship_img,(x,y))
# bullet
bullet=pygame.image.load('space-invaders.png')
bulletX=PlayerX
bulletY=PlayerY
bulletX_change=0
bulletY_change=0
def bullet(x,y):
    screen.blit(spaceship_img,(x,y))

#normal enemy
normal_enemy_img=pygame.image.load("ufo.png")
normal_enemyX=random.randint(0,736)
normal_enemyY=random.randint(0,200)
normal_enemyX_change=5
normal_enemyY_change=0
def normalenemy(x,y):
    screen.blit(normal_enemy_img,(x,y))


running = True

while running:
    # background RGB
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    # Quit game command by clicking on cross
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        # keystroke command
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("Left key is pressed")
                PlayerX_change=-5
            if event.key==pygame.K_RIGHT:
                print("Right key is pressed")
                PlayerX_change=5
            if event.key==pygame.K_UP:
                print("up key is pressed")
                PlayerY_change=-5
            if event.key==pygame.K_DOWN:
                print("Down key is pressed")
                PlayerY_change=5
            if event.key==pygame.K_SPACE:
                print("Space key is pressed")
            if event.key==pygame.K_RSHIFT:
                print("Rshift key is pressed")

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                print("key has been released")
                PlayerX_change=0
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                print("key has been released")
                PlayerY_change=0
                

    # spaceship and its movement
    PlayerX+= PlayerX_change
    PlayerY+= PlayerY_change
    if PlayerX<=0:
        PlayerX=0
    if PlayerX>=736:
        PlayerX=736
    if PlayerY<=300:
        PlayerY=300
    if PlayerY>=536:
        PlayerY=536
    spaceship(PlayerX,PlayerY)  
    # normal enenmy and its movement
    normalenemy(normal_enemyX,normal_enemyY)  
    if normal_enemyX<=0:
        normal_enemyX_change=5
    elif normal_enemyX>=736:
        normal_enemyX_change=-5
    normal_enemyX+=normal_enemyX_change




    pygame.display.update()