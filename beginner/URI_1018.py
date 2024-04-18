valor = int(input())

print(valor)

if valor >= 100:
    print(f"{(valor - (valor % 100)) / 100:.0f} nota(s) de R$ 100,00")
    valor = valor % 100
    # print(valor)
else:
    print(f"0 nota(s) de R$ 100,00")

if valor >= 50:
    print(f"{(valor - (valor % 50)) / 50:.0f} nota(s) de R$ 50,00")
    valor = valor % 50
    # print(valor)
else:
    print(f"0 nota(s) de R$ 50,00")

if valor >= 20:
    print(f"{(valor - (valor % 20)) / 20:.0f} nota(s) de R$ 20,00")
    valor = valor % 20
else:
    print(f"0 nota(s) de R$ 20,00")

if valor >= 10:
    print(f"{(valor - (valor % 10)) / 10:.0f} nota(s) de R$ 10,00")
    valor = valor % 10
else:
    print(f"0 nota(s) de R$ 10,00")

if valor >= 5:
    print(f"{(valor - (valor % 5)) / 5:.0f} nota(s) de R$ 5,00")
    valor = valor % 5
else:
    print(f"0 nota(s) de R$ 5,00")

if valor >= 2:
    print(f"{(valor - (valor % 2)) / 2:.0f} nota(s) de R$ 2,00")
    valor = valor % 2
else:
    print(f"0 nota(s) de R$ 2,00")


print(f"{valor} nota(s) de R$ 1,00")
