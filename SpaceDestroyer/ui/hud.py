import settings
import pygame

# Carrega a fonte usada no Score do jogo
font = pygame.font.Font("assets/fonts/gomarice_no_continue.ttf", 40)

POSITION_TEXTS_SCORE = (25, 25)
COLOR_TEXTS_SCORE = (1, 255, 213)

POSITION_TEXT_LIFE = (700, 600)
COLOR_TEXT_LIFE = (44, 255, 75)


def render_fonts(points, secs, life=3):
    points_text = font.render(f"Points: {points}", True, COLOR_TEXTS_SCORE)
    settings.screen.blit(points_text, POSITION_TEXTS_SCORE)

    seconds_text = font.render(f"{secs:.1f}", True, COLOR_TEXTS_SCORE)
    settings.screen.blit(seconds_text, (POSITION_TEXTS_SCORE[0], POSITION_TEXTS_SCORE[1] + 50))
    

def draw_life_bar(total_life):
    pygame.draw.rect(settings.screen, 'green', ((570, 630), (total_life*250, 25)))
    pygame.draw.rect(settings.screen, 'white', ((570, 630), (250, 25)), 5)