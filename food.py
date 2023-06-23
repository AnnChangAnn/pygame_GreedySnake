import pygame
import random

class Food:
    def __init__(self):
        self.color = pygame.Color(255, 0, 0) #red
        self.panel = 9
        self.position = []

    def draw_food(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], self.panel, self.panel))
    
    # create a random food
    def random_food(self, surface, wall_edge, center):
        # 食物到中心點的距離要可以被 panel 整除，才能剛好和蛇對齊
        # 因此左或上的實際邊界不會剛好等於牆邊
        # 右或下則需扣掉 panel，才不會長到牆上
        edge_left = wall_edge[0] + (center[0] - wall_edge[0])%self.panel
        edge_top = wall_edge[2] + (center[1] - wall_edge[2])%self.panel
        pos_x = random.randrange(edge_left, wall_edge[1] - self.panel, self.panel)
        pos_y = random.randrange(edge_top, wall_edge[3] - self.panel, self.panel)
        self.position = [pos_x, pos_y]
        self.draw_food(surface)