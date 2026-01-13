# Task 1.1 – Areas of shapes
import math

def circle_area(r):
    return math.pi * r * r

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h

# Task 1.2 – Sum and average of arrays
arrays = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [10, 20]
]

for arr in arrays:
    s = sum(arr)
    avg = s / len(arr)
    print(arr, "Sum:", s, "Average:", avg)



print(triangle_area(5, 7))
