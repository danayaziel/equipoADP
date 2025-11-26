def convertir_temp_v2(valor, hacia='F'):
    """Convierte una temperatura entre Celsius y Fahrenheit.
    
    - hacia='F' convierte de °C → °F
    - hacia='C' convierte de °F → °C
    Valida que 'hacia' sea 'F' o 'C'.
    """
    if hacia not in ('F', 'C'):
        raise ValueError("El parámetro 'hacia' debe ser 'F' o 'C'.")

    if hacia == 'F':
        # Celsius a Fahrenheit
        resultado = (valor * 9/5) + 32
    else:
        # Fahrenheit a Celsius
        resultado = (valor - 32) * 5/9

    return round(resultado, 2)

valor = float(input("Introduce la temperatura: "))
hacia = input("¿Convertir a Fahrenheit (F) o Celsius (C)? ").upper()
print(f"Resultado: {convertir_temp_v2(valor, hacia)}°{hacia}")
# Pruebas
print("20°C → F (v2):", convertir_temp_v2(20))        # esperado: 68.0
print("68°F → C (v2):", convertir_temp_v2(68, 'C'))   # esperado: 20.0