import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300, 50)
import pygame
import pgzrun
import random

#this vrsion is for coding the movement part
#Screen Setting
TITLE = 'Rabbitto'
WIDTH = 800
HEIGHT = 600

#RabbitActor
RabbitSprite = Actor('rabbit1')
RabbitSprite.pos = (70,420)
RabbitRun = ['rabbit1', 'rabbit2']
RabbitSprite.vy = 0

#SnailActor
SnailSprite = Actor('snail1')
SnailSprite.pos = (750,440)
SnailRun = ['snail1', 'snail2']

#FlyActor
FlySprite = Actor('fly1')
FlySprite.pos = (750,290)
FlyRun = ['fly1', 'fly2']

#CarrotActor
CarrotSprite = Actor('carrot')
CarrotSprite.pos = (750,250)

#other valuable
counter_fast = 0
counter_slow = 0
Jump_Velocity = -20 #สูงขึ้น ลบมากขึ้น
GRAVITY = 0.5
rabbit_on_ground = True
score = 0
life = 10
game_state = ' '

def SnailMove():
      SnailSprite.x = SnailSprite.x - 1
      if SnailSprite.x <= 0 :
            SnailSprite.x = 750
            ResetSnail()

def ResetSnail(): #to reset snail position when the snail เลยขอบ
        SnailSprite.pos = (750,440)

def FlyMove():
      FlySprite.x = FlySprite.x - 4
      if FlySprite.x <= 0 :
         FlySprite.pos = (750,300)
         ResetFly()

def ResetFly(): #to reset fly position when the fly เลยขอบ
        FlySprite.pos = (750,300)

def CarrotMove():
      CarrotSprite.x = CarrotSprite.x - 3
      if CarrotSprite.x <= 0 :
         CarrotSprite.pos = (750,300)
         ResetCarrot()

def ResetCarrot(): #to reset carrot position when the carrot เลยขอบ
        CarrotSprite.pos = (750,280)

def Animate_fast():
      global counter_fast
      counter_fast = counter_fast + 1
      RabbitSprite.image = RabbitRun[counter_fast % 2]
      FlySprite.image = FlyRun[counter_fast % 2]

def Animate_slow():
      global counter_slow
      counter_slow = counter_slow + 1
      SnailSprite.image = SnailRun[counter_slow % 2]

clock.schedule_interval(Animate_fast,0.2)
clock.schedule_interval(Animate_slow,0.3)

def rabbitJump():
      global rabbit_on_ground
      if keyboard.space == True and rabbit_on_ground == True:
            RabbitSprite.vy = Jump_Velocity
            RabbitSprite.y = RabbitSprite.y + RabbitSprite.vy
      else :
            RabbitSprite.vy  = RabbitSprite.vy + GRAVITY
            RabbitSprite.y = RabbitSprite.y + RabbitSprite.vy
      if RabbitSprite.y >= 400:
            RabbitSprite.y = 400
            rabbit_on_ground = True       #rabbit on the ground
      else :
            rabbit_on_ground = False      #rabbit in the air

def LifeAndScore():
      global score
      global life
      global game_state
      if RabbitSprite.colliderect(CarrotSprite):
            score = score + 1
            print ('score :', score)
            ResetCarrot()
      if RabbitSprite.colliderect(SnailSprite):
            life = life - 1
            print ('life :', life)
            ResetSnail()
      if RabbitSprite.colliderect(FlySprite):
            life = life - 2
            print ('life :', life)
            ResetFly()
      if score >= 5 :
            print ('win')
            game_state = 'win'
      if life <=0:
            print ('game over')
            game_state = 'game over'

def update():
      if game_state == 'play' :
            SnailMove()
            FlyMove()
            CarrotMove()
            LifeAndScore()
            rabbitJump()

def draw():
      global game_state
      screen.blit('sky', (0,0))
      screen.blit('ground', (0,450))
      def restart():
            global game_state
            global life
            global score
            screen.draw.text('Press s to Start', center = (400,300), color = 'lightcoral', fontsize = 50)
            if keyboard.s == True :
                  game_state = 'play'
                  score = 0
                  life = 10
                  ResetFly()
                  ResetSnail()
                  ResetCarrot()
                  
      if game_state == ' ' :
            screen.draw.text('Rabbitto', center = (400,250), color = 'deeppink2', fontsize = 50)
            restart()
      elif game_state == 'win' :
            screen.draw.text('Victory!', center = (400,225), color = 'dodgerblue2', fontsize = 50)
            restart()
      elif game_state == 'game over' :
            screen.draw.text('Defeat!', center = (400,225), color = 'dodgerblue2', fontsize = 50)
            restart()
      elif game_state == 'play' :
            RabbitSprite.draw()
            SnailSprite.draw()
            FlySprite.draw()
            CarrotSprite.draw()
            screen.draw.text('Score : ' + str(score), (15,10), color = 'brown1', fontsize = 40)
            screen.draw.text('Goal : ' + '5', (15,40), color = 'brown1', fontsize = 40)
            screen.draw.text('Life : ' + str(life), (660,10), color = 'brown1', fontsize = 40)


pgzrun.go()
