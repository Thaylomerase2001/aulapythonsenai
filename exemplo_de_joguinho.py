numero_secreto = 42
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