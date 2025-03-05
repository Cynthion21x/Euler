import math

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

def choose(n, k):

    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

def f(primeFactors):

    l = len(primeFactors)

    noDupe = list(set(primeFactors))

    print(primeFactors)
    print(noDupe)

    duplicateCount = l - len(noDupe)

    nodupeL = len(noDupe)

    totalFactors = 0

    for i in range(1, l+1):

        totalFactors += choose(l, i)

    print(totalFactors) 

    if duplicateCount != 0:
        totalFactors /= duplicateCount
        totalFactors += nodupeL

    '''
    if duplicateCount != 0:

        totalFactors *= duplicateCount + 1

    coefficient = 0

    for i in range(0, duplicateCount):

        coefficient += choose(duplicateCount, i)

    totalFactors -= duplicateCount * (coefficient)
    '''
    return int(totalFactors + 1)

print(f(primeFactors(45)))
