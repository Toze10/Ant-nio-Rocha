class Aluno():
    def _init_ (self, nome, numero):
        self.nome = ""
        self.numero = ""

    def _str_(self):
        return "Numero {} | Nome {}".format(self.numero, (self.nome.title))

#dados do aluno
#Aluno()  
#Aluno.nome = input ("Insira o nome do aluno: ")
#Aluno.numero = input ("Insira numero do aluno: ")
