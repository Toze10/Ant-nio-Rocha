numero=int(input("Escreva um numero inteiro"))
if numero == 2:
    print(" O numero {} primo ".format(numero))
else:
        while numero > 1:
            for i in range(2,numero):
                if numero % i == 0:
                    print(" O numero {} não é primo ".format(numero))
                    break
                else:
                    print(" O numero {} é primo ".format(numero))
                    break
            break
if numero <= 1:
    print("Para ser numero primo ter de ser superior a 1, se não {} é invalido ".format(numero))