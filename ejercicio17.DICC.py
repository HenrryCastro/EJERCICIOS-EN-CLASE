# FECHA 28/03/2026
# DICCIONARIOS         3
# El banquete del Ogro Gourmet


# Crear el diccionario con los platos y sus niveles de delicia
banquete = {
    "Sopa de pantano": 4,
    "Pastel de rocas": 7,
    "Filete de dragón": 10
}

# 1. El ogro decide que la Sopa de pantano está mejor. Actualizar a 6.
banquete["Sopa de pantano"] = 6

# 2. Imprimir solo los nombres de los platos (las llaves)
# Usamos el método .keys() para obtener solo los nombres
print("Menú del Ogro Gourmet:")
print(list(banquete.keys()))

# 3. Condicional para el Filete de dragón
if banquete["Filete de dragón"] > 8:
    print("¡Un festín digno de un rey ogro!")


    