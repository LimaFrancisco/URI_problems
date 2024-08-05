A = list(map(int, input().split()))
total_sum = 0

for item in range(A[len(A) -1]):
    total_sum += A[0] + item

print(total_sum)

