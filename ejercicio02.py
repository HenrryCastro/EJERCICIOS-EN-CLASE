
# Henrry Genaro Castro Jímenez  FECGA 21/03/2026

# Ejercicio: El Ascensor Infinito
# Objetivo: Imprimir los pisos del 1 al 5 mientras el ascensor sube.


def control_ascensor():
    # Inicializamos la variable en 1 (Piso actual)
    piso_actual = 1
    
    print("El ascensor está subiendo...")
    
    # El ciclo continúa mientras el piso sea menor o igual a 5
    # Esto permite que el piso 5 también sea procesado.
    while piso_actual <= 5:
        print(f"Piso actual: {piso_actual}")
        
        # Aumentamos el valor de uno en uno
        piso_actual += 1
        
    print("El ascensor ha llegado al piso 5.")

if __name__ == "__main__":
    control_ascensor()
