A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

if (A + B <= C) or (B + C <= A) or (A + C <= B):
    print(f"Area = {((A + B) * C)/ 2}")
else:
    print(f"Perimetro = {A + B + C:.1f}")
