#! python3


def primes(n):
    """returns prime numbers of given list"""
    all_primes = []
    for possible_prime in range(n):

        prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                prime = False

        if prime:
            all_primes.append(possible_prime)
    return all_primes


def is_prime(n):
    """checks if number is prime"""
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
