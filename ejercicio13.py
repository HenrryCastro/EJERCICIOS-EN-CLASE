# FECHA 21/03/2026

# =========================
# REGISTRO DE VISITANTES
# =========================
 
with open("visitantes.txt", "a") as archivo:
   
    print("=== REGISTRO ===")
   
    nombre = input("Nombre: ")
    edad = input("Edad: ")
   
    amuleto = input("¿Tiene amuleto? (si/no): ").lower()
    palabra = input("¿Conoce la palabra secreta? (si/no): ").lower()
   
    archivo.write(f"Nombre: {nombre}, Edad: {edad}, Amuleto: {amuleto}, Palabra: {palabra}\n")
 
print("✅ Guardado correctamente\n")
 
 
# =========================
# ANÁLISIS DE VISITANTES
# =========================
 
contador_si = 0
contador_no = 0
 
with open("visitantes.txt", "r") as archivo:
   
    print("=== RESULTADOS ===\n")
   
    for linea in archivo:
       
        datos = linea.strip().split(", ")
       
        nombre = datos[0].split(": ")[1]
        edad = int(datos[1].split(": ")[1])
        amuleto = datos[2].split(": ")[1]
        palabra = datos[3].split(": ")[1]
       
        if edad >= 18 and (amuleto == "si" or palabra == "si"):
            print(f"{nombre} -> Puede entrar")
            contador_si += 1
        else:
            print(f"{nombre} -> No puede entrar")
            contador_no += 1
 
print("\n=== RESUMEN ===")
print(f"Pueden entrar: {contador_si}")
print(f"No pueden entrar: {contador_no}")

