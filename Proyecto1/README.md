# Proyecto1 - AppEduca

Este es un proyecto web desarrollado con Django para administrar estudiantes, profesores, entregas de proyectos y cursos. Permite agregar, buscar y visualizar información de los usuarios que son parte.

## Requisitos Previos

Asegúrate de tener instaladas las siguientes versiones de Python y Django:

- Python 3.11.5
- Django 4.2.5

## Instalación

1. Clona el repositorio:
git clone https://github.com/TuUsuario/Proyecto1-AppEduca.git

2. Navega al directorio del proyecto:
cd Proyecto1-AppEduca

3. Instala las dependencias del proyecto desde el archivo `requirements.txt`:
pip install -r requirements.txt

4. Ejecuta las migraciones para crear la base de datos:
python manage.py migrate

5. Inicia el servidor de desarrollo:
python manage.py runserver

7. Abre tu navegador y visita [http://localhost:8000](http://localhost:8000) para acceder al proyecto.


## Funcionalidad

La aplicación web AppEduca consta de las siguientes funcionalidades:

- **Estudiantes:** Permite agregar estudiantes con nombre, apellido, edad y email a través de un formulario conectado a la base de datos.

- **Profesores:** Permite agregar profesores con nombre, apellido, especialidad y email a través de un formulario conectado a la base de datos.

- **Entrega de Proyectos:** Permite registrar entregas de proyectos con información como fecha de entrega, estado (entregado o no entregado) y el nombre del proyecto entregado.

- **Cursos:** Permite agregar cursos con nombre y comisión a través de un formulario conectado a la base de datos.

- **Búsqueda de Cursos:** Desde la página de inicio (index.html), puedes buscar cursos por nombre y ver información sobre el curso y la comisión.

- **Búsqueda de Estudiantes:** También desde la página de inicio, puedes buscar estudiantes por nombre y ver todos sus datos.

## Dependencias

Este proyecto utiliza las siguientes librerías y dependencias:
- Bootstrap para la parte de diseño y estilos. Las dependencias necesarias ya están incluidas en el repositorio, así que no es necesario instalar nada adicionalmente.

## Contacto

Si tienes alguna pregunta o comentario, no dudes en ponerte en contacto con johatumio@hotmail.com.

## Estado del Proyecto

Este proyecto está en desarrollo activo y se mantendrá actualizado con nuevas características y correcciones de errores.

# Autor

Este proyecto fue desarrollado por Johanna Tumio como parte del curso de Python en CoderHouse.