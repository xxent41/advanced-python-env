# Euclid GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 5.1 – Subtract fractions (FIXED)
A, B = 3, 4
C, D = 1, 6

num = A * D - C * B
den = B * D
g = gcd(abs(num), den)

print(num // g, "/", den // g)

# 5.2 – Divisors of a number
n = int(input("Enter number: "))
divs = [str(i) for i in range(1, n + 1) if n % i == 0]
print(" ".join(divs))
