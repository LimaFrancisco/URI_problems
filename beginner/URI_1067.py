X = int(input())

if 1 <= X <= 1000:
    X = X + 1
    for item in range(1, X, 2):
        print(item)