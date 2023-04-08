produto_1 = float(input("Insira o preço do primeiro produto:\n"))
produto_2 = float(input("Insira o preço do segundo produto:\n"))
produto_3 = float(input("Insira o preço do terceiro produto:\n"))

if(produto_1 < produto_2 and produto_1 < produto_3):
    print("Você deve comprar o produto que custa R$ {}".format(produto_1))
if(produto_2 < produto_1 and produto_2 < produto_3):
    print("Você deve comprar o produto que custa R$ {}".format(produto_2))
if(produto_3 < produto_1 and produto_1 < produto_3):
    print("Você deve comprar o produto que custa R$ {}".format(produto_2))