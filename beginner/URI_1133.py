X = int(input())
Y = int(input())

greather = max([X, Y])
less = min([X, Y])

for item in range(less + 1, greather):
    if (item % 5 == 2) or (item % 5 == 3):
        print(item)
