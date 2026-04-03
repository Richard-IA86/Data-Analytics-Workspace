"""
Tests unitarios — Herramientas/mis_funciones.py
Suite: data_analytics — qa/cobertura_herramientas
"""

import pytest

from Herramientas.mis_funciones import (
    calcular_media,
    calcular_mediana,
    contar_frecuencias,
    es_par,
    limpiar_nulos,
    normalizar,
)


# ── es_par ──────────────────────────────────────────────────
class TestEsPar:
    def test_numero_par(self) -> None:
        assert es_par(4) is True

    def test_numero_impar(self) -> None:
        assert es_par(7) is False

    def test_cero_es_par(self) -> None:
        assert es_par(0) is True

    def test_negativo_par(self) -> None:
        assert es_par(-6) is True

    def test_negativo_impar(self) -> None:
        assert es_par(-3) is False


# ── calcular_media ───────────────────────────────────────────
class TestCalcularMedia:
    def test_lista_simple(self) -> None:
        assert calcular_media([1.0, 2.0, 3.0]) == pytest.approx(2.0)

    def test_un_elemento(self) -> None:
        assert calcular_media([5.0]) == pytest.approx(5.0)

    def test_lista_vacia_lanza_error(self) -> None:
        with pytest.raises(ValueError):
            calcular_media([])

    def test_valores_negativos(self) -> None:
        assert calcular_media([-2.0, 0.0, 2.0]) == pytest.approx(0.0)

    def test_valores_decimales(self) -> None:
        assert calcular_media([1.5, 2.5]) == pytest.approx(2.0)


# ── calcular_mediana ─────────────────────────────────────────
class TestCalcularMediana:
    def test_lista_impar(self) -> None:
        assert calcular_mediana([1.0, 3.0, 5.0]) == pytest.approx(3.0)

    def test_lista_par(self) -> None:
        assert calcular_mediana([1.0, 2.0, 3.0, 4.0]) == pytest.approx(2.5)

    def test_un_elemento(self) -> None:
        assert calcular_mediana([7.0]) == pytest.approx(7.0)

    def test_desordenada(self) -> None:
        assert calcular_mediana([5.0, 1.0, 3.0]) == pytest.approx(3.0)

    def test_lista_vacia_lanza_error(self) -> None:
        with pytest.raises(ValueError):
            calcular_mediana([])


# ── limpiar_nulos ─────────────────────────────────────────────
class TestLimpiarNulos:
    def test_sin_nulos(self) -> None:
        assert limpiar_nulos([1.0, 2.0, 3.0]) == [1.0, 2.0, 3.0]

    def test_todos_nulos(self) -> None:
        assert limpiar_nulos([None, None]) == []

    def test_lista_vacia(self) -> None:
        assert limpiar_nulos([]) == []

    def test_nulos_intercalados(self) -> None:
        resultado = limpiar_nulos([1.0, None, 3.0, None, 5.0])
        assert resultado == [1.0, 3.0, 5.0]


# ── contar_frecuencias ────────────────────────────────────────
class TestContarFrecuencias:
    def test_sin_repeticiones(self) -> None:
        assert contar_frecuencias([1, 2, 3]) == {1: 1, 2: 1, 3: 1}

    def test_con_repeticiones(self) -> None:
        assert contar_frecuencias(["a", "b", "a"]) == {"a": 2, "b": 1}

    def test_lista_vacia(self) -> None:
        assert contar_frecuencias([]) == {}

    def test_un_solo_valor(self) -> None:
        assert contar_frecuencias([5, 5, 5]) == {5: 3}


# ── normalizar ────────────────────────────────────────────────
class TestNormalizar:
    def test_rango_cero_uno(self) -> None:
        resultado = normalizar([0.0, 5.0, 10.0])
        assert resultado == pytest.approx([0.0, 0.5, 1.0])

    def test_lista_vacia_lanza_error(self) -> None:
        with pytest.raises(ValueError):
            normalizar([])

    def test_todos_iguales_retorna_ceros(self) -> None:
        assert normalizar([3.0, 3.0, 3.0]) == [0.0, 0.0, 0.0]

    def test_un_elemento(self) -> None:
        assert normalizar([7.0]) == [0.0]

    def test_valores_negativos(self) -> None:
        resultado = normalizar([-10.0, 0.0, 10.0])
        assert resultado == pytest.approx([0.0, 0.5, 1.0])
