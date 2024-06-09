even_numbers = 0
odd_numbers = 0
positive_numbers = 0
negative_numbers = 0

for item in range(5):
    value = int(input())

    if value % 2 == 0:
        even_numbers = even_numbers + 1

    if value % 2 != 0:
        odd_numbers = odd_numbers + 1

    if value > 0:
        positive_numbers = positive_numbers + 1

    if value < 0:
        negative_numbers = negative_numbers + 1

print(f"{even_numbers} valor(es) par(es)")
print(f"{odd_numbers} valor(es) impar(es)")
print(f"{positive_numbers} valor(es) positivo(s)")
print(f"{negative_numbers} valor(es) negativo(s)")
