# Checklist de Pruebas - CRUD Jugadores

## Verificacion de entorno y base de datos
- [ ] Servicio MySQL/MariaDB activo en XAMPP.
- [ ] Base de datos club_deportivo creada y migraciones aplicadas.
- [ ] Servidor Django iniciado con python manage.py runserver.

## Casos de prueba funcionales
1. Crear jugador: registrar un jugador con datos validos y verificar redireccion y persistencia en la tabla.
2. Validaciones: probar edad fuera de rango, numero de camiseta duplicado o invalido y correo sin formato valido.
3. Buscar y consultar detalle: filtrar jugadores en el listado y abrir la vista de detalle.
4. Editar jugador: modificar datos de un jugador existente y confirmar el cambio en el listado y en phpMyAdmin.
5. Eliminar jugador: borrar un registro de prueba desde la pantalla de confirmacion y verificar que ya no figura.
