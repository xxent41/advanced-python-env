# 8.1 – Numbers divisible by all digits
n = int(input())
for i in range(1, n + 1):
    digits = [int(d) for d in str(i) if d != '0']
    if digits and all(i % d == 0 for d in digits):
        print(i, end=" ")

print()

# 8.2 – Swap first and last
m = int(input("Length: "))
A = list(map(int, input("Elements: ").split()))

print("Original:", A)
A[0], A[-1] = A[-1], A[0]
print("Result:", A)
