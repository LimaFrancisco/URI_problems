final_result = []
while True:
    values = list(map(int, input().split()))

    M = max(values)
    N = min(values)

    if M <= 0 or N <= 0:

        for item in final_result:
            print(item)

        exit()

    sum_values = 0
    result = ''

    for item in range(N, M + 1):
        sum_values += item
        result += str(item) + ' '

    result += f'Sum={sum_values}' 
    final_result.append(result)
        