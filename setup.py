from commonequations import *
from pygame import Vector2, display

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
eqIndx = 0
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