# Flujo de Trabajo: Análisis de Datos (Colab / GitHub / VS Code)

Este documento sirve como guía paso a paso para asegurar que nuestro trabajo esté siempre organizado, sincronizado y seguro entre nuestro entorno local y la nube.

## 🔄 Esquema Rápido del Ciclo

El ciclo de vida de los archivos siempre es:
`Colab ---> GitHub ---> VS Code ---> GitHub`

Para abrir un archivo siempre es:
`Colab ---> pestaña GitHub`

*Nota sobre Google Drive:* Nuestro flujo principal **omite** Google Drive para evitar desincronizaciones. Si por algún motivo específico necesitas una copia en Drive, debes subir manualmente el archivo `.ipynb` desde tu pc local (`C:\Dev\Data Analytics\TPX\...`) a tu cuenta de Drive.

## 📝 El Ciclo de Trabajo Detallado

Cada vez que recibamos un nuevo Trabajo Práctico (TP) o actividad, seguiremos este orden:

### 1. Preparación del Entorno
* **En VS Code (Local):** 
  * Verificamos que estamos en la carpeta del proyecto.
  * Si es un nuevo TP, creamos la carpeta (ej: `TP2`).
  * Ejecutamos `git pull` en la terminal para asegurarnos de tener la última versión de todo.

### 2. Ejecución y Desarrollo (En la Nube)
* Ingresamos a [Google Colab](https://colab.research.google.com/).
* Si empezamos algo desde cero:
  * Creamos un "**Nuevo cuaderno**".
  * Configuramos nuestras celdas de Markdown (texto) y Código (Python).
* Si continuamos un trabajo:
  * Vamos a la pestaña **GitHub**.
  * Seleccionamos nuestro repositorio (`Richard-IA86/Data-Analytics-Workspace`).
  * Abrimos el archivo que queremos editar.

### 3. Guardado en la Nube (Commit)
* Una vez finalizado el trabajo o al hacer una pausa:
  * En Colab: `Archivo > Guardar una copia en GitHub`.
  * Elegimos la rama `main`.
  * Indicamos la ruta correcta (ej. `TP1/notebook.ipynb`).
  * Ponemos un "Mensaje de confirmación" claro (ej: "Completo Actividad 1 - Correcciones menores").

### 4. Sincronización al Entorno Local (Pull)
* Volvemos a **VS Code**.
* En la terminal (asegurándonos de estar en `C:\Dev\Data Analytics`), ejecutamos:
  ```powershell
  git pull
  ```
* Esto bajará todos los cambios y nos dejará el archivo listo para revisión o ajustes técnicos precisos.

### 5. Revisiones Finas en VS Code (Opcional pero recomendado)
* Abrimos el cuaderno `.ipynb` en VS Code.
* Gracias al entorno `.venv`, podemos probar el código, arreglar sintaxis o mejorar el Markdown que no quedó bien en la web.
* Si hacemos cambios locales, actualizamos el repositorio con la secuencia técnica:
  ```powershell
  git add .
  git commit -m "Descripción de lo que corregí localmente"
  git push origin main
  ```

---
*Documento vivo: Este proceso puede refinarse a medida que incorporemos nuevas herramientas o pasos en el curso.*
