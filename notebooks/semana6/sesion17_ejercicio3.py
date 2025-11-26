# Variable global
estado = "ok"

def forzar_error():
    """Usa la variable global 'estado' y la cambia a 'error'."""
    global estado
    estado = "error"

def resetear():
    """Devuelve la cadena 'ok' (sin usar global) para reasignar manualmente."""
    return "ok"


# 🔹 Interacción con el usuario
print("Estado actual:", estado)

accion = input("¿Deseas forzar un error (E) o resetear (R)? ").upper()

if accion == "E":
    forzar_error()
elif accion == "R":
    estado = resetear()
else:
    print("Opción no válida.")

print("Estado actual:", estado)