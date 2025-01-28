#Creando una lista con list()
#(un buen uso de list es para cuando se quieren crear una lista vacia, es decir, sin elementos)
lista = list(["dany", 34, 12.7, True])
lista1 = list([272,32,67,99,12,4842,False,True,-33993,-20,0.8383])
lista2 = [True, False, 2 , 8993, -3939]

#devuelve la cantidad de elementos de la lista
cantidad_de_elementos_ = len(lista)
print( cantidad_de_elementos_)

#Contamos la cantidad de elementos de la lista
lista.__len__()

#agregamos otro elemento a la lista
lista1.append("SIUUUUU")

#agregamos un elementoa la lista en un indice especifico
lista1.insert(1, "I'M STILL STANDING")

#agregamos varios elementos a la lista
# se deben agregar en forma de lista []
lista1.extend([False, "Soy feliz...", 777])


#Eliminando un elemento de la lista(por su indice)
#tecnica para eliminar el ultimo elemento de la tabla es establecer el incice de pop en -1, -2 para el anteultimo y asi sucesivamente,-3..,
lista1.pop(-1) 

#Remueve un elemento de la lista, por su valor
lista1.remove(99)


#Elimina todos los elementos de una lista
#lista.clear()

#Ordena una lista de forma ascendente a descendente (no funciona con datos alfanumericos)
lista2.sort()
#Si le agregamos este parametro a sort(reverse=True) orden en reversa, es decir, de descendente a ascendente
lista2.sort(reverse=True)
print(lista2)
#invierte los elementos de una lista
lista.reverse()

#Verificando un elemento de la lista
#en las tuplas solo podemos contar (count) y buscar un elemnto de la lista (index)
#en los conjuntos solo se puede sacar elementos(pop) y remover elementos(remove)
#encontrando_elemnto = lista.index()
