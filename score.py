import pygame

class Score:
    def __init__(self, font, size):
        self.color = pygame.Color(255, 255, 255) #
        self.value = 0
        self.font = font
        self.size = size

    # 得分
    def get_score(self, score):
        self.value += score

    # 顯示分數
    def show_score(self, surface):
        score_surface = pygame.font.SysFont(self.font, self.size).render('Score : ' + str(self.value), True, self.color)
        score_rect = score_surface.get_rect()
        surface.blit(score_surface, score_rect)