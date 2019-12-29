import pygame
import random
import block
def check_on_block(blocks,xcoords,ycoords):
    touching = False
    for x in range(len(blocks)):
        if blocks[x].locationx == xcoords and blocks[x].locationy == ycoords:
            touching = True
        else:
            pass
    return touching
def check_blocks_right(blocks,xcoords,ycoords):
    touching = False
    for x in range(len(blocks)):
        if blocks[x].check_right(xcoords,ycoords):
            touching = True
        else:
            pass
    return touching
def check_blocks_left(blocks,xcoords,ycoords):
    touching = False
    for x in range(len(blocks)):
        if blocks[x].check_left(xcoords,ycoords):
            touching = True
        else:
            pass
    return touching
def check_blocks_above(blocks,ycoords,xcoords):
    touching = False
    for x in range(len(blocks)):
        if blocks[x].check_above(ycoords,xcoords):
            touching = True
        else:
            pass
    return touching
def check_blocks_below(blocks,ycoords,xcoords):
    touching = False
    for x in range(len(blocks)):
        if blocks[x].check_below(ycoords,xcoords):
            touching = True
        else:
            pass
    return touching

blocks = []

#Top Left Cross
block1 = block.FBlock(60,60)
block10 = block.FBlock(60,80)
block11 = block.FBlock(80,60)
block12 = block.FBlock(60,40)
block13 = block.FBlock(40,60)

# Bottom Right Cross
block2 = block.FBlock(340,340)
block14 = block.FBlock(340,360)
block15 = block.FBlock(360,340)
block16 = block.FBlock(340,320)
block17 = block.FBlock(320,340)

#Top Right Cross
block3 = block.FBlock(340,60)
block18 = block.FBlock(360,60)
block19 = block.FBlock(320,60)
block20 = block.FBlock(340,40)
block21 = block.FBlock(340,80)

#Bottom Left Cross
block4 = block.FBlock(60,340)
block22 = block.FBlock(40,340)
block23 = block.FBlock(80,340)
block24 = block.FBlock(60,360)
block25 = block.FBlock(60,320)

# Middle Cross
block5 = block.FBlock(200,200)
block6 = block.FBlock(200,220)
block7 = block.FBlock(220,200)
block8 = block.FBlock(200,180)
block9 = block.FBlock(180,200)

# Left V
block26 = block.FBlock(80,180)
block27 = block.FBlock(100,200)
block28 = block.FBlock(80,220)

# Top V
block29 = block.FBlock(180,80)
block30 = block.FBlock(200,100)
block31 = block.FBlock(220,80)

#Right V
block32 = block.FBlock(320,180)
block33 = block.FBlock(300,200)
block34 = block.FBlock(320,220)

#Bottom V
block35 = block.FBlock(180,320)
block36 = block.FBlock(200,300)
block37 = block.FBlock(220,320)

# Addng all blocks
blocks.append(block1)
blocks.append(block2)
blocks.append(block3)
blocks.append(block4)
blocks.append(block5)
blocks.append(block6)
blocks.append(block7)
blocks.append(block8)
blocks.append(block9)
blocks.append(block10)
blocks.append(block11)
blocks.append(block12)
blocks.append(block13)
blocks.append(block14)
blocks.append(block15)
blocks.append(block16)
blocks.append(block17)
blocks.append(block18)
blocks.append(block19)
blocks.append(block20)
blocks.append(block21)
blocks.append(block22)
blocks.append(block23)
blocks.append(block24)
blocks.append(block25)
blocks.append(block26)
blocks.append(block27)
blocks.append(block28)
blocks.append(block29)
blocks.append(block30)
blocks.append(block31)
blocks.append(block32)
blocks.append(block33)
blocks.append(block34)
blocks.append(block35)
blocks.append(block36)
blocks.append(block37)

