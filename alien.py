import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting positiong"""
        super().__init__()
        self.screen = ai_game
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/ship_mario.bmp")
        self.rect = self.image.get_rect()
        # Star a new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store  the alien's exact horizontal position.
        self.x = float(self.rect.x)
        
