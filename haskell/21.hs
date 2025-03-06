sumOfDivisor n = (sum [ x | x <- [1..(n `div` 2)], n `mod` x == 0])

isAmbicable n = x == n && n /= sumOfDivisor n
        where x = sumOfDivisor (sumOfDivisor n)

ans = sum [ x | x <- [1..10000], isAmbicable x]

main = print ans
