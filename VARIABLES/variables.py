#definiendo una variable con CamelCase
nombreCompleto = "Dany"

#definiendo una variable Snake_case (Recomendado en python)
nombre_completo = "Dany Heredia"


#concatenar con +
nombre = "Dany"
bienvenida1= "Hola " + nombre +  " ¿como estas"
#No es un uso muy optimo ya que no se pueden concatenar numeros


#concatenar con f-strings
#para concatenar con caracteres de texto y numericos ejemplo: 7, Cristiano Ronaldo
bienvenida = f"Hola {nombreCompleto} ¿Como estas?"


#operadores de pertenencia (in/ not in)
print("Dany" in bienvenida) #Dany esta en bienvenida, si esta True
("Dany" not in bienvenida) # Dany no esta en bievenida, si esta entonces la afirmacion es False
