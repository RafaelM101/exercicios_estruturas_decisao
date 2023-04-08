letter_user = input("Digite a letra:\n").upper()

if(letter_user == 'M'):
    print("{} - Masculino".format(letter_user))
elif(letter_user == 'F'):
    print("{} - Feminino".format(letter_user))
else:
    print("{} - Sexo inválido".format(letter_user))