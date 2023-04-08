ano = int(input("Insira o ano:\n"))

if(ano%4 == 0):
    if((ano%100==0) == False):
        print("\nO ano é bissexto.\n")
    else:
        if(ano%400==0):
            print("\nO ano é bissexto.\n")
        else:
            print("\nO ano não é bissexto.\n")
else:
    print("O ano não é bissexto.\n")