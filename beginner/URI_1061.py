from datetime import datetime

def calcular_duracao(dia_inicio, hora_inicio, dia_fim, hora_fim):
    formato = 'Dia %d %H : %M : %S'
    inicio = datetime.strptime(dia_inicio + ' ' + hora_inicio, formato)
    fim = datetime.strptime(dia_fim + ' ' + hora_fim, formato)
    
    duracao = fim - inicio
    
    dias = duracao.days
    segundos_restantes = duracao.seconds
    horas = segundos_restantes // 3600
    segundos_restantes %= 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    
    return dias, horas, minutos, segundos

dia_inicio = input()
hora_inicio = input()
dia_fim = input()
hora_fim = input()

dias, horas, minutos, segundos = calcular_duracao(dia_inicio, hora_inicio, dia_fim, hora_fim)

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
