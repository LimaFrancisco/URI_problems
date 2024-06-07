even_numbers = 0

for item in range(5):
    value = int(input())

    if value % 2 == 0:
        even_numbers = even_numbers + 1

print(f"{even_numbers} valores pares")