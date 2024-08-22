def is_perfect(value):

    if value == 1:
        return f'{value} nao eh perfeito'

    value_sum = 0
    for item in range(1, value + 1):
        value_sum += item

        if value_sum == value:
            return f'{value} eh perfeito'

    return f'{value} nao eh perfeito'


n = int(input())

if (1 <= n <= 100):
    for item in range(n):
        value = int(input())
        
        if (1 <= value <= (10**8)): 
            print(is_perfect(value))

