# Ejercicio tabla de multiplcar 

# OBJETIVO
 
# Genere la tabla del multiplicar del 10
# La guarde en un archivo de texto 
# Luego lea el archivo y muestre su contenido en pantalla

with open("", "w") as archivo:
    for i in range(1, 11):
        resultado = 10 * i
        archivo.write(f"10 x {i} = {resultado}\n")

with open("tabla_multiplicar_10.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


# No ha sido terminado terminalo por favor 
