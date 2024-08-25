X = [] * 10

for item in range(10):
    n = int(input())

    if n > 0:
        X.append(n)
    else:
        X.append(1)


for item in range(10):
    print(f'X[{item}] = {X[item]}')
