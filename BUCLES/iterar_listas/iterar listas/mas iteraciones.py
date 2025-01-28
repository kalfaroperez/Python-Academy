futbol = ["messi", "cr7", "mbappe", "neymar", "vini"]
cadena = "MUCHAS GRACIAS MI AFICCION"
numeros = [2,7,9,4]

#EVITANDO UN PARAMETRO CON LA SENTENCIA continue
for fut in futbol:
    if fut == 'messi':
        continue
    print(f"MIS JUGADORRS DE FUTBOL SON: {fut}")
    

#Cerrando de choque el bucle con el parametro break(el else no se ejecuta tampoco)
for fut in futbol:
    if fut == 'neymar':
        break
    print(f"MIS JUGADORRS DE FUTBOL SON: {fut}")
print("Bucle terminado")

#iterar una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
doble_numeros = [x*2 for x in numeros]
print( doble_numeros)