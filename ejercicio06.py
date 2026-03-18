# Ejercicio: El Sistema de Seguridad
# Objetivo: Crear un sistema de PIN con un límite de 3 intentos.

def sistema_seguridad():
    # 1. Definimos el PIN correcto y el límite de intentos
    pin_correcto = "1234"
    intentos_maximos = 3
    
    # Variables de control: contador de intentos y estado de éxito
    intentos = 0
    acertado = False
    
    print("--- SISTEMA DE SEGURIDAD DEL CAJERO ---")
    
    # 2. El ciclo tiene MÚLTIPLES condiciones de salida:
    # - Se detiene si el usuario acierta el PIN.
    # - Se detiene si se agotan el total de intentos.
    while intentos < intentos_maximos and not acertado:
        pin_usuario = input(f"\nIntento {intentos + 1}: Ingrese su PIN: ")
        
        if pin_usuario == pin_correcto:
            # Condición de ÉXITO
            acertado = True
        else:
            # Condición de FRACASO: incrementamos el contador
            intentos += 1
            print("PIN incorrecto.")
            
            # Mostramos cuántos intentos le quedan
            if intentos < intentos_maximos:
                print(f"Le quedan {intentos_maximos - intentos} intentos.")

    # 3. Al salir del ciclo, evaluamos por qué se detuvo el programa
    if acertado:
        print("\n¡Acceso concedido! Bienvenido a su cuenta.")
    else:
        print("\n****************************************")
        print("TARJETA BLOQUEADA por exceso de intentos.")
        print("Por favor, acuda a su banco más cercano.")
        print("****************************************")

if __name__ == "__main__":
    sistema_seguridad()
