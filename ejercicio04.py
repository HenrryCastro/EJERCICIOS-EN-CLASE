
# Henrry Genaro Castro Jímenez FECHA 07/03/2026

# Ejercicio: La alcancía de Ahorros
# Objetivo: Ahorrar hasta llegar a Q500 usando un acumulador.

def alcancia_ahorros():
    costo_consola = 500
    # El acumulador empieza en 0
    ahorro_total = 0
    
    print(f"¡Bienvenido! Vamos a ahorrar para tu consola de Q{costo_consola}.")
    
    # El ciclo se repite mientras el ahorro sea MENOR al costo
    while ahorro_total < costo_consola:
        print(f"\nLlevas ahorrado: Q{ahorro_total}")
        falta = costo_consola - ahorro_total
        print(f"Te faltan Q{falta} para llegar a la meta.")
        
        try:
            monto_hoy = float(input("¿Cuánto dinero vas a meter hoy a la alcancía? Q"))
            
            if monto_hoy > 0:
                # Aquí usamos el ACUMULADOR: sumamos el nuevo monto al total
                ahorro_total += monto_hoy
            else:
                print("Por favor, ingresa un monto mayor a 0.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

    # Al salir del ciclo es porque ahorro_total >= 500
    print(f"\n¡Felicidades! Tienes Q{ahorro_total}. ¡Ya puedes comprar tu consola!")

if __name__ == "__main__":
    alcancia_ahorros()
