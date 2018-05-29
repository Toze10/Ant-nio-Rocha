class Aluno():
    def _init_ (self, nome, numero):
        self.nome = ""
        self.numero = ""

    def _str_(self):
        return "Numero {} | Nome {}".format(self.numero, (self.nome.title))


class Turma():
def  _init_(self, nome, anoletivo):
    self.nomedaturma = nome
    self.anoletivo = anoletivo
    self.listadealunos = []
    self.totaldealunos = 0

def validaraluno(self, Aluno):
    for i in range(self.totaldealunos):
        if self.listadealunos[i] == Aluno
            return True
        return False

def insere_instancia_aluno(self, Aluno):    
    if self.validaraluno(Aluno) == False:
        self.listadealunos.append(Aluno)
        self.totaldealunos += 1
        return True
    return False

def _inseriraluno_(self, nome, numero):
    self Aluno(nome, numero)
    return self.inser(self, Aluno)