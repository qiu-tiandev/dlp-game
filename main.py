from os import waitid_result
import os
import pygame
import sys
import bin
from bin import Bin
from trash import *
import score
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
lives = 0
# Set up display
width, height = 250, 375

screen = pygame.display.set_mode((width, height))
initTrash(width,height)
bin = Bin(width,height,screen)
pygame.display.set_caption("Group 6 game")

# Set score
score = score.Score()

# Define black color
black = (0, 0, 0)
big_font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 30)
# Define blue color
blue = (0,0,125)
background_image = pygame.image.load(os.path.join(ASSETS_DIR, 'background.png')).convert()
background_image = pygame.transform.smoothscale(background_image, (width*1, height*1))
def handleCollision(bin_instance, generatedtrash):
    collided = False
    to_remove = []
    for i, trash in generatedtrash.items():
        dist, bin_type = bin_instance.checkDist(trash)
        if dist < 15:
            collided = True
            # Determine trash type: 0 for recyclable, 1 for non-recyclable
            trash_type = 1 if trash[2] < 9 else 0
            # Check if placed in correct bin
            if trash_type == bin_type:
                to_remove.append(i)  # Correctly placed: mark for removal
            else:
                generatedtrash.pop(i)  # Remove wrong bin trash immediately
                return -1  # Indicate wrong bin placement
    for i in to_remove:
        del generatedtrash[i]
    return 1 if collided else 0  # All good, no wrong placement found

# Define lives
lives = 5
heart_image = pygame.image.load(os.path.join(ASSETS_DIR, "lives.png"))
def subtractLives():
    global lives
    lives-=1
def renderLives():
    for i in range(lives):
        screen.blit(heart_image, (10+i * 20, 30))
# Main loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with blue
    screen.fill(blue)
    screen.blit(background_image, (0, 0))
    bin.renderbin()
    bin.movebin()
    collisionSate = handleCollision(bin,getTrash())
    if collisionSate == 1:
        score.add_points()
    elif collisionSate == -1:
        subtractLives()
    if generateTrash():
        score.subtract_points()
    if speed_trash(score.get_score()):
        score.subtract_points(20)
    score.draw(screen)
    renderTrash(screen)
    renderLives()
    
    # Update the display
    pygame.display.flip()
    for i in range(lives):
        screen.blit(heart_image, (i * 30, 10))
    if lives == 0:
       running =False
while 1:
    screen.fill(black)
    gameovertext = big_font.render("Game Over", True, (255, 0,0))
    gameoverscore = small_font.render(f"Your score is: {score.get_score()}", True, (255, 0,0))
    screen.blit(gameovertext, (width//2 - gameovertext.get_width()//2,
         height//2 - gameovertext.get_height()//2))
    screen.blit(gameoverscore, (width//2 - gameoverscore.get_width()//2, height//2 - gameoverscore.get_height()//2 + 50))
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
