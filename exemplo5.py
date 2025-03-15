#entrar com um valor e fazer a tabuada do valor de 1 até 10
x = int(input("Insira a tabuada que gostaria de estudar: "))
#esse aqui "i" é o contador que vamos usar com o while, aqui iniciamos ele a partir de um determinado numero
# meu contador precisa iniciar de algum ponto, no caso do zero 
i = 0
#comando while só cria um laço de repetição quantas vezes voce falar que quer ele repita
while i <= 10:
    resultado = x * i
    # f" " coloca as variaveis lado a lado, em formato de tabela
    print (f" {x} X {i} = {x * i}")
    i += 1