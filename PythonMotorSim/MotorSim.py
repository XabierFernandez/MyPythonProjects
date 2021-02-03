#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:44:30 2020

@author: xabier
"""
import numpy as np
from scipy import signal

# Motor params
R = 5.5                # [Ohm]
L = 0.0028             # [H]
phi = 0.5              # [Wb]
k = 1.0                # []
J = 0.5                # [kg m^2]
Cr = 0.1               # [Nm] Assumed Cr constant.
V = 24.0               # [V] Nominal voltage

# Building the system
H = np.matrix([[L,0.0],[0.0,J]])

A = H.getI()  * np.matrix([[-R,(-k*phi)],[(k*phi), 0.0]])
B = H.getI() * np.matrix([[V],[-Cr]])
C = np.matrix([[0.0,1.0]])
D = np.matrix([[0]])

#current / angular speed
print(("Current/angular speed: {0} / {1} ".format((-A.getI() * B).item(0,0) , (-A.getI() * B).item(1,0)))) 

print("H shape: ",H.shape, H)
print("A shape: ",A.shape, A)
print("B shape: ",B.shape, B)
print("C shape: ",C.shape, C)

sys = signal.StateSpace(A, B, C, D)
print(sys)
