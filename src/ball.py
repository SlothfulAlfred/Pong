import pygame
import random

class Ball():
    """ A class that stores the ball image, x and y coordinates"""
    def __init__(self, x, y, vector):
        self.img = pygame.image.load('assets/ball.jpg')
        self.x = x
        self.y = y
        self.vector = vector
        self.hit = False

    def getPos(self) -> tuple:
        return self.x, self.y

    def draw(self, screen):
        screen.blit(self.img, self.getPos())

    def move(self):
        self.x += self.vector[0]
        self.y += self.vector[1]
    
    def vBounce(self):
        if self.y > 590 or self.y < 0:
            self.vector[1] *= -1

    def hBounce(self):
        if self.x > 735 or self.x < 55:
            self.vector[0] *= -1

    def reset(self) -> int:
        if self.x > 800 or self.x < 0:
            self.hit = False
            temp = self.x
            self.x = 394
            self.y = 294
            self.vector[0] = random.choice([0.25, -0.25]) / 3
            self.vector[1] = random.choice([0.25, 0.20, 0.15, 0.10, -0.10, -0.15, -0.20, -0.25]) / 3
            if temp > 800:
                return 1
            return 2
        return 0


