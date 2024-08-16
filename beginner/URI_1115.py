def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "primeiro"
    elif x < 0 and y > 0:
        return "segundo"
    elif x < 0 and y < 0:
        return "terceiro"
    elif x > 0 and y < 0:
        return "quarto"

while True:
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        break
    print(find_quadrant(x, y))
