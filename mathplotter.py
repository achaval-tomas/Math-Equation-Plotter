from pygame import *
from commonequations import *
from math import floor

init() # pygame init.

'''
Use ARROW UP and DOWN to zoom in and out of the grid respectively.
Press H to return to home (initial zoom).
Press SPACE to navigate through different loaded equations.
Press I to plot the integral of the current function (in the current frame).

'''

# Equations are represented as f(x) = sum(Equation[i]*x^i)
equations = [   classicLinear(),
                classicCuadratic(),
                classicCubic(),
                taylorForCos(),
                taylorForSin(),
                exponential(),
                naturalLog(),
                funQuintic()
                # Add your own equations here!
                # Example:
                # equation = [3, 1, 2, 5] = f(x) = 3 + x + 2*x^2 + 5*x^3
            ]

# initialize the first equation.
eqIndx = 0;
equation = equations[eqIndx]

# SELECT A SCALE FOR THE GRID.
homeScale = 50
scale = homeScale

# SELECT A COLOR FOR YOUR FUNCTIONS.
color = "purple"

# Initialize main constants.
width = 720
height = 720
origin = Vector2(width/2, height/2) # Centered origin.

# Set the window up.
screen = display.set_mode((width, height))
display.set_caption("Math Graphs")


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

# Returns f(x)
def applyEq(x, equation):
    y = 0
    for exp in range(0, equation.__len__()):
        y += equation[exp]*power(x, exp)
    return y

# Plot 'equation' with respect to 'scale'.
def plotEq(equation, scale):
    for x in range(-int(origin.x), int(origin.x)+1):
        x2 = x+1
        y = -scale*applyEq(x/scale, equation)
        y2 = -scale*applyEq(x2/scale, equation)
        draw.line(screen, color, origin + (x, y), origin + (x2, y2), 4)

# Draw the integral of an equation.
def plotIntegral(equation, scale):
    for x in range(-int(origin.x), int(origin.x)+1):
        y = -scale*applyEq(x/scale, equation)
        draw.line(screen, (50, 100, 100), origin + (x, y), origin + (x, 0), 1)
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