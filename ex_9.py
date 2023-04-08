while(True):
    num_1 = int(input("Insira o primeiro número:\n"))
    num_2 = int(input("Insira o segundo número:\n"))
    num_3 = int(input("Insira o terceiro número:\n"))
    if((num_3 == num_1 or num_3 == num_2) == False and ((num_1 == num_2) == False)):
        break
    else:
        print("\nVocê inseriu números repetidos. Por favor, digite números diferentes.\n")
        continue

aux = None

if(num_2 > num_1):
    aux = num_2
    num_2 = num_1
    num_1 = aux
if(num_3 > num_2):
    aux = num_3
    num_3 = num_2
    num_2 = aux
if(num_2 > num_1):
    aux = num_2
    num_2 = num_1
    num_1 = aux


print(num_1 , num_2 , num_3)