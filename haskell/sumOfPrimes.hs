smallestFactor n = head [ x | x <- [2..n], n `mod` x == 0]

primeFactors :: Int -> [Int]
primeFactors 1 = []
primeFactors n =
    let factor = smallestFactor n
    in factor : primeFactors (n `div` smallestFactor n)

answer = sum (2000000 `take` [ x | x <- [1..], length (primeFactors x) == 1])

main :: IO()
main = print answer