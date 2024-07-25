N = int(input())

out = []

flag = 1

for item in range(N):
    row = []
    for x in range(4):
        if flag % 4 == 0:
            row.append("PUM")
        else:
            row.append(str(flag))
        flag += 1
    out.append(' '.join(row))

print('\n'.join(out))
