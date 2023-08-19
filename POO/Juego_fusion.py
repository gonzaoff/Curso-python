
class Personajes():
    def __init__(self,nombre,ki):
        self.nombre = nombre
        self.ki = ki
    def __str__(self):
        return f"{self.nombre} (ki={self.ki})"
    def __add__(self,otro_pj):
        nuevo_nombre = f"{self.nombre}-{otro_pj.nombre}"
        nuevo_ki = round(((self.ki + otro_pj.ki)/2)**1.5)
        return Personajes(nuevo_nombre,nuevo_ki)
    
    # personaje1=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    # personaje2=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    # personaje3=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    # personaje4=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    # personaje5=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    # personaje6=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    # personaje7=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    # personaje8=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    
lista_personajes = []


print("""1. Crear Personaje
2. Fusionar Peresonajes
3. Mostrar Personajes
4. Salir""")
seleccion = input("Seleccione una opcion: ")
if seleccion == "1":
    personaje1=Personajes(input("nombre del pj: "),input("poder de pelea: "))
    print("El personaje fue creado con exito")
    lista_personajes.append(print(personaje1))
    print("Deseas crear otro personaje? ")
    selec=input("Si o No? ")
    if selec == "Si":
        personaje2=Personajes(input("nombre del pj: "),input("poder de pelea: "))
        print("El personaje fue creado con exito")
        lista_personajes.append(print(personaje2))
        print(lista_personajes)