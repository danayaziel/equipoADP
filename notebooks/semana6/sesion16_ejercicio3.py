def es_primo_v2(n):
    """ devuelve True si n es un entero primo; de lo contrario False."""
    if n % 2 == 0:
        return False
    else:
        return True
    
n = int(input("Introduce un número: "))
print(es_primo_v2(n))
print("¿11 es primo v2?:", es_primo_v2(11))  # True
print("¿12 es primo v2?:", es_primo_v2(12))  # False
print("¿3.5 es primo v2?:", es_primo_v2(3.5))# False