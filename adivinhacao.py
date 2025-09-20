import random
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_magico = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 100

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Defina o nível:"))
    if dificuldade == 1:
        total_de_tentativas = 20
    elif dificuldade == 2:
            total_de_tentativas = 10
    else:
            total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas +1):
        print("Tentativa: {} de {}" .format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou ",chute)
        numero = int(chute)
        if(numero < 1 or numero > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue
        acerto = numero == numero_magico
        maior = numero > numero_magico
        menor = numero < numero_magico

        if (acerto):
            print(f"Parabéns! 🎉Você acertou e fez {pontos} pontos!")
            break
        else:
            if (maior):
                print("Errou... 😢 Tente novamente! O seu chute foi maior do que o número secreto.")
            if (menor):
                print("Errou... 😢 Tente novamente! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_magico - numero)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")
if __name__ == "__main__":
    jogar()