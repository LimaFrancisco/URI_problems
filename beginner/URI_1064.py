positives = 0
average = 0

for item in range(6):
    entering = float(input())

    if entering > 0:
        positives = positives + 1
        average = average + entering

average = average / positives

print(f"{positives} valores positivos\n{average:.1f}")
