import pygame
import random

class Food:
    def __init__(self):
        self.color = pygame.Color(255, 0, 0) #red
        self.panel = 9
        self.position = []

    def draw_food(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], self.panel, self.panel))
    
    #create a random food
    def random_food(self, surface, wall_edge, center):
        edge_width = self.panel//2 + 1 if self.panel%2 != 0 else self.panel/2
        edge_left = wall_edge[0] + (center[0] - wall_edge[0])%self.panel
        edge_top = wall_edge[2] + (center[1] - wall_edge[2])%self.panel
        pos_x = random.randrange(edge_left, wall_edge[1] - self.panel, self.panel)
        pos_y = random.randrange(edge_top, wall_edge[3] - self.panel, self.panel)
        #pos_x = random.randrange(edge_left + 47*self.panel, wall_edge[1] - edge_width, self.panel)
        #pos_y = random.randrange(edge_top + 45*self.panel, wall_edge[3] - edge_width, self.panel)
        '''
        width = self.panel//2 + 1
        pos_x = random.randrange(wall_edge[0] + width, wall_edge[1] - width, self.panel)
        pos_y = random.randrange(wall_edge[2] + width, wall_edge[3] - width, self.panel)
        '''
        self.position = [pos_x, pos_y]
        self.draw_food(surface)