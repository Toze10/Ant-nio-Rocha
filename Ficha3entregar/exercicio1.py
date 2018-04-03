numero=int(input("Insira um número inteiro: "))

print("Os 5 números anteriores a {} são: ".format(numero))
for i in range(numero-1, numero-6, -1):
    print(i, end=" ")

print()

print("Os 5 números seguintes a {} são: ".format(numero))
for i in range(numero+1, numero+6, 1):
    print(i, end=" ")