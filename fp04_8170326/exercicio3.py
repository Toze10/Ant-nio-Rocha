
caracter = input("Introduza o caracter que deseja: ")
linhas = int(input("Introduza o tamanho da linha que deseja: "))
colunas = int(input("Introduza o tamanho da coluna que deseja: "))

def figura(linhas, colunas, caracter) :
     
    for i in range(1, linhas + 1) :
        for j in range(1, colunas + 1) :
            if (i == 1 or i == linhas or j == 1 or j == colunas) :
                print(caracter, end="")            
            else :
                print(" ", end="")            
        print()

figura(linhas, colunas, caracter)