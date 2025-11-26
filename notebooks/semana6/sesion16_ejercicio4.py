def contar_vocales(texto):
    """Cuenta el número de vocales en 'texto' (a, e, i, o, u)."""
    texto = texto.lower()
    vocales = "aeiou"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador
    
# Pruebas
texto = input("Introduce tu palabra: ")
print(f"'{texto}' tiene {contar_vocales(texto)} vocales")
print("Vocales en 'Hola Mundo':", contar_vocales("Hola Mundo"))  # esperado: 4
