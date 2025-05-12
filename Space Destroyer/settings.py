import pygame
from pygame.time import Clock
from pygame.display import set_mode, set_caption


pygame.init()

WIDTH, HEIGHT = 850, 720
screen = set_mode((WIDTH, HEIGHT))
screen_ds = set_mode((WIDTH, HEIGHT))
set_caption('Space Destroyer Game', '')
clock = Clock()
running = True
dt = 0