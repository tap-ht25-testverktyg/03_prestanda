
def is_prime_2(n):
    """Returnera True om n är ett primtal."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


def get_primes_2(amount):
    """Returnera en lista med de amount första primtalen.
    Tidskomplexitet: O(n^2)
    """
    primes = []
    i = 2
    while len(primes) < amount:
        if is_prime_2(i):
            primes.append(i)
        i += 1
    return primes


