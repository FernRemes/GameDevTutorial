import pygame, sys  ## important
from pygame.locals import * # important

pygame.init() #important

screen = pygame.display.set_mode((640,360),0,32) ## build a screen

## list of points for polygon
points = [(20,120),(140,140),(110,30)]
color1 = (255,255,0)

## for circle
color2 = (230,170,0)
position = (300,176)
radius = (60)

## for ellipse
color3 = (0,255,255)
rectangle = (40,80,150,90)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
      
  screen.lock()

  pygame.draw.rect(screen, (140,250,45), Rect((100,100),(130,170))) ## create rectangle
  pygame.draw.polygon(screen, color1, points) # create polygon
  pygame.draw.circle(screen,color, position, radius) # create circle
  pygame.draw.ellipse(screen,color,rectangle) # create ellipse
  
  screen.unlock()

  pygame.display.update()
