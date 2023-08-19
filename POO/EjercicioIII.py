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


goku=Personajes("Goku",543)
vegeta=Personajes("Vegeta",324)
bills=Personajes("Bills",789)

nuevo_personaje=goku+bills+vegeta
print(nuevo_personaje)
