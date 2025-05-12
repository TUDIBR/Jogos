import pygame

class Bullet:
    WIDTH = 10 # Largura da bala
    HEIGHT = 20 # Altura da bala
    SPEED = 600  # Velocidade da bala

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        self.color = (255, 0, 0)

    def update(self, dt):
        self.rect.y -= self.SPEED * dt

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0, 100)

    def is_off_screen(self):
        return self.rect.bottom < 0
    
    def bullet_rect(self):
        return self.rect
