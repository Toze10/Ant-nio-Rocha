valor = float(input('Insira um valor: '))
print('Introduza um caracter de conversão:')
print('Insira "E" para converter dollars para euros') 
print('Insira "D" para converter euros para dollars')
op = input('opção: ')

def conversao(valor, op) :
    if op == 'E' :
        conv = valor * 0.81
        print('O valor convertido é de:', round(conv, 2))
    elif op == 'D' :
        conv = valor * 1.23
        print('O valor convertido é de:', round(conv, 2))
    else :
        print('Caracter inválido !!')

conversao(valor,op)
