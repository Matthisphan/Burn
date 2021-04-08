import pygame
from data.scripts.game import Game
from data.scripts.menu import Menu
from data.scripts.rules import Rule


pygame.init()

pygame.display.set_caption("Burn")
screen = pygame.display.set_mode((800, 450))

clock = pygame.time.Clock()

frame_rate = 60
frame_count = 0
start_time = 90

font = pygame.font.Font("data/font/ARCADE.TTF", 25)

menu = Menu(screen)
game = Game(screen)
rules = Rule(screen)
rule_count = 0


running = True

while running:
    #print (rule_count)
    #print (pygame.mouse.get_pos())
    menu.blit_main_background()


    if game.is_playing:
        game.update()



        total_seconds = frame_count // frame_rate

        minutes = total_seconds // 60
        seconds = total_seconds % 60

        output_string = "{0:02}:{1:02}".format(minutes, seconds)

        text = font.render(output_string, True, (0, 0, 0))
        screen.blit(text, (350, 0))

        frame_count += 1

    elif menu.main_menu:
        menu.blit_main_menu()

    elif menu.second_menu:
        menu.blit_second_menu()

        if menu.second_background_left_rect.collidepoint(pygame.mouse.get_pos()):
            menu.blit_second_background_left()
            menu.blit_solo_button()


        elif menu.second_background_right_rect.collidepoint(pygame.mouse.get_pos()):
            menu.blit_second_background_right()
            menu.blit_one_vs_one_button()


    elif rules.rule_one:
        rules.blit_first_rule()
        if rule_count == 1:
            rules.switch_to_second_rule()

    elif rules.rule_two:
        rules.blit_second_rule()
        if rule_count == 2:
            rules.leave_rule()
            menu.switch_to_main_menu()



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if menu.main_menu == False:
                rule_count += 1


            if menu.play_button_rect.collidepoint(event.pos):
                menu.switch_to_second_menu()

            elif menu.solo_button_rect.collidepoint(event.pos):
                frame_count = 0
                game.start()
                menu.switch_to_main_menu()

            elif menu.one_vs_one_button_rect.collidepoint(event.pos):
                print("comming soon")

            elif menu.rules_button_rect.collidepoint(event.pos):
                menu.leave_menu()
                rule_count = 0
                rules.switch_to_first_rule()


            elif menu.quit_button_rect.collidepoint(event.pos):
                running = False

    clock.tick(frame_rate)

    pygame.display.flip()


pygame.quit()

