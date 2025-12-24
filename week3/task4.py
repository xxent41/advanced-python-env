# Euclid algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 4.1 – Divide fractions
A, B = 1, 2
C, D = 3, 4

num = A * D
den = B * C
g = gcd(num, den)

print(num // g, "/", den // g)

# 4.2 – Points inside circle
def inside_circle(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 <= r*r

points = [(1, 1), (5, 5), (0, 0)]
count = 0
for p in points:
    if inside_circle(p[0], p[1], 0, 0, 3):
        count += 1

print("Points inside:", count)
