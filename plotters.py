from commonequations import power
from setup import *
from pygame import draw, display

# bounds y barely out of frame to avoid looong lines
def boundHeight(y):
    if (y>origin.y):
        return origin.y+1
    if (y<-origin.y):
        return -origin.y-1
    return y

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
        draw.line(screen, color, origin + (x, boundHeight(y)), origin + (x2, boundHeight(y2)), 4)

# Draw the integral of an equation.
def plotIntegral(equation, scale):
    for x in range(-int(origin.x), int(origin.x)+1):
        y = -scale*applyEq(x/scale, equation)
        draw.line(screen, (50, 100, 100), origin + (x, boundHeight(y)), origin + (x, 0), 1)
    plotEq(equation, scale)
    display.flip()