import pygame
from pygame.locals import *
import time
import gamelib
from elements import *

class SquashGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    millis = int(round(time.time() * 1000))
    
    def __init__(self):
        super(SquashGame, self).__init__('Squash', SquashGame.BLACK)
         # self.ball = Ball(radius=10,
         #                 color=SquashGame.WHITE,
         #                 pos=(self.window_size[0]/2,
         #                      self.window_size[1]/2),
         #                 speed=(200,50))
        self.player = Player(x=320,y=240 ,color=SquashGame.GREEN)
        self.holes = []
        for i in range(9):
            x = Hole(i,SquashGame.WHITE)
            self.holes.append(x)
        self.Exit = Exit()
        # self.score = 0


    def init(self):
        super(SquashGame, self).init()

    def update(self):
        # self.ball.move(1./self.fps, self.surface, self.player)

        if self.is_key_pressed(K_UP):
            self.player.move_up()
        if self.is_key_pressed(K_DOWN):
            self.player.move_down()
        if self.is_key_pressed(K_RIGHT):
            self.player.move_right()
        if self.is_key_pressed(K_LEFT):
            self.player.move_left()
        for i in range(9):
            if(self.player.hit(self.holes[i])):
                self.is_terminated = True
        if(self.player.reach(self.Exit)):
            self.player = Player(x=320,y=240 ,color=SquashGame.GREEN)
            self.holes = []
            for i in range(9):
                x = Hole(i,SquashGame.WHITE)
                self.holes.append(x)
        
        # if self.player.can_hit(self.ball):
        #     self.score += 1
        #     self.ball.bounce_player()

    def render(self, surface):
        # self.ball.render(surface)
        # if(SquashGame.millis % 10 == 0):
        #     self.player.gravity(self.holes[1])
        self.player.render(surface)
        for i in range(9):
            self.holes[i].draw(surface)
        self.Exit.draw(surface)

def main():
    game = SquashGame()
    game.run()

if __name__ == '__main__':
    main()