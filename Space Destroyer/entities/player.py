import pygame
from settings import screen
from entities.bullet import Bullet


class Player():
    def __init__(self):
        self.load()
        self.bullets = []
        self.shoot_cooldown = 0.3  # cooldown entre tiros
        self.shoot_timer = 0

    def load(self) -> None:
        PLAYER_START_POSITION = (380, 620)
        self.player_sprite = pygame.image.load("assets/images/sprites/player.png").convert_alpha()
        self.player_sprite = pygame.transform.scale(self.player_sprite, (65, 65))
        self.player_collision = self.player_sprite.get_rect()
        self.player_collision.topleft = PLAYER_START_POSITION

    def render(self) -> None:
        screen.blit(self.player_sprite, self.player_collision)
        return self.player_collision.x

    def move(self, delta, key) -> None:
        if key == 'right' or key == 'd':
            if self.player_collision.right < 800:
                self.player_collision.move_ip(800 * delta, 0)
        elif key == 'left' or key == 'a':
            if self.player_collision.left > 50:
                self.player_collision.move_ip(-800 * delta, 0)

    def shoot(self, player_x, player_y):
        bullet_x = player_x  # centraliza a bala no meio da nave
        bullet_y = player_y
        self.bullets.append(Bullet(bullet_x, bullet_y))

    def update_bullets(self, dt):
        for bullet in self.bullets[:]:
            bullet.update(dt)
            if bullet.is_off_screen():
                self.bullets.remove(bullet)

    def draw_bullets(self, surface):
        for bullet in self.bullets:
            bullet.draw(surface)