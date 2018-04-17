def login(username,passe): 
    utilizador = "Aluno"
    password = "estg2018"

    if username == utilizador and password == passe:
        return True
    return False

def validar():
    contar = 0
    while contar != 3:
        print ("Insira o seu utlizador e a sua password ")
        username = input ("Username ")
        passe = input ("Password ")
        if login (username,passe):
            print ("Sessão iniciada")
            break
        else: 
            print ("Utilizador ou password estao incorretos ")
        contar +=1
        if contar >=3:
            print("Tente mais tarde ")
validar ()