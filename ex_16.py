valor_a = float(input("Insira o valor de A:\n"))
if(valor_a == 0):
    print("\nO valor de A é 0. A Equação não é do segundo grau.\n")
else:
    valor_b = float(input("\nInsira o valor de B:\n"))
    valor_c = float(input("\nInsira o valor de C:\n"))
    delta_1 = valor_b**2-4*(valor_a * valor_c)
    raiz_1 = ((- valor_b) + (delta_1**0.5))/(2*valor_a) 
    raiz_2 = ((-valor_b) - (delta_1**0.5))/(2*valor_a) 
    if(delta_1 < 0):
        print("\nA Equação não possui raízes reais.\n")
    elif(delta_1 == 0):
        print("\nA Equação possui apenas uma raiz real;")
        print(raiz_1, raiz_2)
    else:
        print("\nA Equação possui duas raízes reais;")
        print(raiz_1, raiz_2)