entran = 0  
no_entran = 0

with open("visitantes.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if not linea:  
            continue
            
        datos = linea.split(",")
        
        nombre = datos[0]
        edad = int(datos[1])
        amuleto = datos[2].lower()
        palabra = datos[3].lower()

        if edad >= 18 and (amuleto == "si" or palabra == "si"):
            print(nombre, "- Puede entrar")
            entran += 1
        else:
            print(nombre, "- No puede entrar")
            no_entran += 1

print("\nResumen:")
print("Entraron:", entran)
print("No entraron:", no_entran)




