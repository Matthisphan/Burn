import pygame


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.main_menu = True
        self.second_menu = False

        self.title = pygame.image.load("data/img/main_menu/title.png")
        self.title_rect = self.title.get_rect()
        self.title_rect.x = (800 // 2) - (130 // 2)
        self.title_rect.y = (450 // 8)

        self.play_button = pygame.image.load("data/img/main_menu/play.png")
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = (800 // 2) - (91 // 2)
        self.play_button_rect.y = self.title_rect.y + 150

        self.rules_button = pygame.image.load("data/img/main_menu/rules.png")
        self.rules_button_rect = self.rules_button.get_rect()
        self.rules_button_rect.x = (800 // 2) - (129 // 2)
        self.rules_button_rect.y = self.play_button_rect.y + 50

        self.quit_button = pygame.image.load("data/img/main_menu/quit.png")
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.x = (800 // 2) - (134 // 2)
        self.quit_button_rect.y = self.rules_button_rect.y + 50

        self.solo_button = pygame.image.load('data/img/second_menu/solo.png')
        self.solo_button_rect = self.solo_button.get_rect()
        self.solo_button_rect.x = 150
        self.solo_button_rect.y = 350

        self.one_vs_one_button = pygame.image.load('data/img/second_menu/1vs1.png')
        self.one_vs_one_button_rect = self.one_vs_one_button.get_rect()
        self.one_vs_one_button_rect.x = 550
        self.one_vs_one_button_rect.y = 350

        self.background_left = pygame.image.load("data/img/background/background_left.png")
        self.background_left_rect = self.background_left.get_rect()
        self.background_left_rect.x = 0

        self.background_right = pygame.image.load("data/img/background/background_right.png")
        self.background_right_rect = self.background_right.get_rect()
        self.background_right_rect.x = 400

        self.second_background = pygame.image.load("data/img/background/second_background.png")

        self.second_background_left = pygame.image.load("data/img/background/second_background_left.png")
        self.second_background_left_rect = self.second_background_left.get_rect()
        self.second_background_left_rect.x = 0

        self.second_background_right = pygame.image.load("data/img/background/second_background_right.png")
        self.second_background_right_rect = self.second_background_right.get_rect()
        self.second_background_right_rect.x = 400

    def blit_main_background(self):
        self.screen.blit(self.background_left, self.background_left_rect)
        self.screen.blit(self.background_right, self.background_right_rect)

    def blit_title_button(self):
        self.screen.blit(self.title, self.title_rect)

    def blit_play_button(self):
        self.screen.blit(self.play_button, self.play_button_rect)

    def blit_rules_button(self):
        self.screen.blit(self.rules_button, self.rules_button_rect)

    def blit_quit_button(self):
        self.screen.blit(self.quit_button, self.quit_button_rect)

    def blit_main_menu(self):
        self.blit_main_background()
        self.blit_title_button()
        self.blit_play_button()
        self.blit_rules_button()
        self.blit_quit_button()

    def blit_second_background(self):
        self.screen.blit(self.second_background, (0, 0))

    def blit_second_background_left(self):
        self.screen.blit(self.second_background_left, self.second_background_left_rect)

    def blit_second_background_right(self):
        self.screen.blit(self.second_background_right, self.second_background_right_rect)

    def blit_solo_button(self):
        self.screen.blit(self.solo_button, self.solo_button_rect)

    def blit_one_vs_one_button(self):
        self.screen.blit(self.one_vs_one_button, self.one_vs_one_button_rect)

    def blit_second_menu(self):
        self.blit_second_background()
        self.blit_solo_button()
        self.blit_one_vs_one_button()

    def blit_second_menu_button(self):
        self.blit_solo_button()
        self.blit_one_vs_one_button()

    def switch_to_main_menu(self):
        self.main_menu = True
        self.second_menu = False

    def switch_to_second_menu(self):
        self.main_menu = False
        self.second_menu = True

    def leave_menu(self):
        self.main_menu = False
        self.second_menu = False