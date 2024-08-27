A = []

for item in range(100):
    A.append(float(input()))

for item in range(len(A)):
    if A[item] <= 10:
        print(f'A[{item}] = {A[item]:.1f}')
