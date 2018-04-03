voto=int(input("Insira o seu voto (1, 2, 3 ,4), (0 para voto nulo), (9 para voto em branco) e (-1 para terminar) : "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
votobranco = 0
votonulo = 0
while voto != -1:
    if voto == 1:
        candidato1 += 1
    if voto == 2:
        candidato2 += 1
    if voto == 3:
        candidato3 += 1
    if voto == 4:
        candidato4 += 1
    if voto == 0:
        votobranco += 1
    if voto == 9:
        votonulo += 1
    voto=int(input("Insira o seu voto (1, 2, 3 ,4), (0 para voto nulo), (9 para voto em branco) e (-1 para terminar) : "))

totalvotos= candidato1 + candidato2 + candidato3 + candidato4 + votonulo + votobranco
percentagem_candidato1 = (candidato1 * 100) / totalvotos
percentagem_candidato2 = (candidato2 * 100) / totalvotos
percentagem_candidato3 = (candidato3 * 100) / totalvotos
percentagem_candidato4 = (candidato4 * 100) / totalvotos
percentagem_branco = (votonulo * 100) / totalvotos
percentagem_nulo = ( votobranco * 100) / totalvotos

print("O total de votos desta eleição são : {}".format(totalvotos))
print("O total de votos para o candidato 1 são : {}".format(candidato1))
print("O total de votos para o candidato 2 são : {}".format(candidato2))
print("O total de votos para o candidato 3 são : {}".format(candidato3))
print("O total de votos para o candidato 4 são : {}".format(candidato4))
print("O total de votos em branco são : {}".format(votobranco))
print("O total de votos nulos são : {}".format(votonulo))
print("A percentagem de votos para o candidato 1 são : {} %".format(percentagem_candidato1))
print("A percentagem de votos para o candidato 2 são : {} %".format(percentagem_candidato2))
print("A percentagem de votos para o candidato 3 são : {} %".format(percentagem_candidato3))
print("A percentagem de votos para o candidato 4 são : {} %".format(percentagem_candidato4))
print("A percentagem de votos em branco são : {} %".format(percentagem_branco))
print("A percentagem de votos nulos são : {} %".format(percentagem_nulo))