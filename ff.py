# from turtle import Screen, color
# import pygame
# a=pygame.init()
# windows=pygame.display.set_mode((600,600),pygame.RESIZABLE)
# caption=pygame.display.set_caption('LUDO')
# icon=pygame.image.load("ludo.png")
# set_icon=pygame.display.set_icon(icon)
# x,y=windows.get_size()
# color='skyblue'
# windows.fill(color)

# # def draw(x,y,width,height):
# #     pygame.draw.rect(windows,'blue',[x,y,width,height])
# #     circle_x= width / 2 + x
# #     circle_y= height / 2+y
# #     if height<width:
# #         radius=height/2
# #     else:
# #         radius=width/2
# #     pygame.draw.circle(windows,'green',[circle_x,circle_y],radius)
# # draw(50,500,200,100)

# # # rentangle_list=[pygame.Rect(50,100,500,200),
# # pygame.Rect(70,120,520,220),
# # pygame.Rect(90,140,540,240),
# # pygame.Rect(110,160,560,260)]

# # pygame.draw.ellipse(windows,'red',[400,400,100,100])
# # pygame.draw.circle(windows,'green',[400,400],56)
# # pygame.draw.polygon(windows,'red',[[100,100],[560,322],[350,250]])


# # # col_1=['red','blue','green','yellow']
# # # col_var=0
# # # for rectangle in rentangle_list:
# # #     pygame.draw.rect(windows,col_1[col_var],rectangle,5)
# # #     col_var+=1



# # # windows.blit(icon,(100,100))
# # # # pygame.display.flip()
# # # pygame.draw.circle(windows,('blue'),(250,250),100)
# # # pygame.Surface.copy(windows)
# # # pygame.Surface.set_colorkey(icon,'blue')
# # # pygame.Surface.set_alpha(icon)
# pygame.draw.rect(windows,'red',[250,250,150,150],5,31)
# # # pygame.draw.circle(windows,'red',[100,120],64,5)
# # # pygame.draw.rect(windows,'red',[20,180,480,180])
# # # pygame.draw.circle(windows,'green',[250,250],100)
# # # # pygame.time.set_timer(500)
# run=True
# while run:
#     for event in pygame.event.get():
#         pygame.display.flip()
    
#         if event.type==pygame.QUIT:
#             pygame.quit()
#     # pygame.display.flip()
    
# pygame.quit()
    
    
    
    
    
    
#     # if color=='red':
#     #     color='blue'
#     # elif color=='blue':
#     #     color='yellow'
#     # else:
#     #     color='red'
#     # windows.fill(color)
#     # pygame.display.flip()





"""pygame mouse click"""
# from turtle import circle, color, position
# import pygame
# a=pygame.init()
# window=pygame.display.set_mode((600,600),(pygame.RESIZABLE))
# icon=pygame.image.load('ludo.png')
# icon=pygame.display.set_icon(icon)
# window.fill('white')
# pygame.display.flip()
# circle_list=[]
# circle_radius=50
# run=True
# while run:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False
#         elif event.type==pygame.MOUSEBUTTONDOWN:
#             position=event.pos
#             circle_list.append(position)
#     for circ_le in circle_list:
#         pygame.draw.circle(window,'blue',circ_le,circle_radius)
#     pygame.display.update()

'''third project'''

# from turtle import circle, color, position
# import pygame
# a=pygame.init()
# window=pygame.display.set_mode((500,500),(pygame.RESIZABLE))
# icon=pygame.image.load('ludo.png')
# icon=pygame.display.set_icon(icon)
# timer=pygame.time.Clock()
# col_or='white'
# window.fill(col_or)
# # pygame.display.flip()
# event1=pygame.USEREVENT+1
# event2=pygame.USEREVENT+2
# box=pygame.Rect(225,225,50,50)
# pygame.time.set_timer(event1,500)
# grow=True
# run=True
# while run:
#     for event in pygame.event.get():
#         if event.type==event1:
#             if col_or=='white':
#                 window.fill('white')
#                 col_or='green'
#             elif col_or=='green':
#                 window.fill('green')
#                 col_or='white'
#         if event.type==event2:
#             if grow:
#                 box.inflate_ip(3, 3)
#                 grow= box.width < 75
#             else:
#                 box.inflate_ip(-3, -3)
#                 grow= box.width < 50
#         if event.type==pygame.QUIT:
#             run=False
#     if box.collidepoint(pygame.mouse.get_pos()):
#         pygame.event.post(pygame.event.Event(event2))
# #     pygame.draw.rect(window,'red',box)
#     pygame.display.update()
#     timer.tick(30)
# # pygame.quit()


