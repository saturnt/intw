def is_prime(n):
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def find_primes(n):
    result = []

    if n < 3:
        result.append(2)

    for i in range(2, n):
        result.append(i) if is_prime(i) else ''

    print result


find_primes(1000000)
