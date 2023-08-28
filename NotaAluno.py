nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

print("Média: ", media)
if media<7.0:
    print("Reprovado!")
elif media<10:
    print("Aprovado")
else:
    print("Aprovado com Distinção!")
