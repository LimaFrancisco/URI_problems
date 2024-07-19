A = float(input())
while A < 0 or A > 10:
    print('nota invalida')
    A = float(input())
  
B = float(input())
while B < 0 or B > 10:
    print('nota invalida')
    B = float(input())

average = (A + B) / 2

print(f'media = {average:.2f}')

