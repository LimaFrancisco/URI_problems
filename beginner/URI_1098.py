
I = 0
J = 1

while I <= 2:
    for item in range(3):
            if I == 0 or I == 1 or I == 2: 
                print(f'I={I:.0f} J={J + item:.0f}')
            else:
                print(f'I={round(I, 1):.1f} J={round(J, 1) + item:.1f}')
    I = round(I + 0.2, 1)
    J = round(J + 0.2, 1)
