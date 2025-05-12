import settings
import pygame
from entities.enemy_bullet import EnemyBullet
from random import randint


class Enemy():
    def __init__(self):
        self.draw()
        self.random_x = randint(0, 820)
        self.random_y = randint(0, 200)
        self.bullets = []
    
    
    def shoot(self):
        self.bullets.append(EnemyBullet(self.enemy_rect.centerx, self.enemy_rect.y))
    

    def move(self):
        self.random_x = randint(0, 820)
        self.random_y = randint(0, 200)


    def draw(self):
        self.enemy_sprite = pygame.image.load("assets/images/sprites/enemy_lv1.png").convert_alpha()
        self.enemy_sprite = pygame.transform.scale(self.enemy_sprite, (60, 60))
        self.enemy_sprite = pygame.transform.rotate(self.enemy_sprite, 180)
        self.enemy_rect = self.enemy_sprite.get_rect()
        self.enemy_rect.centerx = 410
        self.enemy_rect.centery = -50


    def update(self):
        settings.screen.blit(self.enemy_sprite, self.enemy_rect)
    