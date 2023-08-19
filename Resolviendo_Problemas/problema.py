#crear 2 listas; Apellidos y Nombres; usando for

nombres = ["Gonzalo", "Dario", "Federico", "Natalia",]
apellidos= ["Martinez","Rodriguez","Gonzalez","Perez"]

with open("Resolviendo_Problemas\\nombre_y_apellido.txt","w") as arch:
    arch.writelines("los datos son: \n")
    [arch.writelines(f"Nombre: {n} \nApellido: {a}\n-------------\n") for n,a in zip(nombres,apellidos)]
    