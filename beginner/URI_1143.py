N = int(input())

if 1 < N < 1000:
    for item in range(1, N + 1):
        values = f'{item} ' 
        values += f'{item ** 2} '
        values += f'{item ** 3}'
        print(values)

