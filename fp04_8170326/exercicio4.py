def fact(n):
    if n == -1:
        return 0
    elif fact(n - 1):
        return n
    print(n)

num = int(input('Introduza um numero: '))

fact(num)