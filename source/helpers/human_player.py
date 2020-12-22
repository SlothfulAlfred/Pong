from .player import Player
import pygame

class HumanPlayer(Player):
    """ A player controlled by user inputs
    
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.vector = 0

    def move(self, event):
        ''' Moves the player if input is given '''
        if event.key == pygame.K_UP:
            self.vector = -0.4
        elif event.key == pygame.K_DOWN:
            self.vector = 0.4

    def stop(self):
        self.vector = 0






