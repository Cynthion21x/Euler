triangleNum :: Integral a => a -> a
triangleNum n = n * (n + 1) `div` 2


countDivisors :: Integral a => a -> Int
countDivisors n = 
  let sqrtN = floor (sqrt (fromIntegral n))
  in length [d | d <- [1..sqrtN], n `mod` d == 0] * 2 - (if sqrtN * sqrtN == n then 1 else 0) 

findTriangleNumber :: Integer
findTriangleNumber = head [t | n <- [1..], let t = triangleNum n, countDivisors t > 500]

main :: IO ()
main = print findTriangleNumber