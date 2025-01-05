# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pygame-ce",
#   "terminedia",
# ]
# ///

"""
quick script for some "black on black" generative art -
the day 4 prompt for #genuary2025

My way of working for these is creating things on the interactive mode, and
later transpose what is left to a stand-alone script - hence the weird
one-letter global variables and other weird variable and function names.

Also, the "annotations", if any, are meant to give users some documentation,
not to make any tool happy at cost of readability. (if the default for
a parameter is "False", there is no reason but stubordnes to mark that
said parameter should be a boolean explicitly)


About the script:
I leverage my powerfull "ColorGradient" from terminedia to create the
auras needed for black on black. It is the first time I use them
(Or terminedia.Color for that effect), in pygame, and it is quite satisfactory
to see they plug-in directly into pygame)
"""


from random import randint, normalvariate

import pygame
from terminedia import V2, ColorGradient


def doit(pos1: V2, wd: V2, steps: int, gr: ColorGradient):
    gr = gr.scale(steps)
    pos1 = V2(pos1) - steps * V2(1,1)
    wd = V2(wd) + steps * V2(2,2)
    for i in  range(steps):
        pygame.draw.rect(sc, gr[steps - i], (*pos1, *wd))
        pos1 += (1,1)
        wd -= (2,2)
    pygame.display.flip()


def eqis(n: int, zz: ColorGradient, interative=False):
    for j in range(n):
        size = int(max(1, normalvariate(50,25)))
        pos = V2(randint(0, W), randint(0, H))
        thick = max(1, int(normalvariate(25,12)))
        doit(pos, (size, size), thick, zz)
        if interative:
            pygame.time.delay(50)  # 50ms


def main():
    global sc, z2, W, H
    W, H = 800, 600
    sc = pygame.display.set_mode((W,H))

    z2 = ColorGradient([ (0, (0,0,0)), (0.5, (0,0,0)), (0.5001,(.3,.3,.3)), (1, (0,0,0)) ])

    eqis(1000, z2, True)
    pygame.image.save(sc, "day_04.png")
    pygame.quit()


if __name__ == "__main__":
    main()
