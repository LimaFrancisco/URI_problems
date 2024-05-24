from decimal import Decimal

def how_many_notes(value, note):
    amount = value // note
    rest = value % note
    return amount, rest

value = Decimal(input())

print("NOTAS:")
note, value = how_many_notes(value, Decimal("100.00"))
print(f"{note:.0f} nota(s) de R$ 100.00")
note, value = how_many_notes(value, Decimal("50.00"))
print(f"{note:.0f} nota(s) de R$ 50.00")
note, value = how_many_notes(value, Decimal("20.00"))
print(f"{note:.0f} nota(s) de R$ 20.00")
note, value = how_many_notes(value, Decimal("10.00"))
print(f"{note:.0f} nota(s) de R$ 10.00")
note, value = how_many_notes(value, Decimal("5.00"))
print(f"{note:.0f} nota(s) de R$ 5.00")
note, value = how_many_notes(value, Decimal("2.00"))
print(f"{note:.0f} nota(s) de R$ 2.00")

print("MOEDAS:")
note, value = how_many_notes(value, Decimal("1.00"))
print(f"{note:.0f} moeda(s) de R$ 1.00")
note, value = how_many_notes(value, Decimal("0.50"))
print(f"{note:.0f} moeda(s) de R$ 0.50")
note, value = how_many_notes(value, Decimal("0.25"))
print(f"{note:.0f} moeda(s) de R$ 0.25")
note, value = how_many_notes(value, Decimal("0.10"))
print(f"{note:.0f} moeda(s) de R$ 0.10")
note, value = how_many_notes(value, Decimal("0.05"))
print(f"{note:.0f} moeda(s) de R$ 0.05")
note, value = how_many_notes(value, Decimal("0.01"))
print(f"{note:.0f} moeda(s) de R$ 0.01")
