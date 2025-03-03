triangleNum n = n * (n + 1) `div` 2

countDivisors n = 
  let sqrtN = floor (sqrt (fromIntegral n))
  in length [d | d <- [1..sqrtN], n `mod` d == 0] * 2 - (if sqrtN * sqrtN == n then 1 else 0)

findTriangleNumber = head [t | n <- [1..], let t = triangleNum n, countDivisors t > 500]