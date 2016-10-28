#!usr/bin/python

"""
That is RayleighBenardConvectionSim.py

Equation: Navier-Stokes Equation
Method: Velocity-Pressure Method
        SOR Method for Poisson Equation
        Time Difference is analyzed with Second-order accurate forward-difference Scheme.
        Poisson Equation is analyzed with Second-order accurate central-difference Scheme.
Grid: Staggered grid 

Created by.Suga Arata on 2016.10.28

Update ???

"""

import math
import numpy as np


def initPlot():
    # start matplotlib's window
    # setup figure caption, bar, color, title, label...


def initFields():
    # initialize velocity(u,v) array.
    # initialize pressure array.
    # initialize update temp velocity array.
    # initialize phi array.


def updatePlot():
    # update matplotlib's window
    # (if argu is "0" then save image. Otherwise don't do it.)


# solvePoissonEquation
# that calls poissonLoop
def solvePoissonEquation():
    print solvePoisoonEquation
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
    print "!"


def updateFields():
    print "updateFields!"

    # update Pressure
    # update velocity(u,v)
    # check solution by Contiunous Equation


if __name__ == '__main__':
    print "start Program!"
    
    # Initialize Fields
    # Initialize Plot

    # loop:
    #   update field
    #   update plot (if argu is "0" then save image. Otherwise don't do it.
    # endLoop

    print "end Program!"
 





