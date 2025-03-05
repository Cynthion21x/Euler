sumSquared = (sum [ x | x <- [1..100]]) ^ 2
sumOfSquares = sum [ x^2 | x <- [1..100]]

answer = sumSquared - sumOfSquares