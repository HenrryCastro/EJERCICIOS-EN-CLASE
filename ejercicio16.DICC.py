# FECHA 28/03/2026
# DICCIONARIOS         2

# El traductor del robot oxidado

# 1. Crear el diccionario con las traducciones iniciales
memoria_robot = {
    "001": "Hola",
    "010": "Adiós",
    "100": "Aceite"
}

# 1.1 El robot aprende una palabra nueva
memoria_robot["111"] = "Amigo"

# 2. Un usuario dice "010". Imprimir la traducción.
# Acceso directo porque sabemos que existe
print(f"Traducción de '010': {memoria_robot['010']}")

# 3. El robot intenta traducir "101" usando el método .get()
# .get(clave, mensaje_si_no_existe)
resultado = memoria_robot.get("101", "Error: Código no encontrado en mi base de datos")

print(resultado)

