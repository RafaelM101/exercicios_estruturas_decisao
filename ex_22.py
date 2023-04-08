tipo_combustivel = input("Insira o tipo de Combústivel que deseja comprar: Álcool ou Gasolina:\n").upper()
litros_combustivel = int(input(f"Insira quantos litros de {tipo_combustivel}:\n"))
preço_gasolina = float
preço_alcool = float
if(litros_combustivel > 0 and litros_combustivel <= 20):
    tipo_combustivel = tipo_combustivel[0]
    if(tipo_combustivel =='A' or tipo_combustivel == 'Á'):
        preço_alcool = 1.90 - ((1.90*3)/100)
        print(f"O valor total de {litros_combustivel} litros de ÁLCOOL é: R${litros_combustivel*preço_alcool}")
    else:
        preço_gasolina = 2.5 - ((2.5*4)/100)
        print(f"O valor total de {litros_combustivel} litros de GASOLINA é: R${litros_combustivel*preço_gasolina}")

elif(litros_combustivel > 20):
    if(tipo_combustivel =='A' or tipo_combustivel == 'Á'):
        preço_alcool = 1.90 - ((1.90*5)/100)
        print(f"O valor total de {litros_combustivel} litros de ÁLCOOL é: R${litros_combustivel*preço_alcool}")
    else:
        preço_gasolina = 2.5 - ((2.5*6)/100)
        print(f"O valor total de {litros_combustivel} litros de GASOLINA é: R${litros_combustivel*preço_gasolina}")