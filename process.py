import pygame, sys, classes, random

def process(snake, SCREENWIDTH, SCREENHEIGHT):

    # to close the window
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # movement

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_d] and snake.velx != -5 and snake.turn_possible:
        snake.velx = 5
        snake.vely = 0
        snake.turn_possible = False
        snake.turn_counter = 0
    elif keys[pygame.K_a] and snake.velx != 5 and snake.turn_possible:
        snake.velx = -5
        snake.vely = 0
        snake.turn_possible = False
        snake.turn_counter = 0
    elif keys[pygame.K_w] and snake.vely != 5 and snake.turn_possible:
        snake.vely = -5
        snake.velx = 0
        snake.turn_possible = False
        snake.turn_counter = 0
    elif keys[pygame.K_s] and snake.vely != -5 and snake.turn_possible:
        snake.vely = 5
        snake.velx = 0
        snake.turn_possible = False
        snake.turn_counter = 0
        
    # food spawn

    if not snake.food:
        snake.foodx = random.randint(snake.food_radius, SCREENWIDTH - snake.food_radius)
        snake.foody = random.randint(snake.food_radius, SCREENHEIGHT - snake.food_radius)
        snake.food = True

    # food eat

    if (abs(snake.posx - snake.foodx) < snake.food_radius \
       and abs(snake.posy - snake.foody) < snake.food_radius) \
       or (abs(snake.posx + snake.size - snake.foodx) < snake.food_radius \
       and abs(snake.posy + snake.size - snake.foody) < snake.food_radius) \
       or (abs(snake.posx - snake.foodx) < snake.food_radius \
       and abs(snake.posy + snake.size - snake.foody) < snake.food_radius) \
       or (abs(snake.posx + snake.size - snake.foodx) < snake.food_radius \
       and abs(snake.posy - snake.foody) < snake.food_radius) \
       or (abs(snake.posx + (snake.size / 2) - snake.foodx) < snake.food_radius \
       and abs(snake.posy - snake.foody) < snake.food_radius):
        snake.food = False
        snake.body.append([snake.body[len(snake.body) - 1][1], [], [], [], []])

    # turn
        
    if snake.turn_counter >= 4:
        snake.turn_possible = True
        
    snake.turn_counter += 1

    # body collision

    for i in range(2, len(snake.body)):
        if (abs(snake.posx - snake.body[i][0][0]) < snake.size \
            and abs(snake.posy - snake.body[i][0][1]) < snake.size):
            snake.game_over = True
