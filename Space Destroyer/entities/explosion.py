import pygame
from settings import screen

class Explosion:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.radius = 0
        self.max_radius = 40
        self.growing = True
        self.finished = False
        self.alpha = 255

    def update(self, dt):
        if self.growing:
            self.radius += 100 * dt
            self.alpha -= 300 * dt
            if self.radius >= self.max_radius:
                self.growing = False
                self.finished = True  # marca como finalizada
        else:
            self.finished = True

    def draw(self, surface):
        if not self.finished:
            surf = pygame.Surface((self.max_radius * 2, self.max_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (255, 165, 0, max(0, int(self.alpha))), (self.max_radius, self.max_radius), int(self.radius))
            surface.blit(surf, (self.x - self.max_radius, self.y - self.max_radius))
