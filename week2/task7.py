items = input().split()

freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

print("Purchase frequency:")
for k, v in freq.items():
    print(f"{k}: {v}")

most_popular = max(freq, key=freq.get)
print("\nMost popular item:", most_popular)

once = [k for k, v in freq.items() if v == 1]
print("\nPurchased once:", " ".join(once))

print("\nSorted by frequency:")
for k, v in sorted(freq.items(), key=lambda x: -x[1]):
    print(k, v)
