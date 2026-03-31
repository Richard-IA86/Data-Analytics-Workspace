# GIT - Instructivo de Administración Básica

> **Proyecto:** Data Analytics Workspace
> **Repositorio:** Richard-IA86/Data-Analytics-Workspace
> **Rama principal:** main
> **Actualizado:** 2026-03-31

---

## ¿Por qué seguir este instructivo?

Ejecutar estos pasos al inicio y al cierre de cada jornada garantiza que:

- El repositorio local y el remoto (GitHub) estén siempre sincronizados.
- No se pierdan cambios por olvido de commit o push.
- El historial sea limpio y trazable.

---

## ✅ Checklist - INICIO de jornada

Ejecutar **antes** de comenzar a trabajar.

`powershell
# 1. Moverse a la carpeta del proyecto
cd "C:\Dev\Data Analytics"

# 2. Verificar el estado actual del repositorio
git status

# 3. Obtener los últimos cambios del repositorio remoto
git pull origin main

# 4. Confirmar en qué rama estás trabajando
git branch
`

### ¿Qué esperar en cada paso?

| Paso | Resultado esperado |
|------|--------------------|
| git status | 
othing to commit, working tree clean (si no quedaron cambios pendientes de la jornada anterior) |
| git pull | Already up to date. (si no hay cambios nuevos en remoto) o una lista de archivos actualizados |
| git branch | El asterisco * debe estar sobre main |

---

## ✅ Checklist - CIERRE de jornada

Ejecutar **antes** de cerrar VS Code o terminar el trabajo del día.

`powershell
# 1. Revisar todos los archivos modificados o nuevos
git status

# 2. Agregar todos los cambios al área de preparación (staging)
git add .

#    - O bien, agregar solo archivos específicos -
git add ruta/al/archivo.py

# 3. Confirmar los cambios con un mensaje descriptivo
git commit -m "descripción breve y clara de lo hecho"

# 4. Subir los cambios al repositorio remoto
git push origin main

# 5. Verificar que quedó todo limpio
git status
`

### Buenas prácticas para el mensaje de commit

`powershell
# ✔ Mensajes claros y en tiempo presente
git commit -m "Agrega análisis de datos del TP3"
git commit -m "Corrige error en cálculo de correlación"
git commit -m "Actualiza README con instrucciones de configuración"

# ✖ Evitar mensajes vagos
git commit -m "cambios"
git commit -m "arreglos varios"
git commit -m "wip"
`

---

## 📋 Referencia rápida de comandos

| Comando | ¿Para qué sirve? |
|---------|-----------------|
| git status | Ver archivos modificados, nuevos o eliminados |
| git log --oneline -10 | Ver los últimos 10 commits del historial |
| git diff | Ver las diferencias en los archivos modificados antes de hacer commit |
| git add . | Agregar todos los cambios al staging |
| git add <archivo> | Agregar un archivo específico al staging |
| git commit -m "msg" | Guardar los cambios con un mensaje |
| git push origin main | Subir commits al repositorio remoto |
| git pull origin main | Bajar cambios del repositorio remoto |
| git restore <archivo> | Descartar cambios locales en un archivo (irreversible) |
| git restore --staged <archivo> | Sacar un archivo del staging sin perder los cambios |

---

## 🚀 Uso de Ramas y Entornos Virtuales (Python)

Al trabajar con cuadernos (Jupyter/Colab) o scripts Python (.py), es recomendable mantener sincronizado tanto el entorno virtual como las dependencias, así como usar ramas para trabajos grandes.

### 1. Variables de Entorno y Directorios Locales
Dado que utilizamos cuadernos en Colab y localmente, las rutas absolutas pueden generar conflictos. 
- Evita usar rutas locales fijas en los cuadernos (C:\Dev...). En su lugar, usa rutas relativas o monta Google Drive cuando estés en Colab.
- Configura tu entorno virtual (.venv) y asegúrate de no incluirlo en el repositorio (debe estar en .gitignore).

### 2. El Concepto de Ramas (Branches)
- **main:** Es la rama estable. Contiene tus entregas finales o notebooks ya corregidos y funcionales.
- **Ramas temporales (ej. 	p4-analisis):** Cuando empiezas un nuevo trabajo práctico, te sugerimos crearlo en otra rama.

`powershell
# Crear y moverse a la nueva rama
git checkout -b tp4-analisis

# (Aquí realizas todo tu trabajo...)

# Al terminar, integra los cambios en main
git checkout main
git merge tp4-analisis
git push origin main
`

---

## ⚠️ Situaciones comunes y cómo resolverlas

### "Me pide credenciales al hacer push"
`powershell
# Verificar que el remoto esté configurado con HTTPS o SSH
git remote -v
`
Si es HTTPS, usa un **Personal Access Token (PAT)** de GitHub o el administrador de credenciales de Windows.

---

### "Hice commit pero me olvidé de agregar un archivo"
`powershell
# Agrega el archivo olvidado y corrige el último commit sin crear uno nuevo
git add archivo_olvidado.py
git commit --amend --no-edit
`
> Solo usar --amend si aún **no hiciste push**. Si ya subiste el commit, crear uno nuevo.

---

### "Quiero ver qué cambié antes de hacer commit"
`powershell
git diff
# Para ver los archivos en staging
git diff --staged
`

---

### "Quiero deshacer el último commit (sin perder los cambios)"
`powershell
git reset --soft HEAD~1
`

---

*Instructivo adaptado para el repositorio Data Analytics Workspace.*