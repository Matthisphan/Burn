import pygame


class J1(pygame.sprite.Sprite):
    """
    On crée une instance pour le J1
    """
    def __init__(self, game):
        """
        On initialise la class

        Parameters
        game
        """
        super().__init__()
        self.game = game
        self.max_health = 3
        self.health = self.max_health

        self.three_hearts = pygame.image.load("data/img/life/lifeJ1_1.png")
        self.two_hearts = pygame.image.load("data/img/life/lifeJ1_2.png")
        self.one_heart = pygame.image.load("data/img/life/lifeJ1_3.png")

        self.spriteSheet = pygame.image.load("data/img/sprites/J1.png").convert_alpha()
        self.image = self.spriteSheet.subsurface(pygame.Rect(1, 1, 63, 63))
        self.rect = pygame.Rect(1, 1, 63, 63)
        self.rect.x = 368
        self.rect.y = 344

        self.sequences = [(0, 2, True), (2, 6, True)]
        self.sequence_number = 0
        self.image_number = 0
        self.flip = False

        self.delta_time = 0
        self.speed = 4

    def animation_update(self, time):
        """
        On update les animations du joueurs lors de son déplacement tous les
        time secondes

        Parameters
        time : int
            temps entre chaque animation
        """
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
        """
        On met la sequence d'animation du J1 demandée

        Parameters
        n : int
            numéro de la séquence
        """
        if self.sequence_number != n:
            self.image_number = 0
            self.sequence_number = n

    def move_right(self):
        """
        On définit le mouvement du J1 vers la droite
        """
        self.rect = self.rect.move(self.speed, 0)
        self.flip = False
        self.set_sequence(1)

    def move_left(self):
        """
        On définit le mouvement du J1 vers la gauche
        """
        self.rect = self.rect.move(-self.speed, 0)
        self.flip = True
        self.set_sequence(1)

    def damage(self, amount):
        """
        On définit le faite que le J1 prend des dégats

        Parameters
        amount : int
            le J1 prend amount dégats
        """
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def life_update(self, screen):
        """
        On update en continue les images représentant la vie du J1 pour
        afficher 1, 2 ou 3 coeurs

        Parameters
        screen : surface
            surface sur laquelle on affiche la vie du J1
        """
        if self.health == 3:
            screen.blit(self.three_hearts, (0, 408))

        elif self.health == 2:
            screen.blit(self.two_hearts, (0, 408))

        elif self.health == 1:
            screen.blit(self.one_heart, (0, 408))
