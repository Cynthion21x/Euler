sum3or5 xs = sum [ x | x <- xs, ((x `mod` 3) == 0) || ((x `mod` 5) == 0)]

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

sumEven = sum [ x | x <- takeWhile (<4000000) fibs, even x] 

