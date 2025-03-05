import math

currentNum = 1

s = 0

while currentNum < 2000000-1:

    notPrime = False

    currentNum += 2

    for j in range(2, math.isqrt(currentNum)+1):

        if currentNum % j == 0:

            notPrime = True
            break

    if notPrime == False:

        s += currentNum

    print(str(currentNum))

print("The sum is: " + str(s))