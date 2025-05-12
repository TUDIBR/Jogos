import pygame
import settings

font = pygame.font.Font("assets/fonts/gomarice_no_continue.ttf", 40)

POSITION_TEXT = (30, 350)
COLOR = (190, 0, 0)

def init():
    points_text = font.render('You died, press "R" to restart or "M" for menu', True, COLOR)
    settings.screen.blit(points_text, POSITION_TEXT)