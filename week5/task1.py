from collections import Counter
import re

def tokenize(text):
    return re.findall(r"[A-Za-z0-9']+", text.lower())

with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

total_lines = len(lines)
words = []

for line in lines:
    words.extend(tokenize(line))

total_words = len(words)
frequency = Counter(words)

with open("analysis.txt", "w", encoding="utf-8") as f:
    f.write(f"Total lines: {total_lines}\n")
    f.write(f"Total words: {total_words}\n\n")
    f.write("Word frequencies:\n")
    for word, count in frequency.items():
        f.write(f"{word}: {count}\n")

print("Analysis complete.")

