N = int(input())

second = N % 60
minute = (N // 60) % 60
hour = (N // 60) // 60

print(f"{hour}:{minute}:{second}")
