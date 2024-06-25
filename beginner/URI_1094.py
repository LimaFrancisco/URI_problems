N = int(input())
rabbit = 0
mouse = 0
frog = 0

for item in range(N):
    animal_experiment = input().split()
    amount = int(animal_experiment[0])

    if 'C' in animal_experiment and 1 <= amount <= 15:
        rabbit = rabbit + amount
    elif 'R' in animal_experiment and 1 <= amount <= 15:
        mouse = mouse + amount
    elif 'S' in animal_experiment and 1 <= amount <= 15:
        frog = frog + amount

    animal_experiment.clear()

total = rabbit + mouse + frog
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {rabbit}')
print(f'Total de ratos: {mouse}')
print(f'Total de sapos: {frog}')

print(f'Percentual de coelhos: {(rabbit * 100) / total:.2f} %')
print(f'Percentual de ratos: {(mouse * 100) / total:.2f} %')
print(f'Percentual de sapos: {(frog * 100) / total:.2f} %')
