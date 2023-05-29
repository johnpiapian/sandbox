def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


def test_is_prime():
    knownPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    knownNonPrime = [0, 1, 4, 6, 8, 9, 10, 12, 14]

    for i in range(0, len(knownPrime)):
        assert is_prime(knownPrime[i]) == True
        assert is_prime(knownNonPrime[i]) == False


test_is_prime()