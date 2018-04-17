def soma(num1, num2):
    res = (num1 + num2)
    return res

def sub(num1, num2):
    res = num1 - num2
    return res

def mult(num1, num2):
    res = num1 * num2
    return res

def div(num1, num2):
    res = num1 / num2
    return res

num1= int(input('Introduza o primeiro valor: '))
num2= int(input('Introduza o segundo valor: '))

print('Escolha uma das opções abaixo')
print('1- Soma')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')
opcao = int(input('Opção: '))

if opcao == 1 :
    res = soma(num1, num2)
    print(res)

elif opcao == 2 :
    res = sub(num1, num2)
    print(res)

elif opcao == 3 :
    res =mult(num1, num2)
    print(res)

elif opcao == 4 :
    res = div(num1, num2)
    print(res)

else :
    print('ERRO!!')