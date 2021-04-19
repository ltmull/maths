# Extended Euclidean Algorithm
# Purpose: compute gcd and Bezout Identity

# receive operands from user
print("Enter 2 numbers to find gcd(a, b)")
valA = int(input("a = "))
valB = int(input("b = "))

# save initial values 
startA = valA
startB = valB

# perform Euclidean Algorithm to compute greatest common divisor
floor_list = [0]
while valA != 0:
    floorba = valB // valA
    floor_list.append(floorba)
    newA = valB - floorba * valA
    valB = valA
    valA = newA

# print gcd
print("\ngcd(", startB, ",", startA, ") =", valB, "\n")

# construct Bezout Identity
x = 1
y = 0
while len(floor_list) > 1:
    yn = x - (floor_list.pop() * y)
    x = y
    y = yn

# print Bezout Identity
print("Bezout Identity:")
print(valB, "=", startB, "(", x, ") +", startA, "(", y, ")")
