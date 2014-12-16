import pygame
from pygame.locals import *
from random import randrange
import math


class Ball(object):

    def __init__(self, radius, color, pos, speed=(100,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.color = color

    def bounce_player(self):
        self.vx = abs(self.vx) # bounce ball back
        
    def move(self, delta_t, display, player):
        global score, game_over
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t

        # make ball bounce if hitting wall
        if self.x < self.radius:
            self.vx = abs(self.vx)
            game_over = True # game over when ball hits left wall
        if self.y < self.radius:
            self.vy = abs(self.vy)
        if self.x > display.get_width()-self.radius:
            self.vx = -abs(self.vx)
        if self.y > display.get_height()-self.radius:
            self.vy = -abs(self.vy)

    def render(self, surface):
        pos = (int(self.x),int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

#########################################
class Player(object):

    THICKNESS = 10

    def __init__(self, x, y, color, width=100):
        self.width = width
        self.y = y
        self.x = x
        self.color = color
        self.radius = 20

    # def can_hit(self, ball):
    #     return self.y-self.width/2.0 < ball.y < self.y+self.width/2.0 \
    #         and ball.x-ball.radius < self.THICKNESS

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5
    def move_right(self):
        self.x += 5
    def move_left(self):
        self.x -= 5

    def render(self, surface):
        self.pos = (self.x,self.y)
        pygame.draw.circle(surface, self.color, self.pos, self.radius, 0)
    def gravity(self,Hole):
        self.x += (int(math.floor(self.x -Hole.x)))
    def hit(self,Hole):
        return 50 >= math.pow(math.pow((self.x-Hole.x),2)+math.pow((self.y-Hole.y),2),0.5)
    def reach(self,Exit):
        return 50 >= math.pow(math.pow((self.x-Exit.x),2)+math.pow((self.y-Exit.y),2),0.5)


###############################################
class Hole(object):
    def __init__(self, i, color):
        self.radius = 30
        self.color = color
        #self.x = randrange(30,470)
        self.x = randrange(60,470)
        self.y = randrange(60,470)
        while(self.x <370 and self.x >270 and self.y<290 and self.y>190):
            self.x = randrange(60,470)
            self.y = randrange(60,470)
    def draw(self, surface):
        pos = (int(self.x),int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

###############################################
class Exit(object):
    def __init__(self):
        self.radius = 30
        self.color = pygame.Color("red")
        self.x = 640
        self.y = 480
    def draw(self, surface):
        self.pos = (int(self.x),int(self.y))
        pygame.draw.circle(surface, self.color, self.pos, self.radius, 0)