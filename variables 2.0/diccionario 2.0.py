#creando diccionario con dict
diccionario = dict(nombre= "Dany", apellido = "diaz")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Dany", "aburrido y cansado"]) : "xddd"}

#creando diccionarios con fromkeys() valor por defecto none
diccionario = dict.fromkeys(["dany", "etesech"])

#creando diccionarios con fromkeys() valor por defecto cualquiera(XD)
diccionario = dict.fromkeys(["dany", "etesech"],"XD")

print(diccionario)