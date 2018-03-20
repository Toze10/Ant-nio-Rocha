A = int(input ("Introduzir 1 numero "))
B = int(input ("Introduzir 2 numero "))
C = int(input ("Introduzir 3 numero "))

if  A > B and B > C :
    print(A, B, C )
elif A > C and C > B :
    print(A, C, B)
elif B > A and A > C :
    print(B, A, C)
elif B > C and C > A :
    print(B, C, A)
elif C > A and A > B :
    print(C, A, B )
elif C > B and B > A :
    print(C, B, A )
