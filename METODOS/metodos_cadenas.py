cadena1 = "Muchas gracias mi aficcion"
cadena2 = "quiero ser grande por mis padres"
cadena3 = "TE AMO DIOS"
cadena4 = "Halamadrid"
cadena5 = "28"
cadena6 = "me,llamo,barry,allen,soy,el,velocista,mas,rapido,del,planeta"

#La estructura de un metodo de cadenas es: dato.nombre del metodo() ej: cadena7.lower

#convierte a mayusculas(Upper)
mayus = cadena1.upper()


#Convierte a minuscula(Lower)
minus = cadena1.lower()

#Primera letra en mayuscula (Capitalize)
Prim_letra_mayus = cadena2.capitalize()


#Buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1 (Find)
busqueda_find = cadena3.find("S")


#Buscamos una cadena en otra cadena, si no hay coincidencias devuelve un error (Index)
busqueda_index = cadena4.index("d")


#Si es numerico devolvemos true, sino false (Isnumeric)
es_numerico = cadena5.isnumeric()

#Si es alfanumerico devolvemos true, sino false (Isalpha)
#Solo si son letras de la a-z devuelve true
es_alfanumerico = cadena4.isalpha()

#Contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias (Count)
cantidad_de_coincidencia = cadena6.count("barry")


#Contamos cuantos caracteres tiene una cadena (Len)
#len es una funcion
conteo_cadena = len(cadena1)
print(conteo_cadena)

#verificamos si una cadena, empieza con otra cadena dada, si es asi devuelve True (Startswith)
empieza_con = cadena6.startswith("me")


#verificamos si una cadena, termina con otra cadena dada, si es asi devuelve True (Endswith)
termina_con = cadena6.endswith("ta")


#reemplaza un pedazo de cadena dada por otra dada actualmente, si el valor, se encuentra en la cadena original, reemplaza el valor de la misma en 2 (Replace)
cadena_nueva = cadena6.replace("barry allen soy el velocista mas rapido del planeta", "superman, no los puedo salvar a todos porque no soy Dios pero puedo intentarlo porque soy superman")

#separar cadenas con la cadena que le pasemos(Split)
cadena_matriz =cadena6.split(",")

