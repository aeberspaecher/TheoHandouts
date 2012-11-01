#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Plot various representations of the Dirac's Delta function.
"""

import numpy as np
import matplotlib.pyplot as plt


def rectangle(x, x0, epsilon):
    y = np.zeros(len(x))
    y[np.where(np.abs(x- x0) <= epsilon/2.0)] = 1.0/epsilon
    #plt.plot(x, np.abs(x- x0))
    #plt.show()
    return y


def gauss(x, x0, epsilon):
    return 1.0/(np.sqrt(2*np.pi)*epsilon)*np.exp(-(x-x0)**2/(2.0*epsilon**2))
    # TODO: fix Normierung!


def lorentz(x, x0, epsilon):
    return 1.0/np.pi * epsilon/((x-x0)**2 + epsilon**2)


def sinc(x, x0, epsilon):
    y = np.ones(len(x))
    y[np.where(x != 0.0)] = 1.0/epsilon*np.sin(np.pi*(x-x0)/epsilon)/(np.pi*(x-x0))
    return y


if(__name__ == '__main__'):
    x = np.linspace(-3, +3, 5000)

    yRect1 = rectangle(x, -2.0, 0.5)
    yRect2 = rectangle(x, -2.0, 0.3)
    yRect3 = rectangle(x, -2.0, 0.2)
    plt.plot(x, yRect1, c="b", lw=2, ls="-.")
    plt.plot(x, yRect2, c="b", lw=2, ls="--")
    plt.plot(x, yRect3, c="b", lw=2, ls="-")

    yGauss1 = gauss(x, -1.0, 0.35)
    yGauss2 = gauss(x, -1.0, 0.15)
    yGauss3 = gauss(x, -1.0, 0.075)
    plt.plot(x, yGauss1, c="r", lw=2, ls="-.")
    plt.plot(x, yGauss2, c="r", lw=2, ls="--")
    plt.plot(x, yGauss3, c="r", lw=2, ls="-")

    yLor1 = lorentz(x, 0.0, 0.25)
    yLor2 = lorentz(x, 0.0, 0.125)
    yLor3 = lorentz(x, 0.0, 0.07)
    plt.plot(x, yLor1, c="black", lw=2, ls="-.")
    plt.plot(x, yLor2, c="black", lw=2, ls="--")
    plt.plot(x, yLor3, c="black", lw=2, ls="-")

    ySinc1 = sinc(x, 2.001, 0.6)
    ySinc2 = sinc(x, 2.001, 0.5)
    ySinc3 = sinc(x, 2.001, 0.4)
    plt.plot(x, ySinc1, c="gray", lw=2, ls="-.")
    plt.plot(x, ySinc2, c="gray", lw=2, ls="--")
    plt.plot(x, ySinc3, c="gray", lw=2, ls="-")

    plt.xlabel("$t$")
    plt.ylabel("$\delta_\epsilon$")
    plt.tight_layout()

    #plt.show()
    plt.savefig("delta-plot.pdf")
