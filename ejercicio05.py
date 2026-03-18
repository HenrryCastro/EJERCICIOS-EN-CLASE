
# Henrry Genaro Castro Jímenez FECHA 07/03/2026

# Ejercicio: El Menú Interactivo de Restaurante
# Objetivo: Crear un bucle de aplicación que solo cierre al elegir la opción 3.

def menu_restaurante():
    opcion = ""
    
    # El bucle de la aplicación principal
    # Se mantiene "vivo" mientras la opción no sea '3'
    while opcion != "3":
        print("\n--- MENÚ DE RESTAURANTE ---")
        print("1. Pedir")
        print("2. Ver Cuenta")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "1":
            print(">> Has elegido: Realizar un pedido.")
            # Aquí iría el código para pedir comida
        elif opcion == "2":
            print(">> Has elegido: Ver el total de la cuenta.")
            # Aquí iría el código para mostrar la cuenta
        elif opcion == "3":
            print(">> Saliendo del sistema... ¡Gracias por su visita!")
        else:
            print("!! Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    menu_restaurante()
