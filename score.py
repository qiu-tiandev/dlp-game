import pygame

class Score:
    def __init__(self):
        self.points = 0
        self.font = pygame.font.Font(None, 36)  
      
    def add_points(self, amount=100):
        self.points += amount
    def subtract_points(self, amount=100):
        self.points -= amount
    def reset(self):
        self.points = 0

    def get_score(self):
        return self.points

    def draw(self, screen, x=10, y=10, color=(0, 0, 255)):
        score_text = self.font.render(f"Score: {self.points}", True, color)
        screen.blit(score_text, (x, y))
