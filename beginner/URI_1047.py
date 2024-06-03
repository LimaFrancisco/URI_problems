start_hour, start_minute, end_hour, end_minute = map(int, input().split())  

hours = 0
minutes = 0

if (start_hour == end_hour) and (start_minute != end_minute):
    hours = 0
elif (start_hour == end_hour) and (start_minute == end_minute):
    hours = 24 
    minutes = 0
else:
    while start_hour != end_hour:
        hours = hours + 1
        start_hour = start_hour + 1

        if start_hour == 24:
            start_hour = 0

if start_minute > end_minute:
    if hours == 0:
        hours = 23
    else:
        hours = hours - 1
    minutes = 60 - abs(end_minute - start_minute)
else:
    minutes = end_minute - start_minute

print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")
