# 28/03/26
# DICCIONARIOS

# Inventario del alquimista ciego



# 1. Crear el diccionario y agregar los primeros ingredientes
caldero = {
    "Colas de lagartija": 5,
    "Polvo de estrellas": 2
}

# 2. Sumar 3 "Colas de lagartija" más al valor existente
# Accedemos a la clave y le sumamos la nueva cantidad
caldero["Colas de lagartija"] += 3

# 3. Eliminar el ingrediente "Polvo de estrellas"
# Usamos 'del' para borrar la clave y su valor completamente
del caldero["Polvo de estrellas"]

# 4. Imprimir el inventario final
print("Inventario final del caldero:")
print(caldero)

