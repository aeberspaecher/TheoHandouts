#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import matplotlib
matplotlib.use("module://backend_pgf")

import matplotlib.pyplot as plt

plt.figure(figsize=(5,3))

k, T = np.loadtxt("CO2-IR.jdx", usecols=(0,1), unpack=True)

plt.plot(k[::-1], T[::-1], lw=1.5)
plt.xlabel("$k\,[\mathrm{cm}^{-1}]$")
plt.ylabel("relative Transmission")
plt.xlim((np.max(k[::-1]), np.min(k[::-1])))
plt.ylim((0,1.1))
#plt.show()
plt.savefig("CO2-IR.pgf")
#plt.savefig("CO2-IR.pdf")
