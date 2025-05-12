import pygame
import settings
from random import randint

# asteroid.py
class Asteroid():
    SIZE = (70, 70)
    SPEED = 400
    
    def __init__(self):
        self.image = pygame.image.load("assets/images/sprites/asteroid.png")
        self.image = pygame.transform.scale(self.image, self.SIZE)
        self.rect = self.image.get_rect(topleft=(randint(5, 795), 0))

    def update(self, dt: float):
        self.rect.y += self.SPEED * dt

    def draw(self):
        settings.screen.blit(self.image, self.rect)

    def asteroid_rect(self):
        return self.rect