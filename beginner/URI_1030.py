A, B, C = map(float, input().split())

sides = sorted([A, B, C], reverse=True)

if sides[0] >= sides[1] + sides[2]:
    print("NAO FORMA TRIANGULO")
else:
    if sides[0] ** 2 == sides[1] ** 2 + sides[2] ** 2:
        print("TRIANGULO RETANGULO")
    elif sides[0] ** 2 > sides[1] ** 2 + sides[2] ** 2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
