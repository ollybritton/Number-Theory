import math
from fractions import Fraction

pi = math.pi
tau = 2*pi
e = math.e
epsilon = 0.000000001
phi = (1+math.sqrt(5))/2
infinity = float("infinity")

def factors(x):
    factors = []
    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)

    return factors

def prime_factors(x):
    i = 2
    factors = []
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            factors.append(i)
    if x > 1:
        factors.append(x)
    return factors

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def sieve(x):
    size = x//2
    prime_sieve = [1]*size
    limit = int(x**0.5)
    for i in range(1,limit):
        if prime_sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            prime_sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(prime_sieve) if v and i>0]

def prod(arr):
    product = 1
    for i in range(0, len(arr)):
        product *= arr[i]

    return product

def is_prime(x):
    if( sum(factors(x)) == x+1 ):
        return True
    else:
        return False

def next_prime(x):
    prime = x+1
    while True:
        if( is_prime( (prime) ) ):
            break
        else:
            prime += 1

    return prime

def has_duplictaes(list):
    return (len(list) != len(set(list)))

def mobius(x):
    if( has_duplictaes( prime_factors(x) ) == True ):
        return 0
    elif ( x == 1 ):
        return 1
    else:
        return -1**len(prime_factors(x))

def mertens(x):
    addition = 0
    for i in range(1, x+1):
        addition += mobius(i)

    return addition

def run_poly(poly, num):
    # [[coefficent, power],[coefficent, power],[coefficent, power]...]
    addition = 0
    for i in range(0, len(poly)):
        term = (num**poly[i][1])*poly[i][0]
        addition += term

    return addition

def transform_poly_into_array(string):
    string = list(string)


def derivative_poly(poly, order = 1):
    # [x,y] -> [xy, y-1]
    derivative = []
    for i in range(0, len(poly)):
        partOne = poly[i][0]*poly[i][1]
        partTwo = poly[i][1]-1

        if partOne < 0:
            partOne = 0

        if partTwo < 0:
            partTwo = 0

        derivative.append( [poly[i][0]*poly[i][1], poly[i][1]-1] )

    return derivative

def newton_root(poly, limit = 10000, guess = 2):
    derivative = derivative_poly(poly)
    previous = guess
    nextVal = 0

    for i in range(0, limit):
        nextVal = previous - ( run_poly(poly, previous) )/( run_poly(derivative_poly(poly), previous) )
        previous = nextVal

    return previous

def turn_poly_into_str(poly):
    string = ""
    for i in range(0, len(poly)):
        if i != len(poly)-1:
            coefficent = ""
            if poly[i][0] != 1:
                coefficent = str(poly[i][0])

            power = ""
            if poly[i][1] != 1:
                power = "^" + str(poly[i][1])

            string += coefficent + "x" + power + " + "

        else:
            coefficent = ""
            if poly[i][0] != 1:
                coefficent = str(poly[i][0])

            power = ""
            if poly[i][1] != 1:
                power = "^" + str(poly[i][1])

            string += coefficent + "x" + power

    return string


def visual_root_find(poly, limit = 10000, guess = 2):
    root = newton_root(poly, limit, guess)
    polyStr = turn_poly_into_str(poly)
    check = polyStr.replace("x", " " + str(root))

    print("Polynomial Enterered: " + polyStr)
    print("Root Found: " + str(root))
    print("Check: " + str(check) + " = " + str(run_poly(poly, root)))

def sumMultiples(limit, firstMultiple, secondMultiple):
    sum = 0
    for i in range(0, limit):
        if i % firstMultiple == 0 or i % secondMultiple == 0:
            sum += i

    return sum

def nthFib(n):
    if n <= 1:
        return 1
    else:
        return nthFib(n-1) + nthFib(n-2)

def sumFibUnderX(x):
    sum = 0
    i = 1
    while True:
        print(i)
        if nthFib(i) > x:
            break
        else:
            if nthFib(i) % 2 == 0:
                sum += nthFib(i)

        i += 1

    return sum


