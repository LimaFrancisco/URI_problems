values = []
while True:
    X = int(input())
    
    if X >= 0:
        values.append(X)
    else:
        break

print(f'{sum(values) / len(values):.2f}')

