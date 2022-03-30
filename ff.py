import random
from turtle import color
import pygame
width=600
height=500
window=pygame.display.set_mode((width,height))
pixel=50
player_x=width/2-pixel
player_y=450-pixel
player_xchange=0
ball_x=width/2-pixel
ball_y=height/2-pixel
ball_xchange=random.choice((1,-1))
vel=2
color='white'
ball_ychange=1
def collision():
    global ball_xchange
    global ball_ychange
    if player_y <(ball_y+pixel):
        if player_x > ball_x and player_x+pixel <ball_x+pixel or player_x+pixel>ball_x and player_x+pixel<ball_x+pixel:
            ball_xchange*=-1
            ball_ychange*=-1
run=True
while run:
    window.fill(color)
    # window.blit(text_1,)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    if ball_x>=width or ball_x<=0:
        ball_xchange*=-1
    if ball_y>=height or ball_y<=0:
        ball_ychange*=-1
    ball_x+=ball_xchange
    ball_y+=ball_ychange
    pygame.draw.circle(window,'red',(ball_x,ball_y),10)
    
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player_x>0:
        player_x-=vel
    if key[pygame.K_RIGHT] and player_x<600-100:
        player_x+=vel
    pygame.draw.rect(window,'red',(player_x,player_y,100,30))
    collision()
    # if ball_y==height:
    #     pygame.display.quit()
    # print(ball_x,ball_y)
    pygame.display.update()
