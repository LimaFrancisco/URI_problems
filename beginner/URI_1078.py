N = int(input())

if 2 < N < 1000:
    for item in range(1, 11):
        print(f"{item} x {N} = {item * N}")
    