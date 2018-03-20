Nota1 = float(input ("Introduzir 1 nota de 0 a 20 "))
Nota2 = float(input ("Introduzir 2 nota de 0 a 20 "))
Nota3 = float(input ("Introduzir 3 nota de 0 a 20 "))

Média =float((Nota1 * 25 + Nota2 * 35 + Nota3 * 40)/100) 

if Média >= 9.5 :
  print( "O aluno está aprovado com média de ", Média)
else :
    print( "O aluno está reprovado com média de ", Média)