nota_1 = float(input("Insira a primeira nota:\n"))
nota_2 = float(input("Insira a segunda nota:\n"))

media = (nota_1 + nota_2 )/ 2

if(media >= 0 and media <= 4.0):
    conceito = 'E'
    print(f"\nMédia de Aproveitamento: {media:.2f}\nConceito: {conceito}\nREPROVADO.")
elif(media > 4.0 and media <= 6.0):
    conceito = 'D'
    print(f"\nMédia de Aproveitamento: {media:.2f}\nConceito: {conceito}\nREPROVADO.")
elif(media > 6 and media <= 7.5):
    conceito = 'C'
    print(f"\nMédia de Aproveitamento: {media:.2f}\nConceito: {conceito}\nAPROVADO.")
elif(media > 7.5 and media <= 9.0):
    conceito = 'B'
    print(f"\nMédia de Aproveitamento: {media:.2f}\nConceito: {conceito}\nAPROVADO.")
elif(media > 9 and media <= 10.0):
    conceito = 'A'
    print(f"\nMédia de Aproveitamento: {media:.2f}\nConceito: {conceito}\nAPROVADO.")
else:
    print("Você inseriu valores inválidos (Média inferior a 0 ou superior a 10). Verifique as notas inseridas e tente novamnente.\n")

