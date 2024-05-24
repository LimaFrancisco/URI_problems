value = int(input())

year = value // 365
month = (value % 365) // 30
day = (value % 365) % 30

print(f"{year} ano(s)\n{month} mes(es)\n{day} dia(s)")
