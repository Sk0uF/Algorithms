def modulo_properties():
    """
    Some properties of the modulo operation.
    """
    a = 153312
    b = 81273
    c = 132

    # Modulo properties
    print("(a+b)%c = (a%c + b%c)%c")
    print((a+b) % c)
    print((a % c + b % c) % c)
    print()

    print("(a-b)%c = (a%c - b%c)%c")
    print((a-b) % c)
    print((a % c - b % c) % c)
    print()

    print("(a*b)%c = (a%c * b%c)%c")
    print((a*b) % c)
    print((a % c * b % c) % c)
    print()

    # Where b^-1 is the multiplicative modulo inverse of b and c.
    # It doesn't always exist! The property is b*b^-1 Ξ 1 mod c
    # and b^-1 < c. It exists only if b and c are coprime, meaning
    # that GCD(b, c) = 1 or c is prime.
    print("(a/b)%c = (a%c * b^-1%c)%c")


def exponentiate(number, exponent):
    """
    Exponentiation - serial method
    Complexity: O(logEXPONENT)
    """
    if exponent == 2:
        return number ** 2

    if exponent == 1:
        return number

    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = number * result

        number = number ** 2
        exponent //= 2
    return result


def rec_exponentiate(number, exponent):
    """
    Exponentiation - recursive method
    Complexity: O(logEXPONENT)
    """
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return rec_exponentiate(number**2, exponent//2)
    else:
        return number * rec_exponentiate(number**2, exponent//2)


def mod_rec_exponentiate(number, exponent, mod):
    """
    Modular exponentiation - recursive method
    Complexity: O(logEXPONENT)

    Sometimes, when the number can be extremely big, we find
    the answer modulo some other number. We can do it in both
    the recursive and the serial way. For simplicity we just
    implement it in the recursive method.
    """
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return mod_rec_exponentiate((number**2) % mod, exponent//2, mod)
    else:
        return number * mod_rec_exponentiate((number**2) % mod, exponent//2, mod) % mod


def euclidean_gcd(a, b):
    """
    Euclidean algorithm
    Complexity: O(log(min(A, B))

    Euclidean algorithm to find the GCD of two
    numbers. It takes advantage of the property
    GCD(a, b) = GCD(b, a%b).
    """
    if b == 0:
        return a

    return euclidean_gcd(b, a % b)


def extended_euclidean(a, b):
    """
    Extended Euclidean algorithm
    Complexity: O(log(min(A, B))

    Find x and y in the problem a*x + b*y = GCD(a, b).
    The above equation is based in the property
    GCD(a, b) = GCD(b, a%b).
    """
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def is_prime(number):
    """
    Find if a number is prime
    Complexity: O(sqrt(NUMBER))

    If n is a non prime integer then there is a prime
    p that divides n (p | n) and p^2 <= n. We use the
    same technique to find if n is a prime or not.
    """
    if number == 0 or number == 1:
        return False

    # The +1 includes the number. For example if the number is 49
    # then the sqrt is 7 and the code would run from 2 to 6. That's
    # why we add the +1.
    #
    # We can implement the same thing with a while statement like:
    # while i*i <= number but that's slower because it solves the
    # exact same problem but sqrt's implementation is faster.
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


# More research needed to completely understand
# the maths behind the multiplicative modular inverse,
# the reasoning behind the Eratosthenes sieve complexity
# as well as the Eratosthenes sieve complexity for segments.
def modular_inverse_extended_euclidean(a, m):
    """
    Modular Inverse - Extended Euclidean
    Complexity: O(log(min(A, B))

    If a and m are coprime, GCD(a, m) = 1 and
    a*x + m*y = 1, then x is the modular inverse.
    """
    gcd, x, y = extended_euclidean(a, m)
    return (x % m + m) % m


def modular_inverse_fermat(a, m):
    """
    Modular Inverse - Fermat
    Complexity: O(logM)

    When m is prime and a integer, not a multiple of m,
    we can find the multiplicative modulo inverse of a and m
    using Fermat's little theorem: a^(m-1) Ξ 1 mod m. In
    general, Fermat's little theorem state that if m is a
    prime number, then for any integer a, the number a^m - a
    is an integer multiple of m, or a^m Ξ a mod m. The modular
    inverse of a number a, is the number a^-1 for which
    a*a^-1 Ξ 1 mod m or (a * a^-1) mod m = 1. From Fermat's
    little theorem we can say:

    a*a^(m-2) Ξ 1 mod m
    a*a^-1 Ξ 1 mod m

    So, it's clear that the a^-1 is a^(m-2). Continuing, we have
    [a*mod(m) * a^(m-2)*mod(m)]mod(m) = 1
    [a*mod(m) * a^-1*mod(m)]mod(m) = 1

    So, we can just find a^(m-2)*mod(m). Note that the inverse must
    be < m, thus a^-1 and a^-1*mod(m) is the exact same number.
    """
    return mod_rec_exponentiate(a, m-2, m)


def eratosthenes_sieve(n):
    """
    Sieve of Eratosthenes
    Complexity: O(NloglogN)

    We can find all the prime number up to specific
    point. This technique is based on the fact that
    the multiples of a prime number are composite numbers.
    That happens because a multiple of a prime number will
    always have 1, itself and the prime as a divisor (maybe
    even more) and thus, it's not a prime number. A common
    rule for sieves is that they have O(logn) complexity.
    """
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    final_primes = []
    for i in range(len(primes)):
        if primes[i]:
            final_primes.append(i)

    return final_primes


def segment_eratosthenes_sieve(l, r):
    """
    Sieve of Eratosthenes for segments
    Complexity: ?????

    Only useful when we can create an array
    of length R-L+1.
    """
    primes = [True] * (r-l+1)
    final_primes = []
    for i in range(2, int(r**0.5) + 1):
        for j in range(max(i*i, (l+i-1) // i * i), r+1, i):
            primes[j-l] = False

    for i in range(max(l, 2), r+1):
        if primes[i-l]:
            final_primes.append(i)

    return final_primes


def mod_sqrt_fact_eratosthenes_sieve(n):
    """
    Something like a sieve of Eratosthenes for factorization - 1
    Complexity: O(sqrt(N))

    We can find all the factors of a number using a simple
    alternation to the Eratosthenes sieve. Factors are the
    numbers you multiply to get another number. Those numbers
    can be written as prime only numbers. Why? Lets take the
    number 20 for example. Its factors are 4 and 5, or 2 and 10
    etc. All of these can be written as 2 * 2 * 5 though, which
    is unique. It becomes obvious that every non prime number
    can be written as the multiplication of primes. As already
    states if n is non prime then there is a prime that divides
    it and p^2 <= n and that's the reason why we loop only up
    to sqrt(n). We basically find the minimum prime that divides
    our number. When we find it, we divide the number by that
    prime and we continue the same process.
    """
    factorial = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factorial.append(i)
            n //= i

    if n != 1:
        factorial.append(n)

    return factorial


def mod_log_fact_eratosthenes_sieve(n):
    """
    Something like a sieve of Eratosthenes for factorization - 2
    Complexity: O(logN) - assuming we have precomputed some values

    If for some reason we have found the minimum prime factor for
    all the numbers up to the number we want to factorize then we
    can factorize with that technique. We can do that in O(NloglogN)
    using the original Eratosthenes sieve. Thus, this O(logN) is
    misleading. We also need to be able to create an array of length
    N, which may not be effective in cases where N is very big.
    """
    # Finding the minimum prime factor for every number up to n
    # using Eratosthenes sieve in O(NloglogN) time.
    min_prime = [0] * (n+1)
    for i in range(2, int(n**0.5) + 1):
        if min_prime[i] == 0:
            for j in range(i*i, n+1, i):
                if min_prime[j] == 0:
                    min_prime[j] = i

    for i in range(2, n+1):
        if min_prime[i] == 0:
            min_prime[i] = i

    # Finding the factors in O(logN) time.
    factorial = []
    while n != 1:
        factorial.append(min_prime[n])
        n //= min_prime[n]

    return factorial, min_prime


# print(exponentiate(5, 5))
# print(rec_exponentiate(5, 5))
# print(euclidean_gcd(16, 10))
# print(extended_euclidean(16, 10))
# print(is_prime(49))
# print(modular_inverse_fermat(5, 11))
# print(modular_inverse_extended_euclidean(5, 11))
# print(eratosthenes_sieve(20))
# print(mod_sqrt_fact_eratosthenes_sieve(20))
# print(mod_log_fact_eratosthenes_sieve(20))
# print(segment_eratosthenes_sieve(0, 20))
