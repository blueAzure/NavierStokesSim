#!user/bin/python

# testProgram.py
# Created on 2016/10/14
# Copyright(c) by.Suga Arata 

# For Test calculation in numpy array


import math
import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib as mpl
#import matplotlib.animation as animation


xLen = 20
yLen = 30

# use Staggered Grid
pressure = np.zeros((xLen+2, yLen+2))
velocity_x = np.zeros((xLen+2+1, yLen+2))
velocity_y = np.zeros((xLen+2, yLen+2+1))






