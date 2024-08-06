X = int(input())
Z = int(input())

count = 2
flag = X

while Z <= X:
    Z = int(input())

while True:
    if flag > Z:
        break

    flag += flag + count
    count += 1

print(count)

