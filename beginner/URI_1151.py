def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n = int(input())
result = fibonacci(n)
print(" ".join(map(str, result)))