def largest_prime_factor(x):
    return max(prime_factors(x))

def is_palindrome(x):
    new = list( str(x) )[::-1]
    return new == list( str(x) )

def largest_palindrome_product(digits):
    allNums = []
    for i in range(10**(digits-1), (10**digits)-1):
        for j in range(10**(digits-1), (10**digits)-1):
            if is_palindrome(i*j):
                allNums.append(i*j)

    return max(allNums)

def smallest_multiple(arr):
    i = 1
    while True:
        if can_be_divided(i, arr):
            return i
        else:
            i += 1


def difference_between_sumSquares_vs_squareSum(limit):
    numbers = []
    for i in range(1, limit+1):
        numbers.append(i)

    sumSquares = sum(map(lambda x: x**2, numbers))
    squareSum = sum(numbers)**2

    return squareSum - sumSquares


def can_be_divided(num, arr):
    count = 0
    for i in range(0, len(arr)):
        if num % arr[i] == 0:
            count += 1
        else:
            count -= 1

    return count == len(arr)

def nth_prime(x):
    i = 1
    count = 0
    while True:
        if(count == x):
            return i
        else:
            i = next_prime(i)
            count += 1

def collatz(x, count = 1):
    if x == 1:
        return count

    if x % 2 == 0:
        return collatz(x/2, count + 1)
    else:
        return collatz((3*x)+1, count + 1)

def longest_collatz_sequence(limit):
    numbers = []
    for i in range(1, limit+1):
        numbers.append(i)

    numbers = map(lambda x: collatz(x), numbers)
    return max(numbers)

def max_prime_factor(x):
    return max(prime_factors(x))

def digits(x):
    return [int(d) for d in str(x)]

def digit_product(x):
    product = 1
    x_digits = x
    for i in range(0, len(x_digits)):
        product *= x_digits[i]

    return product

def digits_to_num(arr):
    string = ""
    for i in range(0, len(arr)):
        string += str(arr[i])

    return int(string)

def largest_digit_product(x, bite):
    x_digits = digits(x)
    arr_of_digits = []
    products = []
    for i in range(0, len(x_digits) - bite):
        arr_of_digits.append( x_digits[i:i+bite] )

    print(arr_of_digits)
    for i in range(0, len(arr_of_digits)):
        products.append( digit_product(arr_of_digits[i]) )

    return max(products)

def is_pythagorean_triple(arr):
    return arr[0]**2 + arr[1]**2 == arr[2]**2

def sum_of_primes(limit):
    return sum(sieve(limit))

def totient(n):
    summation = 0
    for k in range(1, n+1):
        summation += gcd(k,n)*math.cos((tau*k)/n)

    return summation

def lambert_w(x, limit = 100):
    w = x
    while True:
        ew = math.exp(w)
        wNew = w - (w * ew - x) / (w * ew + ew)
        if abs(w - wNew) <= epsilon: break
        w = wNew
    return w

def sum_digits(x):
    return sum(digits(x))

def nth_tri(x):
    return (x*(x+1))/2

def first_triangle_with_x_divisors(x):
    i = 0
    leFin = 0
    while True:
        print(i, nth_tri(i))
        if len(factors(nth_tri(i))) >= x:
            leFin = i
            break


        i += 1

    return nth_tri(leFin)

def goldbach(x):
    for i in range(0, x):
        for j in range(0, x):
            if i+j == x and is_prime(i) and is_prime(j):
                return i,j

def calculateLimit(poly, value):
    leftSum = run_poly(poly, value - 10**(-10))
    rightSum = run_poly(poly, value + 10**(-10))

    return (leftSum+rightSum)/2

def number_length(x):
    return len(str(x).replace('.',''))

def length_of_decimal(x):
    return len(str(x).split("_", 1)[-1])

