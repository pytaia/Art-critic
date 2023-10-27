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
    font5 = pygame.font.SysFont("arialblack", 20)

    clock = pygame.time.Clock()

    MAIN_MENU = True
    NEW_ROOM = False
    CREATE_THE_ROOM = False

    crashed = False
    active1 = False
    active2 = False

    create_picture = False
    create_spawn = False
    done_active = False

    new_room_button = pygame.Rect(70, 140, 220, 40)
    new_room_button2 = pygame.Rect(70, 260, 220, 40)
    vertical_line = pygame.Rect(320, 50, 2, 400)
    quit_button = pygame.Rect(70, 400, 100, 30)
    input_box1 = pygame.Rect(175, 148, 20, 20)
    input_box2 = pygame.Rect(175, 208, 20, 20)
    next_button = pygame.Rect(750, 70, 40, 40)
    previous_button = pygame.Rect(690, 70, 40, 40)

    background_rect = pygame.Rect(0, 0, 500, 500)
    vertical_line2 = pygame.Rect(500, 0, 1, 500)
    horizontal_line = pygame.Rect(580, 70, 320, 3)
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

    text1 = "1200"
    text2 = "400"
    page = 0
    error_text = ""
    room_name = ""

    next_arrow_color = "black"
    previous_arrow_color = "black"
    color1 = "black"
    color2 = "black"

    create_label = font1.render("Создать", True, "black")
    your_label = font1.render("Ваши комнаты:", True, "black")
    new_room_label = font2.render("Новая комната", True, "white")
    quit_label = font2.render("ВЫЙТИ", True, "white")
    width_label = font2.render("Ширина:", True, "black")
    height_label = font2.render("Высота:", True, "black")
    next_label = font1.render(">", True, next_arrow_color)
    previous_label = font1.render("<", True, previous_arrow_color)
    error_label = font4.render(error_text, True, "red")
    sm1_label = font4.render("(см)", True, "black")
    sm2_label = font4.render("(см)", True, "black")

    add_a_picture_label1 = font5.render("Добавить", True, "#000000")
    add_a_picture_label2 = font5.render("картину", True, "#000000")
    room_name_label = font1.render(room_name, True, "black")
    add_a_spawn_label1 = font5.render("Добавить точку", True, "#000000")
    add_a_spawn_label2 = font5.render("начала", True, "#000000")
    add_a_spawn_label3 = font5.render("маршрута", True, "#000000")
    done_label = font5.render("Завершить", True, "#000000")

    my_event = pygame.USEREVENT + 1
    pygame.time.set_timer(my_event, 1)

    while not crashed:
        if MAIN_MENU:
            screen.fill("white")
            pygame.display.set_caption("Меню")
            # display_the_background("background.png", 0, 0)

            next_label = font1.render(">", True, next_arrow_color)
            previous_label = font1.render("<", True, previous_arrow_color)

            pygame.draw.rect(screen, "#959696", new_room_button)
            pygame.draw.rect(screen, "black", vertical_line)
            pygame.draw.rect(screen, "#A35b5b", quit_button)
            pygame.draw.rect(screen, "#F1f1f1", next_button)
            pygame.draw.rect(screen, "#F1f1f1", previous_button)

            buttons = []
            # received_data = room_data()
            received_data = [(1, (200, 400), ((123, (23, 45), 34), (123, (230, 45), 16))),
                             (2, (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             (3, (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             (4, (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             (5, (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90)))]
            # rooms: [name, size, (pictures)]
            # pictures: (key, (x, y), t)
            y = 140
            page_min = 0
            page_max = len(received_data) - 4
            page1 = page * 4

            if page == page_max:
                page2 = len(received_data)
            else:
                page2 = page * 4 + 4

            for i in range(page1, page2):
                new_rect = pygame.Rect(400, y, 270, 40)
                pygame.draw.rect(screen, "gray", new_rect)
                new_label = font3.render("Комната #" + str(received_data[i][0]), True, "white")
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
                    if next_button.collidepoint((x, y)):
                        if page + 1 <= len(received_data) - 4:
                            page += 1
                    if previous_button.collidepoint((x, y)):
                        if page - 1 >= 0:
                            page -= 1
                if event.type == my_event:
                    x, y = pygame.mouse.get_pos()
                    if quit_button.collidepoint((x, y)):
                        pygame.draw.rect(screen, "red", quit_button)
                    if new_room_button.collidepoint((x, y)):
                        pygame.draw.rect(screen, "grey", new_room_button)
                    if next_button.collidepoint((x, y)):
                        next_arrow_color = "white"
                    else:
                        next_arrow_color = "black"
                    if previous_button.collidepoint((x, y)):
                        previous_arrow_color = "white"
                    else:
                        previous_arrow_color = "black"

            screen.blit(create_label, (70, 70))
            screen.blit(your_label, (400, 70))
            screen.blit(new_room_label, (80, 145))
            screen.blit(quit_label, (74, 398))
            screen.blit(next_label, (761, 70))
            screen.blit(previous_label, (701, 70))

            pygame.display.update()
        if NEW_ROOM:
            if active1:
                color1 = "pink"
            else:
                color1 = "black"
            if active2:
                color2 = "pink"
            else:
                color2 = "black"

            screen.fill("white")
            pygame.display.set_caption("Меню")
            # display_the_background("background.png", 0, 0)

            next_label = font1.render(">", True, next_arrow_color)
            previous_label = font1.render("<", True, previous_arrow_color)
            error_label = font4.render(error_text, True, "red")

            pygame.draw.rect(screen, "black", vertical_line)
            pygame.draw.rect(screen, "#A35b5b", quit_button)
            pygame.draw.rect(screen, "#959696", new_room_button2)
            pygame.draw.rect(screen, "#F1f1f1", next_button)
            pygame.draw.rect(screen, "#F1f1f1", previous_button)

            txt_surface1 = font4.render(text1, True, "black")
            txt_surface2 = font4.render(text2, True, "black")

            width1 = 110
            width2 = 110
            input_box1.w = width1
            input_box2.w = width2

            screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y - 1))
            pygame.draw.rect(screen, color1, input_box1, 2)

            screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y - 1))
            pygame.draw.rect(screen, color2, input_box2, 2)

            buttons = []
            # received_data = room_data()
            received_data = [(1, (200, 400), ((123, (23, 45), 34), (123, (230, 45), 16))),
                             (2, (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             (3, (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             (4, (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90))),
                             (5, (700, 300), ((123, (0, 56), 67), (123, (200, 0), 90)))]
            # rooms: [id, size, (pictures)]
            # pictures: (key, (x, y), t)
            y = 140
            page_min = 0
            if len(received_data) <= 4:
                page_max = 0
            else:
                page_max = len(received_data) - 4
            page1 = page * 4

            if page == page_max:
                page2 = len(received_data)
            else:
                page2 = page * 4 + 4

            for i in range(page1, page2):
                new_rect = pygame.Rect(400, y, 270, 40)
                pygame.draw.rect(screen, "gray", new_rect)
                new_label = font3.render("Комната #" + str(received_data[i][0]), True, "white")
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
                        error_text = ""
                    elif input_box2.collidepoint((x, y)):
                        active2 = True
                        active1 = False
                        error_text = ""
                    else:
                        active1 = False
                        active2 = False
                    if new_room_button2.collidepoint((x, y)):
                        if text1 == "" or text2 == "":
                            print("hey")
                            error_text = "Введите длину и ширину"
                        elif not(300 <= int(text1) <= 2000):
                            error_text = "Ширина должна быть от 3 до 20м"
                        elif not(300 <= int(text2) <= 2000):
                            error_text = "Длина должна быть от 3 до 20м"
                        else:
                            if int(text1) >= int(text2):
                                the_room = pygame.Rect(100, int((500 - int((300 * int(text2)) / int(text1))) / 2), 300, int((300 * int(text2)) / int(text1)))
                                rect_x = 100
                                rect_y = int((500 - int((300 * int(text2)) / int(text1))) / 2)
                                rect_width = 300
                                rect_length = int((300 * int(text2)) / int(text1))
                            else:
                                the_room = pygame.Rect(int((500 - int((300 * int(text1)) / int(text2))) / 2), 100, int((300 * int(text1)) / int(text2)), 300)
                                rect_x = int((500 - int((300 * int(text1)) / int(text2))) / 2)
                                rect_y = 100
                                rect_width = int((300 * int(text1)) / int(text2))
                                rect_length = 300
                            room_name = "Комната #" + str(len(received_data) + 1)
                            room_name_label = font1.render(room_name, True, "black")
                            NEW_ROOM = False
                            CREATE_THE_ROOM = True
                    if next_button.collidepoint((x, y)):
                        if page + 1 <= len(received_data) - 4:
                            page += 1
                    if previous_button.collidepoint((x, y)):
                        if page - 1 >= 0:
                            page -= 1
                if event.type == my_event:
                    x, y = pygame.mouse.get_pos()
                    if quit_button.collidepoint((x, y)):
                        pygame.draw.rect(screen, "red", quit_button)
                    if new_room_button2.collidepoint((x, y)):
                        pygame.draw.rect(screen, "grey", new_room_button2)
                    if next_button.collidepoint((x, y)):
                        next_arrow_color = "white"
                    else:
                        next_arrow_color = "black"
                    if previous_button.collidepoint((x, y)):
                        previous_arrow_color = "white"
                    else:
                        previous_arrow_color = "black"
                if event.type == pygame.KEYDOWN:
                    if active1 or active2:
                        if active1:
                            if event.key == pygame.K_RETURN:
                                text1 = ""
                            elif event.key == pygame.K_BACKSPACE:
                                text1 = text1[:-1]
                            else:
                                if len(text1) < 8:
                                    if event.unicode.isdigit():
                                        text1 += event.unicode
                        if active2:
                            if event.key == pygame.K_RETURN:
                                text2 = ""
                            elif event.key == pygame.K_BACKSPACE:
                                text2 = text2[:-1]
                            else:
                                if len(text2) < 8:
                                    if event.unicode.isdigit():
                                        text2 += event.unicode

            screen.blit(create_label, (70, 70))
            screen.blit(your_label, (400, 70))
            screen.blit(quit_label, (74, 398))
            screen.blit(width_label, (50, 140))
            screen.blit(height_label, (50, 200))
            screen.blit(new_room_label, (80, 263))
            screen.blit(next_label, (761, 70))
            screen.blit(previous_label, (701, 70))
            screen.blit(error_label, (60, 300))
            screen.blit(sm1_label, (55, 162))
            screen.blit(sm2_label, (55, 222))

            pygame.display.update()
        if CREATE_THE_ROOM:
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
            pygame.draw.polygon(screen, "white",  [[597, 250], [600, 247], [621, 268], [618, 272]])
            pygame.draw.polygon(screen, "white", [[597, 268], [618, 247], [621, 250], [600, 272]])
            pygame.draw.rect(screen, "#F6F6F6", done_button)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if create_a_picture_button.collidepoint((x, y)):
                        create_picture = True
                        create_spawn = False
                    elif create_a_spawn_button.collidepoint((x, y)):
                        create_spawn = True
                        create_picture = False
                    else:
                        create_spawn = False
                        create_picture = False
                if event.type == my_event:
                    x, y = pygame.mouse.get_pos()
                    if done_button.collidepoint((x, y)):
                        done_active = True
                    else:
                        done_active = False
                    if background_rect.collidepoint((x, y)):
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
                        pygame.draw.circle(screen, "#E76E6E", (xx, yy), 7)

            screen.blit(add_a_picture_label1, (650, 130))
            screen.blit(add_a_picture_label2, (650, 158))
            screen.blit(room_name_label, (580, 37))
            screen.blit(add_a_spawn_label1, (650, 225))
            screen.blit(add_a_spawn_label2, (650, 250))
            screen.blit(add_a_spawn_label3, (650, 275))
            screen.blit(done_label, (610, 390))

            pygame.display.update()

pygame.quit()
