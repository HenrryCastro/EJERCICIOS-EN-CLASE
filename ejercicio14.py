# FECHA 21/03/2026

# El control dde asistencia del curso

# Contadores
aprobados = 0
riesgo = 0
reprobados = 0

# Abrir archivo
with open("asistencia.text", "r") as archivo:
    for linea in archivo:
        # Separar datos (suponiendo formato: nombre,asistidas,total)
        datos = linea.strip().split(",")

        nombre = datos[0]
        asistidas = int(datos[1])
        total = int(datos[2])

        # Calcular porcentaje
        porcentaje = (asistidas / total) * 100

        # Evaluar reglas
        if porcentaje >= 80:
            estado = "Aprobado por asistencia"
            aprobados += 1
        elif 60 <= porcentaje < 80:
            estado = "En riesgo"
            riesgo += 1
        else:
            estado = "Reprobado por inasistencia"
            reprobados += 1

        # Mostrar resultado por estudiante
        print(f"{nombre}: {porcentaje:.2f}% - {estado}")

# Resultados finales
print("\nResumen:")
print(f"Aprobados: {aprobados}")
print(f"En riesgo: {riesgo}")
print(f"Reprobados: {reprobados}")