def add_fractions(frac_1, frac_2):
    frac_1 = frac_1.split("/")
    frac_2 = frac_2.split("/")

    numerator = [int(frac_1[0]), int(frac_2[0])]
    denominator = [int(frac_1[1]), int(frac_2[1])]

    top = numerator[0]*denominator[1] + denominator[0]*numerator[1]
    bottom = denominator[0] * denominator[1]

    gcdNum = gcd(top, bottom)
    top /= gcdNum
    bottom /= gcdNum

    return str(top) + "/" + str(bottom)

    # a/b + c/d = ad+bc/bd

def convert_to_fraction(x):
    return str(Fraction(x))


def continued_fraction(x, limit):
    expansion = []
    prev = x
    nxt = 0

    for i in range(0, limit):
        nxt = 1/(prev - math.floor(prev))
        expansion.append( int(math.floor(prev)))
        prev = nxt

    return expansion

def continued_fraction_at_point(x, limit, fraction = True):
    continued = continued_fraction(x, limit)
    summation = 0

    for i in range(1, limit):
        summation = 1/(continued[-i]+summation)

    if(fraction == True):
        return str(Fraction(summation + continued[0]))
    else:
        return summation + continued[0]

def gamma(x):
    return math.gamma(x)

def tetrarion(x, limit):
    if limit == infinity:
        # return (lambert_w( -math.log(x) ))/(-math.log(x))
        if x < e**(1/e) and x > e**(-e) and x != 1:
            return (lambert_w( -math.log(x) ))/(-math.log(x))
        elif x == 1:
            return 1
        else:
            return infinity

    else:
        powers = x
        for i in range(0, limit):
            powers = powers**x

        return powers

def square_super_root(x):
    # Number y such that x^x = y
    return math.exp(lambert_w( math.log(x) ))

def eta(s, limit = 10000):
    summation = 0
    for k in range(1, limit+1):
        numerator = (-1)**(k-1)
        denominator = k**s

        summation += float(numerator)/float(denominator)

    return summation


def zeta(s, limit = 10000):
    return eta(s)/(1-(2**(1-s)))

def pi_prime_count(x):
    return len(sieve(x))

def is_perfect(x):
    return sum(factors(x))-x == x

def next_perfect(x):
    i = x+1
    while is_perfect(i) != True:
        i += 1

    return i

def nth_perfect(x):
    curr = 0
    for i in range(0, x):
        curr = next_perfect(curr)

    return curr

def three_numbers_that_sum_to_x(x):
    vals = []
    for i in range(1, x):
        for j in range(1, x):
            for k in range(1, x):
                if i+j+k == x:
                    vals.append([i,j,k])

    return vals

def pythagorean_triples_up_that_sum_to_x(x):
    vals = []
    partitions = three_numbers_that_sum_to_x(x)
    for i in range(0, len(partitions)):
        if is_pythagorean_triple(partitions[i]):
            vals.append(partitions[i])

    return vals

def navigate_grid(arr, row_length, curr, direction):
    # 1 = Down, -1 = Up
    # 2 = Forwards, -2 = Backwards
    # 3 = Diagonally Downwards, -3 = Diagonally Upwards.

    if row_length**2 != len(arr) or row_length < 2:
        print("The grid is to small or it isn't a square at that row_length.")
        return None

    if direction == 1:
        return arr[curr + row_length]
    elif direction == -1:
        return arr[curr - row_length]
    elif direction == 2:
        return arr[curr + 1]
    elif direction == -2:
        return arr[curr - 1]
    elif direction == 3:
        return arr[curr + (row_length + 1)]
    elif direction == -3:
        return arr[curr - (row_length - 1)]

def number_of_ways_through_n_by_n_grid(n):
    return (factorial(2*n))/(factorial(n)**2)

def digit_sum(x):
    return sum(digits( x ))

def nth_bernoulli(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fraction(1, m+1)
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
    return A[0]

print( nth_bernoulli(4) )
