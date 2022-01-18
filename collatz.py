# Exploration of Collatz Conjecture
# sequence:
#   x[i] = (x[i-1] % 2 == 0) ? x[i-1] / 2 : 3 * x[i-1] + 1
# conjecture:
#   All positive integer seeds will eventually reach 1

max_iter = 10000

# return (success, iteration)
def collatz(seed):
    i = 1
    xlast = seed
    while i < max_iter:
        xi = (xlast // 2) if (xlast % 2 == 0) else (3 * xlast + 1)
        print("x[" + str(i) + "] = " + str(xi))
        if xi == 1:
            return 1, i
        xlast = xi
        i += 1

    # exiting loop means maximum iterations reached
    return 0, 0

cont = "qQnN"
inp = "y"
while (cont.find(inp) < 0):
    print("Enter a positive seed integer")
    seed = int( input("x[0] = ") )
    success, its = collatz(seed)
    if (success == 1):
        print("Success! Seed x[0] =", seed, "reached 1 at x[" + str(its) + "]")
    else:
        print("Failure. Seed x[0] =", seed, "did not reach 1 in", max_iter, "iterations")
    inp = input("Go again? ([QqNn] to exit) ")
    print("\n")
