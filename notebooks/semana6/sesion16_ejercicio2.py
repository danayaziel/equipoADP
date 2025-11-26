def promedio_v2(numeros):
    """ devuelve el promedio o None si la lista está vacía."""
    if len(numeros) == 0:
        return None
    else: 
        promedio = sum(numeros) / len(numeros)
        return promedio

#pruebas

valores = input("Introduce tus valores: ")
numeros = [float(i) for i in valores.split()]
resultado = promedio_v2(numeros)
print("El promedio es: ", resultado)

print("Promedio v2 [1,2,3]:", promedio_v2([1,2,3]))
print("Promedio v2 []:", promedio_v2([])) 

