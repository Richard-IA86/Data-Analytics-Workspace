# QA — Propuesta: Procedimiento de Presentación de Ejercicios

**Fecha:** 2026-04-17
**Estado:** PENDIENTE DE APROBACIÓN
**Autor:** GitHub Copilot (análisis estructural)
**Revisado por:** — (pendiente)

---

## 1. Objetivo del Informe

Definir un procedimiento estándar y reproducible para la presentación de
ejercicios en los Trabajos Prácticos del curso Data Analytics.

El procedimiento se basa en la observación directa de los materiales
existentes: modelos del docente, consignas oficiales y TPs entregados.

---

## 2. Fuentes Analizadas

| Archivo | Rol | Observación |
|---|---|---|
| `docs/modelos/ejercicio-clase2.ipynb` | Modelo docente | Estructura base H1 numerado |
| `docs/modelos/ejercicio-clase3.ipynb` | Modelo docente | Estructura base H1 numerado |
| `docs/modelos/clase3.ipynb` | Notas de clase | Demo sin estructura de entrega |
| `docs/modelos/repasoPython.ipynb` | Notas de clase | Demo sin estructura de entrega |
| `docs/modelos/importar-csv-pandas-nulos-duplicados.ipynb` | Notas de clase | Demo sin estructura de entrega |
| `docs/modelos/limpieza-datos.ipynb` | Notas de clase | Demo sin estructura de entrega |
| `docs/modelos/dataFrames-1,2y3D.ipynb` | Notas de clase | H1 temático + código estructurado |
| `docs/clase-3.md` | Consigna oficial | Patrón canónico del enunciado |
| `docs/clase-4.md` | Consigna oficial | Patrón canónico del enunciado |
| `TP1/PrimeraPractica.ipynb` | TP entregado | Nivel básico |
| `TP2/Actividad_2_Repaso_en_Python.ipynb` | TP entregado | Nivel intermedio |
| `TP3/Actividad_3_Introduccion_NumPy_Pandas.ipynb` | TP entregado | Nivel maduro ✅ |
| `TP3/Ejercicio_Practico.ipynb` | TP entregado | Nivel maduro ✅ |

---

## 3. Hallazgos — Patrones Identificados

### 3.1. Estructura de los modelos del docente

Los notebooks de ejercicio del docente (`ejercicio-clase2`, `ejercicio-clase3`)
siguen un patrón consistente:

```
# N - Título de la sección         ← Celda Markdown (H1 numerado)
  * a. texto de la consigna
  * b. texto de la consigna

[código Python]                    ← Celda Código
  print("N. A. ")
  → resolución a
  print("N. B. ")
  → resolución b
```

**Características:**
- Sin metadata de identificación (sin nombre alumno, sin mentor)
- Sin objetivo explícito
- Prints etiquetados con número y letra: `print("2. A. ")`
- Una celda Markdown + una celda Código por sección principal

---

### 3.2. Estructura de la consigna oficial (`docs/clase-N.md`)

```
# Ejercicios DATA ANALYTICS - Clase NN
## Actividad N: Título
**Obligatorio** (cuando aplica)
### Objetivos
### Contexto          ← Incluye mentor, rol, empresa (SynthData)
### Consigna          ← Ítems numerados 1, 2, 3...
### Datos             ← Nombre del dataset
### ¿Por qué importa esto en SynthData?
---
```

---

### 3.3. Evolución de los TPs entregados

| TP | Nivel | Aspectos positivos | Aspectos a mejorar |
|---|---|---|---|
| TP1 | Básico | Badge Colab, identificación alumno | Sin estructura de ejercicios |
| TP2 | Intermedio | `##N.` y `###N.N.`, explicaciones teóricas | Mezcla teoría y ejercicio sin separación clara |
| TP3/Actividad_3 | Maduro ✅ | Clase, Actividad, Mentor, Objetivo, `### Ejercicio N —` | Referencia completa |
| TP3/Ejercicio_Practico | Maduro ✅ | `## N - Título`, `# a.` en código, prints etiquetados | Referencia completa |

**Referencia canónica:** `TP3/Actividad_3_Introduccion_NumPy_Pandas.ipynb`

---

## 4. Propuesta de Procedimiento

### 4.1. Nomenclatura del archivo

```
TP{N}/Actividad_{N}_{Titulo_Descriptivo}.ipynb
```

