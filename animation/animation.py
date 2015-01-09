#!/usr/bin/env python3

import pygame, sys
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN

class spritesheet(object):
  def __init__(self, filename):
    self.sheet = pygame.image.load(filename).convert()
  
  def image_at(self, rectangle, colorkey = None):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(self.sheet, (0,0), rect)
    if colorkey is not None:
      if colorkey is -1:
        colorkey = image.get_at((0,0))
      elif type(colorkey) not in (pygame.Color,tuple,list):
        colorkey = image.get_at((colorkey,colorkey))
      image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image

  def images_at(self, rects, colorkey = None):
    return [self.image_at(rect, colorkey) for rect in rects]
  def load_strip(self, rect, image_count, colorkey = None):
    tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
    return self.images_at(tups,colorkey)

class SpriteStripAnim(object):
  def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
    self.filename =  filename
    ss = spritesheet(filename)
    self.images = ss.load_strip(rect, count, colorkey)
    self.i = 0
    self.loop = loop
    self.frames = frames
    self.f = frames
  def iter(self):
    self.i = 0
    self.f = self.frames
    return self
  def next(self):
    if self.i >= len(self.images):
      if not self.loop:
        raise StopIteration
      else:
        self.i = 0
    image = self.images[self.i]
    self.f -= 1
    if self.f == 0:
      self.i += 1
      self.f = self.frames
    return image
  def __add__(self, ss):
    self.images.extend(ss.images)
    return self
    

pygame.init()
screen = pygame.display.set_mode([640,480])

FPS = 120
frames = FPS / 12

strips = [
  SpriteStripAnim('Explode1.bmp', (0,0,24,24), 8, 1, True, frames),
  SpriteStripAnim('Explode2.bmp', (0,0,12,12), 7, 1, True, frames),
  SpriteStripAnim('Explode3.bmp', (0,0,48,48), 4, 1, True, frames) +
  SpriteStripAnim('Explode3.bmp', (48,48,48,48), 4, 1, True, frames),
  SpriteStripAnim('Explode4.bmp', (0,0,24,24), 6, 1, True, frames),
  SpriteStripAnim('Explode5.bmp', (0,0,48,48), 4, 1, True, frames) +
  SpriteStripAnim('Explode5.bmp', (48,48,48,48), 4, 1, True, frames)
]

black = Color('black')
clock = pygame.time.Clock()
n=0
image = strips[n].next()
while True:
  for e in pygame.event.get():
    if e.type == KEYUP:
      if e.key == K_ESCAPE:
        sys.exit()
      elif e.key == K_RETURN:
        n+=1
        if n >= len(strips):
          n=0
        strips[n].iter()
  screen.fill(black)
  screen.blit(image,(0,0))
  pygame.display.flip()
  image = strips[n].next()
  clock.tick(FPS) 


black = Color('black')
