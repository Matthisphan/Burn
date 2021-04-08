import pygame
from random import randint


class Fireball(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game

        self.spriteSheet = pygame.image.load("data/img/sprites/fire_ball.png").convert_alpha()
        self.image = self.spriteSheet.subsurface(pygame.Rect(1, 1, 63, 63))
        self.rect = pygame.Rect(1, 1, 63, 63)
        self.rect.x = randint(63, 737)
        self.rect.y = 0 - randint(0, 100)

        self.sequences = [(0, 6, True)]
        self.sequence_number = 0
        self.image_number = 0
        self.flip = False

        self.delta_time = 0
        self.speed = 6

        self.attack = 1

    def animation_update(self, time):
        self.delta_time += time

        if self.delta_time >= 200:
            self.delta_time = 0

            n = self.sequences[self.sequence_number][0] + self.image_number
            self.image = self.spriteSheet.subsurface(pygame.Rect((n % 10 * 64) + 1, (n // 10 * 64) + 1, 63, 63))

            if self.flip:
                self.image = pygame.transform.flip(self.image, True, False)

            self.image_number += 1

            if self.image_number == self.sequences[self.sequence_number][1]:
                if self.sequences[self.sequence_number][2]:
                    self.image_number = 0
                else:
                    self.image_number -= 1

    def set_sequence(self, n):
        if self.sequence_number != n:
            self.image_number = 0
            self.sequence_number = n

    def fall(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect = self.rect.move(0, self.speed)
            self.set_sequence(0)
            if self.rect.y > 346:
                self.rect.y = 0 - randint(0, 100)
                self.rect.x = randint(0, 737)
        else:
            self.rect.x = randint(63, 737)
            self.rect.y = 0 - randint(0, 100)
            self.game.J1.damage(self.attack)
