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



NT=10 # Number of Time Steps
NX=100 # Number of X Partitions
NY=100 # Number of Y Partitions
DT=0.01 # Number of Real Time 
DX=0.001 # Number of X Real cell Length
DY=0.001 # Number of Y Real cell Length






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


# solvePoissonEquation
# that calls poissonLoop
def solvePoissonEquation():
    print "solvePoisoonEquation"
    # init velocity temp Array for update
    # init pressure temp Array for update
    NTER = 1000 # max number of Loop count. about xLength*yLength???

    for count in range(NTER):
        pass
        # call modPhi
        # check error
        # endLoops


# modPhi: modify Phi number.
# Phi is modificated Pressure
# that is called "solvePoissonEquation" 
def calcCorrectionPhi():
    print "calcCorrectionPhi"
    solvePoissonEquation()

    # check solution by Contiunous Equation 
    

def calcPredictionalVel():
    print "calcPredictionalVel"


def calcVelocity():
    print "calcVelocity"


def calcPressure():
    print "calcPressure"


def updateFields():
    print "updateFields"

    calcPredictionalVel() # calc predictional velocity(u,v)
    calcCorrectionPhi() # calc correction pressure(Phi) by SOR method
    calcVelocity() # update velocity(u,v)
    calcPressure() # update pressure



if __name__ == '__main__':
    print "start Program!"
    
    initFields() # Initialize Fields
    initPlot() # Initialize Plot

    for time in np.linspace(0, NT, NT/DT):
        print "time:", round(time, 3)
        updateFields() 
        updatePlot()
        
    print "end Program!"
 





