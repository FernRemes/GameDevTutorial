bif = "bg.jpg"
mif = "ball.png"

import pygame, sys  ## important
from pygame.locals import * # important

pygame.init() #important

screen = pygame.display.set_mode((640,360),0,32) ## build a screen

background = pygame.image.load(bif).convert() ## coverted image to the background
mouse_c = pygame.image.load(mif).convert_alpha() ## alpha for transparency
x = 0
clock = pygame.time.Clock() ## set time
speed = 250

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  screen.blit(background, (0,0))
  screen.blit(mouse_c, (x, 160))
  ## x += 1
  milli = clock.tick() ## set millisseconds to real time milliseconds
  seconds = milli / 1000. ## the point for a floating point variable
  dm = seconds * speed

  x += dm

  if x > 640: # so it doesnt go off teh screen
    x = 0

  pygame.display.update()
