#!/usr/bin/env python3

import pygame, sys

class SpriteSheet:
  def __init__(self, filename):
    self.sheet = pygame.image.load(filename).convert()
  
  def image_at(self, rectangle, colorkey = None):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(self.sheet, (0,0), rect)
    return image

  def images_at(self, rects, colorkey = None):
    return [self.image_at(rect, colorkey) for rect in rects]

pygame.init()
surface = pygame.display.set_mode([640,480])
FPS = 20
clock = pygame.time.Clock()

ss = SpriteSheet('MasterChiefOriginal.png')
n = 0
sprites = ss.images_at([
                         (0,0,51,71),
                         (51,0,61,71), 
                         (115,0,50,71),
                         (168,0,43,71),
                         (214,0,49,71),
                         (265,0,49,71),
                         (314,0,49,71),
                         (369,0,49,71),
                         (418,0,49,71)
                       ])
chief_posx = 0
chief_posy = 0
chief_facing = "right"
while True:
  if n >= len(sprites):
    n = 0
  surface.fill((0,0,0))
  
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        sys.exit()

  keys = pygame.key.get_pressed()
  if keys:
    surface.blit(sprites[0], (chief_posx, chief_posy))
  if keys[pygame.K_LEFT]: 
    chief_posx -= 5
    if chief_facing == "right":
      sprites[n] = pygame.transform.flip(sprites[n],1,0)
      chief_facing = "left"
    surface.blit(sprites[n], (chief_posx,chief_posy))
    if n < len(sprites)-1:
      n += 1
    else:
      n = 0
  elif keys[pygame.K_RIGHT]: 
    if chief_facing == "left":
      sprites[n] = pygame.transform.flip(sprites[n],1,0)
      chief_facing = "right"
    chief_posx += 5
    surface.blit(sprites[n], (chief_posx,chief_posy))
    if n < len(sprites)-1:
      n += 1
    else:
      n = 0
  if keys[pygame.K_UP]:
    chief_posy -= 5
    surface.blit(sprites[n], (chief_posx,chief_posy))
    if n < len(sprites)-1:
      n += 1
    else:
      n = 0
  elif keys[pygame.K_DOWN]:
    chief_posy += 5
    surface.blit(sprites[n], (chief_posx,chief_posy))
    if n < len(sprites)-1:
      n += 1
    else:
      n = 0


  pygame.display.update()
  clock.tick(FPS)

