def factorization(n):
    factors = []
    while (n%2 == 0):
        factors.append(2)
        n = n/2
    i = 3
    while (i <= math.sqrt(n)):
        if (n % i == 0):
            factors.append(i)
            n = n/i
        i += 2
    if (n > 2):
        factors.append(n)
    return factors
