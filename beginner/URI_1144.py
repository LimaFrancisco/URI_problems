def result_maker(item) -> str:
    values = f'{item} '
    values += f'{item ** 2} '
    values += f'{item ** 3}\n'

    values += f'{item} '
    values += f'{(item ** 2) + 1} '
    values += f'{(item ** 3) + 1}'
    return values
    
N = int(input())

if 1 < N < 1000:
    for item in range(1, N  + 1):

        result = result_maker(item)
        print(result)
        