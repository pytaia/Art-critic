import pygame
from data.elements import *

def create_the_room_window(width, length, number):  # str, str, int
    pygame.init()
    size = window_width, window_height = 900, 500
    screen = pygame.display.set_mode(size)
    font1 = pygame.font.SysFont("arialblack", 27)
    font2 = pygame.font.SysFont("arialblack", 22)
    font3 = pygame.font.SysFont("arial", 22)
    font4 = pygame.font.SysFont('arialblack', 13)
    font5 = pygame.font.SysFont("arialblack", 20)

    crashed = False
    active3 = False

    create_picture = False
    create_spawn = False
    done_active = False
    ask_size = False

    background_rect = pygame.Rect(0, 0, 500, 500)
    vertical_line2 = pygame.Rect(500, 0, 1, 500)
    horizontal_line = pygame.Rect(580, 70, 320, 3)
    horizontal_line2 = pygame.Rect(0, 350, 500, 1)
    create_a_picture_button = pygame.Rect(570, 120, 240, 75)
    bck_picture_btn = pygame.Rect(568, 118, 244, 79)
    create_a_spawn_button = pygame.Rect(570, 220, 270, 90)
    bck_spawn_btn = pygame.Rect(568, 218, 274, 94)
    square1 = pygame.Rect(590, 140, 40, 40)
    square2 = pygame.Rect(590, 240, 40, 40)
    plus1 = pygame.Rect(607, 145, 5, 30)
    plus2 = pygame.Rect(595, 157, 30, 5)
    done_button = pygame.Rect(570, 380, 200, 50)
    bck_done_btn = pygame.Rect(568, 378, 204, 54)
    input_box3 = pygame.Rect(320, 388, 20, 20)
    add_button = pygame.Rect(70, 425, 150, 30)
    background_rect2 = pygame.Rect(0, 350, 500, 150)

    text3 = ""
    error_text2 = ""

    add_a_picture_label1 = font5.render("Добавить", True, "#000000")
    add_a_picture_label2 = font5.render("картину", True, "#000000")
    room_name_label = font1.render("Комната" + str(number), True, "black")
    add_a_spawn_label1 = font5.render("Добавить точку", True, "#000000")
    add_a_spawn_label2 = font5.render("начала", True, "#000000")
    add_a_spawn_label3 = font5.render("маршрута", True, "#000000")
    done_label = font5.render("Завершить", True, "#000000")
    size_label = font2.render("Размер картины:", True, "black")
    add_label = font3.render("Добавить", True, "white")

    my_event = pygame.USEREVENT + 1
    pygame.time.set_timer(my_event, 1)

    if int(width) >= int(length):
        the_room = pygame.Rect(100, int((500 - int((300 * int(length)) / int(width))) / 2) - 65, 300,
                               int((300 * int(length)) / int(width)))
        rect_x = 100
        rect_y = int((500 - int((300 * int(length)) / int(width))) / 2) - 65
        rect_width = 300
        rect_length = int((300 * int(length)) / int(width))
    else:
        the_room = pygame.Rect(int((500 - int((300 * int(width)) / int(length))) / 2), 35,
                               int((300 * int(width)) / int(length)), 300)
        rect_x = int((500 - int((300 * int(width)) / int(length))) / 2)
        rect_y = 100 - 65
        rect_width = int((300 * int(width)) / int(length))
        rect_length = 300

        room_name = "Комната #" + str(number)
        room_name_label = font1.render(room_name, True, "black")
        new_room = [number, (int(width), int(length))]
        new_pictures = []
        current_picture = []
        current_spawn = []

    while not crashed:
        screen.fill("white")
        pygame.display.set_caption("Создать комнату")

        if create_picture:
            pygame.draw.rect(screen, "black", bck_picture_btn)
        if create_spawn:
            pygame.draw.rect(screen, "black", bck_spawn_btn)
        if done_active:
            pygame.draw.rect(screen, "black", bck_done_btn)

        pygame.draw.rect(screen, "#FAFAFA", background_rect)
        pygame.draw.rect(screen, "black", vertical_line2)
        pygame.draw.rect(screen, "black", the_room, 3)
        pygame.draw.rect(screen, "#F8F7F7", create_a_picture_button)
        pygame.draw.rect(screen, "#F8F7F7", create_a_spawn_button)
        pygame.draw.rect(screen, "#B9B8B8", square1)
        pygame.draw.rect(screen, "#B9B8B8", square2)
        pygame.draw.rect(screen, "#FFFFFF", plus1)
        pygame.draw.rect(screen, "#FFFFFF", plus2)
        pygame.draw.rect(screen, "black", horizontal_line)
        pygame.draw.polygon(screen, "white", [[597, 250], [600, 247], [621, 268], [618, 272]])
        pygame.draw.polygon(screen, "white", [[597, 268], [618, 247], [621, 250], [600, 272]])
        pygame.draw.rect(screen, "#F6F6F6", done_button)

        for i in range(len(new_pictures)):
            pygame.draw.circle(screen, "blue", new_pictures[i][1], 10)

        if len(current_picture) > 0:
            pygame.draw.circle(screen, "pink", current_picture[1], 10)
            screen.blit(size_label, (70, 380))
            txt_surface1 = font4.render(text3, True, "black")

            width3 = 100
            input_box3.w = width3
            screen.blit(txt_surface1, (input_box3.x + 5, input_box3.y - 1))

            pygame.draw.rect(screen, color3, input_box3, 2)
            pygame.draw.rect(screen, "#707070", add_button)
            pygame.draw.rect(screen, "black", horizontal_line2)

            screen.blit(add_label, (80, 428))

        if len(current_spawn) > 0:
            pygame.draw.circle(screen, "black", current_spawn[0], 5, 2)

        pictures = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if create_a_picture_button.collidepoint((x, y)):
                    create_picture = True
                    create_spawn = False
                    current_picture = []
                elif create_a_spawn_button.collidepoint((x, y)):
                    create_spawn = True
                    create_picture = False
                    current_picture = []
                elif background_rect.collidepoint((x, y)):
                    if len(current_picture) > 0:
                        if not background_rect2.collidepoint((x, y)):
                            if create_picture:
                                current_picture = []
                                current_picture.append(len(new_pictures) + 1)
                                current_picture.append((xx, yy))
                                ask_size = True
                            elif create_spawn:
                                current_spawn = []
                                current_spawn.append((xx, yy))
                    else:
                        if create_picture:
                            current_picture = []
                            current_picture.append(len(new_pictures) + 1)
                            current_picture.append((xx, yy))
                            ask_size = True
                        elif create_spawn:
                            current_spawn = []
                            current_spawn.append((xx, yy))
                else:
                    create_spawn = False
                    create_picture = False
                if input_box3.collidepoint((x, y)):
                    color3 = "pink"
                    active3 = True
                else:
                    color3 = "black"
                    active3 = False
                if add_button.collidepoint((x, y)):
                    if text3 == '':
                        error_text2 = "Введите длину картины"
                    else:
                        new_pictures.append([len(new_pictures) + 1, current_picture[1], int(text3)])
                        create_picture = False
                        current_picture = []
                        text3 = ""
                else:
                    error_text2 = ""
                if done_button.collidepoint((x, y)):
                    print(str(number), width + "," + length, new_pictures)
                    create_room((number), width + "," + length, new_pictures)
                    text3 = ""
                    pygame.quit()
                    crashed = True
                    break

            if event.type == my_event:
                x, y = pygame.mouse.get_pos()
                if done_button.collidepoint((x, y)):
                    done_active = True
                else:
                    done_active = False
                if background_rect.collidepoint((x, y)):
                    if create_picture:
                        if x <= rect_x:
                            xx = rect_x
                        elif rect_x < x < rect_x + rect_width:
                            if y - rect_y <= rect_length / 2:
                                xx = x
                                yy = rect_y
                            else:
                                xx = x
                                yy = rect_y + rect_length
                        else:
                            xx = rect_x + rect_width
                        if y <= rect_y:
                            yy = rect_y
                        elif rect_y < y < rect_y + rect_length:
                            if x - rect_x <= rect_width / 2:
                                yy = y
                                xx = rect_x
                            else:
                                yy = y
                                xx = rect_x + rect_width
                        else:
                            yy = rect_y + rect_length
                        pygame.draw.circle(screen, "#E76E6E", (xx, yy), 9)
                    elif create_spawn:
                        if x <= rect_x:
                            xx = rect_x
                        elif rect_x < x < rect_x + rect_width:
                            xx = x
                        else:
                            xx = rect_x + rect_width
                        if y <= rect_y:
                            yy = rect_y
                        elif rect_y < y < rect_y + rect_length:
                            yy = y
                        else:
                            yy = rect_y + rect_length
                        pygame.draw.circle(screen, "black", (xx, yy), 4, 4)
            if event.type == pygame.KEYDOWN:
                if active3:
                    if event.key == pygame.K_RETURN:
                        text3 = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text3 = text3[:-1]
                    else:
                        if len(text3) < 8:
                            if event.unicode.isdigit():
                                text3 += event.unicode

        screen.blit(add_a_picture_label1, (650, 130))
        screen.blit(add_a_picture_label2, (650, 158))
        screen.blit(room_name_label, (580, 37))
        screen.blit(add_a_spawn_label1, (650, 225))
        screen.blit(add_a_spawn_label2, (650, 250))
        screen.blit(add_a_spawn_label3, (650, 275))
        screen.blit(done_label, (610, 390))

        error_label2 = font4.render(error_text2, True, "red")
        screen.blit(error_label2, (570, 480))

        pygame.display.update()


create_the_room_window("400", "1200", 5)
