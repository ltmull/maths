#!/bin/python3
# Pollard Rho factoring algorithm
# Find a factor of a given N 

from math import gcd
from time import time_ns

# get N (to factor) and seed
print("Enter a number N to factor and a seed x0")
N   = int(input("N = "))
x_0 = int(input("x0 = "))
print("---------------------------------------")

# set desired print setting and iteration limit
enable_print = False
max_iter = 1000

# initialization
g = 1
i = 0
xlist = []
xlist.append(x_0)
if enable_print:
    print("i =", i, ": x[", i, "] =", xlist[i])

# start timer
start_time = time_ns()

# loop while no factor found and below iteration limit
while (g < 2 and i < max_iter):
    # x[i] = (x[i-1]^2 + 1) mod N
    i += 1
    xi = int(((xlist[i-1])**2)+1)
    xi = xi % N
    xlist.append( xi )
    if enable_print:
        print("i =", i, ": x[", i, "] =", xlist[i])

    # for even i, calculate gcd(N, x[i]-x[i/2])
    if i % 2 == 0:
        g = gcd( N, ( xlist[i] - xlist[i//2] ) )
        # ignore when gcd returns N
        if (g == N):
            g = 1
        if enable_print:
            print("\tg =", g)

# after loop, a factor is found or max iters. reached
if i < max_iter:
    print("Factor found:", g)
    print(N, "=", g, "*", N/g)
    
else:
    print("No factor found in " + str(max_iter) + " iterations")

# end timer
end_time = time_ns()
time_passed = end_time - start_time
print(f"Time to solve: {time_passed / 1000000000} seconds")
