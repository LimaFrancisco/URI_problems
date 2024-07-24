list = [0] * 3

while True:

    value = int(input())

    if value == 1:
        list[0] += 1
    elif value == 2:
        list[1] += 1
    elif value == 3:
        list[2] += 1
    elif value == 4:
        break

print(f'MUITO OBRIGADO\nAlcool: {list[0]}\nGasolina: {list[1]}\nDiesel: {list[2]}')
    