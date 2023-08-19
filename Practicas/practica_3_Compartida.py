
#Define una función llamada celsius_a_fahrenheit que tome como parámetro una temperatura en grados Celsius y retorne la temperatura equivalente en grados Fahrenheit. 
#Utiliza la fórmula: Fahrenheit = Celsius * 9/5 + 32.
#Define otra función llamada fahrenheit_a_celsius que tome como parámetro una temperatura en grados Fahrenheit y retorne la temperatura equivalente en grados Celsius.
#Utiliza la fórmula: Celsius = (Fahrenheit - 32) * 5/9.
#En la función principal, solicita al usuario que elija una opción: convertir de Celsius a Fahrenheit (opción 1) o de Fahrenheit a Celsius (opción 2).
#Si el usuario elige la opción 1, solicita al usuario que ingrese una temperatura 
#en grados Celsius y muestra la temperatura equivalente en grados Fahrenheit utilizando la función celsius_a_fahrenheit.
#Si el usuario elige la opción 2, solicita al usuario que ingrese una temperatura 
# en grados Fahrenheit y muestra la temperatura equivalente en grados Celsius utilizando la función fahrenheit_a_celsius.


print("""Seleccione el valor a cambiar:
1) Fahrenheit a Celsius
2) Celsius a Fahrenheit""")

seleccion = float(input())

if seleccion == 1:
    #De fahrenheit a celsius
    print("ingrese el valor en grados fahrenheit: ")
    fahrenheit = float(input())
    conversion = (fahrenheit - 32)*100 * 5/9 //100
    print(f"La temperatura es {conversion} F°")
    
elif seleccion == 2:
    #De Celsius a Fahrenheit
    print("Ingrese una temperatura en grados Celsius")
    celsius_a_fahrenheit = float(input())
    calculo = ( celsius_a_fahrenheit * 9/5 + 32 )
    print (f"{calculo} Farenheits")
else:
    print("La opcion seleccionada es invalida")










