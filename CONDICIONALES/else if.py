#el condicional else if en python se usa como elif
ingreso_mensual = 900000
gasto_mensual = 100

#if anidados y elif (else if)
if ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en quiebra manolo")
    elif ingreso_mensual - gasto_mensual > 30000:
        print("VAS BIEN ")
    else:
        print("Gastas mucho bot :/")
    
elif ingreso_mensual > 100:
    print("ESTAS BIEN ECONOMICAMENTE EN COLOMBIA")  
elif ingreso_mensual > 900:
    print("ESTAS BIEN ECONOMICAMENTE EN PORTUGAL") 
elif ingreso_mensual > 50:
    print("ESTAS BIEN ECONOMICAMENTE EN AFRICA") 
else:
    print("eres alto pobre amigo :()")