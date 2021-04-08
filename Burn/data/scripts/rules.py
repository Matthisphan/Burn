import pygame


class Rule:

    def __init__(self, screen):
        self.screen = screen
        self.rule_one = True
        self.rule_two = False

        self.first_rule = pygame.image.load('data/img/rules/first_rules.png')
        self.first_rule_rect = self.first_rule.get_rect()
        self.first_rule_rect.x = 0
        self.first_rule_rect.y = 450

        self.second_rule = pygame.image.load('data/img/rules/second_rules.png')
        self.second_rule_rect = self.first_rule.get_rect()
        self.second_rule_rect.x = 0
        self.second_rule_rect.y = 450

    def blit_first_rule(self):
        self.screen.blit(self.first_rule, (0, 0))

    def blit_second_rule(self):
        self.screen.blit(self.second_rule, (0, 0))

    def first_menu_rule(self):
        self.blit_first_rule()

    def second_menu_rule(self):
        self.blit_second_rule()

    def switch_to_first_rule(self):
        self.rule_one = True
        self.rule_two = False

    def switch_to_second_rule(self):
        self.rule_one = False
        self.rule_two = True

    def leave_rule(self):
        self.rule_one = False
        self.rule_two = False
