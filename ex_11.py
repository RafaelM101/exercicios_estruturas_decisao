salario = float(input("Insira o valor do seu salário para que calculemos a porcentagem de aumento:\n"))

if(salario <= 280.00):
    print(f"""
    Seu salário antes do reajuste era: R$ {salario:.2f}
    Sua porcentagem de reajuste é de 20%
    O valor do aumento é de: R$ {(salario*20)/100:.2f}
    O valor após o aumento é de R$ {salario + ((salario*20)/100):.2f}
""")
elif(salario > 280.00 and salario < 700.00):
    print(f"""
    Seu salário antes do reajuste era: R$ {salario:.2f}
    Sua porcentagem de reajuste é de 15%
    O valor do aumento é de: R$ {(salario*15)/100:.2f}
    O valor após o aumento é de R$ {salario + ((salario*15)/100):.2f}
""")
elif(salario > 700.00 and salario < 1500.00):
    print(f"""
    Seu salário antes do reajuste era: R$ {salario:.2f}
    Sua porcentagem de reajuste é de 10%
    O valor do aumento é de: R$ {(salario*10)/100:.2f}
    O valor após o aumento é de R$ {salario + ((salario*10)/100):.2f}
""")
elif(salario >= 1500.00):
    print(f"""
    Seu salário antes do reajuste era: R$ {salario:.2f}
    Sua porcentagem de reajuste é de 5%
    O valor do aumento é de: R$ {(salario*5)/100:.2f}
    O valor após o aumento é de R$ {salario + ((salario*5)/100):.2f}
""")