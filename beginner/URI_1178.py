X = float(input())

N = []

N.append(X)

for item in range(99):
    X = X / 2
    N.append(X)

for item in range(100):
    print(f'N[{item}] = {N[item]:.4f}')
