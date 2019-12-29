import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import block
import enemy
import random

# Variables
pygame.init();
pygame.display.set_caption("GridBlast")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((420,420))
screenbounds = 420
done = False
green = (41,167,38)
darkgreen = (0,92,6)
blue = (17,30,139)
red = (223,0,47)
yellow = (255,230,0)
orange = (255,129,37)
black = (0,0,0)
white = (255,255,255)
px = 0
py = 0
ycoords = py
xcoords = px
path = [[0],[0]]
counter = 0
drawpath = False
blocks = []
shooting = False
blockson = True
direction = "none"
badmove = False
counter2 = 0
tracebadguy = False
playerhealth = 0
shootbadguy = False
xdiff = 0
ydiff = 0
badshotdir = "none"
randome = 0
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(score), True, black, white)
textRect = text.get_rect()
textRect.center = (screenbounds / 2, screenbounds / 8)


#Functions
def draw_grid():
    for x in range(22):
        for i in range(22):
            if i % 2 == 0 and x % 2 == 0:
                color = darkgreen
            elif i % 2 != 0 and x % 2 == 0:
                color = green
            elif i % 2 == 0 and x % 2 != 0:
                color = green
            else:
                color = darkgreen
            pygame.draw.rect(screen, color, pygame.Rect(((i-1)*20),((x-1)*20),20,20))
            screen.blit(text,textRect)

def player(px, py):
    boundsx = px-60
    boundsy = py-60
    return pygame.draw.rect(screen, blue, pygame.Rect(boundsx,boundsy,140,140)) and pygame.draw.rect(screen, red, pygame.Rect(px,py,20,20))
def draw_blocks(blocks):
    for x in blocks:
        x.redraw()
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

def check_shot(px,py,badguy,direction):
    total = 0
    if direction == "up":
        if badguy.x == px and badguy.y-20 == py:
            total += 20
        if badguy.x == px and badguy.y-40 == py:
            total += 20
        if badguy.x+20 == px and badguy.y-40 == py:
            total += 20
        if badguy.x-20 == px and badguy.y-40 == py:
            total += 20
        if badguy.x == px and badguy.y-60 == py:
            total += 20
        if badguy.x-40 == px and badguy.y-60 == py:
            total += 20
        if badguy.x-20 == px and badguy.y-60 == py:
            total += 20
        if badguy.x+20 == px and badguy.y-60 == py:
            total += 20
        if badguy.x+40 == px and badguy.y-60 == py:
            total += 20
    elif direction == "right":
        if badguy.x+20 == px and badguy.y == py:
            total += 20
        if badguy.x+40 == px and badguy.y+20 == py:
            total += 20
        if badguy.x+40 == px and badguy.y == py:
            total += 20
        if badguy.x+40 == px and badguy.y-20 == py:
            total += 20
        if badguy.x+60 == px and badguy.y-40 == py:
            total += 20
        if badguy.x+60 == px and badguy.y-20 == py:
            total += 20
        if badguy.x+60 == px and badguy.y == py:
            total += 20
        if badguy.x+60 == px and badguy.y+20 == py:
            total += 20
        if badguy.x+60 == px and badguy.y+40 == py:
            total += 20
    elif direction == "left":
        if badguy.x-20 == px and badguy.y == py:
            total += 20
        if badguy.x-40 == px and badguy.y+20 == py:
            total += 20
        if badguy.x-40 == px and badguy.y == py:
            total += 20
        if badguy.x-40 == px and badguy.y-20 == py:
            total += 20
        if badguy.x-60 == px and badguy.y-40 == py:
            total += 20
        if badguy.x-60 == px and badguy.y-20 == py:
            total += 20
        if badguy.x-60 == px and badguy.y == py:
            total += 20
        if badguy.x-60 == px and badguy.y+20 == py:
            total += 20
        if badguy.x-60 == px and badguy.y+40 == py:
            total += 20
    elif direction == "down":
        if badguy.x == px and badguy.y+20 == py:
            total += 20
        if badguy.x == px and badguy.y+40 == py:
            total += 20
        if badguy.x+20 == px and badguy.y+40 == py:
            total += 20
        if badguy.x-20 == px and badguy.y+40 == py:
            total += 20
        if badguy.x == px and badguy.y+60 == py:
            total += 20
        if badguy.x-40 == px and badguy.y+60 == py:
            total += 20
        if badguy.x-20 == px and badguy.y+60 == py:
            total += 20
        if badguy.x+20 == px and badguy.y+60 == py:
            total += 20
        if badguy.x+40 == px and badguy.y+60 == py:
            total += 20
    return total

