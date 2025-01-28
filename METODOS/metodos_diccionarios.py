#Inicia el diccionario con comillas simples
diccionario = {
    'nombre':"Dany",
    'pais':"Colombia",
    'futbolista':"Cristiano Ronaldo",
    'edad': 19
}    

#Nos devuelve un objeto dic items (se puede iterar tambien) 
claves = diccionario.keys()


#Obteniendo un elemento con get()  (sino encuentra nada el programa continua)
valor_clave_edad = diccionario.get("jsksk")


#Elimina todo el diccionario
#elimina_diccionario = diccionario.clear()

#Eliminando un elemnto del diccionario
diccionario.pop("nombre")

#Obteniendo un elemento dic items iterable
elemento_iterable = diccionario.items()
print(elemento_iterable)
