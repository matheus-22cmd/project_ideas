X = "x"
O = "o"
VAZIO = " "

tabuleiro = [VAZIO, VAZIO, VAZIO,
            VAZIO, VAZIO, VAZIO,
            VAZIO, VAZIO, VAZIO]

jogada = 0
jogo_valido = True
Vencedor = False
jogador1 = VAZIO
jogador2 = VAZIO
jogador1 = input("Escolha X ou O: ")

if jogador1 == X:
    jogador2 = O
else:
    jogador2 = X

while jogo_valido:
    jogada = jogada + 1 
    casa = int(input("Escolha onde jogar:"))
    tabuleiro[casa] = X
    if jogada%2 ==1:
        tabuleiro[casa]= jogador1
    else:
        tabuleiro[casa] = jogador2
    for i in range(0, 9, 3):
        print(i,"|",i+1,"|", i+2, "        ", tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])
#horizontal
    for i in range(0,9,3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
            
            Vencedor = tabuleiro[i]
#vertical
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
            
            Vencedor = tabuleiro[i]
#diagonal
    if not Vencedor:
        for i in range(0,3,2):
            if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
                Vencedor = tabuleiro[i]
    if Vencedor:
        jogo_valido = False
    print("Vencedor", Vencedor)
else:
    if not  VAZIO in tabuleiro:
        jogo_valido = False
        print("Deu velha")