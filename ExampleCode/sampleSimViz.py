#!/usr/bin/env python3


# pydulum.py
# Copyright (c) 2015 Yuichi NAGAYAMA
# 
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation

from scipy.integrate import odeint

m = 0.1     # 振子の重さ[kg]
M = 4.0     # 台車の重さ[kg]
I = 5.0e-3  # 重心まわりの振子の慣性モーメント [kg m^2]
L = 0.3     # 振子の重心の位置[m]
g = 9.8     # 重力加速度[m/s^2]
k = 5.0e-2  # 摩擦係数

carwidth = 0.30         # 台車の幅
carheight = 0.20        # 台車の高さ
pendulumwidth = 0.04    # 振子の幅
pendulumheight = 2*L    # 振子の長さ

# 初期値(振子の角度[rad]，角速度[rad/s]，台車の位置[m]，速度[m/s])
x0 = [math.pi/16, 0.0, 0.0, 0.0]
tend = 20.0     # シミュレーション時間[s]
tstep = 0.01    # 時間の刻み幅[s]

def plot(t, x, label):
    for i, v in enumerate(label):
        plt.figure()
        plt.plot(t, x[:, i], linewidth=2.0) 
        plt.xlabel('t[s]')
        plt.ylabel(v)
        plt.grid()
        # plt.savefig('%d.png' % i)

   #  plt.show()

def video(y, theta):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, xlim=(-0.8, 0.8), ylim=(-0.6, 1.0))
    ax.set_xlabel('位置[m]')
    ax.grid()

    car = plt.Rectangle((y[0] - carwidth/2, 0), carwidth, carheight, fill=False)

    pendulum = plt.Rectangle((y[0] - pendulumwidth/2, carheight/2), pendulumwidth, pendulumheight, fill=False)
    ts0 = ax.transData
    coords0 = [y[0], carheight/2]
    tr0 = mpl.transforms.Affine2D().rotate_deg_around(coords0[0], coords0[1], 180*theta[0]/math.pi) + ts0
    pendulum.set_transform(tr0)

    def init():
        ax.add_patch(car)
        ax.add_patch(pendulum)
        return car, pendulum

    def anime(i):
        ts = ax.transData
        coords = [y[i], carheight/2]
        tr = mpl.transforms.Affine2D().rotate_deg_around(coords[0], coords[1], 180*theta[i]/math.pi) + ts

        car.set_x(y[i] - carwidth/2)
        pendulum.set_xy((y[i] - pendulumwidth/2, carheight/2))
        pendulum.set_transform(tr)

        ax.add_patch(car)
        ax.add_patch(pendulum)
        return car, pendulum

    ani = animation.FuncAnimation(fig, anime, np.arange(1, len(y)), interval=tstep*1.0e+3, blit=True, init_func=init)
    # ani.save('pydulum.mp4', fps=1/tstep, extra_args=['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])
    plt.show()

def controlinput(x):
    return 0.0
    # return 150.0*x[0] + 20.0*x[1] + 30.0*x[2] + 15.0*x[3] + 50.0*x[4] + 10.0*x[5]

def integral(x):
    return x

def pendulum(x, t):
    theta = x[0]
    dtheta = x[1]
    y = x[2]
    dy = x[3]

    F = controlinput(x)

    delta = (I + m*L**2)*(m + M) - m**2 * L**2 * math.cos(theta)**2
    A = [[m + M, -m*L*math.cos(theta)],
         [-m*L*math.cos(theta), I + m*L**2]]
    B = [m*g*L*math.sin(theta), F + m*L*dtheta**2*math.sin(theta) - k*dy]

    ddtheta, ddy = np.dot(A, B) / delta
    dxi = integral([x[0], x[2]])

    return np.r_[dtheta, ddtheta, dy, ddy, dxi]

if __name__ == '__main__':
    xi = [0.0, 0.0]
    t = np.linspace(0, tend, num=tend/tstep)
    x = odeint(pendulum, np.r_[x0, xi], t)

    label = [r'$\theta$[rad]', r'$\dot{\theta}$[rad/s]', r'$y$[m]', r'$\dot{y}$[m/s]']
    plot(t, x[:, :4], label)

    theta = x[:, 0]
    y = x[:, 2]

    video(y, theta)
