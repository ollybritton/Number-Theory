## Some Number Theory Stuff.

_ Note: This is not a library, it's just stuff I do in my spare time._

This is a list of the functions currently in the file.

- `factors(x)` -> Returns the factors of x. (Duh...)
- `prime_factors(x)` -> Returns the prime factors of x.
- `factorial(x)` -> Returns the factorial of x , using recursion.
- `gcd(x,y)` -> Returns the gcd of x & y.
- `sieve(x)` -> Returns all the primes up to x.
- `prod(arr)` -> Returns the product of all the items in the array.
- `is_prime(x)` -> Returns true or false, depending on if x is prime.
- `next_prime(x)` -> Returns the prime after x.
- `primes_under_x(x)` -> Returns a list of all the primes under x.
- `has_duplictaes(list)` -> Returns true or false depending on if the list has any repeated items.
- `mobius(x)` -> Returns the mobius function of x, which is kind of hard to explain.
- `mertens(x)` -> Returns the sum of all the mobi... mobien... mobiuses... I don't know; the sum of all the mobi under x.
- `run_poly(poly, num)` -> Runs a polynomial. The polynomials are given in the format: [[coefficent, power], [coefficent,power]...]. So [[1,2],[1,0]] is equal to `1x**2 + 1`.
- `derivative_poly(poly, order = 1)` -> Returns the nth derivative of a polynomial using the power rule.
- `newton_root(poly, guess, limit = 10000)` -> Returns the real root of any polynomial using newton's method.
- `turn_poly_into_str(poly)` -> Attempts to turn a list into a text-polynomial.
- `visual_root_find(poly, guess, limit = 10000)` -> Just a fancy way of looking at the root of a polynomial and checking it.
- `sumMultiples(limit, firstMultiple, secondMultiple)` -> Returns the sum of all the multiples under limit.
- `nthFib(x)` -> Have a guess.
- `sumFibUnderX(x)` -> Returns the sum of all the fibbonaci numbers under x.
- `largest_prime_factor(x)` -> Returns the largest prime factor of x.
- `is_palindrome(x)` -> Checks if a number is a palindrome.
- `largest_palindrome_product(digits)` -> The largest product of digits that will make a palindrome.
- `smallest_multiple(arr)` -> Returns the number which divides into everything in the array evenly.
- `difference_between_sumSquares_vs_squareSum(limit)` -> Returns the difference between the sum of squares and sum squared.
- `can_be_divided(num, arr)` -> Returns true or false depending on whether num divides everything in the array evenly.
- `nth_prime(x)` -> Returns the nth prime.
- `collatz(x)` -> Returns the length of the hailstone sequence for x.
- `longest_collatz_sequence(limit)` -> Returns the longest collatz sequence under n.

__NEEDS TO BE FINISHED.__
