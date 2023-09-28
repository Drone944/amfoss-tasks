loop2 :: Int -> Bool
loop2 n
  | n <= 1 = False
  | n == 2 = True
  | otherwise = all (\x -> n `mod` x /= 0) [2..n-1]

loop1 :: Int -> [Int]
loop1 n = filter loop2 [2..n]

main :: IO ()
main = do
  putStrLn "Enter a number :"
  input <- getLine
  let n = read input :: Int
  let p = loop1 n
  if n==0||n==1
  then putStrLn (show n ++ " is neither a prime or a composite number.")
  else  print p