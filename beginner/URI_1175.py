N = [] * 20

for item in range(20):
    N.append(int(input()))

N.reverse()

for item in range(len(N)):
    print(f'N[{item}] = {N[item]}')
