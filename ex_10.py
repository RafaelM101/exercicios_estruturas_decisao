turno = input("Insira em que turno você estuda: Manhã, Tarde ou Noite:\n").upper()

if(turno[0] == "M"):
    print("\nBom dia!")
elif(turno[0] == "N"):
    print("\nBoa noite!")
elif(turno[0] == "T"):
    print("\nBoa tarde!")
else:
    print("\nValor inválido!")