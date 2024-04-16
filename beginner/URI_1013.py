from typing import Type

def maior(a: Type[int], b: Type[int]):
    maior = (a + b + abs(a - b)) / 2
    return maior

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

maiorAB = maior(a, b)
maiorABC = maior(maiorAB, c)

print(f"{maiorABC:.0f} eh o maior")
