# 7.1 – Quadrilateral area
def right_triangle(a, b):
    return a * b / 2

def rectangle(a, b):
    return a * b

X, Y, Z, T = 3, 4, 5, 6
area = right_triangle(X, Y) + rectangle(Z, T)
print("Area:", area)

# 7.2 – 10-digit octal
n = int(input())
print(format(n, '010o'))
