X, Y = map(int, input().split())

numbers = list(range(1, Y + 1))

sublists = [numbers[i:i + X] for i in range(0, len(numbers), X)]

result = '\n'.join(' '.join(map(str, sublist)) for sublist in sublists)

print(result)

