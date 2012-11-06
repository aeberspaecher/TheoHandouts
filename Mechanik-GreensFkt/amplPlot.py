#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""PLot amplitude of driven damped oscillator.
"""

import numpy as np
import matplotlib as mpl
mpl.use("module://backend_pgf")
import matplotlib.pyplot as plt
plt.figure(figsize=(5,3))


def ampl(Omega, gamma, omega0=1.0, f0=1.0):
    return f0/((omega0**2 - Omega**2)**2 + gamma**2*Omega**2)


if(__name__ == '__main__'):

    Omega = np.linspace(0, 2, 5000)

    yGamma1 = ampl(Omega, 0.5)
    yGamma2 = ampl(Omega, 0.4)
    yGamma3 = ampl(Omega, 0.3)
    yGamma4 = ampl(Omega, 0.2)

    plt.plot(Omega, yGamma1, ls="-", c="b", lw=1.25)
    plt.plot(Omega, yGamma2, ls="-", c="r", lw=1.25)
    plt.plot(Omega, yGamma3, ls="-", c="g", lw=1.25)
    plt.plot(Omega, yGamma4, ls="-", c="k", lw=1.25)
    plt.plot((1.0, 1.0), (0.0, 1.1*np.max(yGamma4)), ls="--", c="k", lw=1.0)
    plt.ylim((0.0, 1.1*np.max(yGamma4)))

    plt.xlabel(r"$\Omega/\omega_0$")
    plt.ylabel("$A$")
    plt.tight_layout()

    #plt.show()
    plt.savefig("ampl-plot.pgf")
