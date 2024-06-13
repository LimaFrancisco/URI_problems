N = int(input())

for item in range(2, N + 1, 2):
    if item % 2 == 0:
        print(f"{item}^2 = {item ** 2}")