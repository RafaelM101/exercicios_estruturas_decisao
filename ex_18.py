data = input("Insira a data no formato dd/mm/aaaa:\n").upper()
data_nova = data.replace('/',' ')
dia = int(data_nova[0:2])
mes = int(data_nova[3:5])
ano = int(data_nova[6:])

meses_30 = [4,6,9,11]
meses_31 = [1,3,5,7,8,10,12]


bissexto = False

if(ano > 0):
    if(ano%4 == 0):
        if(ano%100!=0):
            bissexto = True
        else:
            if(ano%400==0):
                bissexto = True
            else:
                bissexto = False
else:
    bissexto = False

print(bissexto)

if(dia > 0 and dia <= 31 and mes >= 1 and mes <=12 and ano >=1 ):
    if(dia <= 30 and mes!=2 and mes in meses_30):
        print(f"\nA data digitada foi: {data}; e ela é uma data válida.\n")
    elif(dia <= 31 and mes!=2 and mes in meses_31):
        print(f"\nA data digitada foi: {data}; e ela é uma data válida.\n")
    elif(dia <= 28 and mes == 2 and bissexto == False):
        print(f"\nA data digitada foi: {data}; e ela é uma data válida.\n")
    elif(dia <= 29 and mes == 2 and bissexto == True):
        print(f"\nA data digitada foi: {data}; e ela é uma data válida.\n")
    else:
        print(f"\nA data digitada foi: {data}; e ela é uma data inválida.\n")
else:
    print(f"\nA data digitada foi: {data}; e ela é uma data inválida.\n")