# Principio de inversion de dependencia 
# (Dependency inversion principle)
# La nocion de que se debe "depender-
# de abstracciones, no depender de 
# implementaciones"

# class Diccionario():
#     def verificar_palabra(self,palabra):
#         # logica para verificar palabras
#         pass

# class CorrectorOrtografico():
#     def __init__(self):
#         self.diccionario = Diccionario()
#     def corregir_texto(self,texto):
#         # usamos el diccionario para corregir texto
#         pass

from abc import ABC, abstractmethod

class CorrectorOrtografico():
    def __init__(self,verificador):
        self.verificador = verificador
    def corregir_texto(self,texto):
        # usamos el verificador para corregir el texto
        pass

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        pass

class ServicioWeb(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para usar el servicio online
        pass











