def lerinteiro(min,max) : 
    num = min - 1
    while num < 0 or num > 10 :
        num = int(input('Introduza um numero inteiro: '))
    return num

def valor() :
    num = lerinteiro(0,50)
    print('*' * num)

valor()