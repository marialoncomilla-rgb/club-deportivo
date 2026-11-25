# Informe del proyecto: Sistema de Gestión de Jugadores de un Club Deportivo

**Estudiante:** Dasne Estefanía Meneses López  
**Asignatura:** Programación Backend  
**Unidad:** 2 — Framework Backend  
**Temática asignada:** Club deportivo  
**Entidad principal:** Jugador  

## 1. Introducción
Este proyecto consiste en desarrollar una aplicación web para administrar la información de los jugadores de un club deportivo. La solución permite mantener los registros organizados y realizar operaciones desde una interfaz sencilla.

## 2. Objetivo
Desarrollar una aplicación web con Django conectada a una base de datos MySQL/MariaDB que permita crear, consultar, modificar y eliminar registros de jugadores.

## 3. Tecnologías utilizadas
- **Python:** lenguaje utilizado para desarrollar la lógica.
- **Django:** framework backend utilizado para construir la aplicación web.
- **MySQL/MariaDB:** sistema de base de datos para almacenar los registros.
- **XAMPP:** entorno utilizado para iniciar el servicio MySQL.
- **HTML y Bootstrap:** herramientas utilizadas para construir y dar estilo a las páginas.

## 4. Funcionamiento
La página principal presenta un resumen de los jugadores registrados y activos. Desde el menú se puede acceder al listado y al formulario de registro. Cada jugador puede consultarse en una ficha individual, editarse o eliminarse mediante una confirmación.

## 5. Modelo de datos
La entidad principal es `Jugador`. Sus atributos son: nombre, apellido, edad, posición, número de camiseta, correo electrónico, teléfono, fecha de ingreso y estado activo. El número de camiseta es único para evitar duplicaciones.

## 6. Operaciones CRUD
- **Crear:** registra un nuevo jugador mediante un formulario.
- **Consultar:** muestra el listado y la ficha individual.
- **Modificar:** permite actualizar la información de un jugador.
- **Eliminar:** borra el registro previa confirmación.

## 7. Validaciones
Se controlan los campos obligatorios, el formato del correo electrónico, la edad permitida, el rango del número de camiseta, la unicidad del número y el formato básico del teléfono.

## 8. Base de datos
Django se conecta a MySQL/MariaDB mediante la configuración `DATABASES` de `settings.py`. Las migraciones crean la tabla correspondiente al modelo `Jugador`.

## 9. Conclusión
El proyecto aplica los conceptos de desarrollo backend mediante Django y la conexión con MySQL. La aplicación permite gestionar los datos de jugadores y demuestra las cuatro operaciones CRUD solicitadas en la evaluación.

**Nota:** Antes de entregar, ejecutar y probar el proyecto en el equipo de presentación, y agregar capturas reales de su funcionamiento y evidencia propia de Git/GitHub.
