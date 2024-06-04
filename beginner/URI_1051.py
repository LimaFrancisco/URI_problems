salary = float(input())

if salary <= 2000:
    print("Isento")

elif salary <= 4500:
    taxablePart = salary - 2000
    if taxablePart <= 1000:
        tax = taxablePart * 0.08
    else:
        tax = 1000 * 0.08 + (taxablePart - 1000) * 0.18

    print(f"R$ {tax:.2f}")
else:
    taxablePart = salary - 4500
    tax = 1000 * 0.08 + 1500 * 0.18 + taxablePart * 0.28

    print(f"R$ {tax:.2f}")
