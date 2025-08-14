class Pessoa ():

    def __init__(self, nome='', idade=0, cidade='', telefone='', email=''):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, mora em {self.cidade}"
