## Number Theory Stuff.

__Note: This is not a library, it's just stuff I do in my spare time. (I'm sad)__

You can try out the cool codez here: [I'm a link.](https://repl.it/FlFv/0)
This is a list of the functions currently in the file.

- `factors(x)`:<br>
Returns [the factors](http://mathworld.wolfram.com/Factor.html) of `x`, which are all the numbers that can divide into `x`. It's returned as a list. For example, `factors(12) = [12,6,4,3,2,1,]` and `factors(5) = [5,1]`.

- `prime_factors(x)`:<br>
Returns [the prime factors](http://mathworld.wolfram.com/PrimeFactorization.html) of x, which are the unique prime numbers that when multiplied together make `x`. Some examples: `prime_factors(4) = [2,2]`, `prime_factors(12) = [2,2,3]`.


- `factorial(x)`:<br>
Returns [the factorial](http://mathworld.wolfram.com/Factorial.html) of x , using recursion. The factorial of an integer is defined as `x! = x*(x-1)*(x-2)...*1`. For example, `4! = 4*3*2*1 = 4*6 = 24`.

- `gcd(x,y)`:<br>
Returns the gcd of `x` & `y`. This is the biggest factor that both numbers share. If the `gcd(x,y)` is one, then `x` and `y` are said to be co-prime.

- `sieve(x)`:<br>
Returns all the primes up to x from 1, using the [*sieve of erothest... eeratostheniens... eratosthenes... yeah.*](http://mathworld.wolfram.com/SieveofEratosthenes.html). I won't try to explain it.

- `prod(arr)`:<br>
Returns the product of all the items in an array.

- `is_prime(x)`:<br>
Returns true or false, depending on if `x` is [prime](http://mathworld.wolfram.com/PrimeNumber.html). For example: `is_prime(2) = True`, `is_prime(12) = False`.

- `next_prime(x)`:<br>
Returns the prime after `x`, not counting `x` itself.

- `has_duplictaes(list)`:<br>
Returns true or false depending on if the list has any repeated items.

- `mobius(x)`:
Returns the [Möbius function](http://mathworld.wolfram.com/MoebiusFunction.html) of `x`, which is kind of hard to explain. It's a function, denoted `mu(x)`, and returns different results depending on how `x`'s prime factors behave.

- `mertens(x)`:<br>
Returns the sum of all the mobi... moibouse... mobi of under `x`.

- `run_poly(polynomial, num)`:<br>
Given a polynomial and a number, it will run that polynomial. The polynomial is given in the format `[[a,b],[c,d]]` ⤑ `ax^b + cx^d`.

- `derivative_poly(poly, order = 1)`:<br>
Returns the [derivative](http://mathworld.wolfram.com/Derivative.html) of a polynomial using the power rule: `ax^b = (ab)x^(b-1)`.

- `newton_root(poly, limit = 10000, guess = 2)`:<br>
Returns the [root](http://mathworld.wolfram.com/Root.html) (also called the zero) of any polynomial, using [newtons method](http://mathworld.wolfram.com/NewtonsMethod.html).

- `turn_poly_into_str(poly)`:<br>
Attempts to turn a polynomial in the list format into a more human-readable format, however it currently can't do this very well.

- `visual_root_find(poly, guess, limit = 10000)`:<br>
Just a fancy way of looking at the root of a polynomial. Prints three things:

  - Polynomial entered.
  - Root found.
  - Evaluating the polynomial with the root.


- `sumMultiples(limit, firstMultiple, secondMultiple)`:<br> Returns the sum of all the two under `limit`.

- `nthFib(x)`:<br>
Returns the nth fibonacci number.

- `sumFibUnderX(x)`:<br>
Returns the sum of all the fibonacci numbers under x.

- `largest_prime_factor(x)`:<br>
Returns the largest prime factor of `x`.

- `is_palindrome(x)`:<br>
Checks if a number is a palindrome, meaning it can be read the same forwards and backwards.

- `largest_palindrome_product(n)`:<br>
The largest palindromic number that can be made from the product of `n` amount digits.

- `smallest_multiple(arr)`:<br>
Returns the number which divides into everything in the array evenly.

- `difference_between_sumSquares_vs_squareSum(limit)`:<br> Returns the difference between the sum of squares and sum squared.

- `can_be_divided(num, arr)`:<br>
Returns true or false depending on whether num divides everything in the array evenly.

- `nth_prime(x)`:<br>
Returns the nth prime.

- `collatz(x)`:<br>
Returns the length of the [hailstone](http://mathworld.wolfram.com/CollatzProblem.html) sequence for x.

- `longest_collatz_sequence(limit)`: Returns the longest [hailstone](http://mathworld.wolfram.com/CollatzProblem.html) sequence under n.

- `digits(x)`:<br>
Returns a list of all the digits of `x`.

- `digit_product(x)`:<br>
Returns a product of all the digits in `x`.

- `digits_to_num(arr)`:<br>
Returns the number made up of the list of digits (it inverses digits).

- `largest_digit_product(x, bite)`:<br>
Returns the largest number that is made from multiplying a section of the digits `x`, which is `bite` long.

- `is_pythagorean_triple(arr)`:<br>
Checks if the three items in the array are a [pythagorean triple](http://mathworld.wolfram.com/PythagoreanTriple.html).

- `sum_of_primes(limit)`:<br>
Returns the sum of all primes underneath limit.

- `totient(n)`:<br>
Returns the [Euler's phi(n)](http://mathworld.wolfram.com/TotientFunction.html), which is equal to the number of numbers that are co-prime with n.

- `lambert_w(x)`:<br>
Returns the [product log](http://mathworld.wolfram.com/LambertW-Function.html) of x, which is equal to the inverse of `f(x) = xe^x`.

- `sum_digits(x)`:<br>
Returns the sum of the digits in a number.

- `nth_tri(x)`:<br>
Returns the nth [triangle number](http://mathworld.wolfram.com/TriangularNumber.html).

- `first_triangle_with_x_divisors(x)`:<br>
Returns the first triangle number that has more than or equal to `x` divisors, or in other words more than or equal to `x` factors.

- `goldbach(x)`:<br>
Returns the [two primes that when added together](http://mathworld.wolfram.com/GoldbachConjecture.html) make x. This usually only works for even x.

- `number_length(x)`:<br>
Returns the length of a number's digits, not counting the decimal point.

- `length_of_decimal(x)`:<br>
Returns how many decimal places there are in x.

- `add_fractions(frac_1, frac_2)`:<br>
Returns the fraction made when two fractions are added together. This is done using the rule `a/b + c/d = (ad+bc)/bd`. `frac_1` & `frac_2` are both strings in the format `"1/2"` and `"25/81"`.

- `convert_to_fraction(x)`:<br>
Turns a number into a fraction. It's currently a bit dodgy with big numbers.

- `continued_fraction(x, limit)`:<br>
Works out the [simple continued fraction](http://mathworld.wolfram.com/SimpleContinuedFraction.html) of `x` up to a limit, which is a way of expressing any number as a fraction.

- `continued_fraction_at_point(x, limit, fraction = False)`:<br>
Works out the number made when you stop a continued fraction at a point.

- `gamma(x)`:<br>
Returns the [gamma](http://mathworld.wolfram.com/GammaFunction.html) of `x`, which is the factorial function analytically extended to negative & non-integer inputs.

- `tetrarion(x, limit)`:<br>
Returns the fourth [hyperoperation](https://en.m.wikipedia.org/wiki/Hyperoperation), the [iterated exponential function](https://en.m.wikipedia.org/wiki/Tetration). Basically, it returns `x^^limit`, which means `x^x^x...`, `limit` amount of times. Hey, it even supports infinite limits! You can use it like so: `tetrarion(1.4, infinity)` = `1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^...`. However, this only [converges](https://en.m.wikipedia.org/wiki/Limit_(mathematics)) on the interval `[e^(-e), e^(1/e)]`, which is roughly `[0.06, 1.44]`.

- `square_super_root(x)`:<br>
Returns the `ssrt(x)`, which is the number `y` such that `x^x` = `y`.

- `zeta(s, limit = 10000)`:<br>
Returns [the zeta](http://mathworld.wolfram.com/RiemannZetaFunction.html) of `s`, which is a special function in number theory, as it is deeply connected with prime numbers.
