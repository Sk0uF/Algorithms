def modulo_properties():
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


def exponentiate(number, exponent):
    """
    O(log(exponent))
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
    O(log(exponent))
    """
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return rec_exponentiate(number**2, exponent//2)
    else:
        return number * rec_exponentiate(number**2, exponent//2)


def euclidean_gcd(a, b):
    """
    O(log(min(a, b))
    """
    if b == 0:
        return a

    return euclidean_gcd(b, a % b)


def is_prime(number):
    """
    O(sqrt(number))
    """
    if number == 0 or number == 1:
        return False

    for i in range(2, int(number**(1/2))):
        if number % i == 0:
            return False

    return True


# print(exponentiate(5, 5))
# print(rec_exponentiate(5, 5))
print(euclidean_gcd(16, 10))
print(is_prime(11))