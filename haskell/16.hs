quicksort [] = []
quicksort (p:xs) = (quicksort small) ++ [p] ++ (quicksort big)
    where
        small = filter (< p) xs
        big = filter (>= p) xs
