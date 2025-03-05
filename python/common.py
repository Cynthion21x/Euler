import math
import os

def choose(n, k):

    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

def primeFactors(n):

    i = 2
    factors = []

    while i*i <= n:

        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors

def textToList(path):

    ans = []

    with open(path) as f:

        for line in f:

            l = line.rstrip()

            row = []
            num = ""
            for i in range(len(l)):
                
                try:
                    int(l[i])
                    num += l[i]

                except:
                    if len(num) > 0:
                        row.append(int(num))
                        num = ""

            if len(num) > 0:
                row.append(int(num))

            ans.append(row)

    return ans

