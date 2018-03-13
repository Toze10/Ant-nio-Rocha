Nota1 = float(input ("Introduzir nota 1 "))
Nota2 = float(input ("Introduzir nota 2 "))
Nota3 = float(input ("Introduzir nota 3 "))

Média =float((Nota1 * 25 + Nota2 * 35 + Nota3 * 40)/100) 
Médiainteira = float ((Nota1 * 25 + Nota2 * 35 + Nota3 * 40)//100)
Médiamd = (Nota1 * 25 + Nota2 * 35 + Nota3 * 40)%100

print ("Média é de ", Média )
print ("Média inteira é de", Médiainteira)
print ("Média de módulo de duvisão é de ", int (Médiamd))