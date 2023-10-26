import sys
import pygame
import time
# from ... import room_data, picture_data

if __name__ == '__main__':
    pygame.init()
    size = window_width, window_height = 900, 500
    screen = pygame.display.set_mode(size)
    font1 = pygame.font.SysFont("arialblack", 27)
    font2 = pygame.font.SysFont("arialblack", 22)
    font3 = pygame.font.SysFont("arial", 22)
    font4 = pygame.font.SysFont('arialblack', 13)

    clock = pygame.time.Clock()

    MAIN_MENU = True
    NEW_ROOM = False

    crashed = False
    active1 = False
    active2 = False

    new_room_button = pygame.Rect(70, 140, 200, 40)
    new_room_button2 = pygame.Rect(70, 260, 200, 40)
    vertical_line = pygame.Rect(320, 50, 2, 400)
    quit_button = pygame.Rect(70, 400, 70, 30)
    input_box1 = pygame.Rect(165, 148, 20, 20)
    input_box2 = pygame.Rect(165, 208, 20, 20)
    next_button = pygame.Rect(620, 70, 40, 40)
    previous_button = pygame.Rect(680, 70, 40, 40)

    text1 = ""
    text2 = ""

    create_label = font1.render("Create", True, "black")
    your_label = font1.render("Your rooms", True, "black")
    new_room_label = font2.render("New room", True, "white")
    quit_label = font2.render("QUIT", True, "white")
    width_label = font2.render("Width:", True, "black")
    height_label = font2.render("Height:", True, "black")
    next_label = font1.render(">", True, "black")
    previous_label = font1.render("<", True, "black")

    my_event = pygame.USEREVENT + 1
    pygame.time.set_timer(my_event, 1)

    while not crashed:
        if MAIN_MENU:
            screen.fill("white")
            pygame.display.set_caption("Main menu")
            # display_the_background("background.png", 0, 0)

            pygame.draw.rect(screen, "#959696", new_room_button)
            pygame.draw.rect(screen, "black", vertical_line)
            pygame.draw.rect(screen, "#A35b5b", quit_button)
            pygame.draw.rect(screen, "#F1f1f1", next_button)
            pygame.draw.rect(screen, "#F1f1f1", previous_button)

            buttons = []
            # received_data = room_data()
            received_data = [("Room #1", (200, 400), ((123, (23, 45), 34), (123, (230, 45), 16))),
                             ("Room #2", (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             ("Room #3", (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             ("Room #4", (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             ("Room #5", (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90)))]
            # rooms: [name, size, (pictures)]
            # pictures: (key, (x, y), t)
            y = 140
            if len(received_data) <= 4:
                for i in range(len(received_data)):
                    new_rect = pygame.Rect(400, y, 270, 40)
                    pygame.draw.rect(screen, "gray", new_rect)
                    new_label = font3.render(received_data[i][0], True, "white")
                    screen.blit(new_label, (410, y + 7))
                    y = y + 70

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if quit_button.collidepoint((x, y)):
                        pygame.quit()
                        sys.exit()
                    if new_room_button.collidepoint((x, y)):
                        screen.fill("white")
                        MAIN_MENU = False
                        NEW_ROOM = True
                if event.type == my_event:
                    x, y = pygame.mouse.get_pos()
                    if quit_button.collidepoint((x, y)):
                        pygame.draw.rect(screen, "red", quit_button)
                    if new_room_button.collidepoint((x, y)):
                        pygame.draw.rect(screen, "grey", new_room_button)

            screen.blit(create_label, (70, 70))
            screen.blit(your_label, (400, 70))
            screen.blit(new_room_label, (80, 145))
            screen.blit(quit_label, (74, 398))
            screen.blit(next_label, (691, 70))
            screen.blit(previous_label, (631, 70))

            pygame.display.update()
        if NEW_ROOM:
            screen.fill("white")
            pygame.display.set_caption("Main menu")
            # display_the_background("background.png", 0, 0)

            pygame.draw.rect(screen, "black", vertical_line)
            pygame.draw.rect(screen, "#A35b5b", quit_button)
            pygame.draw.rect(screen, "#959696", new_room_button2)
            pygame.draw.rect(screen, "#F1f1f1", next_button)
            pygame.draw.rect(screen, "#F1f1f1", previous_button)

            txt_surface1 = font4.render(text1, True, "black")
            txt_surface2 = font4.render(text2, True, "black")

            width1 = max(110, txt_surface1.get_width())
            width2 = max(110, txt_surface2.get_width())
            input_box1.w = width1
            input_box2.w = width2

            screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y - 1))
            pygame.draw.rect(screen, "black", input_box1, 2)

            screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y - 1))
            pygame.draw.rect(screen, "black", input_box2, 2)

            buttons = []
            # received_data = room_data()
            received_data = [("Room #1", (200, 400), ((123, (23, 45), 34), (123, (230, 45), 16))),
                             ("Room #2", (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90)))]
            # rooms: [name, size, (pictures)]
            # pictures: (key, (x, y), t)
            y = 140
            for i in range(len(received_data)):
                new_rect = pygame.Rect(400, y, 270, 40)
                pygame.draw.rect(screen, "gray", new_rect)
                new_label = font3.render(received_data[i][0], True, "white")
                screen.blit(new_label, (410, y + 7))
                y = y + 70

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if quit_button.collidepoint((x, y)):
                        pygame.quit()
                        sys.exit()
                    elif input_box1.collidepoint((x, y)):
                        active1 = True
                        active2 = False
                    elif input_box2.collidepoint((x, y)):
                        active2 = True
                        active1 = False
                    else:
                        active1 = False
                        active2 = False
                if event.type == my_event:
                    x, y = pygame.mouse.get_pos()
                    if quit_button.collidepoint((x, y)):
                        pygame.draw.rect(screen, "red", quit_button)
                    if new_room_button2.collidepoint((x, y)):
                        pygame.draw.rect(screen, "grey", new_room_button2)
                if event.type == pygame.KEYDOWN:
                    if active1 or active2:
                        if active1:
                            if event.key == pygame.K_RETURN:
                                text1 = ""
                            elif event.key == pygame.K_BACKSPACE:
                                text1 = text1[:-1]
                            else:
                                text1 += event.unicode
                        if active2:
                            if event.key == pygame.K_RETURN:
                                text2 = ""
                            elif event.key == pygame.K_BACKSPACE:
                                text2 = text2[:-1]
                            else:
                                text2 += event.unicode

            screen.blit(create_label, (70, 70))
            screen.blit(your_label, (400, 70))
            screen.blit(quit_label, (74, 398))
            screen.blit(width_label, (60, 140))
            screen.blit(height_label, (60, 200))
            screen.blit(new_room_label, (80, 263))
            screen.blit(next_label, (691, 70))
            screen.blit(previous_label, (631, 70))

            pygame.display.update()


pygame.quit()
