numero_user = int(input("Insira um número inteiro menor do que 1000:\n"))
centenas = 1
dezenas = 1
unidades = 1

centenas = numero_user//100
dezenas = (numero_user%100)//10
unidades = (numero_user%100)%10
if(centenas > 1):
    if(dezenas > 1):
        if(unidades > 1):
            print("{} centenas, {} dezenas e {} unidades.".format(centenas,dezenas,unidades))
        elif(unidades == 1):
            print("{} centenas, {} dezenas e {} unidade".format(centenas,dezenas,unidades))
        else:
            print("{} centenas e {} dezenas".format(centenas,dezenas))
    elif(dezenas == 1):
        if(unidades > 1):
            print("{} centenas, {} dezena e {} unidades.".format(centenas,dezenas,unidades))
        elif(unidades == 1):
            print("{} centenas, {} dezena e {} unidade".format(centenas,dezenas,unidades))
        else:
            print("{} centenas e {} dezena".format(centenas,dezenas))
    elif(dezenas == 0):
        if(unidades > 1):
            print("{} centenas e {} unidades.".format(centenas,unidades))
        elif(unidades == 1):
            print("{} centenas e {} unidade".format(centenas,unidades))
        else:
            print("{} centenas".format(centenas))    
elif(centenas == 1):
        if(dezenas > 1):
            if(unidades > 1):
                print("{} centena, {} dezenas e {} unidades.".format(centenas,dezenas,unidades))
            elif(unidades == 1):
                print("{} centena, {} dezenas e {} unidade.".format(centenas,dezenas,unidades))
            else:
                print("{} centena, {} dezenas.".format(centenas,dezenas))
        elif(dezenas == 1):
            if(unidades > 1):
                print("{} centena, {} dezena e {} unidades.".format(centenas,dezenas,unidades))
            elif(unidades == 1):
                print("{} centena, {} dezena e {} unidade.".format(centenas,dezenas,unidades))
            else:
                print("{} centena, {} dezena.".format(centenas,dezenas))
        else:
            if(unidades > 1):
                print("{} centena e {} unidades.".format(centenas,unidades))
            elif(unidades == 1):
                print("{} centena e {} unidade.".format(centenas,unidades))
            else:
                print("{} centena.".format(centenas))
else:
    if(dezenas > 1):
        if(unidades > 1):
            print(f"{dezenas} dezenas e {unidades} unidades.")
        elif(unidades == 1):
            print(f"{dezenas} dezenas e {unidades} unidade.")
        else:
            print(f"{dezenas} dezenas.")
    elif(dezenas == 1):
        if(unidades > 1):
            print(f"{dezenas} dezena e {unidades} unidades.")
        elif(unidades == 1):
            print(f"{dezenas} dezena e {unidades} unidade.")
        else:
            print(f"{dezenas} dezena.")
    else:
        if(unidades > 1):
            print(f"{unidades} unidades.")
        elif(unidades == 1):
            print(f"{unidades} unidade.")
        else:
            print(f" Você digitou {numero_user}")


