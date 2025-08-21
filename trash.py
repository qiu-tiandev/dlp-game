import pygame
import random
from score import *
trash = {}
trashId = 0
cache = {}
def initTrash(screenw,screenh):
  global nonrecycable,recycable,cache,generatedtrash,bin
  nonrecycable = pygame.image.load("non-recycable.png").convert_alpha()
  recycable = pygame.image.load("recycable.png").convert_alpha()
  global screenwidth,screenheight
  screenwidth = screenw
  screenheight = screenh
  for i in range(18):
    if i < 9:
      col = i % 3
      row = i // 3
      trash[i] = [col * 233, row * 233]
    else:
      col = (i-9) % 3
      row = (i-9) // 3
      trash[i] = [col * 233, row * 233]
  generatedtrash = {}
  for i, coords in trash.items():
    if i < 8:
        base_sprite = nonrecycable.subsurface((coords[0], coords[1], 233, 233))
    else:
        base_sprite = recycable.subsurface((coords[0], coords[1], 233, 233))

    resized_sprite = pygame.transform.smoothscale(
        base_sprite, (int(screenwidth * 0.2), int(screenheight * 0.15))
    )
    cache[i] = resized_sprite
class Trash:
  def __init__(self,x, y, type):
    global trashId,generatedtrash
    self.x,self.y = x,y
    self.type = type
    trashId +=1
    generatedtrash[trashId] = [x,y,type]
def generateTrash():
    if random.random() < 0.005:
      Trash(random.randint(int(screenwidth*0.05), int(screenwidth*0.9)),screenheight*0.007,random.randint(0,17))

      
def moveTrash(speed=1):
  subpoints =False
  for i in list(generatedtrash.keys()):
    generatedtrash[i][1] += speed
    if generatedtrash[i][1] > screenheight*0.8:
      generatedtrash.pop(i)
      subpoints = True
  return subpoints
      
def renderTrash(screen):
  subpoints = False
  if moveTrash():
    subpoints = True
  for i in generatedtrash:
    sprite = cache[generatedtrash[i][2]]
    screen.blit(sprite, (generatedtrash[i][0], generatedtrash[i][1]))
    return subpoints
def getTrash():
  return generatedtrash


def speed_trash(points, trashhole = 1000):
  speed = 1
  while points >= trashhole:
    speed += 1
    moveTrash(int(speed))
    trashhole += 1000