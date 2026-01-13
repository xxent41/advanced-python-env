import math

# 3.1 – Hypotenuse comparison
def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

h1 = hypotenuse(3, 4)
h2 = hypotenuse(6, 8)

print("Greater:", max(h1, h2))
print("Smaller:", min(h1, h2))

# 3.2 – Sort letters in each word
s = "hello world python"
result = " ".join("".join(sorted(word)) for word in s.split())
print(result)

