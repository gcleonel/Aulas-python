from random import randint
print("Bem Vindos!!")
numero_sorteado = randint(1,100)
# print(numero_sorteado)
novo_jogo = True
while novo_jogo != False:
    contator = 1
    while True:
        chute = int(input("Chute um numero"))
        if chute == numero_sorteado:
            print("Parabens, voce acertou.")
            break
        else:
            print("Alto" if chute > numero_sorteado else "Baixo")
        contator += 1
    print("Fim do Jogo!!!")
    print("Numeor sorteado: "+str(numero_sorteado))
    print("Numero chutado: "+str(chute))
    print("Numero de Tentativas: "+str(contador))
    novo_jogo = init(input("Jogar novamente? 1 - Sim ou 0 - Nao: "))
