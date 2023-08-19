class animal():
    def comer(self):
        return "puedo comer"

class mamifero(animal):
    def amamantar(self):
        return "puedo amamantar"

class aves(animal):
    def volar(self):
        return "puedo volar"


class murcielago(mamifero,aves):
    def puedo(self):
        return f"{self.amamantar(), self.comer(), self.volar()}"

murci=murcielago()

print(murci.puedo())












