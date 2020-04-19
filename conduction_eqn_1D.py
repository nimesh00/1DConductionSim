#!/usr/bin/env python3

'''
Script for simulation of 1D conduction in a rod. (Linear and Non-Linear both).

Requirements: Python 3.6.9 + gnuplot 5.2 patchlevel 2

Author(s): Nimesh Khandelwal
E-mail: nimesh6798@gmail.com
Github-repo: https://github.com/nimesh00/1DConductionSim.git
'''

'''
Some points to keep in mind while using this script:
* Keep the value of a < 0 (the slope should be negative) for non-linear case.
* keep the value of ko lower than 0.1 for a stable solution. (values like 0.11 & 0.12 produce solutions that are oscillating for some nodes in time domain).
* Very high or Very low boundary conditions make the solution unstable.
* To simulate Linear conduction comment Line 73 and uncomment Line 74
'''

import numpy as np
import os
import time

# Length of rod
L = 10
# seconds
t = 50

# time step
dt = 0.1

# step 
dx = 0.1
dt_dx_2 = dt / (dx ** 2)

# Number of nodes
N = int(L / dx)

T = np.zeros((2, N))

# Number of time steps (iterations)
N_t = int(t / dt)

# conductivity constants
ko = 0.11
a = -0.001

c_rho = 2

#boundary conditions
T_l = -10
T_r = 30


def plot_continuous_array(array):
    file_ptr = open('1DConductionVarK.dat', 'w+')
    for i in range(len(array) - 1):
        data = str(i)  + " " + str(array[i])
        file_ptr.write("%s\n" %data)
    file_ptr.write(str(len(array) - 1) + " " + str(array[len(array) - 1]))
    file_ptr.close()

def main():
    print("Press 'x' to exit the gnuplot window first then stop the python script.!!\n")
    os.system("gnuplot 1DConductionPlot.gnu &")
    T[:, 0] = T_l
    T[:, N - 1] = T_r

    for i in range(N_t):
        print("Iteration: ", i + 1)
        for j in range(1, N - 1):
            c = (ko + a * T[0, j]) * dt_dx_2 / c_rho
            # c = ko * dt_dx_2 / c_rho
            T[1, j] = c * (T[0, j + 1] + T[0, j - 1]) + (1 - 2 * c) * T[0, j]
        T[0, :] = T[1, :]
        plot_continuous_array(T[0, :])
        time.sleep(0.1)



if __name__ == "__main__":
    main()