#aqui vamos criar um jogo que escolha um numero aleatorio, para isso vamos importar uma biblioteca de aleatoridade do python (import random)
#depois modificar a variavel numero_secreto para ela ser o numero aleatorio que pode ir de 1 até 100, em numeros inteiros (randint (int))
import random
numero_secreto = random.randint(1,100)
tentativa = 1
while tentativa <= 3:
    palpite = int(input("Adivinhe o numero secreto: "))
    if palpite == numero_secreto:
        print("Parabens, voce acertou!!")
        break
    else:
        if palpite> numero_secreto:
            print("O numero secreto é menor do que", palpite)
        else:
            print("O numero secreto é maior do que", palpite)
    tentativa += 1 
if tentativa > 3:
    print("Suas tentativas acabaram. O numero secreto era", numero_secreto)
#lista de bibliotecas do python https://blog.botcity.dev/pt-br/2024/01/15/bibliotecas-python/