#Creando una lista(se puede modificar)
lista = ["Dany heredia", "SIUUU", True, 1.78, 1.79]


#Creando una tupla( no se puede modificar)
tupla = ("Dany heredia", "Viva cristo rey", False, 7.77)

#Esto es valido  
lista[3] = "QUE MACIZOOOO"

#Esto no es valido  
#tula[3] = "QUE MACIZOOOO"


#Creando un conjunto (set) (No accede a elementos por su indice, no almacena datos duplicados)
conjunto={"GOAT", "CR7", True, 1.86}
#print(conjunto[3]) -> no se puede acceder al elemento

#Creando un diccionario (dict)(La estructura del diccionario es 'key' : "value" y separamos con comas )
diccionario ={
    'nombre': "Dany",
    'canal' : "danyxdxd",
    'esta_feliz' : True,
    'altura' : 1.86,
    'eres Ryan G.' : "so easy, se acabo para mi"
}

#podemos acceder a los elementos del diccionario no por el indice sino por el nombre asignado
print(diccionario['altura'] + 2)






