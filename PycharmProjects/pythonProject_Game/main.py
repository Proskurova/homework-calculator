import pygame
import time
import random
import pygame as pg


pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 780
dis_height = 520

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
sc = pygame.Surface((dis_width, dis_height))
snake_img = pg.image.load('Snake_game.jpeg')
pygame.display.update()

clock = pygame.time.Clock()


snake_block = 10
snake_speed = 5

font_style = pygame.font.SysFont("monaco", 55)
score_font = pygame.font.SysFont("monaco", 35)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, black, [i[0], i[1], snake_block, snake_block])


def message(msg, color):
    mes_g = font_style.render(msg, True, color)
    dis.blit(mes_g, [dis_width / 3, dis_height / 2])


game_over = False

x1 = dis_width / 2
y1 = dis_height / 2

x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1

food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
        else:
            dis.blit(sc, (0, 0))
            sc.blit(snake_img, (0, 0))
            time.sleep(0.2)
            pygame.display.update()
    if x1 >= dis_width or y1 >= dis_height or x1 <= 0 or y1 <= 0:
        game_over = True
    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)
    pygame.display.update()
    pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
    snake_head = [x1, y1]
    snake_List.append(snake_head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_head:
            game_over = True

    our_snake(snake_block, snake_List)
    your_score(Length_of_snake - 1)

    pygame.display.update()

    if x1 == food_x and y1 == food_y:
        food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    clock.tick(snake_speed)


message("You lost", red)
pygame.display.update()
time.sleep(1)

pygame = quit()
quit()
