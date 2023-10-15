def find_primes_slower(n):
    primes = []
    def is_prime(n):
        return False if n < 2 else all(n % i for i in primes)
    for i in range(n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def find_primes(n):
    if n <= 2:
        return 0

    primes = [True] * n
    primes[0] = False
    primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            t = i * 2
            while t < n:
                primes[t] = False
                t += i

    all_primes = []
    for num, is_prime in enumerate(primes):
        if is_prime:
            all_primes.append(num)

    return all_primes

print(find_primes(14))
# [2, 3, 5, 7, 11, 13]