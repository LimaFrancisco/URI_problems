def incriase(valor):
    if valor >= 0 and valor <= 400:
        return (valor + (valor * 0.15)), (valor * 0.15), 15
    elif valor >= 400.01 and valor <= 800:
        return (valor + (valor * 0.12)), (valor * 0.12), 12
    elif valor >= 800.01 and valor <= 1200:
        return (valor + (valor * 0.10)), (valor * 0.10), 10
    elif valor >= 1200.01 and valor <= 2000:
        return (valor + (valor * 0.07)), (valor * 0.07), 7
    elif valor > 2000:
        return (valor + (valor * 0.04)), (valor * 0.04), 4
    

valor = float(input())

newSalary, moneyEamed, percentage = incriase(valor)

print(f"Novo salario: {newSalary:.2f}\nReajuste ganho: {moneyEamed:.2f}\nEm percentual: {percentage} %")
