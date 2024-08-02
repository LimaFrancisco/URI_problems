
A, N = map(int, input().split())
total_sum = 0

while N <= 0:
    N = int(input())

for i in range(N):
    total_sum += A
    A += 1

print(total_sum)

