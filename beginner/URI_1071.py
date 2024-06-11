X = int(input())
Y = int(input())

values_sum = 0

if X > Y:
    start = Y 
    end = X
else:
    start = X
    end = Y

for item in range(start + 1, end):
    if item % 2 != 0:
        values_sum = values_sum + item

print(values_sum)
