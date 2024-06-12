N = int(input())

listX = [] * N

ini = 0
out = 0 

for item in range(N):
    listX.append(int(input()))

    if 10 >= listX[item] <= 20:
        out = out + 1
    else:
        ini = ini + 1

print(f"{ini} in\n{out} out")
