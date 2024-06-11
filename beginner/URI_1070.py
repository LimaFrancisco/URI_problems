X = int(input())

if X % 2 == 0:
    X = X + 1

for item in range(0, 12, 2):
    print(X)
    X = X + 2
    