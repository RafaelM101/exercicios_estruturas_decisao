num_1 = int(input("Insira o primeiro número:\n"))
num_2 = int(input("Insira o segundo número:\n"))

if num_1 == num_2:
    print("Os dois números digitados são iguais.")
elif num_1 > num_2:
    print("O maior número é: {}".format(num_1))
else:
    print("O maior número é: {}".format(num_2))