num = int(input("Digite um numero: "))
base = int(input("Digite [1] para transformar em binário \n "
                 "Digite [2] para tranformar em octal\n Digite [3] para transformar em hexadecimal"))

if base ==1:
    conversao = bin(num)[2:]
elif base ==2:
    conversao  = oct(num)[2:]
elif base ==3:
    conversao = hex(num)[2:]
else:
    print("Numero Invalido !")

    print("O numero {} conertido para a base {} é {}".format(num, base))