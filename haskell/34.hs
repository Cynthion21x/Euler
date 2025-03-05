factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial (n - 1)

digits 0 = []
digits x = x `mod` 10 : digits (x `div` 10)

sumOfFact n = sum [ factorial x | x <- digits n] 

answer = [ x | x <- [1..], sumOfFact x == x]

