# Guía de presentación y defensa — Dasne

## Presentación breve
“Mi proyecto se llama Sistema de Gestión de Jugadores de un Club Deportivo. Su objetivo es permitir administrar los datos de los jugadores de manera ordenada. Está desarrollado con Django y utiliza MySQL como base de datos. La aplicación permite crear, consultar, modificar y eliminar jugadores.”

## Recorrido de demostración
1. Mostrar la página principal y explicar el resumen de jugadores registrados y activos.
2. Entrar a “Registrar jugador” y crear un registro de prueba.
3. Volver al listado y mostrar el nuevo jugador.
4. Abrir “Ver” para consultar su ficha.
5. Seleccionar “Editar”, cambiar un dato y guardar.
6. Seleccionar “Eliminar” y mostrar la confirmación. Para la demostración puedes cancelar o eliminar un registro de prueba.
7. Explicar que los datos quedan guardados en MySQL y se pueden revisar en phpMyAdmin, dentro de la tabla `jugadores_jugador`.

## Pregunta técnica 1: ¿Qué es un modelo en Django y para qué se utiliza?
Respuesta sugerida: “Un modelo representa la estructura de los datos que se guardan en la base de datos. En mi proyecto, el modelo `Jugador` define campos como nombre, apellido, edad, posición y número de camiseta. Django utiliza ese modelo para crear y consultar registros en MySQL.”

## Pregunta técnica 2: ¿Qué significa CRUD y cómo lo implementaste?
Respuesta sugerida: “CRUD corresponde a Crear, Consultar, Modificar y Eliminar. En mi aplicación, crear registra un jugador mediante un formulario; consultar muestra el listado y el detalle; modificar permite editar sus datos; y eliminar borra el registro después de pedir confirmación.”

## Otras preguntas que podrían hacerte
- **¿Qué función cumple `views.py`?** Contiene las funciones que reciben las solicitudes y deciden qué información mostrar o guardar.
- **¿Qué función cumple `urls.py`?** Relaciona cada dirección web con una vista.
- **¿Qué es una migración?** Es el mecanismo de Django para aplicar cambios de los modelos a la estructura de la base de datos.
- **¿Por qué usaste MySQL?** Porque la evaluación solicita conectar Django con MySQL/MariaDB y almacenar los registros allí.
- **¿Qué validaciones tiene?** Campos obligatorios, correo con formato válido, edad entre 5 y 80 años, número de camiseta entre 1 y 99 y número de camiseta único.
- **¿Qué pasa si se repite un número de camiseta?** La base de datos y el formulario impiden guardar dos jugadores con el mismo número.
- **¿Dónde se conecta Django con MySQL?** En `settings.py`, dentro de `DATABASES`; los datos de conexión se leen desde `.env`.

## Antes de presentar
- Iniciar MySQL desde XAMPP.
- Confirmar que existe la base `club_deportivo`.
- Activar el entorno virtual.
- Ejecutar `python manage.py migrate`.
- Ejecutar `python manage.py runserver`.
- Probar crear, editar y eliminar un jugador de prueba.
- No memorices sin comprender: practica explicar con tus propias palabras cada paso.
