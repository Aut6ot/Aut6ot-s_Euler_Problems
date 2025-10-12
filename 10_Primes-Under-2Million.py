# Find the sum of all primes under 2 Million

def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if prime[p]:
            # mark all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collect all remaining numbers (all are prime)
    result = []
    for p in range(2, n + 1):
        if prime[p]:
            result.append(p)

    return result


n = 2000000
primes = sieve_of_eratosthenes(n)
sum_of_primes = 0
for x in primes:
    sum_of_primes += x
print(f"The sum of all primes under {n} is {sum_of_primes}")

