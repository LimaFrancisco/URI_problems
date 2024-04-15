valorA, valorB, valorC = input().split()

valorA = float(valorA)
valorB = float(valorB)
valorC = float(valorC)

triangulo = (valorA * valorC) / 2
circulo = 3.14159 * (valorC ** 2)
trapezio = ((valorA + valorB) / 2) * valorC
quadrado = valorB ** 2 
retangulo = valorA * valorB

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
