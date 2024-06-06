positives = 0

for item in range(6):
    entering = float(input())

    if entering > 0:
        positives = positives + 1

print(f"{positives} valores positivos")
