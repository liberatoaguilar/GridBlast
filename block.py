import pygame
class Block:
    def __init__(self, locationx, locationy, screen):
        self.locationx = locationx
        self.locationy = locationy
        self.screen = screen
        pygame.draw.rect(self.screen, (92,0,0), pygame.Rect(self.locationx,self.locationy,20,20))
    def check_above(self,y,x):
        if y-20 == self.locationy and x == self.locationx:
            return True
        else:
            return False
    def check_below(self,y,x):
        if y+20 == self.locationy and x == self.locationx:
            return True
        else:
            return False
    def check_right(self,x,y):
        if x+20 == self.locationx and y == self.locationy:
            return True
        else:
            return False
    def check_left(self,x,y):
        if x-20 == self.locationx and y == self.locationy:
            return True
        else:
            return False
    def redraw(self):
        pygame.draw.rect(self.screen, (92,0,0), pygame.Rect(self.locationx,self.locationy,20,20))
        
#Fake Block (Doesn't draw it)
class FBlock:
    def __init__(self, locationx, locationy):
        self.locationx = locationx
        self.locationy = locationy
    def check_above(self,y,x):
        if y-20 == self.locationy and x == self.locationx:
            return True
        else:
            return False
    def check_below(self,y,x):
        if y+20 == self.locationy and x == self.locationx:
            return True
        else:
            return False
    def check_right(self,x,y):
        if x+20 == self.locationx and y == self.locationy:
            return True
        else:
            return False
    def check_left(self,x,y):
        if x-20 == self.locationx and y == self.locationy:
            return True
        else:
            return False
