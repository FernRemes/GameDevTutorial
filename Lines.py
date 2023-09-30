import pygame, sys  ## important
from pygame.locals import * # important

pygame.init() #important

screen = pygame.display.set_mode((640,360),0,32) ## build a screen

color = (200,155,64)
pos1 = (20,20)
pos2 = (150,143)

points = [] # empty list 

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == MOUSEBUTTONDOWN:
      points.append(event.pos)
  if len(points) > 1:
    pygame.draw.lines(screen, color, False, points, 3) ## line drawing 
  screen.lock()
  pygame.draw.line(screen, color, pos1, pos2, 3) ## create line
  screen.unlock()

  pygame.display.update()

  
