
running = True

n = 1

while running:

    x = 20 * n

    for i in range(19, 2, -1):

        if (x % i) == 0:

            if (i == 2):

                running = False
                print(x)

        else:

            break

    n = n + 1