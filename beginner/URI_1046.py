start, end = map(int, input().split())

hours = 0

if start == end:
    hours = 24
else:
    while start != end:
        hours = hours + 1
        start = start + 1

        if start == 24:
            start = 0

print(f"O JOGO DUROU {hours} HORA(S)")
