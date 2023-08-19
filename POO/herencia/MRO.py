class A:
    def hablar(self):
        print("Hola desde A")

class B():
    # pass
    def hablar(self):
        print("Hola desde B")

class C(A):
    # pass
    def hablar(self):
        print("Hola desde C")

# no importa desde donde herede
# siempre da prioridad a la clase
# desde donde estas escribiendo
class D(B,C):
    # pass
    def hablar(self):
        print("Hola desde D")
# Hereda desde la primer clase D("B",C)
# Busca en las clases padre de las
# subclases desde donde hereda

d=D()
d.hablar()

# mostrar orden de herencia
print(D.mro())










