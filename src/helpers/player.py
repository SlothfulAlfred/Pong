import pygame
import math 

pygame.mixer.init()
pong_channel = pygame.mixer.Channel(2)
blip = pygame.mixer.Sound('./assets/New Pong Sound Effect.mp3')

class Player():
    """ 
    Abstract Player Class
    Attributes
    -----------------
    x: float
        the x position
    y: float
        the y position
    
    Methods
    ------------
    getPos() -> tuple
        returns the coordinates of the character
    draw(screen: pygame.display) -> None
        places the character on the screen
    """

    def __init__(self, x, y):
        '''
        parameters:
        x: int
            x position on the screen
        y: int
            y position on the screen
        '''
        self.x = x
        self.y = y
        self.img = pygame.image.load('assets/pongChar.jpg')
    
    def getPos(self) -> tuple:
        return self.x, self.y

    def draw(self, screen) -> None:
        '''
        places the character on the screen

        params:
        screen: pygame.display
            the surface that the character will be drawn on
        '''
        screen.blit(self.img, (self.getPos()))
        return

    def isCollision(self, ball):
        '''
        checks to see if the ball has collided with the ball
        '''
        if (ball.y < self.y + 100) and (ball.y - 14 > self.y + 1):
            ball.hBounce()
            if ball.hit == False:
                ball.vector[0] *= 3
                ball.vector[1] *= 3
                ball.hit = True
            pong_channel.play(blip)
            return True
        return False

    def bound(self):
        if self.y > 500:
            self.y = 500
        elif self.y < 0:
            self.y = 0



