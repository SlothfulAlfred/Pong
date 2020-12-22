from .player import Player
import pygame
import math

class ComputerPlayer(Player):
    """ 
    A computer player that plays automatically
    Attributes
    ------------------
    speed: int
        the movement speed of the character
    """

    def __init__(self, x, y, diff='easy'):
        super().__init__(x, y)
        # sets the movement speed depending on the set difficulty 
        self.diff = diff
        if self.diff == 'easy':
            self.speed = 0.15
        elif self.diff == 'medium':
            self.speed = 0.2
        elif self.diff == 'hard':
            self.speed = 0.3

    def move(self, ball):
        if self.diff == 'easy':
            if math.fabs(self.x - ball.x) > 200:
                return
        elif self.diff == 'medium':
            if math.fabs(self.x - ball.x) > 300:
                return
        elif self.diff == 'hard':
            if math.fabs(self.x - ball.x) > 400:
                return
        if self.y + 50 < ball.y - 13:
            self.y += self.speed
        elif self.y + 50 > ball.y: 
            self.y -= self.speed
        self.bound()





