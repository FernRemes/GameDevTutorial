bif = "bg.jpg"
mif = "ball.png"

import pygame, sys  ## important
from pygame.locals import * # important

pygame.init() #important

screen = pygame.display.set_mode((640,360),0,32) ## build a screen

background = pygame.image.load(bif).convert() ## coverted image to the background
mouse_c = pygame.image.load(mif).convert_alpha() ## alpha for transparency
x = 0
y = 0
clock = pygame.time.Clock() ## set time
speedX = 150
speedY = 170

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
      
  screen.blit(background, (0,0))
  screen.blit(ball, (x,y))

  milli = clock.tick()
  seconds = milli/ 1000. ## the dot for floating poiint variable
  dmX = seconds * speedX
  dmY = seconds * speedY

  X += dmX
  Y += dmY

  if x > 640:
    x = 0
  if y > 360:
    y = 0
  
  pygame.display.update()
