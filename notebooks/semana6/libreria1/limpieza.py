"""Utilidades de limpieza para listas de diccionarios (filas de CSV)."""
from typing import List, Dict, Any, Callable, Optional

Fila = Dict[str, Any]

def eliminar_duplicados(filas: List[Fila], clave: str) -> List[Fila]:
    """Elimina filas duplicadas según una 'clave' (columna)."""
    vistos = set()
    resultado = []
    for f in filas:
        k = f.get(clave)
        if k not in vistos:
            vistos.add(k)
            resultado.append(f)
    return resultado

def reemplazar_nulos(filas: List[Fila], sustitutos: Dict[str, Any]) -> List[Fila]:
    """Reemplaza valores vacíos/None por sustitutos por columna."""
    def esta_vacio(x):
        return x is None or (isinstance(x, str) and x.strip() == "") or x == "N/A"
    out = []
    for f in filas:
        nuevo = f.copy()
        for col, val in sustitutos.items():
            if col in nuevo and esta_vacio(nuevo[col]):
                nuevo[col] = val
        out.append(nuevo)
    return out

def convertir_tipos(filas: List[Fila], conversores: Dict[str, Callable[[str], Any]]) -> List[Fila]:
    """Aplica funciones de conversión por columna (por ej., int, float, str)."""
    out = []
    for f in filas:
        nuevo = f.copy()
        for col, func in conversores.items():
            if col in nuevo:
                try:
                    nuevo[col] = func(nuevo[col])
                except Exception:
                    # si falla, deja el valor original
                    pass
        out.append(nuevo)
    return out
    