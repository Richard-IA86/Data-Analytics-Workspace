# Contenido del archivo para tu referencia rápida
"""
# Arquitectura del Ecosistema: Curso de Data Analytics (Python + Colab + VSC + Git)

Esta arquitectura está diseñada para proporcionar un entorno de grado profesional, separando la ingeniería de código de la experimentación de datos.

## 1. Componentes del Ecosistema

| Componente | Función Principal | Herramientas Relacionadas |
| :--- | :--- | :--- |
| **Desarrollo Local** | Escritura de scripts, módulos .py y gestión de versiones. | Visual Studio Code (VSC), Git, Terminal. |
| **Control de Versiones** | Repositorio central ("Source of Truth") y puente de sincronización. | GitHub / GitLab. |
| **Entorno de Ejecución** | Ejecución de notebooks, visualización y computación en la nube. | Google Colab (Kernel de Python). |
| **Persistencia de Datos** | Almacenamiento a largo plazo de datasets y resultados de alumnos. | Google Drive. |

---

## 2. Arquitectura de Carpetas Recomendada

Esta estructura debe mantenerse sincronizada tanto en el repositorio de Git como en el Google Drive del alumno para asegurar la idempotencia del código.

```text
/curso-data-analytics/
├── .gitignore              # Archivos a ignorar (ej. .ipynb_checkpoints, __pycache__)
├── README.md               # Guía general del curso y configuración inicial
├── requirements.txt        # Librerías de Python necesarias
│
├── notebooks/              # Archivos .ipynb (Exclusivos para Colab)
│   ├── 01_introduccion.ipynb
│   ├── 02_limpieza_datos.ipynb
│   └── 03_analisis_exploratorio.ipynb
│
├── src/                    # Código fuente (Editado en VSC)
│   ├── __init__.py
│   ├── limpieza.py         # Scripts de procesamiento
│   ├── visualizacion.py    # Funciones personalizadas para gráficos
│   └── utilidades.py       # Helpers generales
│
├── data/                   # Gestión de Datasets
│   ├── raw/                # Datos originales (Inmutables)
│   └── processed/          # Salidas generadas tras la limpieza
│
└── tests/                  # Pruebas unitarias para los scripts de /src

---

## 3. Análisis de Viabilidad — Workspace Actual (2026-04-21)

**Autor del análisis:** GitHub Copilot  
**Estado:** Pendiente revisión QA

### 3.1. Veredicto general

La propuesta describe una arquitectura válida para un **repositorio nuevo**.
Para el workspace actual **no se recomienda migración**: el proyecto tiene
4 Trabajos Prácticos completados, pipeline QA en VERDE (46 tests,
black + flake8 + mypy OK) y una estructura consolidada y aprobada.

El costo de migración (reescritura de imports, rutas en tests, notebooks)
supera cualquier beneficio operativo. La propuesta tiene valor como
**referencia documental y plantilla para proyectos futuros**.

### 3.2. Equivalencias con la arquitectura actual

| Propuesta (`nueva_propuesta.md`) | Workspace actual | Equivalencia |
| :--- | :--- | :---: |
| `src/` — Código fuente Python | `Herramientas/` (`mis_funciones.py`) | ✅ Equivalente |
| `tests/` — Pruebas unitarias | `tests/` (`test_mis_funciones.py`) | ✅ Idéntico |
| `data/raw/` — Datos originales (inmutables) | `input_raw/` (CSVs de curso) | ✅ Equivalente |
| `data/processed/` — Salidas generadas | No existe (aún no necesario) | ➖ Sin equivalente |
| `notebooks/` — Archivos `.ipynb` para Colab | `TP1/`, `TP2/`, `TP3/`, `TP4/`, `docs/modelos/` | ✅ Cumple el rol |
| `.gitignore`, `README.md`, `requirements.txt` | Idénticos en la raíz | ✅ Idéntico |
| — | `config/` (`estado_proyecto.json`) | ➕ Extra (protocolo de jornada) |
| — | `scripts_docs/` (contexto, instructivos) | ➕ Extra (no contemplado) |

### 3.3. Flujo de datos — Diferencia clave

La propuesta asume que los datasets **no se suben a Git** (solo a Drive).
En el workspace actual los CSVs sí están versionados en Git porque:

- Son archivos pequeños (KB, no GB).
- Garantizan reproducibilidad sin depender de Drive.
- Cualquier alumno puede clonar el repo y ejecutar inmediatamente.

Este diseño es **correcto y preferible** para el contexto del curso.

### 3.4. Observación sobre entornos virtuales

El workspace genera un `.venv` local (dependencias del proyecto) que está
correctamente excluido en `.gitignore`. El pipeline QA (pre-commit hook)
corre desde un entorno separado en `C:\dev\dev_richard_ia86\.venv`.
No es un error de diseño: es el patrón estándar de separar herramientas
de desarrollo del entorno de ejecución del proyecto.

### 3.5. Decisión recomendada

| Acción | Recomendación |
| :--- | :--- |
| Migrar workspace actual a esta arquitectura | ❌ No recomendado |
| Usar como plantilla para proyectos futuros | ✅ Recomendado |
| Retroadaptar TP1–TP4 | ❌ No aplica (D2 aprobado) |
| Mantener pipeline QA y estructura actual | ✅ Mantener |