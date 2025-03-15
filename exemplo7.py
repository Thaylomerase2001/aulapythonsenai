tentativas = 0
while tentativas < 3:
    senha = input("Digite a senha:")
    if senha == "senha123":
        print("Acesso concedido")
        break
    else:
        print("Senha incorreta, tente novamente")
        tentativas +=1
else:
    print("Voce excedeu o numero máximo de tentativas")
