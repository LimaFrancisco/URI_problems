flag = True

while flag == True:
	password = int(input())
	
	if password != 2002:
		print('Senha Invalida')
	else:
		print('Acesso Permitido')
		flag = False
