N = int(input())
total = 0
sum = []

for item in range(N):

    X, Y = map(int, input().split())

    if X < Y:
        start = X + 1
        end = Y
    else:
        start = Y + 1
        end = X

    for value in range(start, end):
        
        if value % 2 != 0:
            total += value
    
    sum.append(total)
    total = 0

for i in sum:
    print(i)
