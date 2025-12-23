valid_letters = set("ABCEHKMOPTXY")

n = int(input())
for _ in range(n):
    plate = input().strip()

    if (
        len(plate) == 6 and
        plate[0] in valid_letters and
        plate[1:4].isdigit() and
        plate[4] in valid_letters and
        plate[5] in valid_letters
    ):
        print("Yes")
    else:
        print("No")