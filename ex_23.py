while(True):
    escolha_user = int(input("Insira o tipo de carne que seja comprar:\n1 - FILE DUPLO\n2 - ALCATRA\n3 - PICANHA:\n"))
    forma_pagamento = int(input(f"Insira a forma de pagamento:\n1 - A VISTA\n2 - CARTÃO CRÉDITO\n3 - CARTÃO TABAJARA:\n"))
    carrinho = int
    desconto = 0
    preço = float
    if((escolha_user == 1 or escolha_user == 2 or escolha_user == 3)and(forma_pagamento == 1 or forma_pagamento == 2 or forma_pagamento == 3)):
        quantidade_carne = int(input(f"\nInsira a quantidade de KG's de carne que você irá comprar:\n"))
        break
    else:
        print('\n'*9)
        print("OPÇÃO INVÁLIDA!\nDigite o número correspondente a opção escolhida.\n")

if(quantidade_carne <= 5):
    match escolha_user:
        case 1:
            preço = 4.90
            carrinho = preço * quantidade_carne
            escolha_user = "FILÉ DUPLO"
        case 2:
            preço = 5.90
            carrinho = preço * quantidade_carne
            escolha_user = "ALCATRA"
        case 3:
            preço = 6.90
            carrinho = preço * quantidade_carne
            escolha_user = "PICANHA"
    match forma_pagamento:
        case 3:
            desconto = (5*carrinho)/100
else:
    match escolha_user:
        case 1:
            preço = 4.60
            carrinho = preço * quantidade_carne
            escolha_user = "FILÉ DUPLO"
        case 2:
            preço = 5.50
            carrinho = preço * quantidade_carne
            escolha_user = "ALCATRA"
        case 3:
            preço = 6.40
            carrinho = preço * quantidade_carne
            escolha_user = "PICANHA"
    match forma_pagamento:
        case 1:
            forma_pagamento = 'A VISTA'
        case 2:
            forma_pagamento = 'CARTÃO DE CRÉDITO'
        case 3:
            forma_pagamento = "CARTÃO TABAJARA"
            desconto = (5*carrinho)/100


print('\n'*6,"#"*60,f''' 
            CUPOM FISCAL - HIPERMERCADO TABAJARA
ITENS:                                  QTD:      PREÇO UN:
{escolha_user}  ------------------------------ {quantidade_carne} ----   R$ {preço}



FORMA DE PAGAMENTO:--------------------{forma_pagamento}
PREÇO TOTAL:---------------------------R$ {carrinho:.2f}
DESCONTO:------------------------------R$ {desconto:.2f}
TOTAL:---------------------------------R$ {carrinho - desconto:.2f}
''')