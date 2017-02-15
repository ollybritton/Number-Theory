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
- `digits(x)` -> Returns a list of all the digits of x.
- `digit_product(x)` -> Returns a product of all the digits.
- `digits_to_num(arr)` -> Returns the number made up of the list of digits.
- `largest_digit_product(x, bite)` -> Returns the largest number that is made by taking the product of a group of digits in the range of bite.
- `is_pythagorean_triple(arr)` -> Checks if whether three items in an array are a pythagorean triple.
- `sum_of_primes(limit)` -> Returns the sum of all primes underneath limit.
- `totient(n)` -> Returns the phi(n), which is equal to the number of numbers that are co-prime with n.
- `lambert_w(x)` -> Returns the y when `y*exp(y) = x`.
- `sum_digits(x)` -> Returns the sum of the digits in a number.
- `nth_tri(x)` -> Returns the nth triangle number.
- `first_triangle_with_x_divisors(x)` -> Returns the first triangle number that has over x divisors, or factors.
- `goldbach(x)` -> Returns the two primes that when added together make x... usually only works for even x.
- `number_length(x)` -> Returns the length of a number's digits.
- `length_of_decimal(x)` -> Returns how many decimal places there are in x.
- `add_fractions(frac_1, frac_2)` -> Returns the fraction made when two fractions are added together. `frac_1` & `frac_2` are both strings.
- `convert_to_fraction(x)` -> Turns a number into a fraction. It's a bit dodgy with big numbers.
- `continued_fraction(x, limit)` -> Works out the continued fraction of x up to a limit.
- `continued_fraction_at_point(x, limit, fraction = False)` -> Works out the number made when the continued fraction is cut of at that point. Setting fraction to true will give it as a fraction, although it's not always accurate.
- `gamma(x)` -> Returns the gamma (factorial) of x.
- `tetrarion(x, limit)` -> Returns `x^x^x^x...` limit amount of times.
- `square_super_root(x)` -> Returns the number such that x^x = y.
