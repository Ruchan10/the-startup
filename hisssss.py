import pygame
import random

pygame.init()

screen = pygame.display.set_mode(((800, 500)))
pygame.display.set_caption('Sarpa khel')

def game_loop():
    # color
    white = (255, 255, 255)
    black = (0, 0, 0)
    yello = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 200, 0)

    snk_x = 100
    snk_y = 100
    snk_xchange = 0
    snk_ychange = 0
    snk_list = []
    snk_length = 1

    score = 0
    game_over = False

    food = pygame.image.load('fmouse.png')
    food_x = 400
    food_y = 300
    food_xchange = 0
    food_ychange = 0


    def plot_snk(screen,color,snk_list,snk_width,snk_height):
        for i in snk_list:
            pygame.draw.rect(screen, black,(i[0], i[1], 20, 20))

    font = pygame.font.SysFont('comicsansms',30)

    def show_score(text,color,x,y):
        score = font.render(text,True,color)
        screen.blit(score,(x,y))


    run = True

    while run:
        if game_over:
            screen.fill(black)
            show_score('Game over !!press enter to continue or esc to quit',red,20,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        run = False

        else:

            screen.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        snk_ychange = 0
                        snk_xchange = 1
                    if event.key == pygame.K_LEFT:
                        snk_ychange = 0
                        snk_xchange = -1
                    if event.key == pygame.K_DOWN:
                        snk_xchange = 0
                        snk_ychange = 1
                    if event.key == pygame.K_UP:
                        snk_xchange = 0
                        snk_ychange = -1
            # movement of snake
            snk_x += snk_xchange
            snk_y += snk_ychange

            # for snake boundary
            if snk_x >800 or snk_x <0 or snk_y <0 or snk_y >500:
                game_over = True

            # for food boudary
            #     if food_x < 0:
            #         food_x = 800
            # if food_x > 800:
            #     food_x = 0
            #
            # if food_y < 0:
            #     food_y = 500
            # if food_y > 500:
            #     food_y = 0

            # snake length increase

            body = []
            body.append(snk_x)
            body.append(snk_y)
            snk_list.append(body)

            if len(snk_list)>snk_length:
                del snk_list[0]

            # food interaction
            if abs(snk_x - food_x) < 13 and abs(snk_y - food_y) < 10:
                score += 1
                snk_length += 7
                food_x = random.randint(20, 780)
                food_y = random.randint(20, 480)



            screen.blit(food,(food_x, food_y, 8,8))
            pygame.draw.rect(screen, black, (snk_x, snk_y, 20, 20))
            plot_snk(screen,black,snk_list,20,20)
            show_score('Score: '+ str(score),green,650,20)
        pygame.display.update()
game_loop()
pygame.quit()
quit()
