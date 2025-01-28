carros= {"mazda", "chevypop", "nissan", "ferrari"}
numeros = {1,4,5,78}

#recorriendo la conjunto animales
for carro in carros:
    print(f"Ahora la variable carro es igual a: {carro}")
    
#recorriendo la conjunto numeros y * 2 
for numero in numeros:
    resultado = numero *2
    print(resultado)
 
#recorriendo 2 conjuntos a la vez   
for carro, numero in zip(carros, numeros):
    print(f"recorriendo conjunto 1: {carro}")
    print(f"recorriendo conjunto 2: {numero}")
    
#Recorre un bucle con rango establecido desde el inicial al penultimo y si solo tiene un numero sera desde 0 a ese numero 
for num in range(1,8):
    print(num)

for num1 in range(10):
    print(num1)    

#forma correcta para recorrer una conjunto por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
    
#ejecutando for con else
for carro in carros:
    print(f"Ahora la variable carro es igual a: {carro}")
else:
    print("el bucle finiquito")