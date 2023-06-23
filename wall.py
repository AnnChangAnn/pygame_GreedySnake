import pygame

class Wall:
    def __init__(self, width, height):
        self.color = pygame.Color(0, 0, 255) #blue
        self.width = width
        self.height = height
        self.panel = 7
        # left, right, top, bottom
        self.edge = []
    
    # draw the wall
    def create_wall(self, surface, center):
        # 計算方形四角點
        wall_left_top = [center[0] - self.width//2, center[1] - self.height//2]
        wall_right_top = [center[0] + self.width//2, center[1] - self.height//2]
        wall_left_bottom = [center[0] - self.width//2, center[1] + self.height//2]
        wall_right_bottom = [center[0] + self.width//2, center[1] + self.height//2]

        # 畫出邊界
        pygame.draw.line(surface, self.color, wall_left_top, wall_right_top, self.panel)
        pygame.draw.line(surface, self.color, wall_left_top, wall_left_bottom, self.panel)
        pygame.draw.line(surface, self.color, wall_right_top, wall_right_bottom, self.panel)
        pygame.draw.line(surface, self.color, wall_left_bottom, wall_right_bottom, self.panel)

        # 計算四面牆的內邊位置
        if self.panel%2 != 0:
            wall_right = wall_right_top[0] - self.panel//2 
            wall_left = wall_left_top[0] + self.panel//2
            wall_top = wall_left_top[1] + self.panel//2 
            wall_bottom = wall_right_bottom[1] - self.panel//2
        else:
            wall_right = wall_right_top[0] - self.panel//2 - 1
            wall_left = wall_left_top[0] + self.panel//2 + 1
            wall_top = wall_left_top[1] + self.panel//2 + 1
            wall_bottom = wall_right_bottom[1] - self.panel//2 - 1
        self.edge = [wall_left, wall_right, wall_top, wall_bottom]