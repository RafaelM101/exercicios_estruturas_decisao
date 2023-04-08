valor_hora = float(input("Insira o valor em R$ da sua hora de trabalho:\n"))
horas_trabalhadas = int(input("\nInsira a quantidade de horas trabalhadas:\n"))
salario_bruto = valor_hora * horas_trabalhadas
imp_renda = None

def ContraCheque():
    SIND = 3
    INSS = 10
    FGTS = 11
    imposto_renda = salario_bruto*imp_renda/100
    sind = (salario_bruto*SIND)/100
    inss = (salario_bruto*INSS)/100
    fgts = (salario_bruto*FGTS)/100
    total_descontos = sind + inss + imposto_renda
    salario_liquido = salario_bruto - total_descontos
    print(f"""
Salário Bruto: ({valor_hora:.2f} * {horas_trabalhadas}) :                            R$ {salario_bruto:.2f}
( - ) IR: {imp_renda}% :                                                                      R$ {imposto_renda:.2f}
( - ) INSS: {INSS}% :                                                                    R$ {inss:.2f}
( - ) SIND: {SIND}% :                                                                     R$ {sind:.2f}
( + ) FGTS: {FGTS}% :                                                                    R$ {fgts:.2f}
Total de Descontos:                                                                  R$ {total_descontos:.2f}
Salário Líquido:                                                                     R$ {salario_liquido:.2f}
    """) 

if(salario_bruto <= 900.00):
    imp_renda = 0
    ContraCheque()
elif(salario_bruto > 900.00 and salario_bruto <= 1500.00):
    imp_renda = 10
    ContraCheque()
elif(salario_bruto > 1500.00 and salario_bruto <= 2500.00):
    imp_renda = 15
    ContraCheque()
else:
    imp_renda = 20
    ContraCheque()