| Ejemplo correcto | Ejemplo incorrecto |
|---|---|
| `TP4/Actividad_4_Limpieza_Datos.ipynb` | `TP4/actividad4.ipynb` |
| `TP3/Actividad_3_Introduccion_NumPy_Pandas.ipynb` | `TP3/Ejercicio_Practico.ipynb` |

> `{Titulo_Descriptivo}` usa `PascalCase_con_guiones_bajos`,
> sin tildes ni caracteres especiales.

---

### 4.2. Jerarquía de celdas

```
┌─────────────────────────────────────────────────────────────────────┐
│ CELDA 1  │ Markdown │ Encabezado del documento                      │
│          │          │ (Clase, Actividad, Mentor, Objetivo)          │
├─────────────────────────────────────────────────────────────────────┤
│ CELDA 2  │ Markdown │ ### Ejercicio 1 — Título breve                │
│ CELDA 3  │ Python   │ # a. descripción + código + print             │
├─────────────────────────────────────────────────────────────────────┤
│ CELDA 4  │ Markdown │ ### Ejercicio 2 — Título breve                │
│ CELDA 5  │ Python   │ # a. descripción + código + print             │
│          │          │ (repetir el par Markdown+Python por ejercicio)│
└─────────────────────────────────────────────────────────────────────┘
```

---

### 4.3. Template del encabezado (Celda 1)

```markdown
# Clase NN — DATA ANALYTICS

## Actividad N: Título de la Actividad
**Mentor:** Nombre (Rol en SynthData)

Objetivo: descripción breve en una línea.

---
```

---

### 4.4. Template de cada ejercicio (par de celdas)

```markdown
### Ejercicio N — Descripción breve del ejercicio
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

### 4.5. Reglas de estilo en celdas Python

| Elemento | Regla |
|---|---|
| Comentario de sub-ítem | `# a.` minúscula, sin punto final en la descripción |
| Print de salida | f-string con etiqueta: `print(f"Label: {var}")` |
| Rutas de archivo | Ruta local → `ruta = "../input_raw/archivo.csv"` |
| | Colab → línea comentada debajo indicando cómo sustituir |
| Longitud de línea | Máximo 79 caracteres (PEP8 / black) |
| Separación visual entre items | Una línea en blanco entre bloques `# a.` y `# b.` |

---

### 4.6. Correspondencia consigna → notebook

Cuando existe un `.md` de consigna en `docs/`:

| Campo en `.md` | Celda en notebook |
|---|---|
| `## Actividad N: Título` | `## Actividad N: Título` (idéntico) |
| `### Contexto` — Mentor + empresa | `**Mentor:** Nombre (Rol)` en Celda 1 |
| `### Objetivos` | `Objetivo:` en Celda 1 |
| Ítem N de `### Consigna` | `### Ejercicio N — ...` |
| `### Datos` — nombre archivo | `# Fuente: archivo.csv` como comentario en celda código |

---

## 5. Fuera del Alcance de este Procedimiento

- El badge "Open in Colab" (se genera automáticamente al guardar desde Colab)
- Celdas teóricas/expositivas opcionales (como en TP2 — válidas pero no
  obligatorias)
- Notebooks de repaso libre sin estructura de entrega numerada

---

## 6. Decisiones Pendientes de Aprobación QA

| # | Pregunta | Opciones |
|---|---|---|
| D1 | ¿Se acepta la jerarquía H1 → H2 (`##`) → H3 (`###`) propuesta? | Sí / No / Ajustar |
| D2 | ¿Los TPs ya entregados (TP1, TP2) se retroadaptan o solo aplica a TP4+? | Solo futuros / Retroadaptar todos / Retroadaptar TP2 |
| D3 | ¿Dónde vive el procedimiento definitivo? | `docs/` / `config/` / `README.md` |
| D4 | ¿El campo `**Mentor:**` es obligatorio o solo cuando la consigna lo indica? | Siempre / Solo cuando hay consigna |
| D5 | ¿El `Objetivo:` debe coincidir textualmente con la consigna oficial? | Textual / Libre / Resumen propio |

---

## 7. Próximo Paso (post-aprobación)

Una vez aprobado este informe:

1. Crear `docs/procedimiento_presentacion_ejercicios.md` con el procedimiento
   definitivo.
2. Aplicar el template a `TP4/Actividad_4.ipynb` (próximo TP pendiente).
3. Registrar en `config/estado_proyecto.json`.