def gameover():
    for x in range(22):
        for i in range(22):
            if i % 2 == 0 and x % 2 == 0:
                color = (209, 81, 59)
            elif i % 2 != 0 and x % 2 == 0:
                color = (168, 24, 0)
            elif i % 2 == 0 and x % 2 != 0:
                color = (168, 24, 0)
            else:
                color = (209, 81, 59)
            pygame.draw.rect(screen, color, pygame.Rect(((i-1)*20),((x-1)*20),20,20))
            losetext = font.render("Game Over", True, black, white)
            textRectlose = losetext.get_rect()
            textRectlose.center = (screenbounds / 2, screenbounds / 2)
            screen.blit(losetext,textRectlose)
    pygame.display.update()
    pygame.time.wait(1000)

#Starting Grid and Starting Player and Blocks
draw_grid()
player(px, py)

if blockson:
    #Top Left Cross
    block1 = block.Block(60,60, screen)
    block10 = block.Block(60,80, screen)
    block11 = block.Block(80,60, screen)
    block12 = block.Block(60,40, screen)
    block13 = block.Block(40,60, screen)

    # Bottom Right Cross
    block2 = block.Block(340,340,screen)
    block14 = block.Block(340,360, screen)
    block15 = block.Block(360,340, screen)
    block16 = block.Block(340,320, screen)
    block17 = block.Block(320,340, screen)

    #Top Right Cross
    block3 = block.Block(340,60,screen)
    block18 = block.Block(360,60, screen)
    block19 = block.Block(320,60, screen)
    block20 = block.Block(340,40, screen)
    block21 = block.Block(340,80, screen)

    #Bottom Left Cross
    block4 = block.Block(60,340,screen)
    block22 = block.Block(40,340, screen)
    block23 = block.Block(80,340, screen)
    block24 = block.Block(60,360, screen)
    block25 = block.Block(60,320, screen)

    # Middle Cross
    block5 = block.Block(200,200,screen)
    block6 = block.Block(200,220,screen)
    block7 = block.Block(220,200,screen)
    block8 = block.Block(200,180,screen)
    block9 = block.Block(180,200,screen)

    # Left V
    block26 = block.Block(80,180,screen)
    block27 = block.Block(100,200,screen)
    block28 = block.Block(80,220,screen)

    # Top V
    block29 = block.Block(180,80,screen)
    block30 = block.Block(200,100,screen)
    block31 = block.Block(220,80,screen)

    #Right V
    block32 = block.Block(320,180,screen)
    block33 = block.Block(300,200,screen)
    block34 = block.Block(320,220,screen)

    #Bottom V
    block35 = block.Block(180,320,screen)
    block36 = block.Block(200,300,screen)
    block37 = block.Block(220,320,screen)

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

