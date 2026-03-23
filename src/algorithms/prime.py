
def is_prime(n):
    """Returnera True om n är ett primtal."""
    if n < 2:
        return False

    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def get_primes(amount):
    """Returnera en lista med de amount första primtalen."""
    pass

