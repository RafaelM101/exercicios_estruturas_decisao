lado_1 = float(input("Insira o primeiro lado do triângulo:\n"))
lado_2 = float(input("\nInsira o segundo lado do triângulo:\n"))
lado_3 = float(input("\nInsira o terceiro lado do triângulo:\n"))

if(lado_1 + lado_2 > lado_3 and lado_3 + lado_2 > lado_1 and lado_3 + lado_1 > lado_2):
    if(lado_1  == lado_2 and lado_1 == lado_3):
        print("\nOs lados informados formam um triângulo EQUILÁTERO.\n")
    elif((lado_1 == lado_2) or (lado_2 == lado_3) or (lado_3 == lado_1)):
        print("\nOs lados informados foram um triângulo ISÓSCELES.")
    else:
        print("\nOs lados informados formam um triângulo ESCALENO.")
else:
    print("\nOs lados informados não formam um triângulo.")