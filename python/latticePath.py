import math

def choose(n, k):

    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

pascal = []

for i in range(0, 21):

    pascal.append(choose(20, i))