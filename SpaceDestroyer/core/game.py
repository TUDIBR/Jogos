import pygame
from pygame import QUIT
import pygame.locals
import settings
import ui.hud
import ui.death_screen
from entities.player import Player
from entities.asteroid import Asteroid
from entities.explosion import Explosion
from entities.enemy import Enemy
# from entities.enemy_bullet import EnemyBullet
from systems import score
from random import randint, choices

# Player object
player = Player()

class Main:
    def __init__(self):
        # Variables
        points = 0
        timer = 0.0
        hp = 1.0
        explosions = []
        death = False
        asteroid_spawn = pygame.USEREVENT + 1
        asteroids = []

        enemy_spawn = pygame.USEREVENT + 2
        enemy_move_event = pygame.USEREVENT + 3
        enemies = []
        
        self.enemies_bullets = []
        enemy_shoot = pygame.USEREVENT + 4

        self.player = player
        self.player.load()
        background = pygame.image.load("assets/images/backgrounds/game_bg.png")
        attack_sound = pygame.mixer.Sound("assets/sounds/attack_sound.mp3")
        attack_sound.set_volume(0.2)
        pygame.key.set_repeat(50, 50)
        pygame.time.set_timer(asteroid_spawn, randint(500, 4000))
        pygame.time.set_timer(enemy_spawn, randint(3000, 5000))
        pygame.time.set_timer(enemy_move_event, randint(3000, 4000))
        pygame.time.set_timer(enemy_shoot, 1000)

        # Main loop
        while settings.running:
            if death == False:
                self.player.shoot_timer -= settings.dt # Decreases cooldown according to the delta
                settings.screen.blit(background, (0, 0)) # Update the background
                timer += 1 * settings.dt


                # Events
                for event in pygame.event.get():
                    if event.type == QUIT: # If the user exits the program turns off
                        settings.running = False
                    
                    # Asteroid spawn
                    if event.type == asteroid_spawn:
                        pygame.time.set_timer(asteroid_spawn, randint(500, 1500))
                        asteroids.append(Asteroid())
                    
                    # Enemy spawn
                    if event.type == enemy_spawn:
                        pygame.time.set_timer(enemy_spawn, randint(3000, 5000))
                        if len(enemies) < 10: # Define the maximum of enemies
                            enemies.append(Enemy())
                
                    # Enemy movement
                    if event.type == enemy_move_event:
                        if len(enemies) != 0:
                            for enemy in choices(enemies, k=randint(1, len(enemies))):
                                enemy.move()
                    
                    # Enemy shoot
                    if event.type == enemy_shoot:
                        if len(enemies) != 0:
                            for enemy in choices(enemies, k=randint(1, len(enemies))):
                                enemy.shoot()

                
                    # Player shoot
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.name(event.key)
                        self.player.move(settings.dt, key)
                        if key in ['f', 'space'] and self.player.shoot_timer <= 0:
                            attack_sound.play()
                            self.player.shoot(self.player.player_collision.centerx, self.player.player_collision.y)
                            self.player.shoot_timer = self.player.shoot_cooldown

                
                # Enemy things
                for enemy in enemies:
                    enemy.update()
                    for i, bullet in enumerate(enemy.bullets):
                        bullet.update(settings.dt)
                        bullet.draw(settings.screen)
                        if bullet.bullet_rect().colliderect(self.player.player_collision) == True:
                            enemy.bullets.pop(i)
                            explosions.append(Explosion(self.player.player_collision.centerx, self.player.player_collision.centery))
                            hp -= 0.09

                    if enemy.enemy_rect.centerx < enemy.random_x:
                        enemy.enemy_rect.move_ip(400 * settings.dt, 0)
                    
                    if enemy.enemy_rect.centerx > enemy.random_x:
                        enemy.enemy_rect.move_ip(-400 * settings.dt, 0)

                    if enemy.enemy_rect.centery < enemy.random_y:
                        enemy.enemy_rect.move_ip(0, 400 * settings.dt)
                    
                    if enemy.enemy_rect.centery > enemy.random_y:
                        enemy.enemy_rect.move_ip(0, -400 * settings.dt)


                # Events of movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    player.move(settings.dt, 'right')
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    player.move(settings.dt, 'left')


                # Update asteroids
                for index, asteroid in enumerate(asteroids[:]):
                    asteroid.update(settings.dt)
                    asteroid.draw()
                    if asteroid.asteroid_rect().y > 750:
                        asteroids.pop(index)


                self.player.update_bullets(settings.dt)
                self.player.draw_bullets(settings.screen)


                # Player collide with asteroid
                if player.player_collision.collidelist(asteroids) != -1:
                    index_asteroids = player.player_collision.collidelist(asteroids)
                    explosions.append(Explosion(asteroids[index_asteroids].rect.centerx, asteroids[index_asteroids].rect.centery))
                    asteroids.pop(player.player_collision.collidelist(asteroids))
                    hp -= 0.06
                

                # Bullet collide with asteroid
                for index_bullet, bullet in enumerate(player.bullets):
                    for index_asteroid, asteroid in enumerate(asteroids):
                        if bullet.bullet_rect().colliderect(asteroid.asteroid_rect()) != False:
                            pos_x = asteroids[index_asteroid].asteroid_rect().centerx
                            pos_y = asteroids[index_asteroid].asteroid_rect().centery
                            explosions.append(Explosion(pos_x, pos_y))
                            player.bullets.pop(index_bullet)
                            asteroids.pop(index_asteroid)
                            points += 50
                            

                
                # Bullet collide with enemy
                for index_bullet, bullet in enumerate(player.bullets[:]):
                    for index_enemy, enemy in enumerate(enemies[:]):
                        if bullet.bullet_rect().colliderect(enemy.enemy_rect) != False:
                            pos_x = enemies[index_enemy].enemy_rect.centerx
                            pos_y = enemies[index_enemy].enemy_rect.centery
                            explosions.append(Explosion(pos_x, pos_y))
                            player.bullets.pop(index_bullet)
                            enemies.pop(index_enemy)
                            points += 150

                player_x = player.render()
                
                # Update explosion
                for explosion in explosions[:]:
                    explosion.update(settings.dt)
                    explosion.draw(settings.screen)

                    if explosion.finished == True:
                        explosions.remove(explosion)
                
                # UI
                ui.hud.render_fonts(points, timer)
                ui.hud.draw_life_bar(hp)

                # Player death
                if hp <= 0:
                    death = True
                    
                
                pygame.display.flip()
                settings.dt = settings.clock.tick(60) / 1000
            else:
                for event in pygame.event.get():
                    if event.type == QUIT: # If the user exits the program turns off
                        settings.running = False

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.name(event.key)
                        if key == 'r':
                            points = 0
                            timer = 0.0
                            hp = 1.0
                            explosions = []
                            death = False
                            asteroids = []
                            enemies = []
                            
                            self.enemies_bullets = []

                            self.player = player
                            self.player.load()
                            pygame.time.set_timer(asteroid_spawn, randint(500, 4000))
                            pygame.time.set_timer(enemy_spawn, randint(3000, 5000))
                            pygame.time.set_timer(enemy_move_event, randint(3000, 4000))
                            pygame.time.set_timer(enemy_shoot, 1000)
                        if key == 'm':
                            import os, sys
                            os.execl(sys.executable, sys.executable, *sys.argv)

                values = score.read_score(points, timer)
                score.save_score({'score': values[0], 'survival_time_record': values[1]})
                ui.death_screen.init()
                pygame.display.flip()
                settings.dt = settings.clock.tick(10) / 1000
        pygame.quit()
