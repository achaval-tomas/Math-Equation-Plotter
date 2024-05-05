from pygame import *
from commonequations import *
from plotters import *
from setup import *

init() # pygame init.

'''
Use ARROW UP and DOWN to zoom in and out of the grid respectively.
Press H to return to home (initial zoom).
Press SPACE to navigate through different loaded equations.
Press I to plot the integral of the current function (in the current frame).

'''

# Draw a grid with respect to origin scaled in intervals of 'scale' with color 'clr'.
def drawGrid(scale, clr):
    for i in range(-int(origin.x/scale), int(origin.x/scale)+1):
        draw.line(screen, clr, (origin.x + i*scale, 0), (origin.x + i*scale, height), 1)
    for i in range(-int(origin.y/scale), int(origin.y/scale)+1):
        draw.line(screen, clr, (0, origin.y + i*scale), (width , origin.y + i*scale), 1)

# Simple function to draw X and Y axis.
def drawAxis():
    draw.line(screen, "white", (origin.x, 0), (origin.x, height), 3)
    draw.line(screen, "white", (0, origin.y), (width, origin.y), 3)


# Function to plot the full plane with Axis and Grid divisions.
def plotPlane(scale):

    if scale >= 100:
        drawGrid(scale/4, (10, 10, 10))

    drawGrid(scale, (50, 50, 50))

    drawAxis()

# Displays Axis, Grid and Equation.
def displayAll(scale, equation):
    screen.fill("black")
    plotPlane(scale)
    plotEq(equation, scale)
    display.flip()

# Change the scale of the plane.
def rescale(dir):
    screen.fill("black")
    newscale = 2*dir + scale
    if newscale <= 0:
        newscale = 1
    elif newscale >= 1001:
        newscale = 1000
    
    displayAll(newscale, equation)

    return newscale

# Change the equation to the next one in the equations array.
def changeEquation(eqIndx):
    newIndx = (eqIndx + 1) % equations.__len__()
    newEq = equations[newIndx]
    displayAll(scale, newEq)
    return newEq, newIndx

# Draw the starting plane.
displayAll(scale, equation)

# Init infloop bool.
running = True
clock = time.Clock()
currentTime = time.get_ticks()
lastPress = currentTime

# Main Loop.
while running:

    for e in event.get():
        if e.type == QUIT:
            running = False
    
    currentTime = time.get_ticks()
    
    keys = key.get_pressed()
    if keys[K_UP]:
        scale = rescale(1)
    elif keys[K_DOWN]:
        scale = rescale(-1)
    elif keys[K_h]:
        scale = homeScale
        displayAll(scale, equation)

    if keys[K_SPACE] and (currentTime - lastPress) > 300 :
        lastPress = currentTime
        equation, eqIndx = changeEquation(eqIndx)

    if keys[K_i]:
        plotIntegral(equation, scale)

    clock.tick(60)

quit()