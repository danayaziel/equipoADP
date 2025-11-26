def precio_con_iva_v2(precio, iva=0.16):
    """Devuelve el precio con IVA redondeado a 2 decimales.
    Valida que:
     precio >= 0
     0 <= iva <= 1
    """
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if not (0 <= iva <= 1):
        raise ValueError("El IVA debe estar entre 0 y 1.")

    total = precio * (1 + iva)
    return round(total, 2)

precio = float(input("Introduce el precio: "))
iva = float(input("Introduce el IVA: "))
resultado = precio_con_iva_v2(precio)
print(f"El precio con IVA es: ${resultado}")

# Pruebas
print("$100 con IVA 16% (v2):", precio_con_iva_v2(100))       # esperado: 116.0
print("$100 con IVA 8% (v2):", precio_con_iva_v2(100, 0.08))  # esperado: 108.0
