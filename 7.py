import math

i = 1

currentNum = 1

while i != 10001:

    notPrime = False

    currentNum += 2

    for i in range(2, math.isqrt(currentNum)):

        if currentNum % i == 0:

            notPrime = True
            break

    if notPrime == False:

        i += 1

print(currentNum)
