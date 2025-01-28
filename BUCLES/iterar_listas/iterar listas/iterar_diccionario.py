diccionario = dict(nombre = "Dany", apellido = "Hredia", heroe = "DIOS")
print(diccionario)

#recorriendo diccionario para obtener las claves
for key in diccionario:
    print(f"La clave es: {key}")



#recorriendo diccionario con item() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")