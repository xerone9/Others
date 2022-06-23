import pygame

pygame.init()
infoObject = pygame.display.Info()

root = pygame.display.set_mode((infoObject.current_w, infoObject.current_h - 60))
pygame.display.set_caption("Bounce")


colour = (0,0,255) #green
circle_x = 0
circle_y = 50
circle_radius = 12
border_width = 0 #0 = filled circle
velocity = 10
list_x = [0, -10]
list_y = [0, -10]



run = True

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():  # error is here
        if event.type == pygame.QUIT:
            run = False

    list_x.pop(0)
    list_x.append(circle_x)

    list_y.pop(0)
    list_y.append(circle_y)

    move_direction_logic_x = list_x[0] - list_x[1]
    move_direction_logic_y = list_y[0] - list_y[1]

    print(move_direction_logic_y)

    if move_direction_logic_x <= 0 and circle_x != infoObject.current_w:
        circle_x += velocity
        # circle_y += velocity

    # elif move_direction_logic_x <= 0 and move_direction_logic_y >= 0 and circle_x != infoObject.current_w:
    #     circle_x += velocity
    #     circle_y -= velocity

    # if circle_y != infoObject.current_h:
    #     circle_y -= velocity

    elif move_direction_logic_x >= 0 and circle_x > -2:
        circle_x -= velocity
        print(move_direction_logic_x)








    root.fill((0,0,0))
    pygame.draw.circle(root, colour, (circle_x, circle_y), circle_radius, border_width)

    pygame.display.update()


pygame.quit()

# haider = [0,0]
# haider.append(1)
# haider.pop(0)
# haider.append(2)
# haider.pop(0)
# print(haider)