num_1 = int(input("Insira o primeiro número:\n"))
num_2 = int(input("Insira o segundo número:\n"))
num_3 = int(input("Insira o terceiro número:\n"))

if(num_1 > num_2 and num_1 > num_3):
    print("O maior número é: {}".format(num_1))
elif(num_2 > num_1 and num_2 > num_3):
    print("O maior número é: {}".format(num_2))
elif(num_3 > num_1 and num_3 > num_2):
    print("O maior número é: {}".format(num_2))