smallestFactor n = head [ x | x <- [2..n], n `mod` x == 0]

primeFactors :: Int -> [Int]
primeFactors 1 = []
primeFactors n =
    let factor = smallestFactor n
    in factor : primeFactors (n `div` smallestFactor n)

factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial (n-1)

digits 0 = []
digits x = x `mod` 10 : digits (x `div` 10)