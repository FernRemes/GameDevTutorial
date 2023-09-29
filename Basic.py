bif = "bg.jpg"
mif = "ball.png"

import pygame, sys  ## important
from pygame.locals import * # important

pygame.init() #important

screen = pygame.display.set_mode((640,360),0,32) ## build a screen

background = pygame.image.load(bif).convert() ## coverted image to the background
mouse_c = pygame.image.load(mif).convert_alpha() ## alpha for transparency

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
      
  screen.blit(background, (0,0)) ## blit means copy

x,y = pygame.mouse.get_pos() ## create x y position
x -= mouse_c.get_width()/2
y -= mouse_c.get_height()/2

screen.blit(mouse_c, (x,y))

pygame.display.update() ## important

