## Proyecto Django - `proyecto2`

### Descripción

Este proyecto es una aplicación web desarrollada con el framework Django. Proporciona funcionalidades básicas como la gestión de cursos, profesores, estudiantes y entregables. 

### Estructura del Proyecto

- `db.sqlite3`: Archivo de base de datos SQLite.
- `manage.py`: Script de gestión de Django.
- `.git/`: Directorio del repositorio Git con la configuración y el historial de commits.
- `appcoder/`: Aplicación principal del proyecto.
  - `static/appcoder/css/`: Archivos CSS.
  - `static/appcoder/js/`: Archivos JavaScript.
  - `templates/appcoder/`: Plantillas HTML.
  - `__pycache__/`: Archivos compilados de Python.
- `proyectoCoder/`: Configuración del proyecto Django.
  - `asgi.py`: Configuración para ASGI.
  - `settings.py`: Configuración del proyecto.
  - `urls.py`: Configuración de URLs.
  - `wsgi.py`: Configuración para WSGI.
  - `__pycache__/`: Archivos compilados de Python.

### Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Piglesias2610/Preentrega3-PieroIglesias
   cd proyecto2
   ```

2. **Crear un entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\\Scripts\\activate
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones:**

   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

### Funcionalidades

1. **Gestión de Cursos:**
   - Crear, leer, actualizar y eliminar cursos.
   - Visualizar una lista de todos los cursos disponibles.

2. **Gestión de Profesores:**
   - Crear, leer, actualizar y eliminar profesores.
   - Visualizar una lista de todos los profesores disponibles.

3. **Gestión de Estudiantes:**
   - Crear, leer, actualizar y eliminar estudiantes.
   - Visualizar una lista de todos los estudiantes disponibles.

4. **Gestión de Entregables:**
   - Crear, leer, actualizar y eliminar entregables.
   - Visualizar una lista de todos los entregables disponibles.

5. **Formularios Dinámicos:**
   - Formularios para ingresar y actualizar la información de cursos, profesores, estudiantes y entregables.

6. **Autenticación de Usuarios:**
   - Sistema de registro e inicio de sesión para usuarios.
   - Permisos y roles de usuario para controlar el acceso a diferentes partes de la aplicación.

### Uso

1. Accede al servidor de desarrollo en `http://127.0.0.1:8000/`.
2. Navega por las diferentes secciones de la aplicación (cursos, profesores, estudiantes, entregables) para gestionar la información.

### Autor

Este proyecto fue desarrollado por **Piero Iglesias**.

---

Si tienes alguna pregunta o encuentras algún problema, por favor, abre un *issue* en el repositorio o contacta al autor.
