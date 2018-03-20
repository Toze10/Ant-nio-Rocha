saldo = float(input('Introduza o saldo da sua conta: '))
print('Introduza a opcao que deseja realizar: ')
print('1- Creditar')
print('2- Debitar')
operacao = input('Introduza a operação: ') 

if operacao == '1' :
    credito = float(input('Introduza quanto quer creditar na sua conta: '))
    resultado = saldo + credito
    print('Ficou com um saldo de: ', resultado)
elif operacao == '2' :
    debito = float(input('Introduza quanto quer debitar na sua conta: '))
    resultado = saldo - debito
    if resultado < 0 :
        print('Saldo insuficiente')
    else :
        print('Ficou com um saldo de: ', resultado)