#Enemy
badguy = enemy.Enemy(100,300,300,screen,0)
player(px, py)
draw_blocks(blocks)
screen.blit(text,textRect)
#Actual Game
while not done:
    screen.blit(text,textRect)
    pygame.display.update()
    if badguy.health <= 0:
        randome = random.randint(0,20)
        randome = randome*20
        badguy = enemy.Enemy(100,randome,randome,screen,0)
        score += 1
        text = font.render(str(score), True, black, white)
    if playerhealth >= 50:
        gameover()
        break
    counter += 1
    #Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(path[0]) >= 1:
                draw_grid()
                draw_blocks(blocks)
                drawpath = True

    # Path
    if drawpath == False and shooting == False and badmove == False and tracebadguy == False and shootbadguy == False:
        badguy.redraw()
        player(px,py)
        badguy.redraw_enemy()
        draw_blocks(blocks)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and ycoords >= py-40 and ycoords >= 20 and len(path[0]) <= 10 and check_blocks_above(blocks,ycoords,xcoords) == False:
            ycoords -= 20
            path[1].append(ycoords)
            path[0].append(xcoords)
        if pressed[pygame.K_DOWN] and ycoords <= py+40 and ycoords <= 380 and len(path[0]) <= 10 and check_blocks_below(blocks,ycoords,xcoords) == False:
            ycoords += 20
            path[1].append(ycoords)
            path[0].append(xcoords)
        if pressed[pygame.K_LEFT] and xcoords >= px-40 and xcoords >= 20 and len(path[0]) <= 10 and check_blocks_left(blocks,xcoords,ycoords) == False:
            xcoords -= 20
            path[0].append(xcoords)
            path[1].append(ycoords)
        if pressed[pygame.K_RIGHT] and xcoords <= px+40 and xcoords <= 380 and len(path[0]) <= 10 and check_blocks_right(blocks,xcoords,ycoords) == False:
            xcoords += 20
            path[0].append(xcoords)
            path[1].append(ycoords)
        if pressed[pygame.K_ESCAPE]:
            path[0] = []
            path[1] = []
            xcoords = px
            ycoords = py
            draw_grid()
            badguy.redraw()
            player(xcoords,ycoords)
            badguy.redraw_enemy()
            draw_blocks(blocks)

        for x in range(len(path[0])):
            if counter % 5 == 0:
                pygame.draw.rect(screen, yellow, pygame.Rect(path[0][x],path[1][x],20,20))
            else:
                pygame.draw.rect(screen, blue, pygame.Rect(path[0][x],path[1][x],20,20))
        pygame.draw.rect(screen, red, pygame.Rect(px,py,20,20))

    #Space Pressed
    elif drawpath == True and shooting == False and tracebadguy == False and shootbadguy == False:
        draw_grid()
        badguy.redraw()
        pygame.draw.rect(screen, blue, pygame.Rect(path[0][0]-60,path[1][0]-60,140,140))
        pygame.draw.rect(screen, red, pygame.Rect(path[0][0],path[1][0],20,20))
        badguy.redraw_enemy()
        draw_blocks(blocks)
        if path[0][0] == badguy.x and path[1][0] == badguy.y:
            badguy.losehealth(10)
        if path[0][0] == xcoords and path[1][0] == ycoords:
            path[0] = []
            path[1] = []
            drawpath = False
            shooting = True
            draw_grid()
            badguy.redraw()
            player(xcoords,ycoords)
            badguy.redraw_enemy()
            draw_blocks(blocks)
        try:
            path[0].pop(0)
            path[1].pop(0)
        except:
            pass
        px = xcoords
        py = ycoords

    #Shooting Turn
    elif shooting == True and badmove == False and tracebadguy == False and shootbadguy == False:
        if counter %5==0:
            pygame.draw.rect(screen, red, pygame.Rect(px,py,20,20))
        else:
            pygame.draw.rect(screen, blue, pygame.Rect(px,py,20,20))
        draw_blocks(blocks)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            shooting = False
            drawpath = False
            badguy.check_shot(px,py,direction)
            draw_grid()
            badguy.redraw()
            player(xcoords,ycoords)
            badguy.redraw_enemy()
            draw_blocks(blocks)

            if badguy.health > 0:
                badguy.move()
                badmove = True

        if pressed[pygame.K_DOWN]:
            draw_grid()
            badguy.redraw()
            player(xcoords,ycoords)
            draw_blocks(blocks)
            pygame.draw.rect(screen, orange, pygame.Rect(px,py+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px,py+40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+20,py+40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-20,py+40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px,py+60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-40,py+60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-20,py+60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+20,py+60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+40,py+60,20,20))
            direction = "down"
            badguy.redraw_enemy()
            draw_blocks(blocks)
        if pressed[pygame.K_UP]:
            draw_grid()
            badguy.redraw()
            player(xcoords,ycoords)
            draw_blocks(blocks)
            pygame.draw.rect(screen, orange, pygame.Rect(px,py-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px,py-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+20,py-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-20,py-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px,py-60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-40,py-60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-20,py-60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+20,py-60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+40,py-60,20,20))
            direction = "up"
            badguy.redraw_enemy()
            draw_blocks(blocks)
        if pressed[pygame.K_RIGHT]:
            draw_grid()
            badguy.redraw()
            player(xcoords,ycoords)
            draw_blocks(blocks)
            pygame.draw.rect(screen, orange, pygame.Rect(px+20,py,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+40,py+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+40,py,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+40,py-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+60,py-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+60,py-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+60,py,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+60,py+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px+60,py+40,20,20))
            direction = "right"
            badguy.redraw_enemy()
            draw_blocks(blocks)
        if pressed[pygame.K_LEFT]:
            draw_grid()
            badguy.redraw()
            player(xcoords,ycoords)
            draw_blocks(blocks)
            pygame.draw.rect(screen, orange, pygame.Rect(px-20,py,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-40,py+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-40,py,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-40,py-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-60,py-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-60,py-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-60,py,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-60,py+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(px-60,py+40,20,20))
            direction = "left"
            badguy.redraw_enemy()
            draw_blocks(blocks)
    elif badmove == True and tracebadguy == False and shootbadguy == False:
        draw_grid()
        pygame.draw.rect(screen, (0,187,193), pygame.Rect(badguy.badpath[0][0]-60, badguy.badpath[1][0]-60,140,140))
        pygame.draw.rect(screen, (118,0,138), pygame.Rect(badguy.badpath[0][0],badguy.badpath[1][0],20,20))
        player(xcoords,ycoords)
        draw_blocks(blocks)
        if counter2 < 20:
            for x in range(len(badguy.badpath[0])):
                pygame.draw.rect(screen, (118,0,138), pygame.Rect(badguy.badpath[0][0],badguy.badpath[1][0],20,20))
                pygame.draw.rect(screen, red, pygame.Rect(px,py,20,20))
                if counter % 5 == 0:
                    pygame.draw.rect(screen, (207,230,55), pygame.Rect(badguy.badpath[0][x],badguy.badpath[1][x],20,20))
                else:
                    pygame.draw.rect(screen, (0,187,193), pygame.Rect(badguy.badpath[0][x],badguy.badpath[1][x],20,20))
        counter2 += 1
        if counter2 > 20:
            counter2 = 0
            badmove = False
            tracebadguy = True
    elif tracebadguy == True and shootbadguy == False:
        if len(badguy.badpath[0]) > 0 or badguy.badpath[0] != None:
            draw_grid()
            try:
                pygame.draw.rect(screen, (0,187,193), pygame.Rect(badguy.badpath[0][0]-60, badguy.badpath[1][0]-60,140,140))
                player(px,py)
                pygame.draw.rect(screen, (118,0,138), pygame.Rect(badguy.badpath[0][0],badguy.badpath[1][0],20,20))
                draw_blocks(blocks)
            except:
                pygame.draw.rect(screen, (0,187,193), pygame.Rect(badguy.x-60, badguy.y-60,140,140))
                player(px,py)
                pygame.draw.rect(screen, (118,0,138), pygame.Rect(badguy.x,badguy.y,20,20))
                draw_blocks(blocks)
            try:
                badguy.badpath[0].pop(0)
                badguy.badpath[1].pop(0)
            except:
                pass
            try:
                if badguy.badpath[0][0] == px and badguy.badpath[1][0] == py:
                    playerhealth += 10
                if badguy.badpath[0][0] == badguy.x and badguy.badpath[1][0] == badguy.y:
                    draw_grid()
                    badguy.redraw()
                    player(px,py)
                    draw_blocks(blocks)
                    badguy.redraw_enemy()
                    badguy.badpath[0] = []
                    badguy.badpath[1] = []
                    tracebadguy = False
                    shootbadguy = True
            except:
                draw_grid()
                badguy.redraw()
                player(px,py)
                draw_blocks(blocks)
                badguy.redraw_enemy()
                badguy.badpath[0] = []
                badguy.badpath[1] = []
                tracebadguy = False
                shootbadguy = True
    elif shootbadguy == True:
        xdiff = px-badguy.x
        ydiff = py-badguy.y
        if xdiff <= 0 and ydiff <= 0:
            if abs(xdiff) > abs(ydiff):
                badshotdir = "left"
            elif abs(xdiff) < abs(ydiff):
                badshotdir = "up"
        if xdiff >= 0 and ydiff <= 0:
            if abs(xdiff) > abs(ydiff):
                badshotdir = "right"
            if abs(xdiff) < abs(ydiff):
                badshotdir = "up"
        if xdiff <= 0 and ydiff >= 0:
            if abs(xdiff) > abs(ydiff):
                badshotdir = "left"
            if abs(xdiff) < abs(ydiff):
                badshotdir = "down"
        if xdiff >= 0 and ydiff >= 0:
            if abs(xdiff) > abs(ydiff):
                badshotdir = "right"
            if abs(xdiff) < abs(ydiff):
                badshotdir = "down"

        if badshotdir == "up":
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x,badguy.y-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x,badguy.y-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+20,badguy.y-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-20,badguy.y-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x,badguy.y-60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-40,badguy.y-60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-20,badguy.y-60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+20,badguy.y-60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+40,badguy.y-60,20,20))
            pygame.draw.rect(screen, red, pygame.Rect(px,py,20,20))
            playerhealth += check_shot(px,py,badguy,badshotdir)
        elif badshotdir == "down":
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x,badguy.y+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x,badguy.y+40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+20,badguy.y+40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-20,badguy.y+40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x,badguy.y+60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-40,badguy.y+60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-20,badguy.y+60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+20,badguy.y+60,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+40,badguy.y+60,20,20))
            pygame.draw.rect(screen, red, pygame.Rect(px,py,20,20))
            playerhealth += check_shot(px,py,badguy,badshotdir)
        elif badshotdir == "right":
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+20,badguy.y,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+40,badguy.y+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+40,badguy.y,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+40,badguy.y-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+60,badguy.y-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+60,badguy.y-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+60,badguy.y,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+60,badguy.y+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x+60,badguy.y+40,20,20))
            pygame.draw.rect(screen, red, pygame.Rect(px,py,20,20))
            playerhealth += check_shot(px,py,badguy,badshotdir)
        elif badshotdir == "left":
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-20,badguy.y,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-40,badguy.y+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-40,badguy.y,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-40,badguy.y-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-60,badguy.y-40,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-60,badguy.y-20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-60,badguy.y,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-60,badguy.y+20,20,20))
            pygame.draw.rect(screen, orange, pygame.Rect(badguy.x-60,badguy.y+40,20,20))
            pygame.draw.rect(screen, red, pygame.Rect(px,py,20,20))
            playerhealth += check_shot(px,py,badguy,badshotdir)
        shootbadguy = False
    pygame.display.flip()
    clock.tick(13)
