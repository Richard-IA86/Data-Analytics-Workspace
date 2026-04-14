# Aquí iremos guardando las funciones y herramientas de Python
# que vayamos creando
from typing import Dict, List, Optional


def ejemplo_funcion() -> None:
    print("¡Herramientas listas!")


def es_par(n: int) -> bool:
    """Retorna True si n es par, False si es impar."""
    return n % 2 == 0


def calcular_media(valores: List[float]) -> float:
    """Calcula la media aritmética de una lista no vacía."""
    if not valores:
        raise ValueError("La lista no puede estar vacía.")
    return sum(valores) / len(valores)


def calcular_mediana(valores: List[float]) -> float:
    """Calcula la mediana de una lista no vacía."""
    if not valores:
        raise ValueError("La lista no puede estar vacía.")
    ordenados = sorted(valores)
    n = len(ordenados)
    mitad = n // 2
    if n % 2 == 0:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2
    return float(ordenados[mitad])


def limpiar_nulos(lista: List[Optional[float]]) -> List[float]:
    """Elimina valores None de una lista."""
    return [v for v in lista if v is not None]


def contar_frecuencias(lista: list) -> Dict[object, int]:
    """Cuenta la frecuencia de cada elemento en la lista."""
    frecuencias: Dict[object, int] = {}
    for elemento in lista:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1
    return frecuencias


def normalizar(valores: List[float]) -> List[float]:
    """Normaliza al rango [0, 1] usando min-max scaling."""
    if not valores:
        raise ValueError("La lista no puede estar vacía.")
    minimo = min(valores)
    maximo = max(valores)
    if minimo == maximo:
        return [0.0] * len(valores)
    rango = maximo - minimo
    return [(v - minimo) / rango for v in valores]


def calcular_varianza(valores: List[float]) -> float:
    """Calcula la varianza poblacional de una lista no vacía."""
    if not valores:
        raise ValueError("La lista no puede estar vacía.")
    media = calcular_media(valores)
    return sum((v - media) ** 2 for v in valores) / len(valores)


def calcular_desviacion_estandar(valores: List[float]) -> float:
    """Calcula la desviación estándar poblacional."""
    return calcular_varianza(valores) ** 0.5


def aplanar_lista(lista: List[List[float]]) -> List[float]:
    """Aplana una lista de listas en una lista simple."""
    return [elem for sublista in lista for elem in sublista]


def multiplicar(a: float, b: float) -> float:
    """Retorna el producto de dos números."""
    return a * b


def concatena_info(nombre: str, **kwargs: object) -> str:
    """Combina un nombre con pares clave-valor en un string."""
    partes = [f"Nombre: {nombre}"]
    for clave, valor in kwargs.items():
        partes.append(f"{clave.capitalize()}: {valor}")
    return " | ".join(partes)
