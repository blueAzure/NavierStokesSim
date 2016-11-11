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
import matplotlib.pyplot as plt


NT=1 # Number of Time Steps
NX=100 # Number of X Partitions
NY=100 # Number of Y Partitions
DT=0.02 # Number of Real Time 
DX=0.001 # Number of X Real cell Length
DY=0.001 # Number of Y Real cell Length



preVel_x = np.zeros([NX, NY]) # Predictional Horizontal Velocity component(Vx) array
preVel_y = np.zeros([NX, NY]) # Predictional Vertical Velocity component(Vy) array
vel_x = np.zeros([NX, NY]) # Horizontal Velocity component(Vx) array
vel_y = np.zeros([NX, NY]) # Vertical Velocity component(Vy) array
phi = np.zeros([NX, NY]) # Correctional Pressure array
pres = np.zeros([NX, NY]) # Pressure array




def testUpdateFields():
    for x in range(NX):
        for y in range(NY):
            if x==0 or y==0 or x==NX-1 or y==NY-1:
                continue
            vel_x[x,y] = 0.25*(vel_x[x-1][y] + vel_x[x+1][y] + vel_x[x][y-1] + vel_x[x][y+1])


def testInitFields():
    for x in range(NX):
        for y in range(NY):
            vel_x[x,y] = math.cos(0.1*x) + math.cos(0.1*y) + np.random.rand()*3
    vel_x[5,10] = 10



def initPlot():
    print "initPlot"
    # Open matplotlib's window
    # Setup figure caption, bar, color, title, label...
    
    plt.figure()
    X,Y = np.meshgrid(np.arange(NX), np.arange(NY))
    plt.axis("equal")
    im = plt.imshow(vel_x)
    plt.colorbar()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("vel_x:" + "")
    plt.gca().invert_yaxis()

    plt.draw()
    plt.pause(0.01)
    
    return im


def initFields():
    #print "initFields"
    # Setup Velocity(u,v) array for initial environment
    # Setup Pressure array for initial environment
    pass


def updatePlot(im, time):
    #print "updatePlot"
    # Update matplotlib's window

    im.set_data(vel_x)
    plt.title("time:"+str(time))
    plt.draw()

    pass


# SolvePoissonEquation
# That calls poissonLoop
def solvePoissonEquation():
    #print "solvePoisoonEquation"
    # Init velocity temp Array for update
    # Init pressure temp Array for update
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
    #print "calcCorrectionPhi"
    solvePoissonEquation()

    # check solution by Contiunous Equation 
    pass


def calcPredictionalVel():
    #print "calcPredictionalVel"
    for x in range(NX):
        for y in range(NY):
            AdvectiveTerm_x = 0
            AdvectiveTerm_y = 0
            DiffusionTerm = 0
            preVel_x[x][y] = preVel_x[x][y]
            preVel_y[x][y] = 0

    pass


def calcVelocity():
    #print "calcVelocity"
    pass


def calcPressure():
    #print "calcPressure"
    pass


def updateFields():
    #print "updateFields"

    calcPredictionalVel() # calc predictional velocity(u,v)
    calcCorrectionPhi() # calc correction pressure(Phi) by SOR method
    calcVelocity() # update velocity(u,v)
    calcPressure() # update pressure



if __name__ == '__main__':
    print "start Program!"
    
    #initFields() # Initialize Fields
    testInitFields() ### debug  ###

    im = initPlot() # Initialize Plot

    for time in np.linspace(0, NT, NT/DT):
        print "time:", round(time, 3)
        #updateFields() 
        testUpdateFields() ### debug  ###
        updatePlot(im, time)
    #plt.savefig('OUTPUT/'+"lastUpdate")
        
    print "end Program!"
 





