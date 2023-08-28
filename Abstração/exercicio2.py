class cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def latir(self):
        print("AuAu!")
cachorro = cachorro("Milly", 3)
cachorro.latir()

