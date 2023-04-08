dias_semana = ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado','Domingo']
user = int(input("Insira o número:\n"))

if(user >= 1 and user <= 7):
    print(dias_semana[user-1])
else:
    print("Valor inválido.")