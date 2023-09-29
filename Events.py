## events explanation
bif = "bg.jpg"
mif = "ball.png"

import pygame, sys  ## important
from pygame.locals import * # important

pygame.init() #important

screen = pygame.display.set_mode((640,360),0,32) ## build a screen

background = pygame.image.load(bif).convert() ## coverted image to the background
mouse_c = pygame.image.load(mif).convert_alpha() ## alpha for transparency

x,y = 0,0 
moveX, moveY = 0,0
while True:
  for event in pygame.event.get():
    if event.type == QUIT: ## if they clicked the x at the top right of the window
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN: ## if they pressed down a key 
      if event.key == K_LEFT: ## left arrow button ex. K_a is the a button
        moveX = -1 ## move left
      elif event.key = K_RIGHT: ## right button move right
        moveX = +1
      elif event.key == K_UP: ## up button move up
        moveY = -1
      elif event.key == K_DOWN: ## move y down
        moveY = +1
    if event.type == KEYUP: ## set the the x and y to zero to stop moving
      if event.key == K_LEFT:
        moveX = 0
      elif event.key = K_RIGHT:
        moveX = 0
      elif event.key == K_UP:
        moveY = 0
      elif event.key == K_DOWN:
        moveY = 0
        
  x += moveX
  y += moveY

  screen.blit(background, (0,0))
  screen.blit(mouse_c, (x,y))

  pygame.display.update()
      



