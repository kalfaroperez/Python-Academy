#creando un conjunto con set
conjutno = set(["dato 1", "dato777"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["9dato", "wazaaaa"])
conjunto2 = {conjunto1, "viva Dios"}

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

#verificando si es un subconjunto
#resultado = conjunto2.issubset(conjunto1)

#Otra forma de verificar si es un subconjunto
resultado = conjunto2 <= (conjunto1)

#verificando si es un superconjunto
esultado = conjunto1.issuperset(conjunto2)
esultado = conjunto1 > (conjunto2)


#verificar si hay algun numero en comun
esultado = conjunto2.isdisjoint(conjunto1)
print(esultado)