N = int(input())
result = ''

for item in range(N):
    values = list(map(int, input().split()))
    if values[1] == 0:
        result += 'divisao impossivel\n'
    else:
        result += f'{values[0] / values[1]:.1f}\n'
    
result = result[:-1]

print(result)
