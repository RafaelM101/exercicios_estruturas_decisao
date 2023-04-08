while(True):
    num_1 = int(input("Insira o primeiro número:\n"))
    num_2 = int(input("Insira o segundo número:\n"))
    num_3 = int(input("Insira o terceiro número:\n"))
    if((num_3 == num_1 or num_3 == num_2) == False and ((num_1 == num_2) == False)):
        break
    else:
        print("\nVocê inseriu números repetidos. Por favor, digite números diferentes.\n")
        continue

if(num_1 > num_2 and num_1 > num_3):
    print("O maior número é: {}".format(num_1))
    if(num_2 > num_3):
        print("\nO menor número é:{}".format(num_3))
    else:
        print("\nO menor número é: {}".format(num_2))
if(num_2 > num_1 and num_2 > num_3):
    print("O maior número é: {}".format(num_2))
    if(num_1 > num_3):
        print("O menor número é: {}".format(num_3))
    else:
        print("O menor número é: {}".format(num_1))
if(num_3 > num_1 and num_3 > num_2):
    print("O maior número é: {}".format(num_3))
    if(num_1 > num_2):
        print("O menor número é: {}".format(num_2))
    else:
        print("O menor número é: {}".format(num_1))