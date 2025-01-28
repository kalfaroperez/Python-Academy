#el ser humano habla 2 palabras * 1 segundo
#A)Pedirle al usuario que diga cualquier texto real y
#  -> calcular cuanto tardaria en decir esa frase 
#  -> cuantas palabras dijo

#B)si se tardara mas de un minuto 
#  ->decirle para flaco tampoco te pedi un testamento

Palabra = input("INGRESE UN TEXTO REAL: ")
palabras_separadas = Palabra.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f"dijistes {cantidad_de_palabras} palabras y el tiempo que empleastes fue {cantidad_de_palabras/2} segundos en decirlo")
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")