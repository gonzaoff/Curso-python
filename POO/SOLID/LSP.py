# Principio de sustitucion de Liskov (Liskov substitution principle)
# La nocion de que los "objetos de un programan deberian- 
# ser reemplazables por instancias de sus subtipos- 
# sin alterar el correcto funcionamiento del programa".
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando."

class AveNoVoladora(Ave):
    def nadar(self):
        return "No vuelo, nado."


pinguino=AveNoVoladora()
print(pinguino.nadar())

