#TRABALHO PRATICO 1
#Pedro Carvalho
#Tozé Rocha


#Numero maximo de jogadas no inicio do jogo
jogadas_max = 0

#Dados Class Tabuleiro
class tabuleiro():
    
    def __init__(self):

        self.tabuleiro = [ [None, None, None], 
                           [None, None, None], 
                           [None, None, None] ]

#Definir uma funcao para a criação do tabuleiro
    def __str__(self):
        tab = "\n  A|B|C"
        for j in range (0, 3):
            tab += "\n" + str(j+1) + "|"
            for i in range (0, 3):
                if self.tabuleiro[j][i] == None:
                    tab += " |"
                else:
                    tab += self.tabuleiro[j][i] + "|"
        return tab

#Definir uma funcao para podermos validar a jogada com as respetivas coordenadas    
    def validarjogada(self,jogada,token):        
        if (jogada[0] == "A" or jogada[0] == "B" or jogada[0] == "C") and (jogada[1] == "1" or jogada[1] == "2" or jogada[1] == "3"):
            if jogada[0] == "A":
                coluna = 0
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Por favor escolha outra casa")
                    jogada = input("Jogue entre as respetivas casas (A1 - C3) ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "B":
                coluna = 1
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Por favor escolha outra casa")
                    jogada = input("Jogue entre as respetivas casas (A1 - C3) ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "C":
                coluna = 2
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Por favor escolha outra casa")
                    jogada = input("Jogue entre as respetivas casas (A1 - C3)")
                    self.validarjogada(jogada,token)
        else:
            print("Por favor escolha outra casa")
            jogada = input("Jogue entre as respetivas casas (A1 - C3):  ")
            self.validarjogada(jogada,token)

#Retirado do github do jogo da Velha
#Esta função permite verificar se existe vencedor do jogo
   
    def vitoria(self,nome,token):
        if  (self.tabuleiro[0][0] == token and self.tabuleiro[0][1] == token and self.tabuleiro[0][2] == token) or \
            (self.tabuleiro[1][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[1][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[2][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][0] == token and self.tabuleiro[2][0] == token) or \
            (self.tabuleiro[1][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[1][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[2][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[0][2] == token):
            global winner
            winner = True
        return winner
    
#Dados Class Jogador
class jogador():

#Definir uma função para chamar o nome e o token
#Definir uma função para validar o token do jogador   
    def __init__(self):
        self.nome = ""
        self.token = ""

    def validartokenjogador(self):
        while jogador1.token == jogador2.token:
            print("Token já utilizado do jogador 1 ")
            jogador2.token = input("Por favor escolha outro token: ")
        return self.token
        
#DadosJogador 1
jogador1 = jogador()
jogador1.nome = input("Insira o nome do jogador1: ")
jogador1.token = input("Insira o token que deseja dar ao jogador1: ")

#DadosJogador 2
jogador2 = jogador()
jogador2.nome = input("Insira o nome do jogador2: ")
jogador2.token = input("Insira o token que deseja dar ao jogador2: ")

#Dadosfinais
jogador()
print (" Jogador1 chama-se {} e escolheu o token {} para jogar" .format(jogador1.nome,jogador1.token))
print (" Jogador2 chama-se {} e escolheu o token {} para jogar" .format(jogador2.nome,jogador2.token))

#DadosTabuleiro
#DadosdosJogadores
tabuleiro1 = tabuleiro()
jogador1.validartokenjogador()    
tabuleiro1.__str__()

#DadosJogar
#O ciclo aqui criado serve para limitar as 9 jogadas e para o jogador poder desistir caso opte por essa opçao
#O ciclo também permite verificar se após as 9 jogados temos um empate
print(tabuleiro1)
winner = False
while jogadas_max < 9:
    jogada = input("{}, que jogada pretende fazer (A1 - C3)? Se pretender desistir digite exit:   ".format(jogador1.nome))
    if jogada == "exit":
        print("Como o jogador {} desistiu temos como vencedor o jogador {}  ".format(jogador1.nome,jogador2.nome))
        break
    tabuleiro1.validarjogada(jogada,jogador1.token)
    print(tabuleiro1)
    tabuleiro1.vitoria(jogador1.nome,jogador1.token)
    if winner == True:
        print("O vencedor deste jogo é o :",jogador1.nome)
        break
    jogadas_max += 1
    if jogadas_max == 9:
        print("Temos um empate")
        break
    jogada = input("{}, que jogada pretende fazer (A1 - C3)? Se pretender desistir digite exit: ".format(jogador2.nome))
    if jogada == "exit":
        print("Como o jogador {} desistiu temos como vencedor o jogador {}  ".format(jogador2.nome,jogador1.nome))
        break
    tabuleiro1.validarjogada(jogada,jogador2.token)
    print(tabuleiro1)
    tabuleiro1.vitoria(jogador2.nome,jogador2.token)
    if winner == True:
        print("O vencedor deste jogo é o : ",jogador2.nome) 
        break
    jogadas_max += 1




    #FINAL