N = int(input())

exit = [] * N

for item in range(N):
    x = int(input())

    if x > 0 and x % 2 == 0: 
        exit.append('EVEN POSITIVE')
    elif x < 0 and x % 2 == 0:
        exit.append('EVEN NEGATIVE')
    if x > 0 and x % 2 != 0: 
        exit.append('ODD POSITIVE')
    elif x < 0 and x % 2 != 0:
        exit.append('ODD NEGATIVE')
    elif x == 0:
        exit.append('NULL')

for i in exit:
    print(i)
    