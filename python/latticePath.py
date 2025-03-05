import math

def choose(n, k):

    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

pascal = []

for i in range(0, 21):

    pascal.append(choose(20, i))

def NextR(x):

    r = []
    for n in range(1, len(x)-1):
        r.append(x[(n-1)]+2*x[n]+x[(n+1)])

    return r

ans = NextR(pascal)
print(ans)

while len(ans) != 1:

    if len(ans) == 2:
        ans = 2 * ans[0]
        break

    ans = NextR(ans)

print(ans)