# # import pygame
# # window=pygame.display.set_mode((500,500))
# import pygame
# from turtle import color
# pygame.font.init()
# pygame.font.get_fonts()
# window=pygame.display.set_mode((600,600))
# file1=pygame.font.SysFont('sar.ttf',50)
# # window.fill('white')
# text1=file1.render('ek kahani hai jo sabko sunanii hai',True,'red')
# text=text1.get_rect()
# text.center=(300,300)
# run=True
# while run:
#     pygame.display.flip()
#     window.blit(text1,text)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False


# from turtle import color
# import pygame
# window=pygame.display.set_mode((600,600))
# pygame.font.init()
# text3='SNAKE!!'
# text=pygame.font.SysFont(None,50)
# text1=text.render((text3),True,'red')
# text2=text1.get_rect()
# text2.center=(300,300)
# print()
# window.fill('white')

# run=True
# while run:
#     pygame.display.flip()
#     window.blit(text1,text2)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False
        

        
'''movement'''
# from turtle import color
# import pygame
# window=pygame.display.set_mode((600,600))
# x=100
# y=100
# width=10
# height=10
# vel=4
# run=True
# while run:
#     for eve in pygame.event.get():
#         if eve.type==pygame.QUIT:
#             run =False
    # key=pygame.key.get_pressed()
    # if k+=vel
    # if key[pygame.K_UP]and x>0:
    #     y-=vel
    # if key[pygamey[pygame.K_LEFT]and x>0:
    #     x-=vel
    # if key[pygame.K_RIGHT]and x<600-width:
    #     xe.K_DOWN]and y<600-height:
    #     y+=vel
#     window.fill('black')
    # pygame.draw.rect(window,'red',(x,y,width,height))
#     pygame.display.update()

'''snake game ki kosis'''
# from turtle import color
# import pygame
# import random
# width=600
# height=500
# window=pygame.display.set_mode((width,height))
# pixel=64
# x=100
# y=400
# width1=100
# height1=30-pixel
# vel=4
# event1=pygame.USEREVENT+1
# ball_x=width/2-pixel
# ball_y=height/2
# ball_xchange=random.choice((1,-1))
# ball_ychange=1

# run=True
# while run:
#     window.fill('red')
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False
#         if event.type==event1:
            

#     if ball_x>=width or ball_x<=0:
#         ball_xchange*=-1
#     if ball_y>=height or ball_y<=0:
#         ball_ychange*=-1
#     ball_x+=ball_xchange
#     ball_y+=ball_ychange
#     circle1=pygame.draw.circle(window,'blue',(ball_x,ball_y),15)
#     key=pygame.key.get_pressed()
#     if key[pygame.K_LEFT]and x>0:
#         x-=vel
#     if key[pygame.K_RIGHT]and x<600-width1:
#         x+=vel
#     # if key[pygame.K_UP]and x>0:
#     #     y-=vel
#     # if key[pygame.K_DOWN]and y<600-height1:
#     #     y+=vel
#     rect1=pygame.draw.rect(window,'blue',(x,y,width1,height1))
#     if circle1.collidepoint(ball_x,ball_y):
#         pygame.event.post(pygame.event.Event(event1))
    

#     pygame.display.update()
#     # print(ball_xchange,'\n',ball_ychange)
#     # print(ball_x,'\n',ball_y)


'''snowfall'''

# from textwrap import fill
# from turtle import circle, color
# import pygame
# import random 
# window=pygame.display.set_mode((600,600))
# x=random.randrange(0,400)
# y=random.randrange(0,400)
# snowfall=[]
# for i in range (50):
#     x=random.randrange(0,400)
#     y=random.randrange(0,400)
#     snowfall.append([x,y])
# run=True
# while run:
#     window.fill('white')
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False
#     for i in range(len(snowfall)):
#         pygame.draw.circle(window,'black',snowfall[i],2)
#         snowfall[i][1]+=1
#     if snowfall[i][1]>400:
#         x=random.randrange(0,400)
#         snowfall[i][0]=x
#         y=random.randrange(-50,-10)
#         snowfall[i][1]=y
    
#     pygame.display.flip()

'''curves'''

# from turtle import color
# import pygame
# from math import radians, sin
# from math import cos
# window=pygame.display.set_mode((600,600))
# color('white','red')
# def sar(n,size):
#     point=[]
#     for i in range(0,361):
#         r=size*sin(radians(i*n))
#         x=r*sin(radians(i))
#         y=r*cos(radians(i))
#         list.append(point,(600/2+x,600/2+y))
#         pygame.draw.line(window,'red',point,5)
# def pos():

#     sar(2,10)
# run=True
# while run:
#     window.fill('white')
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False

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
