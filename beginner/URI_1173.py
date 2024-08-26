n = int(input())
values = [] 

if n < 50:

    for item in range(10):
        values.append(n)
        n = n * 2

for item in range(10):
    print(f'N[{item}] = {values[item]}')
