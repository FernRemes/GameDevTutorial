import pygame, sys  ## important
from pygame.locals import * # important

pygame.init() #important

screen = pygame.display.set_mode((640,360),0,32) ## build a screen

color = (200,155,64)
pos1 = (20,20)
pos2 = (150,143)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  screen.lock()
  pygame.draw.line(screen, color, pos1, pos2, 3) ## create line
  screen.unlock()

  pygame.display.update()

  
