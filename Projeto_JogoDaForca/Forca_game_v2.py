# Import
import random 
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    #Windows
    if name == 'nt':
        _=system('cls')

    # Mac ou Linux
    else:
        _=system('clear')
# Função que desenha a forca na tela
def desenho_boneco(chances):

    # Lista de estágios da forca
    estagio = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return estagio[chances]

# Função
def game():

    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")    
    print("Adivinhe a palavra abaixo:\n")

    #Listade palavras
    palavras = ['abacate','maça','uva','acerola','fruta do conde']

    # Escolher aleatorio com a função random
    palavra = random.choice(palavras)

    #Guardar a quantidade de palavras
    letras_descobertas = ['_' for letra in palavra]

    # Numeros de chances
    chances = 6

    # Lista para as Letra erradas
    letras_erradas = []

    while chances > 0:
    #print
        print(desenho_boneco(chances))
        print (" ".join(letras_descobertas))
        print("\nChances restantes: ",chances)
        print("Letras Erradas: "," ".join(letras_erradas))

        #Tentativa
        tentativa = input("\nDigite uma letra: ").lower()
        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances = chances- 1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    # Condicional 
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main
if __name__ == '__main__':
    game()
    print("\nParabéns\n")