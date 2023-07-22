from ..applications.primes import is_prime


def test_is_prime_true():
    for n in 2, 3, 5, 7, 11, 13, 17, 19:
        assert is_prime(n)


def test_is_prime_false():
    for n in 0, 1, 4, 6, 9, 10, 12, 14, 25, 36:
        assert not is_prime(n)