
-- Define Kleisli category for partial functions (define composition and identity).


data Option a = None | Some a deriving Show

-- Composition
(>=>) :: (a -> Option b) -> (b -> Option c) -> (a -> Option c)
f >=> g = \x -> case f x of
                  None -> None
                  Some y -> g y

-- Identity
id' :: a -> Option a
id' = Some

safeRoot :: Double -> Option Double
safeRoot x = if x >= 0 then Some (sqrt x) else None

safeReciprocal :: Double -> Option Double
safeReciprocal x = if x /= 0 then Some (1/x) else None

combined :: Double -> Option Double
combined = safeRoot >=> safeReciprocal

main = do
  putStrLn $ show $ combined 10.0
  putStrLn $ show $ combined 0.0
  putStrLn $ show $ combined (-1.0)
