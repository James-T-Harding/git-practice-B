import math


def is_prime(value):
    if value < 2:
        return False

    limit = int(math.sqrt(value))
    return all(value % n for n in range(2, limit + 1))