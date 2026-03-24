import random
import sympy
import math


def generate_random_prime(bits):
    lower = 2 ** (bits - 1)
    upper = (2 ** bits) - 1
    return sympy.randprime(lower, upper)

def largest_primes_below_mersenne_10():
    m10 = 2**89 - 1
    primes = []
    candidate = m10 - 1
    while len(primes) < 10 and candidate > 2:
        if sympy.isprime(candidate):
            primes.append(candidate)
        candidate -= 1
    return primes

def is_prime_miller_rabin(n, k=40):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modular_exponentiation(base, exponent, modulus):
    return pow(base, exponent, modulus)

def main():
    print("===== Nhiệm vụ 2.6: Số nguyên tố Mersenne, GCD, Lũy thừa modulo =====\n")

    print("1. Số nguyên tố ngẫu nhiên:")
    prime8 = generate_random_prime(8)
    prime16 = generate_random_prime(16)
    prime64 = generate_random_prime(64)
    print(f"   - 8 bit : {prime8}")
    print(f"   - 16 bit: {prime16}")
    print(f"   - 64 bit: {prime64}\n")

    print("2. 10 số nguyên tố lớn nhất nhỏ hơn Mersenne thứ 10 (2^89 - 1):")
    primes_below_m10 = largest_primes_below_mersenne_10()
    for i, p in enumerate(primes_below_m10, 1):
        print(f"   {i}. {p}")
    print()

    print("3. Kiểm tra tính nguyên tố (Miller-Rabin):")
    test_numbers = [2**89 - 2, 2**89 - 3, 2**89 - 5]  
    for num in test_numbers:
        sympy_result = sympy.isprime(num)
        miller_result = is_prime_miller_rabin(num)
        print(f"   Số {num}: sympy.isprime = {sympy_result}, Miller-Rabin = {miller_result}")
    print()

    print("4. Ước chung lớn nhất (GCD) của hai số lớn:")
    a = 123456789012345678901234567890
    b = 987654321098765432109876543210
    gcd_val = gcd_euclid(a, b)
    print(f"   gcd({a}, {b}) = {gcd_val}")
    print()

    print("5. Lũy thừa modulo a^x mod p (với số mũ lớn):")
    base = 7
    exponent = 40
    modulus = 19
    result = modular_exponentiation(base, exponent, modulus)
    print(f"   {base}^{exponent} mod {modulus} = {result}")
    big_exp = 10**100
    result_big = modular_exponentiation(2, big_exp, 1000000007)
    print(f"   2^{big_exp} mod 1000000007 = {result_big}")

if __name__ == "__main__":
    main()