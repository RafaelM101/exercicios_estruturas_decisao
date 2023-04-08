nota_1 = float(input("Insira a primeira nota:\n"))
nota_2 = float(input("\nInsira a segunda nota:\n"))

media = (nota_1 + nota_2) / 2


if(media == 10):
    print("\nAprovado com distinção!")
elif(media >= 7 and media < 10):
    print("\nAprovado!")
else:
    print("\nReprovado!")

print("Sua média é {}".format(media))