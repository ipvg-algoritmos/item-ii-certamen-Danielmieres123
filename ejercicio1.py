# 📝 ejercicio1.py
# ✖️ Tabla de multiplicar con función y bucle for
# Puntaje: 7 puntos

# Instrucciones:
# 1. Crea una función llamada mostrar_tabla(n)
# 2. Esta función debe imprimir la tabla de multiplicar del número n desde 1 hasta 10
# 3. Utiliza un bucle para generar e imprimir los resultados
# 4. Luego, solicita al usuario un número y llama a la función con ese valor

# 👇 Aquí comienza tu código


#aa
def mostrar_tabla(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Solicita al usuario un número
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
mostrar_tabla(numero)
