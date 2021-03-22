'''A Blocky game'''
import pygame
import sys
import time
import random
import copy


pygame.init()
#score variable
score = 0

def main():
    #colours
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    #time  
    clock = pygame.time.Clock()
    #a display and the blit surface
    rawdisplayx=800
    rawdisplayy=800
    rawdisplay = pygame.display.set_mode((rawdisplayx,rawdisplayy))
    rectangle = rawdisplay.get_rect()
    #LOADING IMAGES 
    #character appearance and movement
    characterw = 30
    characterh = 30
    characterx = 278
    charactery = 270
    character = None
    def characters():
        nonlocal character
        character = pygame.draw.rect(rawdisplay, blue, [characterx, charactery, characterw, characterh])

    yvar = 0
    xvar = 0
    speed = 3
    afterspeed = 0
    #obstacles
    obstacle1w = 25
    obstacle1h = 25
    obstacle1x = random.randrange(0,rawdisplayx-obstacle1w)
    obstacle1y = -300
    obstacle2w = 31
    obstacle2h = 31
    obstacle2y = copy.deepcopy(charactery)
    obstacle2x = -300
    obstacle3h = 31
    obstacle3w = 31
    obstacle3x = random.randrange(0,rawdisplayx-obstacle3w)
    obstacle3y = -100
    obstacle1speed = 1.5
    obstacle2speed = 0.5
    obstacle3speed = 0.5
    #blitting images

    #setting text font and rendering
    def text(message,colour,size):
        font = pygame.font.SysFont('monotype.ttf',size)
        rawtext = font.render(message,True,colour)
        return rawtext, rawtext.get_rect()
    #score 
    def scoretext():
        global score
        scoremessage = 'Score '+ str(score)
        scoretoblit, scoretoblitrect = text(scoremessage,green,40)
        rawdisplay.blit(scoretoblit,(0,0))
    
    #specific text functions + position of text
    def crash():
        crashtoblit, crashtoblitrect = text('You crashed',red,80)
        crashtoblitrect.center = rectangle.center
        rawdisplay.fill(black)
        rawdisplay.blit(crashtoblit,crashtoblitrect)
        global score
        score = 0
        pygame.display.update()
    
    #the game event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xvar -= speed
                elif event.key == pygame.K_RIGHT:
                    xvar += speed
                elif event.key == pygame.K_UP:
                    yvar -= speed
                elif event.key == pygame.K_DOWN:
                    yvar += speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    xvar = afterspeed
                elif event.key == pygame.K_LEFT:
                    xvar = -afterspeed
                elif event.key == pygame.K_UP:
                    yvar = -afterspeed
                elif event.key == pygame.K_DOWN:
                    yvar = afterspeed
        if characterx < -10 or characterx > 770 or charactery < -10 or charactery > 770:
            rawdisplay.fill(black)
            crash()
            pygame.display.update()
            time.sleep(2)
            main()
        #post loop
        rawdisplay.fill(white)
        #obstacle(xvalue,yvalue,length,height,colour)
        obstacle1y += obstacle1speed
        obstacle2x += obstacle2speed
        obstacle3y += obstacle3speed
        obstacle1 = pygame.draw.rect(rawdisplay,green,[obstacle1x,obstacle1y,30,30])
        obstacle2 = pygame.draw.rect(rawdisplay,red,[obstacle2x,obstacle2y,30,30])
        obstacle3 = pygame.draw.rect(rawdisplay,black,[obstacle3x,obstacle3y,30,30])
        if obstacle2x > 770:
            obstacle2x = 0
            obstacle2y = copy.deepcopy(charactery)
        if obstacle1y > 770:
            obstacle1y = 0
            obstacle1x = random.randrange(0,rawdisplayx-obstacle1w)
        if obstacle3y > 770:
            obstacle3y = 0
            obstacle3x = random.randrange(0,rawdisplayx-obstacle1w)
        #character
        charactery += yvar
        characterx += xvar
        characters()
        global score
        if character.colliderect(obstacle1):
            score += 1
        if character.colliderect(obstacle2):
            crash()
            time.sleep(2)
            main()
        if character.colliderect(obstacle3):
            crash()
            time.sleep(2)
            main()        
        scoretext()
        if score >  80:
            obstacle2speed = 3.6
            obstacle3speed = 2
        pygame.display.update()
        
        
if __name__ == '__main__':
	main()