T = int(input())

N = [] * 1000
flag = 0


for item in range(1000):
    if flag == T:
        flag = 0

    N.append(flag)

    flag += 1

for item in range(1000):
    print(f"N[{item}] = {N[item]}")
