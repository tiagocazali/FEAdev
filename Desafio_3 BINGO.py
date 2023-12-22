##seu codigo começa aqui
from random import randint

cartela_jogador = [
    [1,8,10],
    [5,3,7],
    [2,6,9],
]

num_sorteados = []

def jogo_do_bingo():
    """Essa é a função principal do Jogo.
       Ela que será executada e chamará todas as outras!"""
    
    #Imprime uma apresentação apenas 1 vez
    print("===  Vamos Jogar Bingo ===")
    print("\nEssa é sua cartela dessa jogada: ")
    imprimir_cartela(cartela_jogador)
    print("\nVamos Começar! Boa sorte!")
    
    #Loop Principal do jogo
    continua = True
    while continua:
        
        #pede para apertar ENTER para sortear um numero, se apertar "q", termina o jogo
        print("======\n")
        x = input("Aperte ENTER para sortear um numero: (q para sair)")
        
        if x == "q":
            continua = False
            break
        
        
        else:
            #Sorteia um numero e pega esse numero sorteado
            sorteado = sortear_bingo()

            #Marca esse numero na cartela do Jogador
            marcar_numero(sorteado, cartela_jogador)

            #Mostra todos os numeros sorteados até agora
            print(f"Numeros sorteados Até agora: {num_sorteados}")

            #mostra como esta a Cartela atual
            print("Sua cartela agora está assim: ")
            imprimir_cartela(cartela_jogador)

            #Verifica se ele fez Bingo, se SIM, termina o jogo
            if verificar_bingo(cartela_jogador):
                print("PARABENS! O jogo acabou!")
                break
        
        #Segurança: Checa se a variavel "num_sorteado" já tem os 20 numeros, e para o programa
        if len(num_sorteados) == 20:
            break


def sortear_bingo():
    """Faz o serteio de um numero aleatório entre 1 e 20
    Faz uso da variável GLOGAL "num_sorteados" """

    #Vefifica se já não foram sorteados os 20 numeros
    while len(num_sorteados)<20:
        
        #Sorteia um numero entre 1 e 20
        temp = randint(1, 20)

        #Se o numero sorteado NÃO estiver em num_sorteados, usa ele!
        if temp not in num_sorteados:
            num_sorteados.append(temp)
            print(f"Numero sorteado: {temp}")

            return temp
            
        

def imprimir_cartela(cartela):
    """Essa função imprime a cartela do jogador"""

    for cada_linha in cartela:
        print(cada_linha)


def marcar_numero(numero, cartela):
    """Essa função procura o numero sorteado na cartela do jogador e marca com X se achar"""

    for linha in range(3):
        for num in range(3):
            if cartela[linha][num] == numero:
                cartela[linha][num] = "X"
                print(f"Sorte! Numero {numero} marcado na sua cartela!")


def verificar_bingo(cartela):
    """Verifica se todos os 9 numeros da cartela foram marcados ("X")"""
    
    aux = 0 #Irá contar quantos X tem na cartela
    for linha in range(3):
        for cada in range(3):
            if cartela[linha][cada] == "X":
                aux += 1
    
    #Verifica se foram encontrado 9 "X" e grita BINGO!
    if aux == 9:
        print("BINGO!!!!")
        return True


#INICIA O JOGO
jogo_do_bingo()
