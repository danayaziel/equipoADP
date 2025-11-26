def area_triangulo_v2(base, altura):
    """Calcula el área de un triángulo"""
    if base <=0 or altura <=0:
        raise ValueError("La base o altura no pueden ser menor o igual a 0")
    else:
        area = (base*altura) / 2
        return area
    
    # Pruebas
try:
    base = float(input("Introduce el valor de la base: "))
    altura = float(input("Introduce el valor de la altura: "))

    resultado = area_triangulo_v2(base, altura)
    print("El área del triángulo es: ", resultado)

except ValueError:
    print("Error")

    



