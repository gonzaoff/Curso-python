#Escribir un algoritmo que convierta los números arábigos 
#en romanos y viceversa (I = 1, V = 5, X = 
#10, L = 50, C = 100, D = 500 y M = 1000). 
print("""Determine la operacion que desea realizar
1) Convertir numeros arabigos a romanos
2) Convertir numeros romanos a arabigos
""")
seleccion = int(input())

#Arabigo a Romano
if seleccion == 1:
    print("Ingrese el valor en numeros Arabigos: ")
    def conversion_entero_romano(entero):
        numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numeral = ''
        i = 0
        while entero > 0:
            for _ in range(entero // numeros[i]):
                numeral += numerales[i]
                entero -= numeros[i]
            i += 1
        return numeral
    print(f"el numero ingresado se traduce como: {conversion_entero_romano(int(input()))}")

#Romano a Arabigo
if seleccion == 2:
    print("Ingrese el valor en numeros Romanos: ")
    def rom_ent(romano):
        romanos = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        return sum(
            romanos[romano[i]] - 2 * romanos[romano[i - 1]]
            if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]
            else romanos[romano[i]]
            for i in range(len(romano))
        )
    print(f"el numero ingresado se traduce como: {rom_ent(input())}")