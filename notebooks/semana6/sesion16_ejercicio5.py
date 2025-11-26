def maximo_lista(numeros):
    """Devuelve el máximo de la lista sin usar max(); None si está vacía."""
    if len(numeros) == 0:
        return None
    else:
        maximo = numeros[0]
        for num in numeros:
            if num > maximo:
                maximo = num
        return maximo

# Pruebas
lista = input("Introduce los valores: ")
numeros = [float(i) for i in lista.split()]
print(f"El número máximo de [{lista}] es {maximo_lista(numeros)}")
print("Máximo de [3, 9, 2, 10]:", maximo_lista([3, 9, 2, 10]))  # esperado: 10
print("Máximo de []:", maximo_lista([]))                        # esperado: None