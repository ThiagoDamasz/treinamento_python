from smartphone import SmartPhone
class Mp3Player(SmartPhone):
    def __init__(self, tamanho, interface, capacidade):
        super().__init__(tamanho, interface)
        self.capacidade = capacidade
