# Procedimiento: Presentación de Ejercicios en Notebooks

**Estado:** APROBADO POR QA  
**Fecha de aprobación:** 2026-04-21  
**Alcance:** TP4 en adelante (no retroactivo a TP1/TP2)

---

## 1. Nomenclatura del archivo

```
TP{N}/Actividad_{N}_{Titulo_Descriptivo}.ipynb
```

- `{Titulo_Descriptivo}` en `PascalCase_con_guiones_bajos`
- Sin tildes ni caracteres especiales
- Ejemplo correcto: `TP4/Actividad_4_Limpieza_Datos.ipynb`

---

## 2. Jerarquía de celdas

| Celda | Tipo | Contenido |
|---|---|---|
| 1 | Markdown | Badge Colab (opcional, se genera en Colab) |
| 2 | Markdown | Encabezado del documento (H1 + H2 + Mentor + Objetivo) |
| 3 | Markdown | `### N.M — Título del sub-ejercicio` |
| 4 | Python | Código de resolución con prints etiquetados |
| … | … | Repetir par Markdown + Python por sub-ejercicio |

---

## 3. Template del encabezado (Celda 2)

```markdown
# Clase NN — DATA ANALYTICS

## Actividad N: Título de la Actividad
**Mentor:** Nombre (Rol en SynthData)

Objetivo: <texto textual de la consigna oficial>.

---
```

**Reglas:**
- `**Mentor:**` es **siempre obligatorio**, aunque la consigna no lo indique.
- `Objetivo:` debe coincidir **textualmente** con el texto de la consigna
  oficial en `docs/clase-N.md`.

---

## 4. Template de cada sub-ejercicio (par de celdas)

```markdown
### N.M — Descripción breve del sub-ejercicio
```

```python
# a. descripción del sub-ítem a
variable_a = ...
print(f"a. Resultado: {variable_a}")

# b. descripción del sub-ítem b
variable_b = ...
print(f"b. Resultado: {variable_b}")
```

---

## 5. Reglas de estilo en celdas Python

| Elemento | Regla |
|---|---|
| Comentario de sub-ítem | `# a.` minúscula, sin punto final en la descripción |
| Print de salida | f-string con etiqueta: `print(f"Label: {var}")` |
| Ruta de archivo local | `ruta = "../input_raw/archivo.csv"` |
| Longitud de línea | Máximo 79 caracteres (PEP8 / black) |
| Separación entre ítems | Una línea en blanco entre bloques `# a.` y `# b.` |

---

## 6. Correspondencia consigna → notebook

| Campo en `docs/clase-N.md` | Celda en notebook |
|---|---|
| `## Actividad N: Título` | `## Actividad N: Título` (idéntico) |
| `### Contexto` — Mentor + empresa | `**Mentor:** Nombre (Rol)` en encabezado |
| `### Objetivos` | `Objetivo:` en encabezado (textual) |
| Ítem N de `### Consigna` | `### N.M — ...` |
| `### Datos` — nombre archivo | Comentario `# Fuente: archivo.csv` en celda código |

---

## 7. Decisiones QA registradas

| # | Pregunta | Decisión |
|---|---|---|
| D1 | Jerarquía H1 → `##` → `###` | **Aceptada** |
| D2 | Retroadaptación TPs anteriores | **Solo futuros** (TP4 en adelante) |
| D3 | Ubicación del procedimiento | **`docs/`** |
| D4 | Campo `**Mentor:**` | **Siempre obligatorio** |
| D5 | Campo `Objetivo:` | **Textual** (igual a la consigna oficial) |

---

## 8. Referencia canónica

`TP3/Actividad_3_Introduccion_NumPy_Pandas.ipynb`
