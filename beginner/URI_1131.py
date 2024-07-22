inter = 0
gremio = 0
empate = 0
grenal = 0
vencedor = ''

while True:
    gols1, gols2 = map(int, input().split())

    grenal += 1

    if gols1 > gols2:
        inter += 1
    elif gols2 > gols1:
        gremio += 1
    else:
        empate += 1

    flag = int(input('Novo grenal (1-sim 2-nao)\n'))

    if flag == 2:
        break

if grenal == 1:
    print('1 grenal')
else:
    print(f'{grenal} grenais')

if inter > gremio:
    vencedor = 'Inter'
elif gremio > inter:
    vencedor = 'Gremio'

print(f'Inter:{inter}\nGremio:{gremio}\nEmpates:{empate}')
print(f'{vencedor} venceu mais')
