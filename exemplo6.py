numero = int(input("insira um numero: "))
while numero < 10:
    if numero == 0:
        print(numero, "é zero")
    elif numero%2 == 0:
        print (numero, "é par")
    else:
        print(numero,"é impar", )
    numero += 1