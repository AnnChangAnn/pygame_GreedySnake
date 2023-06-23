import pygame

class Snake:
    def __init__(self, center):
        self.color = pygame.Color(0, 255, 0)     # green
        self.panel = 9
        self.body = [[center[0], center[1]],
                     [center[0] - self.panel, center[1]],
                     [center[0] - 2*self.panel, center[1]]]
        self.head = self.body[0]
        self.angle = 'right'
        self.change_angle = []

    # draw the snake
    def draw_snake(self, surface):
        for pos in self.body:
            pygame.draw.rect(surface, self.color, pygame.Rect(pos[0], pos[1], self.panel, self.panel))

    # snake move
    def move(self):
        for index in range(len(self.body)-1, 0, -1):
            self.body[index][0] = self.body[index-1][0]
            self.body[index][1] = self.body[index-1][1]
        if self.angle == 'right':
            self.body[0][0] += self.panel
        elif self.angle == 'left':
            self.body[0][0] -= self.panel
        elif self.angle == 'up':
            self.body[0][1] -= self.panel
        elif self.angle == 'down':
            self.body[0][1] += self.panel
    
    # snake change direction
    def change_to(self):
        if self.change_angle:
            direction = self.change_angle.pop()
            if direction == 'right' and self.angle != 'left':
                self.angle = 'right'
            elif direction == 'left' and self.angle != 'right':
                self.angle = 'left'
            elif direction == 'up' and self.angle != 'down':
                self.angle = 'up'
            elif direction == 'down' and self.angle != 'up':
                self.angle = 'down'
    
    # extend snake body
    def extend(self):
        self.body.append(self.body[-1].copy())
    
    # if snake eat food or not
    def eat_food(self, food):
        if (self.head[0] >= food[0] - self.panel//2) and (self.head[0] <= food[0] + self.panel//2) and \
            (self.head[1] >= food[1] - self.panel//2) and (self.head[1] <= food[1] + self.panel//2):
            self.extend()
            return True
        return False
    
    # if hit the wall
    def hit_the_wall(self, wall_edge):
        if (self.head[0] <= wall_edge[0]) or (self.head[0] + self.panel - 1 >= wall_edge[1]) or \
            (self.head[1] <= wall_edge[2]) or (self.head[1] + self.panel - 1 >= wall_edge[3]):
            return True
        return False

    # if hit itself
    def hit_itself(self):
        for pos in self.body[1:]:
            if self.head[0] == pos[0] and self.head[1] == pos[1]:
                return True
        return False