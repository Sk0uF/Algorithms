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
    Complexity: O(log(exponent))
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
    Complexity: O(log(exponent))
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
    Complexity: O(log(exponent))

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
    Complexity: O(log(min(a, b))

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
    Complexity: O(log(min(a, b))

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
    Complexity: O(sqrt(number))

    If n is a non prime integer then there is a prime
    p that divides n (p | n) and p^2 <= n. We use the
    same technique to find if n is a prime or not.
    """
    if number == 0 or number == 1:
        return False

    for i in range(2, int(number**(1/2))):
        if number % i == 0:
            return False

    return True


# More research needed to completely understand
# the maths behind the multiplicative modular inverse.
def modular_inverse_extended_euclidean(a, m):
    """
    Modular Inverse - Extended Euclidean
    Complexity: O(log(min(a, b))

    If a and m are coprime, GCD(a, m) = 1 and
    a*x + m*y = 1, then x is the modular inverse.
    """
    gcd, x, y = extended_euclidean(a, m)
    return (x % m + m) % m


def modular_inverse_fermat(a, m):
    """
    Modular Inverse - Fermat
    Complexity: O(logm)

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

    So, we can just find a^(m-2)*mod(m).
    """
    return mod_rec_exponentiate(a, m-2, m)


# print(exponentiate(5, 5))
# print(rec_exponentiate(5, 5))
print(euclidean_gcd(16, 10))
print(extended_euclidean(16, 10))
print(is_prime(11))
print(modular_inverse_fermat(5, 11))
print(modular_inverse_extended_euclidean(5, 11))
