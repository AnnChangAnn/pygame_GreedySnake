import pygame

class Wall:
    def __init__(self, width, height):
        self.color = pygame.Color(0, 0, 255) #blue
        self.width = width
        self.height = height
        self.panel = 7
        self.edge = []
    
    #draw the wall
    def create_wall(self, surface, center):
        #wall_left_top = [(surface_size[0]-self.width)//2, (surface_size[1]-self.height)//2]
        #wall_right_top = [(surface_size[0]+self.width)//2, (surface_size[1]-self.height)//2]
        #wall_left_bottom = [(surface_size[0]-self.width)//2, (surface_size[1]+self.height)//2]
        #wall_right_bottom = [(surface_size[0]+self.width)//2, (surface_size[1]+self.height)//2]
        wall_left_top = [center[0] - self.width//2, center[1] - self.height//2]
        wall_right_top = [center[0] + self.width//2, center[1] - self.height//2]
        wall_left_bottom = [center[0] - self.width//2, center[1] + self.height//2]
        wall_right_bottom = [center[0] + self.width//2, center[1] + self.height//2]
        pygame.draw.line(surface, self.color, wall_left_top, wall_right_top, self.panel)
        pygame.draw.line(surface, self.color, wall_left_top, wall_left_bottom, self.panel)
        pygame.draw.line(surface, self.color, wall_right_top, wall_right_bottom, self.panel)
        pygame.draw.line(surface, self.color, wall_left_bottom, wall_right_bottom, self.panel)
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
        '''
        pygame.draw.line(surface, self.color, [(surface_size[0]-self.width)/2, (surface_size[1]+self.height)/2], 
                         [(surface_size[0]+self.width)/2, (surface_size[1]+self.height)/2], self.panel)
        pygame.draw.line(surface, self.color, [(surface_size[0]-self.width)/2, (surface_size[1]-self.height)/2], 
                         [(surface_size[0]+self.width)/2, (surface_size[1]-self.height)/2], self.panel)
        pygame.draw.line(surface, self.color, [(surface_size[0]-self.width)/2, (surface_size[1]-self.height)/2], 
                         [(surface_size[0]-self.width)/2, (surface_size[1]+self.height)/2], self.panel)
        pygame.draw.line(surface, self.color, [(surface_size[0]+self.width)/2, (surface_size[1]-self.height)/2], 
                         [(surface_size[0]+self.width)/2, (surface_size[1]+self.height)/2], self.panel)
        wall_right = (surface_size[0]+self.width)/2 - self.panel//2 
        wall_left = (surface_size[0]-self.width)/2 + self.panel//2
        wall_top = (surface_size[0]-self.height)/2 + self.panel//2 
        wall_bottom = (surface_size[0]+self.height)/2 - self.panel//2
        '''
        self.edge = [wall_left, wall_right, wall_top, wall_bottom]