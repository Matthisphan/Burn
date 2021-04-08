import pygame
from data.scripts.player import J1
from data.scripts.fireball import Fireball
from data.scripts.menu import Menu


class Game:

    def __init__(self, screen):
        self.screen = screen

        self.menu = Menu(self.screen)

        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        self.J1 = J1(self)
        self.all_players.add(self.J1)

        self.all_fire_ball = pygame.sprite.Group()

        self.pressed = {}

    def start(self):
        self.is_playing = True
        for fire in range(10):
            pygame.time.wait(50)
            self.spawn_fire_ball()


    def game_over(self):
        self.all_fire_ball = pygame.sprite.Group()
        self.J1.health = self.J1.max_health
        self.is_playing = False
        self.J1.rect.x = 368

    def spawn_fire_ball(self):
        fire_ball = Fireball(self)
        self.all_fire_ball.add(fire_ball)

    def update(self):
        self.screen.blit(self.J1.image, self.J1.rect)

        for fire_ball in self.all_fire_ball:
            fire_ball.fall()
            fire_ball.animation_update(15)

        if self.pressed.get(pygame.K_RIGHT) and self.J1.rect.x + self.J1.rect.width < self.screen.get_width():
            self.J1.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.J1.rect.x > 0:
            self.J1.move_left()

        else:
            self.J1.set_sequence(0)

        self.all_fire_ball.draw(self.screen)
        self.J1.animation_update(15)
        self.J1.life_update(self.screen)

    @staticmethod
    def check_collision(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
