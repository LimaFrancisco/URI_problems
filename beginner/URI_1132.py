total = 0

value1 = int(input())
value2 = int(input())

greather = max([value1, value2])
less = min([value1, value2])

for item in range(less, greather + 1):
    if item % 13 != 0:
        total += item

print(total)
