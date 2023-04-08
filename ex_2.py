num_user = int(input("Insira o número:\n"))

if(num_user == 0):
    print("\nO número digitado foi 0, então ele é neutro.\n")
elif(num_user > 0):
    print("O número digitado foi {}, este número é positivo.".format(num_user))
else:
    print("O número digitado foi {}, este número é negativo.".format(num_user))
    