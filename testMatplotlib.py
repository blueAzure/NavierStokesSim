#!/usr/bin/python

# testProgram.py
# Created on 2016/10/13 
# Copyright(c) by.Suga Arata 

# For Test the matplotlib function.
# added for 2dimension data array on 2016/10/13

import math
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib as mpl
#import matplotlib.animation as animation
#from scipy.integrate import odeint


def testPlot(index, data, title):
    plt.figure()
    plt.plot(index, data, linewidth=2.0) 
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.savefig('OUTPUT/test.png')


def testPlot2Dim(data, title):
    plt.figure()
    plt.imshow(data)
    plt.title(title)
    plt.grid()
    plt.savefig('OUTPUT/'+title)



if __name__ == '__main__':
    print "program start!"

    # create 1dim data plot
    indexArray = np.arange(0, 10, 0.1)
    dataArray = np.sin(indexArray)
    testPlot(indexArray, dataArray, "1dimData")

    # create 2dim data plot
    dataArray = np.random.randn(100, 100)
    testPlot2Dim(dataArray, "2dimData")

    # create 2dim data plot by numpyArray
    xLen, yLen = 200, 300
    npArray = np.zeros((xLen, yLen))
    for x in range(xLen):
        for y in range(yLen):
            npArray[x,y] = (x-1)*yLen + y
    testPlot2Dim(npArray, "2dimDataByNP")

    print "program end!"


