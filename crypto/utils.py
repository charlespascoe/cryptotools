
def gcd(a, b):
    if b == 0: return a
    if a == 0: return b
    if a > b: return gcd(b, a % b)
    return gcd(a, b % a)

def is_coprime(a, n):
    return gcd(a, n) == 1

def compute_coprimes(n):
    return [i for i in range(1, n) if is_coprime(i, n)]

def phi(n):
    # Lazy
    return len(compute_coprimes(n))

def compute_inverse(a, n):
    # Lazy
    if gcd(a, n) != 1:
        return None

    return pow(a, phi(n) - 1, n)

def compute_frequencies(text, alph):
    freqs = [0] * len(alph)

    for char in alph.strip(text):
        freqs[alph.index(char)] += 1

    return freqs

def compute_probabilities(text, alph):
    freqs = compute_frequencies(text, alph)

    total = sum(freqs)

    probs = [0] * len(alph)

    if total == 0:
        return probs

    for i in range(len(alph)):
        probs[i] = freqs[i] / total

    return probs
