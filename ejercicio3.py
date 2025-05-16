# 📝 ejercicio3.py
# 🔁 Verificador de palíndromos
# Puntaje: 15 puntos

# Instrucciones:
# 1. Solicita al usuario una palabra o frase.
# 2. Crea una función llamada es_palindromo(texto) que:
#    - Convierta el texto a minúsculas
#    - Elimine los espacios
#    - Compare el texto con su reverso
# 3. Muestra si es o no un palíndromo con un mensaje claro.

# 👇 Aquí comienza tu código


#ALKJSDGLAUGSD
def es_palindromo(texto):
    texto = texto.lower() 
    texto = texto.replace(" ", "")
    return texto == texto[::-1]

frase = input("Ingresa una palabra o frase: ")

if es_palindromo(frase):
    print("✅ Es un palíndromo.")
else:
    print("❌ No es un palíndromo.")