import forca
import main #adivinhação

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar_forca()
    elif (jogo == 2):
        print("Jogando adivinhação")
        main.jogar_adivinhacao()

if (__name__ == '__main__'):
    escolhe_jogo()