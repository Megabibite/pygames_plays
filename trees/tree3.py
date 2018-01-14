#!/usr/bin/env python

"""A simple starfield example. Note you can move the 'center' of
the starfield by leftclicking in the window. This example show
the basics of creating a window, simple pixel plotting, and input
event management"""


import random, math, pygame
import numpy as np
from pygame.locals import *

#constants
WINSIZE = [1000, 500]
WINCENTER = [WINSIZE[0]/2.0, WINSIZE[1]/2.0]
NUMSTARS = 1500

def green():
    return 12+random.randint(0,50),50+random.randint(0,150),20+random.randint(0,50)
def blue():
    return 20+random.randint(0,50),60+random.randint(0,50),50+random.randint(0,150)   
def red():
    return 255,20+random.randint(0,100),100+random.randint(0,150)   

def init_star_factory():
    colorrot=0
    def init_star():
        "creates new star values"
        nonlocal colorrot
        dir = random.randrange(100000)
        velmult = random.random()*2+4
        rotspeed= (random.random()*0.0001)
        vel = [math.sin(dir) * velmult, math.cos(dir) * velmult,rotspeed]
        z=random.randrange(NUMSTARS)
        if colorrot%100<45:
            color=green()
        elif colorrot%100<90:
            color=blue()
        else:
            color=red()
        colorrot+=1
        return vel, WINCENTER[:],color,z
    return init_star


def initialize_stars(init_star):
    "creates a new starfield"
    stars = []
    for x in range(NUMSTARS):
        star = init_star()
        #vel[0] = vel[0] * (steps * .09)
        #vel[1] = vel[1] * (steps * .09)
        stars.append(star)
    return stars
  

def draw_stars(surface, zsurf,stars, color):
    "used to draw (and clear) the stars"
    for vel, pos,color,z in stars:
        pos = (int(pos[0]), int(pos[1]))
        if z>zsurf[pos]:
            surface.set_at(pos, color)
            zsurf[pos]=z

def move_stars(stars,init_star):
    "animate the star values"
    for vel, pos, color,z in stars:
        r=math.sqrt(pos[0]*pos[0]+pos[1]*pos[1])
        pos[0] = -(pos[1]-WINCENTER[1])*vel[2]*r+pos[0]
        pos[1] = (pos[0]-WINCENTER[0])*vel[2]*r+pos[1]
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]:
            vel[:], pos[:],color,z = init_star()
        else:
            vel[0] = vel[0] * 1
            vel[1] = vel[1] * 1
  

def main():
    "This is the starfield code"
    #create our starfield
    random.seed()
    init_star=init_star_factory()
    stars = initialize_stars(init_star)
    clock = pygame.time.Clock()
    #initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    zsurf=np.zeros(WINSIZE)
    pygame.display.set_caption('pygame Stars Example')
    white = 255, 240, 200
    black = 20, 20, 40
    green=20,200,20
    blue=20,20,200


    screen.fill(black)

    #main game loop
    done = 0
    while not done:
        #screen.fill(black)
        #draw_stars(screen, stars, black)
        move_stars(stars,init_star)
        draw_stars(screen, zsurf,stars, white)
        # move_stars(stars)
        # draw_stars(screen, stars, white)
        # move_stars(stars)
        # draw_stars(screen, stars, white)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1
                break
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                WINCENTER[:] = list(e.pos)
        clock.tick(50)


# if python says run, then we should run
if __name__ == '__main__':
    main()


