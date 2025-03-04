sumOfDigits n
        | n < 10 = n
        | otherwise = (n `mod` 10) + sumOfDigits (n `div` 10)

factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial (n-1)
