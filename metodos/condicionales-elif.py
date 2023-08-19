#Condicionales

#if <condicion>: ##Si:
#    <accion>
#elif <condicion>: ##Sino, Si:
#   <accion>
#else: ## Si no se cumplen ninguna de las condiciones:
#   <accion>

edad = int(input())

if edad >= 18:
    print("sos mayor de edad")
elif edad >= 16:
    print("sos adolescente")
else:
    print("sos menor")









