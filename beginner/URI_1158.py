def sum_of_odds(X, Y):
    total = 0
    num = X
    for _ in range(Y):
        while num % 2 == 0:
            num += 1
        total += num
        num += 2
    return total

N = int(input())

for _ in range(N):
    X, Y = map(int, input().split())
    result = sum_of_odds(X, Y)
    print(result)
