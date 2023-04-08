valor_saque = int(input("Insira o valor do saque:\n"))
if(valor_saque >= 10 and valor_saque <= 600):
    nota_100 = valor_saque//100
    nota_50 = (valor_saque - (nota_100*100))//50
    nota_10 = (valor_saque - (nota_100*100+nota_50*50))//10
    nota_5 = (valor_saque - (nota_100*100+nota_50*50+nota_10*10))//5
    nota_1 =  (valor_saque - (nota_100*100+nota_50*50+nota_10*10+nota_5*5))//1
    print(f"""Você irá receber as seguintes notas:
    Notas de 100: {nota_100}
    Notas de 50:  {nota_50}
    Notas de 10:  {nota_10}
    Notas de 5:   {nota_5}
    Notas de 1:   {nota_1}
    Total: R${nota_100*100+nota_50*50+nota_10*10+nota_5*5+nota_1*1:.2f}
    """)
else:
    print("O valor mínimo para saque é de R$ 10,00 e o valor máximo para saque é de R$ 600,00")