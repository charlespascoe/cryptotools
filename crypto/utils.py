
def gcd(a, b):
    if b == 0: return a
    if a > b: return gcd(b, a % b)
    return gcd(a, b % a)

def compute_coprimes(n):
    coprimes = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def phi(n):
    # Lazy
    return len(compute_coprimes(n))

def compute_inverse(a, n):
    # Lazy
    if gcd(a, n) != 1:
        return None

    return pow(a, phi(n) - 1, n)


