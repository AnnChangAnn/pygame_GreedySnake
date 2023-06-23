import pygame
import time
import random
from wall import Wall
from snake import Snake
from food import Food

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
game_window = pygame.display.set_mode((window_x, window_y))

#import class
wall = Wall(510,492)
snake = Snake(center)
food = Food()
wall.create_wall(game_window, center)
food.random_food(game_window, wall.edge, center)

# FPS（每秒幀數）控制器
fps = pygame.time.Clock()

#player_pos = pygame.Vector2(250.0, 250.0)
while True:
    game_window.fill(black)
    wall.create_wall(game_window, center)
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

    snake.move()
    if snake.eat_food(food.position):
        food.random_food(game_window, wall.edge, center)
    food.draw_food(game_window)
    snake.draw_snake(game_window)
        #game_window.fill(black)
        #game_window.fill(black,[490,490,-490,-490])
        #pygame.draw.rect(game_window, green, pygame.Rect(position[0], position[1], 10, 10))
        #pygame.draw.circle(game_window, "green", player_pos, 10)
        
    pygame.display.update()
    fps.tick(10)