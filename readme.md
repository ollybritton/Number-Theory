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
Returns the sum of all primes underneath the limit.

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
Works out the number made when you stop a continued fraction at a point. **WIP**

- `gamma(x)`:<br>
Returns the [gamma](http://mathworld.wolfram.com/GammaFunction.html) of `x`, which is the factorial function analytically extended to negative & non-integer inputs.

- `tetrarion(x, limit)`:<br>
Returns the fourth [hyperoperation](https://en.m.wikipedia.org/wiki/Hyperoperation), the [iterated exponential function](https://en.m.wikipedia.org/wiki/Tetration). Basically, it returns `x^^limit`, which means `x^x^x...`, `limit` amount of times. Hey, it even supports infinite limits! You can use it like so: `tetrarion(1.4, infinity)` = `1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^1.4^...`. However, this only [converges](https://en.m.wikipedia.org/wiki/Limit_(mathematics)) on the interval `[e^(-e), e^(1/e)]`, which is roughly `[0.06, 1.44]`.

- `square_super_root(x)`:<br>
Returns the `ssrt(x)`, which is the number `y` such that `x^x` = `y`.

- `zeta(s, limit = 10000, etaOptim = True)`:<br>
Returns [the zeta](http://mathworld.wolfram.com/RiemannZetaFunction.html) of `s`, which is a special function in number theory, as it is deeply connected with prime numbers. This can be done in one of two ways, the first being with the `eta` function, denoted `η(s)`. This is the defualt method allows for more precision with less iterations (see below). The second, which occurs when `etaOptim = False`, will have less precision (why would you even wan't to):
`zeta(2, 1000) - zeta(2, 1000, False) = 0.00099949016765`

- `pi_prime_count(x)`:<br>
Returns `π(x)`, the number of primes under `x`.

- `is_perfect(x)`:<br>
Returns true or false depending on whether `x` is a [perfect number](http://mathworld.wolfram.com/PerfectNumber.html). A perfect number is a number where the sum of its factors (bar itself) is equal to the number. For example: `6 -> [1,2,3] = 1+2+3 = 6`.

- `next_perfect(x)`:<br>
The next perfect number after `x`, excluding `x`.

- `nth_perfect(x)`:<br>
The nth perfect number.

- `three_numbers_that_sum_to_x(x)`:<br>
All the combinations of three numbers that add up to `x`. This is linked closely to [partitions](http://mathworld.wolfram.com/Partition.html), which is the amount of ways you can write `n` as a sum of any amount of numbers.

- `pythagorean_triples_up_that_sum_to_x(x)`:<br>
Kind of self explanatory, it gives you a list of all the pythagorean triples that when added together equal your number. For example, `pythagorean_triples_up_that_sum_to_x(30) = [[5,12,13],[12,5,13]]`. Note: For some numbers there will be no solutions.

- `navigate_grid(arr, row_length, curr, direction)`:<br>
Used to navigate a grid. Imagine you have the 4x4 grid,
      1  2  3  4
      5  6  7. 8
      9  10 11 12
      13 14 15 16

    And you you are on 7 (indicated by the dot). This code allows you to navigate up, down, left, right, up diagonally and down diagonally. These all have their own commands:

  - `1`: Down.
  - `-1`: Up.
  - `2`: Forwards.
  - `-2`: Backwards.
  - `3`: Diagonally downwards.
  - `-3`: Diagonally upwards.


- `number_of_ways_through_n_by_n_grid(n)`:<br>
Returns the number of ways you can travel through an `n` by `n` grid. This is done using the formula `2n!/2(n!)`.

- `digit_sum(x)`:<br>
Returns the sum of the digits of a number.

- `nth_bernoulli(n)`:<br>
Returns the `nth` [bernoulli number](http://mathworld.wolfram.com/BernoulliNumber.html), a number which arises in many taylor expansions of functions.

- `prime_zeta(s, limit)`:<br>
Executes the prime zeta function, which is defined as the sum of all the reciprocals of primes to the power of s:

        1/2^s + 1/3^s + 1/5^s + 1/7^s ...

  *Note: Amazingly, the sum of all the reciprocals of primes diverges to infinity, but really, really slowly.*

- `convert_polynomial_to_string(poly, omit_ones = True)`:<br>
Does what it says on the tin. Converts a polynomial in the format `[[a,b],[c,d]]` ⤑ `ax^b + cx^d` into
a human-readable format. If `omit_ones` is equal to false, than the code will allow `[1,1]` ⤑ `1x`, not `x`.

- `general_sum(n, x, func)`:<br>
A general summation using the mathematical sigma notation, `Σ`. `n` is the limit, `x` is the starting value and
`func` is the function that is applied to all of the numbers. It adds up all the numbers from `x` through to `n`
and applies a function to each number. For example, you can write the nth triangle number like so:

      general_sum(*10*, 1, lambda x: x) = 10th Triangle Number, 55

- `general_product(n, x, func)`:<br>
A general product using the mathematical capital pi notation, `π`. `Σ`. `n` is the limit, `x` is the starting value and
`func` is the function that is applied to all of the numbers. It returns the product of the numbers `x` through `n` all
with a function applied to them. For example, you could write (15!\**2) as:

      general_product(15, 1, lambda x: x**2)

- `ackerman(x, y)`:<br>
Returns the ackerman function of `x` and `y`. The ackerman function is a function in number theory that is **add more detail**.

- `diagonal(x)`:<br>
Returns the value of `ackerman(x, x)`. This grows super fast – after just `x = 4`, python can't handle it.

- `evaluate_term(string)`:<br>
Converts a term of a polynomial in the format `ax^b` into the array format `[a,b]`. Also allows things like `a` and `ax`.

- `convert_string_into_polynomial`:<br>
Converts an entire polynomial in the format `ax^b + cx^d + ...` into the array format `[[a,b], [c,d], ...]`.

- `random_polynomial(order, pretty = False)`:<br>
Generates a random polynomial that has order of `order` (funny that, huh?). If `pretty` is set to `True`, it will return the polynomial but coverted into a human readable format.
