from math import sqrt

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

delta = (B ** 2) - 4*A*C

R1 = 0
R2 = 0

try:
    R1 = (-B + sqrt(delta)) / (2 * A)
    R2 = (-B - sqrt(delta)) / (2 * A)
except ZeroDivisionError as error:
    print("Impossivel calcular")
    exit()
except ValueError as error:
    print("Impossivel calcular")
    exit()    

print(f"R1 = {R1:.5f}\nR2 = {R2:.5f}")
