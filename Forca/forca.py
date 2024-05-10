from os import system


#Desenvolvido por Eliseu Franco Samulolo
#Em 10/05/2024

def titulo():
    print('-'*20)
    print(f'{"Jogo da forca":^20}')
    print('-'*20)
    print('  ____')
    print(' |  |  ')
    print(' |  O  ')
    print(" | /|\ ")
    print(" | / \ ")
    print("_|_")

def verificador(secreta):
    '''
        -> Função que recebe a palavra secreta que o jogador introduz
        -> Com base no tamanho da palavra adiciono _ underline para cada um dos indices da lista
        -> Retorno para o programa principal uma lista com os underlines adicionados 
    '''
    lista = list()
    cont = 0
    while len(secreta) > cont:
        lista.append('_')
        cont+=1
    return lista

jogador = input('Diz ao teu amigo para fechar os olhos e escreva a palavra secreta: ').upper().strip()
junta = ''.join(jogador)
tentativa = 6
aux = verificador(junta)
v = ''

while tentativa >= 0:
    titulo()
    print(f'Tentativas: {tentativa}')
    auxq = ''.join(aux) #Junta o retorno da lista que vem da função verificador para uma apresentação mais agradável dos espaços
    print(auxq)
    letra = input("Letra: ")[0].upper().strip()

    for l in range(0,len(junta)):
        if junta[l] == letra:
            aux[l] = letra
            v += aux[l]

    system('cls')
    if len(junta) == len(v):
        print(f"\033[32m Você ganhou🥳, a palavra secreta era \033[m < {junta} >")
        break    
    if tentativa == 0:
        print('\033[31m Você perdeu, não conseguiu acertar a palavra secreta 😔\033[m')
    tentativa -= 1



        



    
