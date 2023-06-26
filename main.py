import pygame
import time
import random
from wall import Wall
from snake import Snake
from food import Food
from score import Score

# 視窗大小
window_x = 540
window_y = 540
center = [window_x/2, (window_y + 40)/2]

# 定義顏色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# 初始化遊戲
pygame.init()
pygame.display.set_caption('Greedy Snake')
surface = pygame.display.set_mode((window_x, window_y))

# import class
wall = Wall(510,492)
snake = Snake(center)
food = Food()
score = Score('times new roman', 20)
wall.create_wall(surface, center)
print(wall.edge)
food.random_food(surface, wall.edge, center)
print(food.position)

# FPS（每秒幀數）控制器
fps = pygame.time.Clock()

game_is_over = False

while not game_is_over:
    # 畫面以黑色塗滿
    surface.fill(black)

    # draw wall
    wall.create_wall(surface, center)

    # 方向控制
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_angle.append('up')
                snake.change_to()
            if event.key == pygame.K_DOWN:
                snake.change_angle.append('down')
                snake.change_to()
            if event.key == pygame.K_RIGHT:
                snake.change_angle.append('right')
                snake.change_to()
            if event.key == pygame.K_LEFT:
                snake.change_angle.append('left')
                snake.change_to()

    # 蛇移動，並確認是否吃到食物
    snake.move()
    if snake.eat_food(food.position):
        score.get_score(1)
        food.random_food(surface, wall.edge, center)
    
    # 是否撞牆或撞到自己
    if snake.hit_the_wall(wall.edge) or snake.hit_itself():
        game_is_over = True
    
    # draw food, snake, score
    food.draw_food(surface)
    snake.draw_snake(surface)
    score.show_score(surface)
    
    # update surface
    pygame.display.update()

    # add speed when get score
    speed = 10 + score.value//3
    fps.tick(speed)