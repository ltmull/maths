# Pollard Rho factoring algorithm
# Find a factor of a given N (max 10000 iterations)

from math import remainder, gcd
print("Enter a number N to factor and a seed x0")
N   = int(input("N = "))
x_0 = int(input("x0 = "))
print("---------------------------------------")

# initialization
g = 1
i = 0
xlist = []
xlist.append(x_0)
#print("i =", i, ": x[", i, "] =", xlist[i])

# loop while g !> 1
while (g < 2 and i < 10000):
    # x[i] = (x[i-1]^2 + 1) mod N
    i += 1
    xi = int( remainder(((xlist[i-1])^2)+1, N))
    xlist.append( xi )
    #print("i =", i, ": x[", i, "] =", xlist[i])

    # for even i, calculate gcd(N, x[i]-x[i/2])
    if i % 2 == 0:
        g = gcd( N, ( xlist[i] - xlist[i//2] ) )
        #print("\tg =", g)

# after loop, a factor is found or max iters. reached
if i < 10000:
    print("Factor found:", g)
    print(N, "=", g, "*", N/g)
    
else:
    print("No factor found, probably prime")
