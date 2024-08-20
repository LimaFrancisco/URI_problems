x = None
even_sum = None

while True:
    x = int(input())
    even_sum = 0

    if x == 0:
        break

    for item in range(x, x+10):
        if item % 2 == 0:
            even_sum += item
            
    print(even_sum)
    