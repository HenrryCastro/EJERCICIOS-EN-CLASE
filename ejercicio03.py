
# Henerry Genaro Castro Jímenez FECHA 07/03/2026

# Ejercicio: El Guardián de la Puerta
# Objetivo: Validar una palabra clave usando un valor centinela.

def guardian_de_la_puerta():
    # Definimos la palabra secreta
    secreto = "SESAMO"
    
    # Inicializamos la variable con un valor vacío para que entre al ciclo
    palabra_usuario = ""
    
    # Ciclo controlado por un valor centinela (sesamo)
    # El ciclo se repite MIENTRAS la palabra sea diferente a "SESAMO"
    while palabra_usuario != secreto:
        palabra_usuario = input("Ingresa la palabra clave para entrar: ")
        
        # Si la palabra es incorrecta, mostramos el mensaje de error
        if palabra_usuario != secreto:
            print("Acceso denegado. Intente de nuevo:")
            
    # Cuando sale del ciclo es porque escribió la palabra correcta
    print("\n¡Acceso concedido! Bienvenido a la zona privada.")

if __name__ == "__main__":
    guardian_de_la_puerta()
