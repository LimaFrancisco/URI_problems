n = int(input())

if (1 <= n <= 100):

    for item in range(n):
        x = int(input())

        if (x > 1) and (1 < x <= (10**7)):
            for i in range(2, x):
                if x % i == 0:
                    print(f'{x} nao eh primo')
                    break
            else:
                print(f'{x} eh primo')
