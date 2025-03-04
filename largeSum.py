
def f(n):

    c = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3*n) + 1
        c += 1
    return c

ans = 0
longestChain = 0

for i in range(899999, 99999, -2):

    L = f(i)

    if L > longestChain:
        ans = i
        longestChain = L


print (ans)