N = int(input())

avareges = [] * N

for item in range(N):
    values = input().split()
    
    values[0] = float(values[0]) * 2 
    values[1] = float(values[1]) * 3
    values[2] = float(values[2]) * 5

    avareges.append(sum(values) / 10)

for item in avareges:
    print(f"{item:.1f}")