class Enemy:
    def __init__(self, health, x, y, screen, direction=0, badpath=[[],[]]):
        self.health = health
        self.x = x
        self.y = y
        self.screen = screen
        self.direction = direction
        self.badpath = badpath
        pygame.draw.rect(self.screen, (0,187,193), pygame.Rect(self.x-60, self.y-60,140,140))
        pygame.draw.rect(self.screen, (118,0,138), pygame.Rect(self.x,self.y,20,20))
    def die(self):
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(self.x,self.y,20,20))
    def losehealth(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
    def redraw(self):
        if self.health > 0:
            pygame.draw.rect(self.screen, (0,187,193), pygame.Rect(self.x-60, self.y-60,140,140))
            pygame.draw.rect(self.screen, (118,0,138), pygame.Rect(self.x,self.y,20,20))
    def redraw_enemy(self):
        if self.health > 0:
            pygame.draw.rect(self.screen, (118,0,138), pygame.Rect(self.x,self.y,20,20))
    def check_shot(self,px,py,direction):
        if direction == "up":
            if px == self.x and py-20 == self.y:
                self.losehealth(20)
            if px == self.x and py-40 == self.y:
                self.losehealth(20)
            if px+20 == self.x and py-40 == self.y:
                self.losehealth(20)
            if px-20 == self.x and py-40 == self.y:
                self.losehealth(20)
            if px == self.x and py-60 == self.y:
                self.losehealth(20)
            if px-40 == self.x and py-60 == self.y:
                self.losehealth(20)
            if px-20 == self.x and py-60 == self.y:
                self.losehealth(20)
            if px+20 == self.x and py-60 == self.y:
                self.losehealth(20)
            if px+40 == self.x and py-60 == self.y:
                self.losehealth(20)
        elif direction == "right":
            if px+20 == self.x and py == self.y:
                self.losehealth(20)
            if px+40 == self.x and py+20 == self.y:
                self.losehealth(20)
            if px+40 == self.x and py == self.y:
                self.losehealth(20)
            if px+40 == self.x and py-20 == self.y:
                self.losehealth(20)
            if px+60 == self.x and py-40 == self.y:
                self.losehealth(20)
            if px+60 == self.x and py-20 == self.y:
                self.losehealth(20)
            if px+60 == self.x and py == self.y:
                self.losehealth(20)
            if px+60 == self.x and py+20 == self.y:
                self.losehealth(20)
            if px+60 == self.x and py+40 == self.y:
                self.losehealth(20)
        elif direction == "left":
            if px-20 == self.x and py == self.y:
                self.losehealth(20)
            if px-40 == self.x and py+20 == self.y:
                self.losehealth(20)
            if px-40 == self.x and py == self.y:
                self.losehealth(20)
            if px-40 == self.x and py-20 == self.y:
                self.losehealth(20)
            if px-60 == self.x and py-40 == self.y:
                self.losehealth(20)
            if px-60 == self.x and py-20 == self.y:
                self.losehealth(20)
            if px-60 == self.x and py == self.y:
                self.losehealth(20)
            if px-60 == self.x and py+20 == self.y:
                self.losehealth(20)
            if px-60 == self.x and py+40 == self.y:
                self.losehealth(20)
        elif direction == "down":
            if px == self.x and py+20 == self.y:
                self.losehealth(20)
            if px == self.x and py+40 == self.y:
                self.losehealth(20)
            if px+20 == self.x and py+40 == self.y:
                self.losehealth(20)
            if px-20 == self.x and py+40 == self.y:
                self.losehealth(20)
            if px == self.x and py+60 == self.y:
                self.losehealth(20)
            if px-40 == self.x and py+60 == self.y:
                self.losehealth(20)
            if px-20 == self.x and py+60 == self.y:
                self.losehealth(20)
            if px+20 == self.x and py+60 == self.y:
                self.losehealth(20)
            if px+40 == self.x and py+60 == self.y:
                self.losehealth(20)

    def move(self):
        if self.health > 0:
            addy = 0
            addx = 0
            self.badpath[0].append(addx+self.x)
            self.badpath[1].append(addy+self.y)
            for x in range(10):
                self.direction = random.randint(0,3)
                if self.direction == 0 and addy <= 20 and self.y+20 < 380 and check_blocks_above(blocks, self.y+addy, self.x+addx) == False:
                    addy += 20
                    self.badpath[0].append(addx+self.x)
                    self.badpath[1].append(addy+self.y)
                if self.direction == 1 and addy <= 20 and self.y-20 > 20 and check_blocks_below(blocks, self.y+addy, self.x+addx) ==  False:
                    addy -= 20
                    self.badpath[0].append(addx+self.x)
                    self.badpath[1].append(addy+self.y)
                if self.direction == 2 and addx <= 20 and self.x+20 < 380 and check_blocks_right(blocks, self.x+addx, self.y+addy) == False:
                    addx += 20
                    self.badpath[0].append(addx+self.x)
                    self.badpath[1].append(addy+self.y)
                if self.direction == 3 and addx <= 20 and self.x-20 > 20 and check_blocks_left(blocks, self.x+addx, self.y+addy) == False:
                    addx -= 20
                    self.badpath[0].append(addx+self.x)
                    self.badpath[1].append(addy+self.y)
            self.x += addx
            self.y += addy
            if check_on_block(blocks,self.x,self.y):
                self.x+=20
                self.y+=20
                self.badpath[0].append(self.x)
                self.badpath[1].append(self.y)
