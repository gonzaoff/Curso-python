#Quiero conocer la diferencia porcentual entre el curso actual(1.5h) y:
#el mas rapido de los otros (2.5h)
#el mas lento de los otros (7h)
#el promedio (4h)

#editado
curso_actual = 1.5 #100%
rapido = 2.5
lento = 7
promedio = 4

diferencia_con_rapido = 100 - curso_actual * rapido
diferencia_con_lento = 100 - curso_actual * lento
diferencia_con_promedio = 100 - curso_actual * promedio

print(f"""------------------------------------------------------------------------
el curso actual es {round(diferencia_con_rapido,2)}% mas rapido que el curso mas rapido. 
el curso actual es {round(diferencia_con_lento,2)}% mas rapido que el curso mas lento.
el curso actual es {round(diferencia_con_promedio,2)}% mas rapido que el curso promedio
------------------------------------------------------------------------""")

#crudo
actual = 3.5
prom_crudo = 5

porcentaje_eliminado_actual = 100 - curso_actual * actual
porcentaje_elim_prom = 100 - promedio * prom_crudo

print(f"""el curso actual editado es {round(porcentaje_eliminado_actual,2)}% mas rapido que el curso crudo
el curso promedio editado es {round(porcentaje_elim_prom,2)}% mas rapido que el promedio crudo
------------------------------------------------------------------------""")

#Equivalencias

valor_curso = curso_actual
equivalencia_rapido = rapido *1000 // valor_curso /100 #Se agregan 2 decimales matematicamente
equivalencia_promedio = promedio *100 // valor_curso /10 #Se agrega 1 decimal matematicamente
equivalencia_lento = lento *100 // valor_curso /10

print(f"""Ver 10 horas de este curso equivalen a {equivalencia_rapido} veces el curso mas rapido.
Ver 10 horas de este curso equivalen a {equivalencia_lento} veces el curso mas lento.
Ver 10 horas de este curso equivalen a {equivalencia_promedio} veces el curso promedio.
------------------------------------------------------------------------""") 

