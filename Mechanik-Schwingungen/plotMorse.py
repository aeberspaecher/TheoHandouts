#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import matplotlib
matplotlib.use("module://backend_pgf")

import matplotlib.pyplot as plt
from scipy.optimize import fsolve

plt.figure(figsize=(5,3))

lastx1 = 1.5

def EMorse(x, a, V0):
    return V0*(1.0 - np.exp(-a*(x-x0)))**2

def xMorse(En, a, V0):
    global lastx1
    print ("Morse E = %s"%En)
    x0 = fsolve(lambda x: abs(EMorse(x, a, V0) - En)**2, x0=0.0)
    x1 = fsolve(lambda x: abs(EMorse(x, a, V0) - En)**2, x0=lastx1)
    lastx1 = x1
    print x0, x1
    return x0, x1

def MorseLevel(n, a, V0):
    f0 = a/(2*np.pi)*np.sqrt(2*V0)
    return f0*(n+0.5) - ((f0*(n+0.5))**2)/(4*V0)

def plotMorseLevel(n, a, V0):
    En = MorseLevel(n, a, V0)
    x0, x1 = xMorse(En, a, V0)
    plt.plot((x0, x1), (En, En), lw=0.75, c="b", ls="-")

def HOlevel(n, a, V0):
    omega0 = np.sqrt(2*V0*a**2)
    return omega0*(n+0.5)/(2*np.pi)

def xHO(n, a, V0):
    Vn = HOlevel(n, a, V0)
    sol0 = np.sqrt(Vn/(V0*a**2)) + x0
    sol1 = -np.sqrt(Vn/(V0*a**2)) + x0
    return sol0, sol1

def plotHOlevel(n, a, V0):
    En = HOlevel(n, a, V0)
    x0, x1 = xHO(n, a, V0)
    plt.plot((x0, x1), (En, En), lw=0.75, c="r", ls="--")

xmax = 4
V0 = 3
x0 = 1
a = 1
x = np.linspace(0,xmax,2000)
y = EMorse(x, a, V0)

plt.plot(x,y, lw=1.5, label="Morsepotential")
plt.plot(x, V0*a**2*(x-x0)**2, lw=1.5, ls="--", c="red", label=r"Harm. N\"aherung")
for i in range(0,15):
    plotMorseLevel(i, a, V0)
    plotHOlevel(i, a, V0)
plt.xlim((0,xmax))
plt.ylim((0,4))
plt.xlabel("$x$")
plt.ylabel("$V$")
plt.legend()
#plt.show()
plt.savefig("Morse.pgf")
#plt.savefig("Morse.pdf")
