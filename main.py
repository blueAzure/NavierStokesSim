#!usr/bin/python

"""
That is RayleighBenardConvectionSim.py

Equation: Navier-Stokes Equation
Method: Velocity-Pressure Method
        SOR Method for Poisson Equation
        Time Difference is analyzed with Second-order accurate forward-difference Scheme.
        Poisson Equation is analyzed with Second-order accurate central-difference Scheme.
Grid: Staggered grid 

Creating by.Suga Arata on 2016.10.28~


"""

import math
import numpy as np



NTS=1000 # Number of Time Steps




def initPlot():
    print "initPlot"
    # start matplotlib's window
    # setup figure caption, bar, color, title, label...


def initFields():
    print "initFields"
    # initialize velocity(u,v) array.
    # initialize pressure array.
    # initialize update temp velocity array.
    # initialize phi array.


def updatePlot():
    print "updatePlot"
    # update matplotlib's window
    #if argu is true then save image. Otherwise don't do it.


# solvePoissonEquation
# that calls poissonLoop
def solvePoissonEquation():
    print "solvePoisoonEquation"
    # init velocity temp Array for update
    # init pressure temp Array for update
    # loop: 
    #   call modPhi
    #   check error
    # endLoop


# modPhi: modify Phi number.
# Phi is modificated Pressure
# that is called "solvePoissonEquation" 
def modPhi():
    print "modPhi"


def updateFields():
    print "updateFields"

    # loop(time):
    #   calc predictional velocity(u,v)
    #   calc correction pressure by SOR method
    #     check solution by Contiunous Equation 
    #   update velocity(u,v)
    #   update pressure
    # endLoop


if __name__ == '__main__':
    print "start Program!"
    
    initFields() # Initialize Fields
    initPlot() # Initialize Plot

    for time in range(NTS):
        print "time:", time
        
    # loop:
    #   update field
    #   update plot
    # endLoop

    print "end Program!"
 





