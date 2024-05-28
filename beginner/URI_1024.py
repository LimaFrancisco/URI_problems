item_valor = [0.0, 4.0, 4.5, 5.0, 2.0, 1.5]

item, amount = input().split()

item = int(item)
amount = int(amount)

total = item_valor[item] * amount

print(f"Total: R$ {total:.2f}")
