import math

# 2.1 – Regular hexagon area using triangle
def triangle_area(a, h):
    return 0.5 * a * h

def hexagon_area(a):
    h = a * math.sqrt(3) / 2
    return 6 * triangle_area(a, h)

print(hexagon_area(4))

# 2.2 – Areas of 3 rectangles
for i in range(3):
    a = float(input("Side A: "))
    b = float(input("Side B: "))
    print("Area:", a * b)
