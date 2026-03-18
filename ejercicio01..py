
# Henrry Genaro Castro Jímenez   FECHA 21/03/2026

# Programa para contar cuántos números ingresa el usuario
# Termina cuando el usuario ingresa el número 0

def programa_contador():
    contador = 0
    print("Ingresa números. El programa terminará cuando escribas 0.")

    while True:
        try:
            # Pedimos el número al usuario
            numero = float(input("Escribe un número: "))
            
            # Condición de salida
            if numero == 0:
                break
            
            # Incrementamos el contador si el número no es 0
            contador += 1
        except ValueError:
            # En caso de que el usuario no ingrese un número válido
            print("Entrada no válida. Por favor, ingresa un número.")

    # Mostramos el resultado final
    print(f"\nSe ingresaron {contador} números en total.")

if __name__ == "__main__":
    programa_contador()
