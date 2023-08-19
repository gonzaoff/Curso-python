import tkinter as tk

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

def rom_ent(romano):
    romanos = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    return sum(
        romanos[romano[i]] - 2 * romanos[romano[i - 1]]
        if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]
        else romanos[romano[i]]
        for i in range(len(romano))
    )

def convertir():
    seleccion = var.get()
    if seleccion == 1:
        entero = int(entry.get())
        resultado = conversion_entero_romano(entero)
        label_resultado.config(text=f"Resultado: {resultado}")
    elif seleccion == 2:
        romano = entry.get()
        resultado = rom_ent(romano)
        label_resultado.config(text=f"Resultado: {resultado}")

root = tk.Tk()
root.title("Conversor de números")

var = tk.IntVar()

label_instruccion = tk.Label(root, text="Determine la operación que desea realizar")
label_instruccion.pack()

radio_arabigo_romano = tk.Radiobutton(root, text="Convertir números arábigos a romanos", variable=var, value=1)
radio_arabigo_romano.pack()

radio_romano_arabigo = tk.Radiobutton(root, text="Convertir números romanos a arábigos", variable=var, value=2)
radio_romano_arabigo.pack()

label_entrada = tk.Label(root, text="Ingrese el valor:")
label_entrada.pack()

entry = tk.Entry(root)
entry.pack()

boton_convertir = tk.Button(root, text="Convertir", command=convertir)
boton_convertir.pack()

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.pack()

root.mainloop()

