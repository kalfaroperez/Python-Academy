# A)Diferencia en porcentaje entre el curso actual y :
#  -> El mas rapido de otros cursos
#  -> El mas lento de otros cursos
#  -> El promedio de los cursos 
 
#     B)Porcentaje de material inservible que se reduce en:
#  -> El promedio de los cursos 
#  -> El curso actual 
 
#     C)Ver 10h de este curso a cuantas de otros cursos equivale y viceversa

#Definimos variables
curso_actual = 1.5
curso_mas_rapido = 2.5
curso_mas_lento = 7
curso_promedio = 4

porcentaje_curso_actual = float(curso_actual * 100)//curso_mas_lento
porcentaje_curso_mas_rapido = float(curso_mas_rapido *100)//curso_mas_lento
porcentaje_curso_mas_lento = float(curso_mas_lento *100)//curso_mas_lento
porcentaje_promedio_cursos = float(curso_promedio * 100)//curso_mas_lento

crudo_curso_actual = 3.5
crudo_curso_actual_min = 1.5
crudo_curso_promedio = 5
crudo_curso_promedio_min = 4

porcentaje_crudo_curso_actual_min = float(crudo_curso_actual_min * 100)/crudo_curso_actual
porcentaje_crudo_curso_actual = float(crudo_curso_actual * 100)/crudo_curso_actual
porcentaje_crudo_curso_promedio = float(crudo_curso_promedio * 100)/crudo_curso_promedio
porcentaje_crudo_curso_promedio_min = float(crudo_curso_promedio_min * 100)/ crudo_curso_promedio



#Operamos el A
Diferencia_mas_rapido = float(porcentaje_curso_actual - porcentaje_curso_mas_rapido) * -1
Diferencia_mas_lento = float(porcentaje_curso_actual - porcentaje_curso_mas_lento) * -1
Diferencia_promedio_cursos = float(porcentaje_curso_actual - porcentaje_promedio_cursos) * -1

#Operamos B
reduccion_curso_actual = float(porcentaje_crudo_curso_actual - porcentaje_crudo_curso_actual_min)
reduccion_curso_prom = float(porcentaje_crudo_curso_promedio - porcentaje_crudo_curso_promedio_min)

#Mostrando diferencia de este curso con otros
equivalencia = curso_promedio *100 // curso_actual /10


print(" -----HORAS TOMADAS PARA CADA CURSO----- ")
print(f" Curso actual es igual a: {curso_actual} ")
print(f" Curso mas rapido es igual a: {curso_mas_rapido} ")
print(f" Curso mas lento es igual a: {curso_mas_lento} ")
print(f" El promedio de los cursos es igual a: {curso_promedio} ")
print("")
print("------DIFERENCIAS EN % ------ ")
print(f" La diferencia en porcentaje entre el curso actual {porcentaje_curso_actual} y el curso mas rapido {porcentaje_curso_mas_rapido} es de: {Diferencia_mas_rapido}% ")
print(f" La diferencia en porcentaje entre el curso actual {porcentaje_curso_actual} y el curso mas lento {porcentaje_curso_mas_lento} es de: {Diferencia_mas_lento}% ")
print(f" La diferencia en porcentaje entre el curso actual {porcentaje_curso_actual} y el curso promedio {porcentaje_promedio_cursos} es de: {Diferencia_promedio_cursos}% ")
print("")
print(" ------LA REDUCCION DE MATERIAL INSERVIBLE EN %----- ")
print(f" El porcentaje que se reduce de material inservible en el promedio de los cursos es de: {reduccion_curso_prom}% ")
print(f" El porcentaje que se reduce de material inservible en el curso actual es de: {reduccion_curso_actual}%")

print("--------------------------------------------")
print(f"ver 10 horas de este curso equivale  a ver en otros cursos: {equivalencia}")