def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

nums = [2, 3, 4, 5, 6, 7, 15, 20, 25]


if __name__ == "__main__":
    for n in nums:
        print(n, is_prime(n))
