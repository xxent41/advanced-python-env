a = input().strip()
b = input().strip()

m = len(b)
rotations = set()

bb = b + b
for i in range(m):
    rotations.add(bb[i:i+m])

count = 0
for i in range(len(a) - m + 1):
    if a[i:i+m] in rotations:
        count += 1

print(count)